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

        mongo.db['user'].find_and_modify(query = {'email' : session['username']},
                                            update = {"$set" : {'password' : pwd}},
                                            upsert = True)

        return render_template('profilec.html')
    else:
        return render_template('editprofile.html')



        #/<String:pwd>/<String:repwd>/<String:gender>

# @app.route('/editprofile.html')
# def showEditProfile():

