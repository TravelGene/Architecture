import sys
sys.path.append("travelgene/pymonk-master/")
from travelgene import app
from travelgene import mongo
from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo
import random
import monk.core.api as ms
from monk.roles.configuration import default_config
from monk.math.cmath import sign0

is_initialized = False
def init_database():
	ents = ms.convert_entities()
	[ent.save() for ent in ents]

def init_monk():
	config=default_config()
	ms.initialize(default_config())
	is_initialized = True
        likeTS = ms.yaml2json('travelgene/pymonk-master/examples/turtle_scripts/turtle_like.yml')
	# print likeTS
	likeT = ms.create_turtle(likeTS)
	likeT.save()

def add_label(ent_id,field,value):
	ent = ms.load_entity(ent_id)
	ent._setattr(field,value)
	ms.crane.entityStore.save_one(ent)

def add_data_to_model(turtle_name,ent_id,creator='monk'):
	ms.add_data(turtle_name,creator,ent_id);

def train(turtleName,creator='monk'):
    trainer = ms.load_turtle(turtleName,creator)
    trainer.train()
    return trainer

def predict(trainer,ent_id,creator='monk'):#How?
    ent = ms.load_entity(ent_id)
    return sign0(trainer.pandas[0].predict(ent))

def get_recommended_place(collection_name):  
	#print collection_name
	ents = ms.load_entities(query={'likeTravel':'Y'},skip=0,num=10,collectionName = collection_name)
	rst = []
	for ent in ents:
		e = {}
		e['place_id'] = ent.place_id
		e['img_url'] = ent.img_url
		e['desc'] = ent.desc
		rst.append(e)
	return rst

def update_recommended_place(creator,collection_name,place_id,value):
        user_turtle = 'likeTravel'
        likeTS = ms.yaml2json('travelgene/pymonk-master/examples/turtle_scripts/turtle_like.yml')

        likeT = ms.create_turtle(likeTS)
        likeT.save()
					# get turtle name from creator? need to updpate database 'user'
    # print collection_name, "collection"
	ent_id = get_entity_id(collection_name,place_id)
	add_label(ent_id,"likeTravel",value)
	add_data_to_model(user_turtle,ent_id,creator)
	trainer = train(user_turtle,creator)

	ents = ms.load_entities()
	for ent in ents:
		if predict(trainer,ent._id)==0:
			add_label(ent._id,'likeTravel','N')
		else:
			add_label(ent._id,'likeTravel','Y')
	return get_recommended_place(collection_name)

def get_entity_id(collection_name,place_id):
	res = mongo.db[collection_name].find_one({'place_id':place_id})
	return res['_id']

def is_initilized():
	return is_initilized
