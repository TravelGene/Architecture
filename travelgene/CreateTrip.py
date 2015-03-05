from travelgene import app
from travelgene import mongo
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
    if request.method == 'GET':
        dest = request.args.get('city');
        date1 = request.args.get('date1');
        date2 = request.args.get('date2');
        activitiesId = request.args.get('activitiesId');
        usrid = request.args.get('userid');
        activitiesList = activitiesId.split('$');
        newTrip = {
            'dest':dest,
            'startdate':date1,
            'endate':date2,
            'activities':activitiesList,
        };
        print newTrip+'\n\n\n\n\n\n';
        mongo.db[usrid].insert(newTrip);
        print 'done';


@app.route('/ActivityInfo/<city>/<id>')
def retrieveActivity(city, id):
    print
    result = mongo.db[city].find_one({'id':id});
    rst = {};
    print result['name'];
    rst['name']=result['name'];
    return json.dump(rst);