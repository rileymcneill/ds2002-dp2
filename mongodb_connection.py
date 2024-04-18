from pymongo import MongoClient
import os
import json

MYMONGOPASS = os.getenv('MYMONGOPASS')
uri = "mongodb+srv://mqt3uz:OxPXuRVOH9uO9wTh@cluster0.rmavpxm.mongodb.net/?retryWrites=true&w=majority&appName=DB_2"
client = MongoClient(uri, username='mqt3uz', password=MYMONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client.DP_2
collection = db.DP2

def import_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            try:
                file_path = os.path.join(directory, filename)
            except Exception as e:
                print(filename, e)
            with open(file_path) as file:
                try:
                    data = json.load(file)
                except Exception as e:
                    print(file, e)
                if isinstance(data, list):
                    collection.insert_many(data)
                else:
                    collection.insert_one(data)

def main():
    directory = "data"
    import_json_files(directory)

if __name__ == "__main__":
    main()