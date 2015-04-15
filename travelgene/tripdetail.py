__author__ = 'lubron'
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
from bson.json_util import dumps
import operator


@app.route('/trip_detail_main')
def tripdetail():
    newTripInfo = mongo.db['trip'].find({}).sort("trip_id", -1).limit(1);

    activityList = []
    for doc in newTripInfo:
        for activity_id in doc['a_id']:
            ## find target activity
            activity = mongo.db['activity'].find_one({'a_id' : activity_id})
            ## get Destination name
            place = str(activity['place_id']).split("_")[0]
            ## search the collection with given destination name to get the specifity activity place name
            place_name = mongo.db[place].find_one({'place_id' : activity['place_id']})['desc']
            ##### here use place_id to store the name of target place
            activity['place_id'] = place_name
            activityList.append(activity);

    return render_template('trip_detail_main.html', activityList = activityList)
