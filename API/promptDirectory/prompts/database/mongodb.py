from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "promptDirectory")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
prompts_collection = db['prompts']

def serialize_prompt(prompt):
    return {
        "id": str(prompt["_id"]),
        "title": prompt.get("title"),
        "content": prompt.get("content"),
        "created_at": prompt.get("created_at"),
        "updated_at": prompt.get("updated_at"),
    }