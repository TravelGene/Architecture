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




@app.route('/friendlist.html', methods=['GET'])
def showFriendList():
    email = session['username']
    userDB = mongo.db['user']
    targetUser = userDB.find_one({'email' : email})
    friendIdList = targetUser['friend_id']
    tripDB = mongo.db['trip']
    # store friends info and their trip info
    friendObjList = []
    # store most 3 popular trip
    tripDict = {}
    # store information of 3 most popular trip
    tripInfoDict ={}

    for friendId in friendIdList:
        friendObj = userDB.find_one({'user_id': friendId})
        tripIdList = friendObj['trip_id']
        tripObjList = []

        # judge whether same person has gone to same place several times
        tripDictSet = {}

        for tripId in tripIdList:
            tripObj = tripDB.find_one({'trip_id':tripId})

            #print tripObj
            if bool(tripObj): # if this trip is not none
                if bool(tripDict) == False or tripDict.has_key(str(tripObj['destination'])) == False:# check this trip has been in dict
                    tripDict[str(tripObj['destination'])] = 1
                    # this person has gone to here
                    tripDictSet[str(tripObj['destination'])] = 1
                elif bool(tripDictSet) == False or tripDictSet.has_key(str(tripObj['destination'])) == False:
                    tripDict[str(tripObj['destination'])] += 1
                    tripDictSet[str(tripObj['destination'])] = 1
                tripInfo = mongo.db['city'].find_one({'dest' :str(tripObj['destination'])})
                tripObj['img_url'] = tripInfo['img_url']
                tripObj['attraction'] = tripInfo['attraction']
                date = str(tripObj['depart_date']).split(" ")[0]
                dateResult = getMonth(date.split("-")[1])
                dateResult += ', '
                dateResult += date.split("-")[0]
                tripObj['depart_date'] = dateResult


            tripObjList.append(tripObj)

        friendObj['trip_list'] = tripObjList
        friendObjList.append(friendObj)

    # sort the trip by their value
    #print tripDict
    sorted_tuple = sorted(tripDict.items(), key = operator.itemgetter(1), reverse = True)
    if bool(sorted_tuple):
        # get the most 3 popular
        rank = 1
        for tripName in sorted_tuple:
            cityName = str(tripName).split("\'")[1] # get the city name from string ('Seattle', 1)
            # find the city info in the city collection
            tripInfo = mongo.db['city'].find_one({'dest' : cityName})
            if tripInfo:
                tripInfoDict[rank] = tripInfo
                rank += 1
                if rank == 4:
                    break

    print tripInfoDict


    return render_template('friendlist.html', friendlist = friendObjList, targetUser = targetUser, tripDictSort = tripInfoDict)
