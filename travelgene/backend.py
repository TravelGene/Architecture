from travelgene import app

from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo

app.config['MONGO2_DBNAME'] = 'nonono'#test second database
mongo1=PyMongo(app, config_prefix='MONGO2')#in this way we could use multiple database
mongo = PyMongo(app)
cors = CORS(app)
@app.route('/test')
def hello_world():
    print app.name
    print mongo.db.Seattle.find_one()
    return "abc"


@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/CreateTrip.html')
def create_trip():
    return render_template('CreateTrip.html')

@app.route('/Activities.html')
def activities():
    print "????????"
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
    allContent = mongo.db[City].find_one();
    result = {};
    result['address'] = allContent['address'];
    result['cato'] = allContent['category_str_list'];
    result['comment'] = allContent['comment'];
    result['name'] = allContent['title'];
    print result;
    return json.dumps(result);

