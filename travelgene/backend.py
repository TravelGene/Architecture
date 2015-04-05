from travelgene import app

from travelgene import mongo
from flask import Flask, render_template, session, redirect, url_for, escape, request, jsonify
import json
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo
import monkapi
import testmonk


# from flask.ext.social import Social
# from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

cors = CORS(app)

@app.route('/test')
def hello_world():
    print app.name
    print mongo.db.Seattle.find_one()
    return "abc"



@app.route('/index')
def logOut():
    session['username'] = None
    print "qiu cheng gong"
    return render_template('index.html')

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

        # transform into first letter upper then lower
        destFirst = dest[0].upper()
        refinedDestName = destFirst + dest[1: len(dest)].lower()

        session['dest'] = refinedDestName;

        # print refinedDestName
        if monkapi.is_initialized == False:
            monkapi.init_monk()
        recommendCityObj = monkapi.get_recommended_place(refinedDestName)

        for r in recommendCityObj:
            print r


        # print recommendCityObj
        # print session,"session in backend"
        tripInfoList = {}
        tripInfoList['dest'] = refinedDestName
        tripInfoList['goDate'] = request.form['goDate']
        tripInfoList['returnDate'] = request.form['returnDate']
        return render_template("create_trip_new.html", recommendCityObj=recommendCityObj, tripInfoList = tripInfoList)

    else:
        return render_template("create_trip_new.html")


# update recommend list with ajax
@app.route('/update_recommend_list')
def add_numbers():
    dest = session['dest']
    place_id = request.args.get('place_id')
    value = request.args.get('value','Y')

    print place_id, "place_id"
    print value, "value"
    print dest, "dest"
    newlist = monkapi.update_recommended_place(dest, place_id, value)
    # print "newlist newlist newlist\n\n",newlist
    # return jsonify(new_place=[i.serialize for i in newlist])
    return json.dumps(newlist)



@app.route('/Activities',methods=['GET'])
def toActivity():
    city=str(request.args.get('city'));
    id=request.args.get('id');
    return render_template("Activities.html");
    #zhiyuel: here jumps to nothing!!!!


# @app.route('/trip_detail_main.html')
# def tripdetail():
#     return render_template('trip_detail_main.html')

@property
def serialize(self):
    return {
        "place_id" : self.place_id,
        "img_url" : self.img_url,
        "desc" : self.desc
    }

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/calendar.html')
def calendar():
    return render_template('calendar.html')
    
# Author: Qiankun
@app.route('/testmonk.html')
def monktest():
    monkapi.init_monk()
    monkapi.init_database()
    ent_id = monkapi.get_entity_id('Seattle','Seattle_00000006')
    # monkapi.add_label(ent_id,'likeTravel','Y')
    monkapi.add_label(ent_id,'place_type','restaurant')
    return render_template('testmonk.html',result='ok')
    

