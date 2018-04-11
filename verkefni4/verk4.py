from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/leikarar')
def leikarar():
    return render_template('leikarar.html')

@app.route('/form')
def form():
    return render_template('form.html')

app.run()

