from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

event_details = {}
leaderboard = []
last_result = {}

def calculate_score(ratings):
    return sum(ratings) / len(ratings)

@app.route("/", methods=["GET", "POST"])
def home():
    global event_details
    if request.method == "POST":
        event_details = {
            "name": request.form["eventName"],
            "date": request.form["eventDate"],
            "teams": int(request.form["numTeams"]),
            "criteria": request.form.getlist("criteria[]")
        }
        return redirect(url_for("index"))
    return render_template("admin.html")

@app.route('/judging', methods=['GET', 'POST'])
def index():
    global last_result
    if not event_details:
        return redirect(url_for("home"))
    if request.method == 'POST':
        team_name = request.form["teamName"]
        ratings = []
        for i, _ in enumerate(event_details["criteria"], start=1):
            rating = int(request.form.get(f"rating{i}"))
            ratings.append(rating)
        score = calculate_score(ratings)
        leaderboard.append({"team": team_name, "score": score})
        leaderboard.sort(key=lambda x: x["score"], reverse=True)
        last_result = {"team": team_name, "score": score}
        return redirect(url_for('results'))
    return render_template('index.html', event=event_details)

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
