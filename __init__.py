<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Évolution des températures de Tawarano</title>
  <!-- Charger la bibliothèque Google Charts -->
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script type="text/javascript">
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ['Année', 'Température (°C)'],
        ['2019', 25],
        ['2020', 26],
        ['2021', 24],
        ['2022', 27],
        // Ajoutez vos données ici
      ]);

      var options = {
        title: 'Évolution des températures de Tawarano',
        legend: { position: 'none' },
        vAxis: { title: 'Température (°C)' },
        hAxis: { title: 'Année' },
        colors: ['#3366CC'], // Couleur des colonnes
        chartArea: { width: '50%' }, // Ajuster la largeur de la zone de tracé
        bar: { groupWidth: '50%' } // Ajuster la largeur des colonnes
      };

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }
  </script>
</head>
<body>
  <!-- Div où le graphique sera affiché -->
  <div id="chart_div" style="width: 900px; height: 500px;"></div>
</body>
</html>
from flask import Flask, rendertemplatestring, rendertemplate, jsonify
from flask import rendertemplate
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3

app = Flask(name)

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route("/contacts/")
def moncontact():
    return render_template("contact.html")

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

@app.route("/Histogramme/")
def mongraphique2():
    return render_template("Histogramme.html")

@app.route('/extract-minutes/<date_string>')
def extract_minutes(date_string):
        date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
        minutes = date_object.minute
        return jsonify({'minutes': minutes})

@app.route("/com/")
def moncommit():
    return render_template("commit.html")


@app.route('/')
def hello_world():
    return render_template('hello.html')

if __name == "__main":
  app.run(debug=True)
