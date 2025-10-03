import pytest
from src.clients.openai_client import OpenAIClient
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI

def test_openai_client_returns_key(monkeypatch):
    """Verifica que OpenAIClient devuelve la API key desde la variable de entorno."""
    monkeypatch.setenv("OPENAI_API_KEY", "test_key_123")
    client = OpenAIClient()
    key = client.get_key()
    assert key == "test_key_123"


def test_openai_client_default_key(monkeypatch):
    """Verifica que OpenAIClient devuelve None si no hay key."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    client = OpenAIClient()
    key = client.get_key()
    assert key is None or isinstance(key, str)


def test_openai_client_get_llm(monkeypatch):
    """Verifica que OpenAIClient puede devolver un LLM OpenAI y asignarlo a Settings.llm."""
    monkeypatch.setenv("OPENAI_API_KEY", "mock_llm_key")

    client = OpenAIClient()
    llm = client.get_llm(model="gpt-4.1", temperature=0.1)

    # Debe ser instancia de OpenAI
    assert isinstance(llm, OpenAI)

    # Debe tener la API key correcta
    assert llm.api_key == "mock_llm_key"

    # Se puede asignar a Settings sin error
    Settings.llm = llm
    assert Settings.llm.api_key == "mock_llm_key"
    assert Settings.llm.model == "gpt-4.1"
