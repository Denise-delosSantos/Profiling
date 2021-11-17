from flask import Flask, render_template, request
import urllib.parse
import requests
import sqlalchemy as db

app = Flask(__name__)
engine = db.create_engine('sqlite:///test.sqlite') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

Student = db.Table('StudentData', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('yearlvl', db.String(5),nullable=False),
              db.Column('password', db.String(255), default=True)
              )

metadata.create_all(engine) #Creates the table

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
    app.run(host="0.0.0.0", port=2020)