from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('checkin.html')

@app.route('/code-check')
def codecheck():
    return render_template('code-check.html')

@app.route('/code-enter')
def codeenter():
    return render_template('code-enter.html')
