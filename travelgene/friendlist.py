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




@app.route('/friendlist.html', methods=['GET'])
def showFriendList():
    email = session['username']
    userDB = mongo.db['user']
    targetUser = userDB.find_one({'email' : email})
    friendIdList = targetUser['friend_id']
    tripDB = mongo.db['trip']
    friendObjList = []
    for friendId in friendIdList:
        friendObj = userDB.find_one({'user_id': friendId})
        tripIdList = friendObj['trip_id']
        tripObjList = []
        for tripId in tripIdList:
            tripObj = tripDB.find_one({'trip_id':tripId})
            tripObjList.append(tripObj)
        friendObj['trip_list'] = tripObjList
        friendObjList.append(friendObj)



    return render_template('friendlist.html', friendlist = friendObjList, targetUser = targetUser)
