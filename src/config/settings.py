import os
from dotenv import load_dotenv

# Cargar variables de .env
load_dotenv()

# --- Claves API ---
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# --- Parámetros por defecto ---
DEFAULT_IMAGE_COUNT = 5
