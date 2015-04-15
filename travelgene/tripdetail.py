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
    routeLocationInfo = []
    for doc in newTripInfo:
        for activity_id in doc['a_id']:
            ## find target activity
            activity = mongo.db['activity'].find_one({'a_id' : activity_id})
            ## get Destination name
            place = str(activity['place_id']).split("_")[0]
            ## search the collection with given destination name to get the specifity activity place name
            place_name = mongo.db[place].find_one({'place_id' : activity['place_id']})['desc']

            ## get geo info
            geo = mongo.db[place].find_one({'place_id' : activity['place_id']})['google_geometry'][0]['geometry']['location']
            # print geo, "geogeogeogeogeogeogeogeogeogeogeogeogeo"

            ##### here use place_id to store the name of target place
            activity['place_id'] = place_name
            activityList.append(activity)
            routeLocationInfo.append(geo)

            # print activity['place_type'], "typetypetypetypetypetypetypetypetype"

            ## find lat and lng in Seattle collection
            



    # listPlaceOnRoute = content['routes'][0]['legs']

    # ## store spots location info along the road
    # #print " the length of list place on route "
    # ## extract from listPlaceOnRoute
    # for item in listPlaceOnRoute:
    #     newPlaceLocation = {}
    #     newPlaceLocation['start_location'] = {}
    #     newPlaceLocation['start_location']['lat'] = item['start_location']['lat']
    #     newPlaceLocation['start_location']['lng'] = item['start_location']['lng']
    #     newPlaceLocation['end_location'] = {}
    #     newPlaceLocation['end_location']['lat'] = item['end_location']['lat']
    #     newPlaceLocation['end_location']['lng'] = item['end_location']['lng']
    #             locationInfo.append(newPlaceLocation)

    # routeLocationInfo = session['routeLocationInfo'] 
    
    # print routeLocationInfo, "routeLocationInfo"
    
    # print "\n\n\n\n"
    
    # print activityList, "activityList"

    return render_template('trip_detail_main.html', activityList = activityList, routeLocationInfo = routeLocationInfo)
