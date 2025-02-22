from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

event_details = {}
leaderboard = []
last_result = {}
team_ratings = {}  # To store ratings from each judge per team

def calculate_score(ratings):
    return sum(ratings) / len(ratings)

@app.route("/", methods=["GET", "POST"])
def home():
    global event_details
    if request.method == "POST":
        # Enforce max of 4 judges
        num_judges = min(int(request.form["numJudges"]), 4)
        event_details = {
            "name": request.form["eventName"],
            "date": request.form["eventDate"],
            "teams": int(request.form["numTeams"]),
            "numJudges": num_judges,
            "criteria": request.form.getlist("criteria[]")
        }
        return redirect(url_for("index"))
    return render_template("admin.html")

@app.route('/judging', methods=['GET', 'POST'])
def index():
    global last_result
    if not event_details:
        return redirect(url_for("home"))
    
    # GET: Render the form
    if request.method == 'GET':
        # If judge and teamName are passed in the query string, use them.
        judge = request.args.get("judge", default=1, type=int)
        team_name = request.args.get("teamName", default="")
        message = request.args.get("message", default="")
        return render_template('index.html', event=event_details, judge=judge, team_name=team_name, message=message)
    
    # POST: Process the submitted rating
    # Get the current judge number (default to 1 if not provided)
    judge = int(request.form.get("judge", 1))
    team_name = request.form.get("teamName")
    
    # Gather ratings based on the criteria defined in admin
    ratings = []
    for i, _ in enumerate(event_details["criteria"], start=1):
        rating = int(request.form.get(f"rating{i}"))
        ratings.append(rating)
    current_score = calculate_score(ratings)
    
    # Save this judge's rating for the team
    if team_name not in team_ratings:
        team_ratings[team_name] = []
    team_ratings[team_name].append(current_score)
    
    # Check if more judges need to rate this team
    if judge < event_details["numJudges"]:
        next_judge = judge + 1
        message = f"Judge {next_judge}, please rate the team."
        # Render the same judging form with team name pre-filled and judge updated.
        return render_template('index.html', event=event_details, judge=next_judge, team_name=team_name, message=message)
    else:
        # All judges have rated: calculate the final score
        final_score = sum(team_ratings[team_name]) / len(team_ratings[team_name])
        leaderboard.append({"team": team_name, "score": final_score})
        leaderboard.sort(key=lambda x: x["score"], reverse=True)
        last_result = {"team": team_name, "score": final_score}
        # (Optionally clear the ratings for this team if you want to reset state)
        # team_ratings.pop(team_name, None)
        return redirect(url_for('results'))

@app.route('/results')
def results():
    if not last_result:
        return redirect(url_for("index"))
    return render_template('results.html',
                           teamName=last_result["team"],
                           score=last_result["score"],
                           leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
