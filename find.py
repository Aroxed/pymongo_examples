import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')

# Select your database and collection
db = client['ecommerce']
collection = db['products']

# documents = collection.find()

documents = collection.find({'category': 'Electronics'}).sort('stock')

for document in documents:
    print(document)
