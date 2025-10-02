from src.clients.nasa_client import get_apod_images
from src.config.settings import DEFAULT_IMAGE_COUNT
from llama_index.core import Document, Settings, GPTVectorStoreIndex, ServiceContext


def build_index(image_count: int = DEFAULT_IMAGE_COUNT) -> GPTVectorStoreIndex:
    """
    Descarga imágenes de APOD y construye un índice vectorial GPTVectorStoreIndex
    usando Settings en lugar de ServiceContext (llama-index 0.14.3+)
    """
    data = get_apod_images(image_count)
    documents = [
        Document(
            text=f"Title: {entry['title']}\nDate: {entry['date']}\nExplanation: {entry['explanation']}\nURL: {entry['url']}"
        )
        for entry in data
    ]

    # Crear índice
    index = GPTVectorStoreIndex.from_documents(documents)
    return index
