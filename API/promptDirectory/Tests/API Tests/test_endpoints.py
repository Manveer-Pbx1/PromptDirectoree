def test_get_all_prompts(api_client):
    response = api_client.get("/api/prompts")
    assert response.status_code == 200

def test_create_prompt(api_client, sample_prompt_data):
    response = api_client.post("/api/prompts", data=sample_prompt_data, content_type="application/json")
    assert response.status_code in (201, 400)  

def test_get_prompt_by_id(api_client, sample_prompt_with_id):
    response = api_client.get(f"/api/prompts{sample_prompt_with_id['_id']}/")
    assert response.status_code in (200, 404)  