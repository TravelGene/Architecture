from travelgene import app
from travelgene import mongo
from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo
import random
from datetime import datetime
from datetime import timedelta
import time
import urllib2


#Author: Qiankun Zhuang
@app.route('/addTrip',methods=['GET'])
def addTrip():

    dest = request.args.get('city');
    date1 = request.args.get('date1');
    date2 = request.args.get('date2');
    placeId = request.args.get('activitiesId')
    # print activitiesId;
    # print 'placeid',placeId
    nTripId = mongo.db['trip'].find({}).count()+1

    destFirst = dest[0].upper()
    dest = destFirst + dest[1: len(dest)].lower()

    activitiesList = placeId.split('$');
    # print activitiesList, " activitiesList"
    nAId = mongo.db['activity'].find({}).count()+1
    aIdList = []
    placeList = []
    for i in range(len(activitiesList)):
        if len(activitiesList[i])==0:
            continue
        place = mongo.db[dest].find_one({'place_id':activitiesList[i]})
        time.sleep(0.5)
        # print place
        # print place['place_type'],'\n\n\n\n\n\n\n\n\n'
        placeList.append(place)
    aIdList = agendaGenerator(placeList,nTripId,nAId,date1)
    newTrip = {
        'trip_id':nTripId,
        'destination':dest,
        'depart_date':date1,
        'return_date':date2,
        'activities':aIdList,
        'img_url':[]
    }
    print newTrip
    print "new ou h"
    mongo.db['trip'].insert(newTrip)

    # print session['user_id'], 'User Session id'
    usrid = session['user_id']
    usr = mongo.db['user'].find_one({'user_id':usrid})
    tripList = usr['trip_list']
    # print tripList, "before"
    tripList.append(nTripId)

    # print tripList, "after"
    n = mongo.db['user'].find_and_modify(query = {'user_id' : usrid},
                                    update = {"$set" : {'trip_list' : tripList}},
                                    upsert = False)
    print 'done'
    return render_template('profilec.html', user = usr)

def agendaGenerator(placeList,nTripId,nAId,date1):
    waypoints = []
    origin = ""
    destination = ""
    for place in placeList:
        # print place['place_type'],'\n\n\n\n\n\n\n\n'
        if(place['place_type']=='hotel'):
            origin = place
            destination = place
        else:
            waypoints.append(place)
    url = "https://maps.googleapis.com/maps/api/directions/json?"+"origin="+origin['address'].strip().replace(' ','+')+"&destination="+destination['address'].strip().replace(' ','+')+"&waypoints=optimize:true";
    for waypoint in waypoints:
        url = url + "|"+waypoint['address'].strip().replace(' ','+')
    key = "AIzaSyB9C0e4iBw9iNWd-g0r7YlsjuOAvbSKM6g"
    url = url + "&key="+key

    hotelActivity = {
        'a_id':nAId,
        'start_time':'default',
        'end_time':'default',
        'place_id':origin['place_id'],
        'trip_id':nTripId
    }
    start_time = datetime.strptime(date1,"%Y-%m-%d")
    start_time = start_time.replace(hour=10)
    end_time = datetime.strptime(date1,"%Y-%m-%d")
    end_time = end_time.replace(hour=22)
    total_time = end_time - start_time
    time_slice = timedelta(seconds = total_time.seconds/len(waypoints))

    rst = url_open(url)
    time.sleep(1)
    if rst == None :
        newOrder = range(len(waypoints))
    else:
        content = json.loads(rst)
        if content['status'] != 'OK':
            newOrder = range(len(waypoints))
        else:
            newOrder = content['routes'][0]['waypoint_order']
    # print type(content['routes'])
    # print content
    print newOrder
    for i in range(len(newOrder)):
        newActivity = {
            'a_id':nAId+i+1,
            'start_time':(start_time+time_slice*i).isoformat(),
            'end_time':(start_time+time_slice*(i+1)).isoformat(),
            'place_id':waypoints[newOrder[i]]['place_id'],
            'trip_id':nTripId
        }
        print newActivity
        #mongo.db['activity'].insert(newActivity)
    

def url_open(pageUrl):
    # print pageUrl
    headers = {  'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  , 'Referer':'https://itunes.apple.com'} 
    req = urllib2.Request(  url = pageUrl,   headers = headers  ) 
    try:
        response = urllib2.urlopen(req)
        contents= response.read()
    except :
        # print error, contents
        return None

    return contents