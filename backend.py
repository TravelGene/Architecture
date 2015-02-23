from flask import Flask, render_template
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
client = MongoClient('localhost', 27017)
db = client['travel']
app = Flask("travel")
cors = CORS(app)
@app.route('/')
def hello_world():
    return app.name
def homeP():
    Seattles = mongo.db.Seattle.find()
    print(type(Seattles))
    return str(Seattles)

@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/CreateTrip.html')
def create_trip():
    return render_template('CreateTrip.html')

@app.route('/Activities.html')
def activities():
    return render_template('Activities.html')

@app.route('/trip_detail_main.html')
def tripdetail():
    return render_template('trip_detail_main.html')

@app.route('/profilec.html')
def profiles():
    return render_template('profilec.html')

@app.route('/friendlist.html')
def friendlist():
    return render_template('friendlist.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/calendar.html')
def calendar():
    return render_template('calendar.html')
    
@app.route('/CityInfo/<City>/<para>')
def get_info(City,para):
    response = db[City]
    allContent = response.find_one();
    result = {};
    result['address'] = allContent['address'];
    result['cato'] = allContent['category_str_list'];
    result['comment'] = allContent['comment'];
    result['name'] = allContent['title'];
    return json.dumps(result);

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = '<replace with a secret key>'
    toolbar = DebugToolbarExtension(app)
    app.run()
