from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")

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
