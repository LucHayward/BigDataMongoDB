from pymongo import MongoClient
from bson.son import SON
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")

# client.list_database_names()
# Database name = NSA
mydb = client.NSA
# db.list_collection_names()
# Collections = Files, Locations, People, Searches
mycol = mydb.Locations
locationQuery = {"coordinates": {"$near": [-44.8546, 93.24565]}}
for x in mycol.find(locationQuery):
    pprint(x)