from src.config.settings import OPENAI_API_KEY

class OpenAIClient:
    """
    Clase para manejar la API de OpenAI.
    Se encarga de validar la clave y crear clientes LLM.
    """

    def __init__(self, api_key: str = None):
        # Usar la API key pasada o la del settings.py
        self.api_key = api_key or OPENAI_API_KEY
        self.validate_api_key()

    def validate_api_key(self):
        """
        Comprueba que la API key está definida.
        Lanza excepción si falta.
        """
        if not self.api_key:
            raise ValueError(
                "Falta configurar OPENAI_API_KEY en .env o pasarla como argumento."
            )

    def get_key(self) -> str:
        """
        Devuelve la API key validada.
        """
        return self.api_key
