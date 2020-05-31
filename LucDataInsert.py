from pymongo import MongoClient
from pprint import pprint
from random import randint
from bson import ObjectId
import datetime

client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")

db = client.NSA
devices = ["Samsung S8", "Samsung S9", "Samsung Fold", "iPhone X", "iPhone 6", "iMac", "iPad"]
searches = []

person = {"threat_level": 1,
          "name": "Bob Jones",
          "date_of_birth": datetime.datetime.strptime("1981-11-10T11:50:32.000Z", "%Y-%m-%dT%H:%M:%S.000Z"),
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
              {"device_description": devices[randint(0, 6)],
               "ip": str(randint(187, 195)) + str(randint(2, 5)) + str(randint(26, 30)) + str(randint(72, 76)),
               "timestamp": datetime.datetime.utcnow(),
               "url": "www.example.com"
               },
              {"device_description": devices[randint(0, 6)],
               "ip": str(randint(187, 195)) + str(randint(2, 5)) + str(randint(26, 30)) + str(randint(72, 76)),
               "timestamp": datetime.datetime.utcnow(),
               "url": "www.example.com"
               },
              {"device_description": devices[randint(0, 6)],
               "ip": str(randint(187, 195)) + str(randint(2, 5)) + str(randint(26, 30)) + str(randint(72, 76)),
               "timestamp": datetime.datetime.utcnow(),
               "url": "www.example.com"
               }
          ]
          }

result = db.People.insert_one(person)
print("Inserted Person: " + str(result.inserted_id))

for i in range(100):
    searches.append({"device_description": devices[randint(0, 6)],
                     "ip": str(randint(187, 195)) + str(randint(2, 5)) + str(randint(26, 30)) + str(randint(72, 76)),
                     "person_id": result.inserted_id,
                     "timestamp": datetime.datetime.utcnow() + datetime.timedelta(randint(-3, 3)),
                     "url": "www.example.com"
                     })

inserted = db.Searches.insert_many(searches)
print("Inserted Searches:")
print(inserted.inserted_ids)

Locations = [{
    "address": {
        "street": str(randint(30, 50)) + " Main Road",
        "city": "Cape Town",
        "zipcode": "7945"
    },
    "geo": {
        "type": "Point",
        "coordinates": [18.459050 + randint(-2, 2)*0.001, -34.118317 + randint(-4, 4)*0.001]
    },
    "timestamp": datetime.datetime.now()+datetime.timedelta(x-100),
    "person_id": result.inserted_id
} for x in range(100)]
inserted = db.Locations.insert_many(Locations)
print("Inserted Locations:")
print(inserted.inserted_ids)
