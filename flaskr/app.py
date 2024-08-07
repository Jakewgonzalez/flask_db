from flask import Flask, render_template, redirect, url_for, request, session, jsonify # type: ignore
import sqlite3
from werkzeug.security import check_password_hash # type: ignore
from datetime import datetime, timezone

app = Flask(__name__)
app.secret_key = 'SECRET'

def db_conn():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def main_app():
    return render_template('index.html')

@app.route("/account", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = db_conn()
        user = conn.execute('SELECT * FROM profile WHERE username = ?', (username,)).fetchone()
        
        if user and check_password_hash(user['password_hash'], password):

            conn.execute('UPDATE profile SET last_login = ? WHERE username = ?', (datetime.now(timezone.utc), username))
            conn.commit()
            conn.close()
                    
            session['username'] = username
            return redirect(url_for('welcome'))
                
        conn.close()
        return 'Error: Invalid username or password'

    return render_template('account.html')

@app.route("/welcome")
def welcome():
    if 'username' in session:
        conn = db_conn()
        user = conn.execute('SELECT last_login FROM profile WHERE username = ?', (session['username'],)).fetchone()
        conn.close()
        
        last_login = user['last_login'] if user else None
        return render_template('welcome.html', username=session['username'], last_login=last_login)
    return redirect(url_for('account'))

@app.route("/home")
def home():
    if 'username' in session:
        conn = db_conn()
        user = conn.execute('SELECT last_login FROM profile WHERE username = ?', (session['username'],)).fetchone()
        conn.close()
        
        last_login = user['last_login'] if user else None
        return render_template('home.html', username=session['username'], last_login=last_login)
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
    if 'username' in session:
        if session['username'] =='admin':
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
        else:
            return 'Only Admin can access this page'
    return 'You are not logged in'

@app.route("/delete", methods=["GET", "POST"])
def env_delete():
    if 'username' in session:
        if session['username'] =='admin':
            if request.method == "POST":

                id = request.form['id']

                conn = db_conn()
                conn.execute('DELETE FROM users WHERE id = ?', (id,))
                conn.commit()
                conn.close()
                return redirect(url_for('env_info'))
            return render_template('delete.html')
        else:
            return 'Only Admin can access this page'
    return 'You are not logged in'

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

@app.route("/chart")
def chart():
    chart_data = {
        'labels': ['AWS', 'Google', 'Oracle'],
        'datasets': [{
            'label': 'Up Time',
            'data': [98, 97, 95],
            'backgroundColor': ['rgba(75, 192, 192, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)'
            ],
            'borderColor': ['rgba(75, 192, 192, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)'
            ],
            'borderWidth': 1
        }]
    }
    return jsonify(chart_data)