# src/config/llama_settings.py
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
import tiktoken

from src.clients.openai_client import OpenAIClient

# 1️⃣ LLM
client = OpenAIClient()
api_key = client.get_key()
Settings.llm = OpenAI(model="gpt-4.1", temperature=0.1, api_key=api_key)

# 2️⃣ Embedding Model
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small", embed_batch_size=100)

# 3️⃣ Node Parser / Text Splitter
Settings.text_splitter = SentenceSplitter(chunk_size=512)  # tamaño de chunks
Settings.chunk_overlap = 20  # opcional

# 4️⃣ Tokenizer
Settings.tokenizer = tiktoken.encoding_for_model("gpt-4.1").encode

# 5️⃣ Callbacks
from llama_index.core.callbacks import TokenCountingHandler, CallbackManager
token_counter = TokenCountingHandler()
Settings.callback_manager = CallbackManager([token_counter])

# 6️⃣ Prompt helper / contexto
Settings.context_window = 4096
Settings.num_output = 256
