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

# code to check for the collections in the database
print(db.list_collection_names())
# Switch to the 'People' collection
col = db.People

# Insert documents into the database
col.insert_one()

# Check the documents in the collection
#for i in col.find():
    #print(i)

# Exclude specific fields from the document
# for x in col.find({},{ "_id": 0 }):
    #print(x)

# Advanced queries, the first argument of the find can be used to filter results
#for j in col.find({ "country_of_birth" : "Germany"} , { "name" : 0}):
    #print(j)

# Sort the documents by ascending or descending order
# for i in col.find().sort("name" , 1)      # the 1 is ascending and -1 will be descending
    #print(i)

# update given documents in the DB
# query = { "name" : "John Doe" }
# newvalues = { "$set" : {"name" : "Jane Doe" } }
# col.update_one(myquery,newvalues)  # alternatively use the update_many command to chnage multiple

# limit the number of results returned
# for x in col.find().limit(5)
#   print(x)
