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

@app.route('/ActivityInfo/<place_id>')
def get_info(place_id):
    City = place_id.split('_')[0]
    allContent = mongo.db[City].find_one({'place_id' : str(place_id)})
    print allContent
    return render_template("Activities.html",city=allContent);
