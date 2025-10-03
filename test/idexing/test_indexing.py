from src.indexing.build_index import build_index


def test_build_index_with_mock():
    """Verifica que build_index funciona con mocks y genera un index"""
    index = build_index(3)

    # Devuelve un objeto que tiene as_query_engine
    engine = index.as_query_engine()
    response = engine.query("Hola")
    assert "response" in response
    assert "Mock response" in response["response"]


def test_build_index_empty_docs(monkeypatch):
    """Verifica que build_index maneja documentos vacíos"""
    import src.clients.nasa_client as nasa_client
    monkeypatch.setattr(nasa_client, "get_apod_images", lambda count: [])

    index = build_index(3)
    engine = index.as_query_engine()
    response = engine.query("test")
    assert "response" in response
