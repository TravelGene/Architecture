__author__ = 'lubron'
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
import operator





@app.route('/friendlist.html', methods=['GET'])
def showFriendList():
    email = session['username']
    userDB = mongo.db['user']
    targetUser = userDB.find_one({'email' : email})
    friendIdList = targetUser['friend_id']
    tripDB = mongo.db['trip']
    friendObjList = []
    tripDict = {}

    for friendId in friendIdList:
        friendObj = userDB.find_one({'user_id': friendId})
        tripIdList = friendObj['trip_id']
        tripObjList = []
        print tripIdList
        for tripId in tripIdList:
            tripObj = tripDB.find_one({'trip_id':tripId})

            # print tripObj
            if bool(tripObj):
                if bool(tripObj['destination']):
                    if bool(tripDict) == False or tripDict.has_key(str(tripObj['destination'])) == False:
                        tripDict[str(tripObj['destination'])] = 1
                    else:
                        tripDict[str(tripObj['destination'])] += 1
            tripObjList.append(tripObj)
        friendObj['trip_list'] = tripObjList
        friendObjList.append(friendObj)

    sorted_tuple = sorted(tripDict.items(), key = operator.itemgetter(1))
    tripDictSort = dict(sorted_tuple)

    rank = 1
    for tripName in tripDictSort:
        tripDictSort[tripName] = rank
        rank += 1
        if rank == 4:
            break
    print tripDictSort


    return render_template('friendlist.html', friendlist = friendObjList, targetUser = targetUser, tripDictSort = tripDictSort)
