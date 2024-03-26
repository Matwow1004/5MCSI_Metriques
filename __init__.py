from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>La page contact d'Anas Mekkaoui</h2>"

@app.route("/contactt/")
def MaPremiereAPI2():
     return render_template('contactt.html')

  
@app.route('/')
def hello_world():
    return render_template('hello.html')

from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# GitHub API endpoint for fetching commits
GITHUB_API_URL = "https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/commits/')
def commits():
    commit_data = get_commit_data()
    return render_template('commits.html', commit_data=commit_data)

def get_commit_data():
    response = requests.get(GITHUB_API_URL)
    if response.status_code == 200:
        commit_data = response.json()
        minutes_data = extract_minutes(commit_data)
        return minutes_data
    else:
        return None

def extract_minutes(commit_data):
    minutes_data = {}
    for commit in commit_data:
        date_string = commit.get('commit', {}).get('author', {}).get('date')
        if date_string:
            date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
            minutes = date_object.minute
            if minutes in minutes_data:
                minutes_data[minutes] += 1
            else:
                minutes_data[minutes] = 1
    return minutes_data

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")
  
@app.route("/histogramme/")
def mongraphique2():
    return render_template("histogramme.html")
  
if __name__ == "__main__":
  app.run(debug=True)
