from flask import Flask
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
client = MongoClient('localhost', 27017)
db = client['travel']
app = Flask("travel")
cors = CORS(app)
@app.route('/')
def hello_world():
    return app.name

@app.route('/user/<mm>')
def user_profile(mm):
    response = db[mm]
    print db.collection_names()
    return str(response.find_one())

@app.route('/CityInfo/<City>/<para>')
def get_info(City,para):
    response = db[City]
    allContent = response.find_one();
    result = {};
    result['address'] = allContent['address'];
    result['cato'] = allContent['category_str_list'];
    result['comment'] = allContent['comment'];
    result['name'] = allContent['title'];
    return json.dumps(result);



@app.route('/t/<tt>')
def hello_world2(tt):
    return tt

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = '<replace with a secret key>'
    toolbar = DebugToolbarExtension(app)
    app.run()
