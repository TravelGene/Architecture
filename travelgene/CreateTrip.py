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
import random





#Author: Qiankun Zhuang
@app.route('/addTrip',methods=['GET'])
def addTrip():
    dest = request.args.get('city');
    date1 = request.args.get('date1');
    date2 = request.args.get('date2');
    placeId = request.args.get('activitiesId')
    # print activitiesId;
    print 'placeid',placeId
    nTripId = mongo.db['trip'].find({}).count()+1

    activitiesList = placeId.split('$');
    nAId = mongo.db['activity'].find({}).count()+1
    for i in range(len(activitiesList)):
        if len(activitiesList[i])==0:
            continue
        activitiesList[i] += dest+'_'+activitiesList[i]
        newActivity = {
            'a_id':nAId+i,
            'start_time':'default',
            'end_time':'default',
            'place_id':activitiesList[i],
            'trip_id':nTripId
        }
        mongo.db['activity'].insert(newActivity)
    print "ddddddddddd",activitiesList
    newTrip = {
        'trip_id':nTripId,
        'destination':dest,
        'depart_date':date1,
        'return_date':date2,
        'activities':activitiesList,
        'img_url':[]
    };
    print newTrip,'\n\n\n\n\n\n'
    mongo.db['trip'].insert(newTrip)

    usrid = request.args.get(session['user_id'])
    usr = mongo.db['user'].find({user_id:usrid})
    print usr
    # usr.getTrip_id
    # nTripId = generateTripid
    # usr.updateTrip_id(nTripId)
    print 'done'
    return render_template('profilec.html')

@app.route('/ActivityInfo/<city>')
def retrieveActivity(city):
    tripId = mongo.db[city].distinct('place_id')
    print "zxcvzvvdfasfaf",tripId
    res = ""
    for id in tripId:
        # if (random.random()*100)%2==0:
        res += (id.split('_')[1]+'$')
    print "here::::::::::::::::",res
    return res



    #         city = id.split('_')[0]
    #         result = mongo.db[city].find({place_id:"id"})
    #         print result
    
    
    # res = "";
    # for s in result:
    #     res += (s+'$')
    # print res
    # return res
