from travel import app
from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo

#Author: Qiankun Zhuang
@app.route('/addActivity/<City>/<id>')
def addActivity(City,id):
	mongo.db[City].get_one('id':id);
	mongo.db[username].insert();
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return "Hello, World!"