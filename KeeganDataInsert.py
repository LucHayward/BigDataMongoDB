from pymongo import MongoClient
from pprint import pprint
from random import randint
from bson import ObjectId
import datetime

client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")

db = client.NSA
col = db.Locations

col.insert_one({
    "address": {
        "street": "110 M Market",
        "city": "Huffington",
        "state": "BB",
        "zipcode": "77684"
    },
    "geo": {
        "type": "Point",
        "coordinates": [93.24565, -44.85466]
    },
    "timestamp": datetime.datetime.strptime("2019-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z"),
    "person_id": ObjectId("5eceb3f059e783337f050986")
    })


