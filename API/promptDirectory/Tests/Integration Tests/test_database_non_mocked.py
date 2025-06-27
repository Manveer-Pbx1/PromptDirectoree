from pymongo import MongoClient

def test_insert_and_find_prompt(test_mongo_settings, sample_prompt_data):
    client = MongoClient(test_mongo_settings['host'], test_mongo_settings['port'])
    db = client[test_mongo_settings['database']]
    collection = db[test_mongo_settings['collection']]
    inserted = collection.insert_one(sample_prompt_data)
    found = collection.find_one({"_id": inserted.inserted_id})
    assert found["title"] == sample_prompt_data["title"]
    collection.delete_one({"_id": inserted.inserted_id})  