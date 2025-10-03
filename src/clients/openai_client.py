import os
from llama_index.llms.openai import OpenAI

class OpenAIClient:
    def __init__(self):
        """
        Inicializa el cliente leyendo la API key desde la variable de entorno OPENAI_API_KEY.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")

    def get_key(self):
        """
        Devuelve la API key almacenada.
        """
        return self.api_key

    def get_llm(self, model="gpt-4.1", temperature=0.1):
        """
        Devuelve un objeto LLM OpenAI listo para usar en Settings o build_index.
        """
        if not self.api_key:
            raise ValueError("No se encontró la API key de OpenAI.")
        return OpenAI(model=model, temperature=temperature, api_key=self.api_key)
