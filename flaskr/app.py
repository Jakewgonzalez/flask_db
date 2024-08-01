from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cloud")
def cloud_services():
    return render_template('cloud.html')

@app.route("/ICS")
def ics_data():
    return render_template('ics.html')

@app.route("/About")
def about():
    return render_template('about.html')