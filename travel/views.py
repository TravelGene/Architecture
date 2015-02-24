from travel import app
from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo

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