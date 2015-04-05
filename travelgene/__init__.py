# @modified: zhiyuel
from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo
from flask_oauth import OAuth

app = Flask(__name__)
# connect to another MongoDB server altogether
app.config['MONGO3_URI']='mongodb://travelgene:genetravel@ds031107.mongolab.com:31107/travelgene'
app.config['MONGO3_HOST'] = 'ds031107.mongolab.com'
app.config['MONGO3_PORT'] = 31107
app.config['MONGO3_DBNAME'] = 'travelgene'
app.config['MONGO3_USERNAME']='travelgene'
app.config['MONGO3_PASSWORD']='genetravel'
cors = CORS(app)
mongo = PyMongo(app, config_prefix='MONGO3')

mongolocal=PyMongo(app)

oauth = OAuth()

# from travelgene import *
from travelgene import views
from travelgene import backend
from travelgene import activities
from travelgene import CreateTrip
from travelgene import friendlist

from travelgene import editprofile

from travelgene import profilec

from travelgene import editprofile

from travelgene import loginFB

