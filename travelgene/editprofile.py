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


@app.route('/editprofile.html', methods=['GET','POST'])
def editProfilePostInfo():
    if request.method == 'POST':
        pwd = request.form['password']

        targetUser = mongo.db['user'].find_one({'email' : session['username']})

        n = mongo.db['user'].update({'email' : session['username']}, {'user_id' : targetUser['user_id'], 'user_name' : targetUser['user_name'], 'password' : pwd,
                                 'email' : targetUser['email'], 'birth' : targetUser['birth'], 'friend_id' : targetUser['friend_id'],
                                 'trip_list' : targetUser['trip_list'], 'icon_url' : targetUser['icon_url'], 'user_id' : targetUser['user_name'],
                                 'phone' : targetUser['phone']}, True)

        return render_template('profilec.html')
    else:
        return render_template('editprofile.html')



        #/<String:pwd>/<String:repwd>/<String:gender>

# @app.route('/editprofile.html')
# def showEditProfile():

