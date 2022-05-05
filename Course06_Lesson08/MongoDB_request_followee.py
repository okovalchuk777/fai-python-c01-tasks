from pymongo import MongoClient
from pprint import pprint

# Query on Embedded/Nested Documents
# https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/
# How to select a single field for all documents in a MongoDB collection?
# https://stackoverflow.com/questions/25589113/how-to-select-a-single-field-for-all-documents-in-a-mongodb-collection

client = MongoClient('127.0.0.1', 27017)
db = client['instagram']
techskills_2022 = db.techskills_2022
for doc in techskills_2022.find({'profile_username': "techskills_2022", 'status': "followee"},
                                {'username': 1, 'user_id': 1, '_id': 0}):
    pprint(doc)


