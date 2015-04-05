import sys
sys.path.append("/Users/lubron/Documents/Course/Competitive Engineering/Architecture/travelgene/pymonk-master/")


from monk.math.cmath import sign0
import pymongo
import monk.core.api as ms
from monk.roles.configuration import default_config
from pymongo import MongoClient
import json
client = MongoClient()

def printJson(my_json):
	parsed = json.loads(my_json)
	print json.dumps(parsed,indent=4,sort_keys=True)

if __name__=='__main__':

	config=default_config()
	ms.initialize(default_config())

	stemTS = ms.yaml2json('turtle_scripts/turtle_stem.yml')
	stemT = ms.create_turtle(stemTS)
	# print stemT.generic()
	ents = ms.load_entities()
	# print len(ents)
	# print ents[0].generic()
	fields=['title', 'comment', 'desc']
	print [stemT.predict(ent, fields) for ent in ents]
	stemT.save()
	[ent.save() for ent in ents]
	likeTS = ms.yaml2json('turtle_scripts/turtle_like.yml')
	# print likeTS
	likeT = ms.create_turtle(likeTS)
	likeT.save()
	ent = ents[0]
	# print ents[0].generic()
	ent._setattr('likeTravel', 'Y')
	ms.crane.entityStore.save_one(ent)
	ms.add_data('likeTravel', 'monk', str(ents[0]._id))
	print likeT.tigress.p
	print likeT.pandas[0].mantis.data
	likeT.tigress.defaulting=True
	likeT.save()
	likeT = ms.load_turtle('likeTravel','monk')
	likeT.train()
	for i in ents:
		ent = ms.load_entity(i._id)
		print likeT.pandas[0].predict(ent)
		print sign0(likeT.pandas[0].predict(ent))
	# likeTS = ms.yaml2json('turtle_scripts/turtle_like.yml')
	# # print likeTS
	# likeT = ms.create_turtle(likeTS)
	# likeT.save()

	# ent = ents[0]
	# # print ents[0].generic()

	# ent._setattr('likeTravel', 'Y')
	# ms.crane.entityStore.save_all(ents)
	# print ent.generic()