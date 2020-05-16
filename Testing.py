from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://dbUser:redcloudhorse@cluster0-p0laa.mongodb.net/test?retryWrites=true&w=majority")
db = client.business

ASingleReview = db.reviews.find_one({})
print('A sample document:')
pprint(ASingleReview)

result = db.reviews.update_one({'_id': ASingleReview.get('_id')}, {'$inc': {'likes': 1}})
print('Number of documents modified : ' + str(result.modified_count))

UpdatedDocument = db.reviews.find_one({'_id': ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)
