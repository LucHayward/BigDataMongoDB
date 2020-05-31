# Contributors: Luc Hayward

# This is a setup file showing all the information I used to configure the database correctly
# Of specific interest is the code used to create and check the indexes for the collections
# We have also included some data insert files showing how to add additional data to the db
from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
from bson import ObjectId
from pprint import pprint

print("Connecting MongoClient")
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")
print("MongoClient connected\n\nDatabases Available:")
print(client.list_database_names())
# Database name = NSA
print("\nCollections in NSA:")
db = client.NSA
print(db.list_collection_names())

# These used to be done with ensure_index which is now deprecated and maps onto create_index
# this will create the index if it is not present and otherwise do nothing.
print("\n\nEnsuring indexes are created:")
print("Ensuring People indexes")
pprint(db.People.create_index([("current_location.geo", GEOSPHERE)]))
print("Ensuring Locations indexes")
pprint(db.Locations.create_index([("geo", GEOSPHERE)]))
pprint(db.Locations.create_index("person_id"))
print("Ensuring Searches indexes")
pprint(db.Searches.create_index("person_id"))
print("Ensuring Files indexes")
pprint(db.Files.create_index("person_id"))

print("\n\nIndex information:\nPeople:")
pprint(db.People.index_information())
print("\nLocations:")
pprint(db.Locations.index_information())
print("\nSearches:")
pprint(db.Searches.index_information())
print("\nFiles:")
pprint(db.Files.index_information())
