from flask import Flask, render_template
import json
from db import *
import api

app = Flask(__name__)

@app.route('/')
def index():
  image_path = "static/flag.jpg"
  return render_template('map.html', image_path = image_path)

@app.route('/trends')
def trends():
  image_path = "static/flag.jpg"
  return render_template("trends.html", image_path = image_path)

@app.route('/coordinates_data')
def data():
  return get_all_coordinates()

@app.route('/crashes_data')
def crash():
  return get_all_crashes()

@app.route('/mapboxapikey')
def mapbox():
    return api.get_key_mp()

@app.route('/summary/<planeid>')
def summary(planeid):

  planeid = int(planeid)
  date = get_all_crashes()[planeid][1]
  time = get_all_crashes()[planeid][2]
  location = get_all_crashes()[planeid][3]
  operator = get_all_crashes()[planeid][4]
  route = get_all_crashes()[planeid][5]
  ACtype = get_all_crashes()[planeid][6]
  crew = get_all_crashes()[planeid][7]
  passengers = get_all_crashes()[planeid][8]
  fatalities = get_all_crashes()[planeid][9]
  ground = get_all_crashes()[planeid][10]
  summary = get_all_crashes()[planeid][11]
  image_path = "../static/flag.jpg"

  return render_template('summary.html', date = date, time = time, location = location, operator= operator, route = route, ACtype = ACtype, crew = crew, passengers = passengers, fatalities = fatalities, ground = ground, summary = summary, image_path = image_path)

if __name__ == '__main__':
  app.debug = True
  app.run()
  route_to_stops() #What is this doing? RAAH
