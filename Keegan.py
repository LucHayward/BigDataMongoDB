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
locations = mydb.Locations
searches = mydb.Searches
people = mydb.People

print("Find all locations that have been recorded that are near [93.24565, -44.8546]")
locationQuery = {"geo": {"$nearSphere": [93.24565, -44.8546]}}
for x in locations.find(locationQuery):
    pprint(x)

print("Find all searches done on a Samsung S8")
phoneQuery = {"device_description": "Samsung S8"}
for y in searches.find(phoneQuery):
    pprint(y)

print("Find all people who have names starting with J")
for i in people.find({"name": {"$gt": "J"}}):
    pprint(i)

print("Find all entries for peopel who visited https://hangouts.google.com/ or https://www.mongodb.com/blog/post/designing-the-perfect-prototyping-workflow-and-collaboration-platform-in-the-cloud")
websiteQuery1 = {"url" : "https://hangouts.google.com/"}
websiteQuery2 = {"url" : "https://www.mongodb.com/blog/post/designing-the-perfect-prototyping-workflow-and-collaboration-platform-in-the-cloud"}
for j in searches.find({"$or": [websiteQuery1, websiteQuery2]}):
    pprint(j)
