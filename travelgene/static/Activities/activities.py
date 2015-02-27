from travelgene import app
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
    allContent = mongo.db[City].find('a_id':City+"_"+id);    
    result = {};
    result['address'] = allContent['address'];
    result['cato'] = allContent['category_str_list'];
    result['comment'] = allContent['comment'];
    result['name'] = allContent['title'];
    print result;
    return json.dumps(result);