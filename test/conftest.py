import pytest
from unittest.mock import MagicMock
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding


@pytest.fixture(autouse=True)
def mock_external_services(monkeypatch):
    """
    Mocks globales para todos los tests:
    - NASA API
    - GPTVectorStoreIndex
    - LLM y Embeddings
    """

    # --- Mock LLM que hereda de OpenAI ---
    class MockLLM(OpenAI):
        def __init__(self):
            super().__init__(api_key="test_key", model="gpt-3.5-turbo")

        def predict(self, prompt, **kwargs):
            return f"Mock LLM response: {prompt}"

    # --- Mock Embedding que hereda de OpenAIEmbedding ---
    class MockEmbedding(OpenAIEmbedding):
        def __init__(self):
            super().__init__(api_key="test_key", model="text-embedding-3-small")

        def embed(self, text):
            return [0.1, 0.2, 0.3]  # vector simulado

    # --- Mock Index y QueryEngine ---
    class MockQueryEngine:
        def query(self, q):
            return {"response": f"Mock response to query: {q}"}

    class MockIndex:
        def __init__(self, documents=None):
            self.documents = documents

        @classmethod
        def from_documents(cls, documents):
            return cls(documents)

        def as_query_engine(self):
            return MockQueryEngine()

    # --- Mock NASA API ---
    def fake_get_apod_images(count=5):
        return [
            {
                "title": "Mock APOD",
                "date": "2025-01-01",
                "explanation": "Mock explanation",
                "url": "http://example.com"
            }
        ]

    # --- Monkeypatch global ---
    import src.clients.nasa_client as nasa_client
    monkeypatch.setattr(nasa_client, "get_apod_images", fake_get_apod_images)

    import src.indexing.build_index as build_index
    monkeypatch.setattr(build_index, "GPTVectorStoreIndex", MockIndex)

    import src.config.llms.llama_settings as llama_settings
    llama_settings.Settings.llm = MockLLM()
    llama_settings.Settings.embed_model = MockEmbedding()
    llama_settings.Settings.chunk_size = 128
    llama_settings.Settings.chunk_overlap = 10

    yield
