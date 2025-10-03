import logging
from src.clients.nasa_client import get_apod_images
from llama_index.core import Document
from llama_index.core import GPTVectorStoreIndex
from src.config.llms.llama_settings import Settings
from src.config.settings import DEFAULT_IMAGE_COUNT  # si tienes un fichero de constantes

# Configuración del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def build_index(image_count: int = DEFAULT_IMAGE_COUNT) -> GPTVectorStoreIndex:
    """
    Descarga imágenes de APOD y construye un índice vectorial GPTVectorStoreIndex
    usando Settings (llama-index 0.14.3+).

    :param image_count: número de imágenes a descargar de la API de NASA
    :return: instancia de GPTVectorStoreIndex
    :raises ValueError: si no se obtienen imágenes
    """
    logger.info("Descargando %d imágenes de la NASA", image_count)

    try:
        data = get_apod_images(image_count)
    except Exception as e:
        logger.exception("Error al descargar imágenes de la NASA")
        raise e

    if not data:
        logger.error("No se obtuvieron imágenes de la API de NASA")
        raise ValueError("No se obtuvieron imágenes de la API de NASA")

    # Crear documentos
    documents = [
        Document(
            text=f"Title: {entry['title']}\nDate: {entry['date']}\nExplanation: {entry['explanation']}\nURL: {entry['url']}"
        )
        for entry in data
    ]

    logger.info("Construyendo índice con %d documentos", len(documents))

    try:
        index = GPTVectorStoreIndex.from_documents(documents)
        logger.info("Índice construido correctamente")
        return index
    except Exception as e:
        logger.exception("Error al construir el índice vectorial")
        raise e
