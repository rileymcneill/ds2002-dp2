from pymongo import MongoClient
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://mqt3uz:OxPXuRVOH9uO9wTh@cluster0.rmavpxm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['Cluster0']
collection = db['DP2']