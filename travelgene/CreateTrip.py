from travel import app
from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo

#Author: Qiankun Zhuang
@app.route('/addTrip',methods=['GET'])
def addTrip():
	dest = request.args.get('city');
    date = request.args.get('date');
    activitiesId = request.args.get('activitiesId');
    usrid - request.args.get('userid');
    activitiesList = activitiesId.split('$');
    newTrip = {
    	'dest':dest,
    	'date':date,
    	'activities':activitiesList,
    };
    mongo.db[usrid].insert(newTrip);


@app.route('/addActivity/<City>/<id>')
def addActivity(City,id):
	mongo.db[City].find_one('id':id);
	mongo.db[username].update();
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return "Hello, World!"

@app.route('/ActivityInfo/<city>/<id>')
def retrieveActivity(city, id):
	result = mongo.db[city].find_one('id':id);
	rst = {};
	rst['name']=result['name'];
	return json.dump(rst);