from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rating1 = request.form.get('rating1', 5)  # default to 5
        rating2 = request.form.get('rating2', 5)
        rating3 = request.form.get('rating3', 5)
        rating4 = request.form.get('rating4', 5)
        rating5 = request.form.get('rating5', 5)        
        return redirect(url_for('results'))
    return render_template('index.html')

@app.route('/results')
def results():
   
    
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
