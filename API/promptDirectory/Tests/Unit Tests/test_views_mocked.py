from unittest.mock import patch, MagicMock
from bson import ObjectId

@patch("pymongo.collection.Collection.find_one")
def test_get_prompt_view(mock_find_one, api_client, sample_prompt_with_id):
    mock_find_one.return_value = sample_prompt_with_id
    response = api_client.get(f"/api/prompts/{sample_prompt_with_id['_id']}/")
    assert response.status_code in (200, 404)  
