from flask import Flask, render_template, redirect, url_for, request, session
import json
import sqlite3
import db_data
import os

app = Flask(__name__)
app.secret_key = 'SECRET'

def db_conn():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_users():
    users = {}
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    return users

users = get_users()

@app.route("/")
def main_app():
    return render_template('index.html')

@app.route("/account", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users.get(username) == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        return 'Error'
    return render_template('account.html')

@app.route("/welcome")
def welcome():
    if 'username' in session:
        return render_template('welcome.html')
    return redirect(url_for('account'))

@app.route("/home")
def home():
    if 'username' in session:
        return render_template('home.html', username = session['username'])
    return 'You are not logged in'

@app.route("/enviroment")
def env_info():
    if 'username' in session:
        conn = db_conn()
        data = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        return render_template('enviroment.html', username = session['username'], data=data)
    return 'You are not logged in'

@app.route("/update", methods=["GET", "POST"])
def env_update():
    if request.method == "POST":

        id = request.form['id']
        name = request.form['name']
        temp = request.form['temp']
        humidity = request.form['humidity']

        conn = db_conn()
        conn.execute('INSERT INTO users (id, name, temp, humidity) VALUES (?, ?, ?, ?)', (id, name, temp, humidity))
        conn.commit()
        conn.close()
        return redirect(url_for('env_info'))
    return render_template('update.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('account'))

@app.route("/cloud")
def cloud_services():
    return render_template('cloud.html')

@app.route("/ICS")
def ics_data():
    return render_template('ics.html')

@app.route("/about")
def about():
    return render_template('about.html')