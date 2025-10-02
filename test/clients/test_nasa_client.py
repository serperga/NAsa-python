import pytest
from src.clients.nasa_client import get_apod_images


def test_get_apod_images_success(monkeypatch):
    """Testea que se obtienen imágenes cuando la API responde 200."""

    def mock_request(url, params=None):
        class MockResponse:
            status_code = 200
            text = '[{"title":"Test Image","date":"2025-01-01","explanation":"Mock explanation","url":"http://example.com"}]'

            def json(self_inner):
                import json
                return json.loads(self_inner.text)

        return MockResponse()

    monkeypatch.setattr("requests.get", mock_request)

    data = get_apod_images(1)
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Test Image"

def test_get_apod_images_error(monkeypatch):
    """Testea que se lanza excepción si la API falla."""
    def mock_request(url, params=None):
        class MockResponse:
            status_code = 500
            text = '{"error":"Internal Server Error"}'
            def json(self_inner):
                import json
                return json.loads(self_inner.text)
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_request)

    # Capturamos la excepción
    with pytest.raises(Exception) as excinfo:
        get_apod_images(1)

    assert "Error en la API de NASA" in str(excinfo.value)
    assert "500" in str(excinfo.value)

