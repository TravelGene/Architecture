#author qiqis
import os
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

# client = MongoClient('localhost', 27017)
# db = client['travelgene']


def getMonth(str):
    monthMap = {}
    monthMap['01'] = 'Jan'
    monthMap['02'] = 'Feb'
    monthMap['03'] = 'Mar'
    monthMap['04'] = 'Apr'
    monthMap['05'] = 'May'
    monthMap['06'] = 'Jun'
    monthMap['07'] = 'Jul'
    monthMap['08'] = 'Aug'
    monthMap['09'] = 'Sep'
    monthMap['10'] = 'Oct'
    monthMap['11'] = 'Nov'
    monthMap['12'] = 'Dec'
    return monthMap[str]


@app.route('/profilec.html',methods=['GET'])
def showProfilec():
    # print session,"profilec"
    email = session['username']
    userDB = mongo.db['user']
    targetUser = userDB.find_one({'email' : email})

    tripIDList = targetUser['trip_id']
    tripDB = mongo.db['trip']

    # judge whether same person has gone to same place several times
    tripDictSet = set()

    cityNumber=0

    # print "show profile"

    tripObjList = []
    for tripId in tripIDList:
        tripObj = tripDB.find_one({'trip_id':tripId})
      #print tripObj

        # print tripObj

        if bool(tripObj): # if this trip is not none
            if str(tripObj['destination']) not in tripDictSet :
                cityNumber+=1
            else:
                tripDictSet.add(str(tripObj['destination']))


            tripInfo = mongo.db['city'].find_one({'dest' :str(tripObj['destination'])})
            # print tripInfo
            tripObj['img_url'] = tripInfo['img_url']
            tripObj['attraction'] = tripInfo['attraction']
            date = str(tripObj['depart_date']).split(" ")[0]
            dateResult = getMonth(date.split("-")[1])
            dateResult += ', '
            dateResult += date.split("-")[0]
            tripObj['depart_date'] = dateResult


        tripObjList.append(tripObj)


    return render_template('profilec.html',user = targetUser, tripList = tripObjList,cityNumber=cityNumber)