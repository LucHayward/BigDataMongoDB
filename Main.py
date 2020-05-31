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
locations = mydb.Locations
searches = mydb.Searches
people = mydb.People

# Keegan's query
print("Find all locations that have been recorded that are near [93.24565, -44.8546]")
locationQuery = {"geo": {"$nearSphere": [93.24565, -44.8546]}}
for x in locations.find(locationQuery):
    pprint(x)

# Leonard's query
print("Update the threat level of all the people born in Germany by 1")
update = col.update_many({"country_of_birth" : "Germany"}, {"$inc": { "threat_level" : 1}})
print(update.modified_count , "documents modified")

# db.Locations.insert_one({
#     "_id": {
#         "$oid": "5ecbe9923424a5bf93c3e1ef"
#     },
#     "address": {
#         "street1": "340 W Market",
#         "city": "Bloomington",
#         "state": "MN",
#         "zipcode": "55425"
#     },
#     "geo": {
#         "type": "Point",
#         "coordinates": [
#             {
#                 "$numberDouble": "-93.24565"
#             },
#             {
#                 "$numberDouble": "44.85466"
#             }
#         ]
#     },
#     "timestamp": {
#         "$date": {
#             "$numberLong": "1332804016000"
#         }
#     },
#     "person_id": "5ecbe3c11c1b2933e5a27032"})

# TODO: Find Dataset

# TODO: Design the database

# TODO: Create and load the data in the database (in code, show)
# TODO: Use insert_many() (for performance)?
# TODO: Must include tests to show everything is correct

# TODO: Database comparison writeups
# TODO: Decide who will take each DB (Graph, Key-Value, Column-Family, Relational
# TODO: For each say what role it could have if polyglot persistence is used, why (or if not useable, also why)
#       You may include other data/use-cases not yet mentioned

# TODO: Test a variety of DB operations (show output), 4 each, sounds like actual testing is needed

# TODO: Write and test a simple program that runs 1 statement each from the above set
