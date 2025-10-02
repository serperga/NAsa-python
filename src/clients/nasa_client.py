import requests
from src.config.settings import NASA_API_KEY, DEFAULT_IMAGE_COUNT
from config.api.api_endpoints import NASA_APOD_BASE_URL

def get_apod_images(count: int = DEFAULT_IMAGE_COUNT):
    """
    Llama a la API de APOD y devuelve una lista de entradas con título, fecha, url y explicación.
    """
    params = {
        "api_key": NASA_API_KEY,
        "count": count,
    }
    response = requests.get(NASA_APOD_BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Error en la API de NASA: {response.status_code} - {response.text}")

    return response.json()
