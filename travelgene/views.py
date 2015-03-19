#author zhiyuel
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


client = MongoClient('localhost', 27017)

db = client['travelgene']

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
    email = request.form['Email or mobile number']
    password = request.form['New password']
    firstname = request.form['First name']
    lastname = request.form['Last name']
    wholename = firstname+lastname

    #print firstname
    #print lastname
    print wholename
    print password

    print email

    db.user.insert({'user_id':'1','user_name':wholename,'password':password,'email':email,'phone':'','birth':'','trip_id':''})
    # zhiyuel: jumps to where????? need to be consistent

    return redirect('CreateTrip.html')
#Nanjie Chenglie
@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        oh=db['user']
        email = request.form['email']
<<<<<<< HEAD

        cont=mongo.db.user.find_one()
        print cont
        print '======'

        Found=oh.find({'email':email})
        dictt=dumps(Found)
        passw=dictt.split("password")[1].split(",")[0].split("\"")[2]
=======
        Found=oh.find_one({'email':email})
        passw = Found['password']
>>>>>>> origin/master
        password = request.form['password']
        #update in database
        if passw==password:
            print "yesyesyes"
            session['username'] = email
            print session['username']
            return render_template("profilec.html", username=email)
            #return redirect(url_for('nextPage', id="test"))#param
        else:
            print "nononononononono"
            return redirect('Nlogin.html')

@app.route('/test/<id>')
def nextPage(id):
    print id
    return redirect('index.html')
