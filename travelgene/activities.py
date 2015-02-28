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

@app.route('/CityInfo/<City>/<id>')
def get_info(City,id):  
    idval = City+"_"+id;
    print idval;
    allContent = mongo.db[City].find_one({'a_id' : str(idval)});  
    print allContent;
    result = {};
    result['address'] = allContent['address'];
    result['cato'] = allContent['category_str_list'];
    result['comment'] = allContent['comment'];
    result['name'] = allContent['title'];
    return json.dumps(result);