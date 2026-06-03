"""
IndianMiningGPT

Singleton Model Manager
"""

from sentence_transformers import (
    SentenceTransformer
)

from sentence_transformers import (
    CrossEncoder
)

from src.common.config import (
    EMBEDDING_MODEL,
    RERANK_MODEL
)


class ModelManager:

    _embedding_model = None

    _reranker_model = None

    @classmethod
    def embedding_model(cls):

        if cls._embedding_model is None:

            print(
                "Loading Embedding Model..."
            )

            cls._embedding_model = (
                SentenceTransformer(
                    EMBEDDING_MODEL
                )
            )

        return cls._embedding_model

    @classmethod
    def reranker_model(cls):

        if cls._reranker_model is None:

            print(
                "Loading Reranker..."
            )

            cls._reranker_model = (
                CrossEncoder(
                    RERANK_MODEL
                )
            )

        return cls._reranker_model
