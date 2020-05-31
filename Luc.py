from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
from bson import ObjectId
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")

# client.list_database_names()
# Database name = NSA
db = client.NSA
# db.list_collection_names()
# Collections = Files, Locations, People, Searches



# for doc in db.locations.find({"geo": {"$nearSphere": [93.24565, -44.85466]}}):
#     pprint(doc)