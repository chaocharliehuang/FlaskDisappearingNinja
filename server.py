from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('tmnt.html')

@app.route('/ninja/<color>')
def each_ninja(color):
    return render_template('ninja.html', color=color)

app.run(debug=True)