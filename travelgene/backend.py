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

# from flask.ext.social import Social
# from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

cors = CORS(app)

@app.route('/test')
def hello_world():
    print app.name
    print mongo.db.Seattle.find_one()
    return "abc"


@app.route('/Nlogin.html')
def unabletologin():
    return render_template('Nlogin.html')


# Lubron
@app.route('/create_trip_new.html', methods = ['GET', 'POST'])
def loadTrip():
    if request.method == 'POST':
        dest = str(request.form['destination'])
        ## store date
        session['goDate'] = request.form['goDate']
        session['returnDate'] = request.form['returnDate']

        destFirst = dest[0].upper()
        refinedDestName = destFirst + dest[1: len(dest)].lower()

        print refinedDestName

        recommendCityObj = mongo.db['city'].find_one({'dest' : refinedDestName})

        return render_template("create_trip_new.html", recommendCityObj=recommendCityObj)

    else:
        return render_template("create_trip_new.html")

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
    
@app.route('/create_trip_new.html')
def createNew():
    return render_template('create_trip_new.html')

