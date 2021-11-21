from flask import Flask, render_template, request
import urllib.parse
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        username =request.form['user']
        password =request.form['password']
    return render_template('login.html')

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/page')
def page():
    return render_template('main.html')

@app.route('/hard')
def hard():
    return render_template('hard.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)