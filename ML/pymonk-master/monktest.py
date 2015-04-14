import pymongo
from pymongo import MongoClient
import monk.core.api as ms
from monk.roles.configuration import default_config
client = MongoClient()

if __name__=='__main__':
	db = client['travelgene']
	print db['travelgene'].find()

	print db