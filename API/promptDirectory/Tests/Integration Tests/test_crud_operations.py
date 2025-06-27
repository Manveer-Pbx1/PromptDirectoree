import pytest
from pymongo import MongoClient

@pytest.mark.integration
def test_crud_workflow(test_mongo_settings, sample_prompt_data):
    client = MongoClient(test_mongo_settings['host'], test_mongo_settings['port'])
    db = client[test_mongo_settings['database']]
    collection = db[test_mongo_settings['collection']]

    inserted = collection.insert_one(sample_prompt_data)
    _id = inserted.inserted_id

    found = collection.find_one({"_id": _id})
    assert found["title"] == sample_prompt_data["title"]

    collection.update_one({"_id": _id}, {"$set": {"title": "Updated"}})
    updated = collection.find_one({"_id": _id})
    assert updated["title"] == "Updated"

    collection.delete_one({"_id": _id})
    assert collection.find_one({"_id": _id}) is None