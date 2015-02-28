
from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo=PyMongo(app);
from travelgene import views
from travelgene import backend
from travelgene import activities

