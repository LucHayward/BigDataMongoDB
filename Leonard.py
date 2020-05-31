import datetime

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint
from bson import ObjectId

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")

# client.list_database_names()
# Database name = NSA
db = client.NSA
# db.list_collection_names()
# Collections = Files, Locations, People, Searches

# code to check for the collections in the database
print("The collections are: " , db.list_collection_names())
# Switch to the 'People' collection
col = db.People

# Check the documents in the collection
for i in col.find():
    pprint(i)

# Query1: Sort the documents by ascending or descending order
print("sorted the people's collection in ascending order by name")
for i in col.find().sort("name" , 1):
    pprint(i)
print("-----------------------------------------------------")
# Query2: Update all the threat level of all the people in Germany by 1
update = col.update_many({"country_of_birth" : "Germany"}, {"$inc": { "threat_level" : 1}})
print(update.modified_count , "documents modified")
print("-----------------------------------------------------")
# Query3: Find all the people in Sudan with threat level greater than 7
print("Here is a list of people")
for i in col.find({"country_of_birth" : "Sudan" , "threat_level" : {"$gt": 7}}):
    pprint(i)
print("-----------------------------------------------------")
# Query4: Change to searches collection and check all the people who searched for a specific URL and return the details of the person that did
newcol = db.Searches
for i in newcol.find({"url" : "https://www.mongodb.com/blog/post/designing-the-perfect-prototyping-workflow-and-collaboration-platform-in-the-cloud"} ,
                  {"person_id" : 1}):
                  for j in col.find({"_id" : i["person_id"] }, {"name" : 1}):
                      pprint(j)
print("-----------------------------------------------------")

# Insert documents into the database
#col.insert_one({"threat_level" : 10,
#                "name" : "Jane Doe",
#                "date_of_birth" : datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z"),
#                "country_of_birth" : "Sudan",
#                "current_location" : {
#                    "address": {
#                        "street": "110 M Market",
#                        "city": "Huffington",
#                        "state": "BB",
#                        "zipcode": "77684"
#                    },
#                    "geo": {
#                        "type": "Point",
#                        "coordinates": [-44.85466 , 93.24565]
#                    },
#                    "timestamp": datetime.datetime.now()
#                },
#                "recent_searches": [
#                    {
#                        "ip": "199.2.04.135",
#                        "device_description": "Samsung S20",
#                        "url": "https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1",
#                        "timestamp": datetime.datetime.now(),
#                        "person_id": "5ecbe3c11c1b2933e5a27033"
#                    }
#                ]
#                })

# Exclude specific fields from the document
# for x in col.find({},{ "_id": 0 }):
# print(x)

# Advanced queries, the first argument of the find can be used to filter results
# for j in col.find({ "country_of_birth" : "Germany"} , { "name" : 0}):
# print(j)

# update given documents in the DB
# query = { "name" : "John Doe" }
# newvalues = { "$set" : {"name" : "Jane Doe" } }
# col.update_one(myquery,newvalues)  # alternatively use the update_many command to chnage multiple

# limit the number of results returned
# for x in col.find().limit(5)
#   print(x)
