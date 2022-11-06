from pymongo import MongoClient
import json

with open('PostamatData.json') as f:
  file_data = json.load(f)

client = MongoClient('localhost', 27017)
db = client['postamats_db']
db.create_collection(file_data)


client.close()