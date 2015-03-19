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


cors = CORS(app)
@app.route('/test')
def hello_world():
    print app.name
    print mongo.db.Seattle.find_one()
    return "abc"


@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/Nlogin.html')
def unabletologin():
    return render_template('Nlogin.html')


@app.route('/CreateTrip.html', methods = ['GET'])
def loadTrip():
    dest = request.args.get('destination')
    date1 = request.args.get('goDate')
    date2 = request.args.get('returnDate')
    print dest,date1,date2;
    return render_template("CreateTrip.html", dest=dest, date1 = date1, date2 = date2)

@app.route('/Activities',methods=['GET'])
def toActivity():
    city=str(request.args.get('city'));
    id=request.args.get('id');
    return render_template("Activities.html",city=city,id=id);
    #zhiyuel: here jumps to nothing!!!!


@app.route('/trip_detail_main.html')
def tripdetail():
    return render_template('trip_detail_main.html')

@app.route('/profilec.html')
def profiles():
    return render_template('profilec.html')



@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/calendar.html')
def calendar():
    return render_template('calendar.html')
    


