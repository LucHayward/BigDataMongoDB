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
newcol = db.Searches

# Insert documents into the database
#col.insert_one({"threat_level" : 10,
#                "name" : "Jane Doe",
#                "date_of_birth" : datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z"),
#                "country_of_birth" : "Germany",
#                "current_location" : {
#                    "address": {
#                        "street": "110 M Market",
#                        "city": "Huffington",
#                        "state": "BB",
#                        "zipcode": "77684"
#                    },
#                    "geo": {
#                        "type": "Point",
#                        "coordinates": [45.43535, 77.12124]
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
#
#newcol.insert_one({ "ip": "199.2.04.135",
#                    "device_description": "Samsung S8",
#                    "url": "https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1",
#                    "timestamp": datetime.datetime.now(),
#                    "person_id" : ObjectId("5ed121c10dddf5cdd9828bb4")
#                })

# Check the documents in the collection
for i in col.find():
    pprint(i)

# Query1: Sort the documents by ascending or descending order
print("Query 1:")
print("Sort the people collection in ascending order by name")
for i in col.find().sort("name" , 1):
    pprint(i)
print("-----------------------------------------------------")

# Query2: Update all the threat level of all the people in Germany by 1
print("Query 2:")
print("Update the threat level of all the people born in Germany by 1")
update = col.update_many({"country_of_birth" : "Germany"}, {"$inc": { "threat_level" : 1}})
print(update.modified_count , "documents modified")
print("-----------------------------------------------------")

# Query3: Find all the people born in Sudan with threat level greater than 7
print("Query 3:")
print("Find all the people in born Sudan with threat level greater than 7")
for i in col.find({"country_of_birth" : "Sudan" , "threat_level" : {"$gt": 7}}):
    pprint(i)
print("-----------------------------------------------------")

# Query4: Change to searches collection and check all the people who searched for a specific URL and return the details of the person that did
print("Query 4:")
print("Find all the people that searched for a specific URL and then use their object id to find their details")
for i in newcol.find({"url" : "https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1"} ,
                  {"person_id" : 1}):
                  for j in col.find({"_id" : i.get("person_id") }, {"name" : 1}):
                      pprint(j)
print("-----------------------------------------------------")
