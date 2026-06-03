"""
IndianMiningGPT
Global Configuration
"""

VERBOSE = False

TOP_K_RETRIEVAL = 20

TOP_K_RERANK = 5

MAX_CONTEXT_CHUNKS = 5

MAX_CONTEXT_CHARS = 12000

EMBEDDING_MODEL = "BAAI/bge-m3"

RERANK_MODEL = (
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

OLLAMA_MODEL = "gemma3:4b"
