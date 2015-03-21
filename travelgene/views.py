#author zhiyuel
import os
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



@app.route('/')
@app.route('/index')

#zhiyuel
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return "Hello, World!"

# zhiyuel
@app.route('/tmp.html')
def tmp():
    print "hello world"
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("tmp.html",
        title = 'Home',
        user = user,
        posts = posts)
#Nanjie Chenglie
@app.route('/signup',methods=['POST'])
def signupp():
    email = request.form['email']
    password = request.form['password']
    firstname = request.form['fname']
    lastname = request.form['lname']
    wholename = firstname+ ' ' +lastname
    # after sign up it is sign in
    session['username'] = email
    #print firstname
    #print lastname


    numberOfUser = mongo.db['user'].count()
    resultId = ''

    for x in range(0, 8 - len(str(numberOfUser))):
        resultId = '0' + resultId

    resultId += str(numberOfUser)

    session['user_id'] = resultId

    mongo.db['user'].insert({'user_id':resultId,'user_name':wholename,'password':password,'email':email,'phone':'','birth':'','trip_id':''})
    # zhiyuel: jumps to where????? need to be consistent

    return redirect('index.html')
#Nanjie Chenglie
@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        oh=mongo.db['user']
        email = request.form['email']
        Found=oh.find_one({'email':email})
        passw = Found['password']
        password = request.form['password']
        #update in database
        if passw==password:
            session['username'] = email
            session['user_id'] = mongo.db['user'].find_one({'email': email})['user_id']

            return render_template("profilec.html", username=email)
            #return redirect(url_for('nextPage', id="test"))#param
        else:
            return redirect('Nlogin.html')

@app.route('/test/<id>')
def nextPage(id):
    print id
    return redirect('index.html')
