from travelgene import app
from travelgene import mongo
from flask import Flask, render_template, session, redirect, url_for, escape, request, jsonify
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
# @app.route('/trip_detail_main.html')
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
    # aIdList = List[0]
    # routeLocationInfo = List[1];

    print "asdfsdasddgrf",aIdList
    newTrip = {
        'trip_id':nTripId,
        'destination':dest,
        'depart_date':date1,
        'return_date':date2,
        'a_id':aIdList,
        'img_url':[]
    }
    print newTrip
    print "new ou h"
    mongo.db['trip'].insert(newTrip)

    # print session['user_id'], 'User Session id'
    usrid = session['user_id']
    # print usrid
    usr = mongo.db['user'].find_one({'user_id':usrid})
    tripList = usr['trip_list']
    # print tripList, "before"
    tripList.append(nTripId)
    ## update trip list in user collection
    # print tripList, "after"
    n = mongo.db['user'].find_and_modify(query = {'user_id' : usrid},
                                    update = {"$set" : {'trip_list' : tripList}},
                                    upsert = False)
    print 'done'

    #return render_template('trip_detail_main.html', activityList = activityList, routeLocationInfo = routeLocationInfo)
    print aIdList

    return redirect(url_for('tripdetail'))



def agendaGenerator(placeList,nTripId,nAId,date1):
    if len(placeList) == 0:
        return []
    waypoints = []
    origin = ""
    destination = ""
    print len(placeList)
    for place in placeList:
        print place['place_type'],'\n\n\n\n\n\n\n\n'
        if(place['place_type']=='hotel') and len(origin)==0:
            origin = place
            destination = place
            hotelActivity = {
                'a_id':nAId,
                'start_time':'',
                'end_time':'',
                'place_id':origin['place_id'],
                'trip_id':nTripId,
                'place_type' : 'hotel'
            }
            mongo.db['activity'].insert(hotelActivity)
        else:
            waypoints.append(place)
    if len(origin) == 0:
        origin = waypoints[0]
        destination = waypoints[-1]
    if len(waypoints) == 0:
        return
    url = "https://maps.googleapis.com/maps/api/directions/json?"+"origin="+origin['address'].strip().replace(' ','+')+"&destination="+destination['address'].strip().replace(' ','+')+"&waypoints=optimize:true";
    for waypoint in waypoints:
        url = url + "|"+waypoint['address'].strip().replace(' ','+')
    key = "AIzaSyB9C0e4iBw9iNWd-g0r7YlsjuOAvbSKM6g"
    url = url + "&key="+key

    
    start_time = datetime.strptime(date1,"%Y-%m-%d")
    start_time = start_time.replace(hour=10)
    end_time = datetime.strptime(date1,"%Y-%m-%d")
    end_time = end_time.replace(hour=22)
    total_time = end_time - start_time
    time_slice = timedelta(seconds = total_time.seconds/(len(waypoints)))
    
    ## route information
    rst= url_open(url)

    locationInfo = []
    time.sleep(1)
    if rst == None :
        newOrder = range(len(waypoints))
    else:
        content = json.loads(rst)
        if content['status'] != 'OK':
            print 'google not ok'
            newOrder = range(len(waypoints))
            
        else:
            newOrder = content['routes'][0]['waypoint_order']
                        ## process route information to get the begin, end, waypoints lat and lng
            print 'new order:',newOrder

    aIdList = []
    if origin != waypoints[0]:
        aIdList.append(nAId)
    for i in range(len(newOrder)):
        newActivity = {
            'a_id':nAId+i+1,
            'start_time':(start_time+time_slice*i).isoformat().replace("T", " "),
            'end_time':(start_time+time_slice*(i+1)).isoformat().replace("T", " "),
            'place_id':waypoints[newOrder[i]]['place_id'],
            'trip_id':nTripId,
            'place_type' : waypoints[newOrder[i]]['place_type']
        }
        aIdList.append(nAId+i+1)
        print newActivity
        mongo.db['activity'].insert(newActivity)
    # result = []
    # result.append(aIdList)
    # result.append(locationInfo)
    return aIdList

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