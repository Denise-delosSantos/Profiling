from flask import Flask, render_template, request
import urllib.parse
import requests
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        try:
            username =request.form['user']
            password =request.form['password']
            
            with sql.connect("profile.db") as con:
                cur = con.cursor()
                statement = f"SELECT user from students WHERE user='{email_add}' AND password='{password}';"
                cur.execute(statement)
                if not cur.fetchone():
                    print("Login Failed")
                else:
                    print("Welcome")
        except:
            con.rollback()
        
        finally:
            return render_template("login.html")
            con.close()

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/addrec',methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            student_id = request.form['student_id']
            email = request.form['email']
            password = request.form['password']

            with sql.connect("profile.db") as con:
                cur = con.cursor()

                cur.execute("""INSERT INTO students (student_id, email_add, password) VALUES (?,?,?)""",(student_id,email,password))
                con.commit()
        except:
            con.rollback()
        
        finally:
            return render_template("login.html")
            con.close()

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
    app.run(host="0.0.0.0", port=8080)