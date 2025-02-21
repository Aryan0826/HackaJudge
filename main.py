from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Example list of hackathon projects
projects = [
    {"name": "Project Alpha", "score": None, "comment": ""},
    {"name": "Project Beta", "score": None, "comment": ""},
    {"name": "Project Gamma", "score": None, "comment": ""}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        for project in projects:
            # Retrieve score and comment for each project
            score_value = request.form.get(f'score_{project["name"]}')
            comment_value = request.form.get(f'comment_{project["name"]}', '')
            try:
                project["score"] = float(score_value) if score_value else 0
            except ValueError:
                project["score"] = 0  # Default to 0 on invalid input
            project["comment"] = comment_value
        return redirect(url_for('results'))
    return render_template('index.html', projects=projects)

@app.route('/results')
def results():
    # Sort projects by score (highest first)
    sorted_projects = sorted(projects, key=lambda x: x["score"], reverse=True)
    return render_template('results.html', projects=sorted_projects)

if __name__ == '__main__':
    app.run(debug=True)
