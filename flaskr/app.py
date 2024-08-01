from flask import Flask, render_template, redirect, url_for, request, session
import json
import os

app = Flask(__name__)
app.secret_key = 'SECRET'

def get_users():
    users = {}
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    return users

users = get_users()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/account", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users.get(username) == password:
            session['username'] == username
            return redirect(url_for('welcome'))
        return 'Error'
    return render_template('account.html')

@app.route("/welcome")
def welcome():
    if 'username' in session:
        return f'logged in as {session["username"]}', render_template('welcome.html')
    return render_template('welcome.html')

@app.route("/enviroment")
def env_info():
    if username in session:
        username = session['username']
        return render_template('enviroment.html')
    return 'You are not logged in'

@app.route("/cloud")
def cloud_services():
    return render_template('cloud.html')

@app.route("/ICS")
def ics_data():
    return render_template('ics.html')

@app.route("/about")
def about():
    return render_template('about.html')