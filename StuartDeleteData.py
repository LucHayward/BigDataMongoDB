from pymongo import MongoClient

client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")
db = client.NSA

print('deleting files')
db.Files.delete_many({})

print('deleting people')
db.People.delete_many({'name': 'Billy Bobbyson'})
db.People.delete_many({'name': 'Manny Edison'})
db.People.delete_many({'name': 'Elon Musk'})
