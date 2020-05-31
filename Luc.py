from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
from bson import ObjectId
from bson import binary
from pprint import pprint
import datetime

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")

# client.list_database_names()
# Database name = NSA
db = client.NSA
# db.list_collection_names()
# Collections = Files, Locations, People, Searches

print("Find all the locations within the given bounding area")
locationQuery = {"geo":
                     {"$geoWithin":
                          {"$geometry":
                               {"type": "Polygon",
                                "coordinates": [[[18.459, -34.118], [18.460, -34.118], [18.459, -34.116],
                                                 [18.459, -34.118]]]
                                }
                           }
                      }
                 }
for x in db.Locations.find(locationQuery):
    pprint(x)

print("\nDisplay the number of devices of each type used for searches")
rs = db.Searches.aggregate([{"$group":
                                 {"_id": "$device_description",
                                  "count": {"$sum": 1}
                                  }
                             }])
for doc in rs:
    pprint(doc)

print("\nFind one person who's at least 21 today")
rs = db.People.find_one({"date_of_birth": {"$gt": datetime.datetime.utcnow() - datetime.timedelta(365 * 21)}})
pprint(rs)

print("\nUpdate the person with the highest threat level and update a plans field, or create it if it is missing")
rs = db.People.find({}, {"_id": 1}).sort([("threat_level", -1)]).limit(1)
id = rs[0]
print("Updating user: " + str(id))
db.People.update_one(id, {"$set" : {"Plan": "Colonise Mars First"}})

# update = col.update_many({"country_of_birth" : "Germany"}, {"$inc": { "threat_level" : 1}})