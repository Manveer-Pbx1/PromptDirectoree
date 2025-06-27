def test_get_nonexistent_prompt(api_client):
    response = api_client.get("/api/prompts/000000000000000000000000")
    assert response.status_code == 404

def test_create_invalid_prompt(api_client, invalid_prompt_data):
    response = api_client.post("/api/prompts", data=invalid_prompt_data, content_type="application/json")
    assert response.status_code == 400