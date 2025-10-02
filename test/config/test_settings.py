from src.config import settings

def test_openai_api_key_loaded():
    assert settings.OPENAI_API_KEY is not None, "OPENAI_API_KEY should not be None"

def test_nasa_api_key_default_or_set():
    assert settings.NASA_API_KEY is not None
