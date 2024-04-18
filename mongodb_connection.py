from pymongo import MongoClient
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://mqt3uz:OxPXuRVOH9uO9wTh@cluster0.rmavpxm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client.DP_2
collection = db.DP2

def import_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            with open(file_path) as file:
                data = json.load(file)
                if isinstance(data, list):
                    collection.insert_many(data)
                else:
                    collection.insert_one(data)

def main():
    directory = "data"
    import_json_files(directory)

if __name__ == "__main__":
    main()