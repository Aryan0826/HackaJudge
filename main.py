from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

WEIGHTS = {
    'rating1': 0.2,   # Innovation and Creativity
    'rating2': 0.25,  # Technical Execution
    'rating3': 0.2,   # Impact and Usefulness
    'rating4': 0.15,  # User Experience and Design
    'rating5': 0.2    # Presentation and Pitch
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rating1 = float(request.form.get('rating1', 5))
        rating2 = float(request.form.get('rating2', 5))
        rating3 = float(request.form.get('rating3', 5))
        rating4 = float(request.form.get('rating4', 5))
        rating5 = float(request.form.get('rating5', 5))

        weighted_average = (
            rating1 * WEIGHTS['rating1'] +
            rating2 * WEIGHTS['rating2'] +
            rating3 * WEIGHTS['rating3'] +
            rating4 * WEIGHTS['rating4'] +
            rating5 * WEIGHTS['rating5']
        )       
        return redirect(url_for('results', score = weighted_average))
    return render_template('index.html')

@app.route('/results')
def results():
    score = request.args.get('score', None)
    try:
        score = float(score)
    except (ValueError, TypeError):
        score = 0
    return render_template('results.html', score = score)

if __name__ == '__main__':
    app.run(debug=True)
