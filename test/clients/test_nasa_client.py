import pytest
from src.clients.nasa_client import get_apod_images
import requests


def test_get_apod_images_returns_mock(monkeypatch):
    """
    Verifica que get_apod_images devuelve datos simulados.
    Se parchea requests.get para devolver un mock controlado.
    """
    class MockResponse:
        status_code = 200
        def json(self):
            return [
                {
                    "title": "Mock APOD",
                    "date": "2025-01-01",
                    "explanation": "Mock explanation",
                    "url": "http://example.com"
                }
            ]

    monkeypatch.setattr(requests, "get", lambda *a, **k: MockResponse())

    data = get_apod_images(3)
    assert isinstance(data, list)
    assert len(data) > 0
    for item in data:
        assert "title" in item
        assert "date" in item
        assert "explanation" in item
        assert "url" in item


def test_get_apod_images_error(monkeypatch):
    """
    Simula un error de API forzado lanzando Exception en requests.get.
    """
    def mock_error(*args, **kwargs):
        raise Exception("API error simulada")

    monkeypatch.setattr(requests, "get", mock_error)

    with pytest.raises(Exception) as exc_info:
        get_apod_images(3)

    assert "API error simulada" in str(exc_info.value)
