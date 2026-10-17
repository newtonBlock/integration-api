import os
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class GCPMongoHandler:

    # Constructor method to initialize the database connection
    def __init__(self, uri: str, db_id: str, user: str):
        """initializes the mongoDB client and selects the target db and collection """

        self.client = MongoClient(uri)
        self.db = self.client[db_id]
        self.collection = self.db[user]

    def create(self, data: dict) -> str:
        """Inserts a single document into the collection and return the string ID."""
        result = self.collection.insert_one(data)
        return str(result.inserted_id)
    
    def create_many(self, data_list: list[dict]) -> list[str]:
        """Insers multiple docs and returns a list of string IDs"""
        result = self.collection.insert_many(data_list)
        return [str(doc_id) for doc_id in result.inserted_ids]

    def close(self):
        """Closes the MongoDB connection."""
        self.client.close()

# def save_APIdata(response):
#     for item in response['results']:
#         collection.insert_one(item)

# test_data = {
#     'product': 'Crowdstrike',
#     'gender': 'Male',
#     "status": {
#         "burstout": True,
#         "high_count": 12,
#         "age": 19
#     }
# }
# try:
#     result = collection.insert_one(test_data)
#     print(f" Successfully saved document to Firestore! Document ID: {result.inserted_id}")
# except Exception as e:
#     print(f"error saving data: {e}")