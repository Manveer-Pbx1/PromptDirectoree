import pytest
from bson import ObjectId

def test_prompt_fields(sample_prompt_data):
    for field in ["title", "content"]:
        assert field in sample_prompt_data
        assert sample_prompt_data[field]

def test_prompt_with_id_fields(sample_prompt_with_id):
    assert "_id" in sample_prompt_with_id
    assert isinstance(sample_prompt_with_id["_id"], ObjectId)
    assert sample_prompt_with_id["title"]
    assert sample_prompt_with_id["content"]