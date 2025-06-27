
def test_long_title_prompt(api_client, sample_prompt_data):
    sample_prompt_data["title"] = "A" * 1000
    response = api_client.post("/api/prompts", data=sample_prompt_data, content_type="application/json")
    assert response.status_code in (201, 400)  