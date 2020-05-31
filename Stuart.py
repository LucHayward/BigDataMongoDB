import datetime

from bson import ObjectId
from pymongo import MongoClient
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

person_1 = {"threat_level": 1,
            "name": "Manny Edison",
            "date_of_birth": datetime.datetime.strptime("2001-11-10T11:50:32.000Z", "%Y-%m-%dT%H:%M:%S.000Z"),
            "country_of_birth": "Canada",
            "current_location": {
                "address": {
                    "street": "8 Stall Way",
                    "city": "Montreal",
                    "zipcode": "8745"
                },
                "geo": {
                    "type": "Point",
                    "coordinates": [-45.43535, 77.12124]
                },
                "timestamp": datetime.datetime.now()
            },
            "recent_searches": [
                {
                    "ip": "102.166.112.131",
                    "device_description": "Samsung A40",
                    "url": "https://www.maplesyrup.com/ingredients",
                    "timestamp": datetime.datetime.now()
                }
            ]
            }

person_2 = {"threat_level": 0,
            "name": "Billy Bobbyson",
            "date_of_birth": datetime.datetime.strptime("2001-11-10T11:50:32.000Z", "%Y-%m-%dT%H:%M:%S.000Z"),
            "country_of_birth": "Brazil",
            "current_location": {
                "address": {
                    "street": "93-R Mountain Trail",
                    "city": "Rio de Janeiro",
                    "zipcode": "4684"
                },
                "geo": {
                    "type": "Point",
                    "coordinates": [65.65489, -20.6848]
                },
                "timestamp": datetime.datetime.now()
            },
            "recent_searches": [
                {
                    "ip": "176.164.111.146",
                    "device_description": "LG G5",
                    "url": "https://www.brazil-snakes.com/deadly/what-to-do-when-bitten.html",
                    "timestamp": datetime.datetime.now()
                }
            ]
            }
person_3 = {"threat_level": 11,
            "name": "Elon Musk",
            "date_of_birth": datetime.datetime.strptime("1971-11-10T11:50:32.000Z", "%Y-%m-%dT%H:%M:%S.000Z"),
            "country_of_birth": "South Africa",
            "current_location": {
                "address": {
                    "street": "45 SpaceX Complex",
                    "city": "Austin",
                    "state": "Texas",
                    "zipcode": "1111"
                },
                "geo": {
                    "type": "Point",
                    "coordinates": [77.3325, -18.5646]
                },
                "timestamp": datetime.datetime.now()
            },
            "recent_searches": [
                {
                    "ip": "106.154.110.148",
                    "device_description": "iPhone 11",
                    "url": "https://www.google.com/?q=XVGT72-DEATH-V11+22MHz+controller+missile+heat+lock+wont+disengage+stackoverflow",
                    "timestamp": datetime.datetime.now()
                }
            ]
            }

# insert multiple records at once
result = db.People.insert_many([person_1, person_2, person_3])
inserted_ids = result.inserted_ids
print(inserted_ids)

# aggregate using people's current city (count the number of people currently in each city
x = db.People.aggregate([{"$group": {"_id": "$name", "count": {"$sum": 1}}}])
for person in x:
    print(person)

# delete files for a specific user
db.Files.delete_many({'_id': ObjectId('5ecbea783424a5bf93c3e1f3')})

# finds a document matching the filter and deletes it
# returns the deleted document
print('deleted: ', db.People.find_one_and_delete({'name': 'Elon Musk'}))

# (for debugging) print out the list of people
x = db.People.find()
for person in x:
    print(person)
