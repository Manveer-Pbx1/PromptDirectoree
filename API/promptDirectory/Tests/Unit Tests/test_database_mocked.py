from unittest.mock import MagicMock

def test_create_prompt_mongo(mock_mongo_collection, sample_prompt_data):
    mock_mongo_collection.insert_one = MagicMock(return_value=MagicMock(inserted_id="someid"))
    result = mock_mongo_collection.insert_one(sample_prompt_data)
    assert result.inserted_id == "someid"

def test_find_prompt_mongo(mock_mongo_collection, sample_prompt_with_id):
    mock_mongo_collection.find_one = MagicMock(return_value=sample_prompt_with_id)
    result = mock_mongo_collection.find_one({"_id": sample_prompt_with_id["_id"]})
    assert result["_id"] == sample_prompt_with_id["_id"]

def test_update_prompt_mongo(mock_mongo_collection, sample_prompt_with_id):
    mock_mongo_collection.update_one = MagicMock(return_value=MagicMock(modified_count=1))
    result = mock_mongo_collection.update_one({"_id": sample_prompt_with_id["_id"]}, {"$set": {"title": "Updated"}})
    assert result.modified_count == 1

def test_delete_prompt_mongo(mock_mongo_collection, sample_prompt_with_id):
    mock_mongo_collection.delete_one = MagicMock(return_value=MagicMock(deleted_count=1))
    result = mock_mongo_collection.delete_one({"_id": sample_prompt_with_id["_id"]})
    assert result.deleted_count == 1