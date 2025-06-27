
def test_valid_prompt_data(sample_prompt_data):
    assert isinstance(sample_prompt_data["title"], str)
    assert isinstance(sample_prompt_data["content"], str)
    assert sample_prompt_data["title"] != ""
    assert sample_prompt_data["content"] != ""

def test_invalid_prompt_data(invalid_prompt_data):
    assert invalid_prompt_data["content"] == ""
    assert len(invalid_prompt_data["title"]) >= 1000