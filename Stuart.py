import datetime
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

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
print('1.a Inserting multiple people')
result = db.People.insert_many([person_1, person_2, person_3])
inserted_ids = result.inserted_ids
print('inserted:', inserted_ids)

file_1 = {
    "name": "Rocketdyne XRS-2200 specifications.txt",
    "contents": "Propellants: LOX/LH2\nThrust in Vacuum: 261,200 lb\nThrust at Sea Level: 206,200 lb\nIsp in vacuum (s): 428.2\nIsp at sea level: 338.3\nMixture Ratio: 5.5:1\nChamber Pressure: 854 psia\nArea Ratio: 58\n",
    "person_id": inserted_ids[2]
}
file_2 = {
    "name": "Liquid Oxygen Prices.txt",
    "contents": "India: 1.6 USD/kg\nGermany: 1.8 USD/kg\nChina: 1.5 USD/kg\n",
    "person_id": inserted_ids[2]
}
file_3 = {
    "name": "mom's berry pie recipe.txt",
    "contents": "Ingredients: homemade pie crust (my recipe makes 2 crusts; 1 for bottom 1 for top)\n6 cups (890g) fresh blueberries\n2/3 cup (135g) granulated sugar\n1/4 cup (28g) cornstarch\n1/4 teaspoon ground cinnamon\n1 Tablespoon (15ml) lemon juice\n1 Tablespoon (15g) unsalted butter, cut into small pieces\n",
    "person_id": inserted_ids[0]
}

print('1.b Inserting multiple files')
result = db.Files.insert_many([file_1, file_2, file_3])
print('inserted:', result.inserted_ids)

# aggregate using people's current city (count the number of people currently in each city
print('2. Grouping and counting people by city')
x = db.People.aggregate([{"$group": {"_id": "$current_location.address.city", "count": {"$sum": 1}}}])
for person in x:
    pprint(person)

print('-----------------------------DEBUG--------------------------------')
print('These are all the people in the database named Elon Musk:')
x = db.People.find({'name': 'Elon Musk'})
for person in x:
    pprint(person)

print('These are all of the files in the database:')
x = db.Files.find()
for file in x:
    pprint(file)
print('------------------------------------------------------------------')
# finds a document matching the filter and deletes it
# returns the deleted document
print('3. deleting one person named Elon Musk')
d = db.People.find_one_and_delete({'name': 'Elon Musk'})
print('deleted: ', d)

# delete files for the user that was just deleted
print('4. Deleting files belonging to the deleted person')
db.Files.delete_many({'person_id': d.get('_id')})

print('-----------------------------DEBUG--------------------------------')
print('These are all the people in the database named Elon Musk:')
x = db.People.find({'name': 'Elon Musk'})
for person in x:
    pprint(person)

print('These are all of the files in the database:')
x = db.Files.find()
for file in x:
    pprint(file)
print('------------------------------------------------------------------')
