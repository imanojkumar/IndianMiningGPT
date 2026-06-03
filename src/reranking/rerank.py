"""
IndianMiningGPT
Phase 10.6

Reranker
(Lazy Loaded)
"""

from src.models.model_manager import (
    ModelManager
)


class Reranker:

    def __init__(self):

        self.model = None

    def _get_model(self):

        if self.model is None:

            self.model = (
                ModelManager
                .reranker_model()
            )

        return self.model

    def rerank(
        self,
        query,
        retrieved_docs,
        top_k=5
    ):

        if not retrieved_docs:
            return []

        model = (
            self._get_model()
        )

        pairs = [
            (
                query,
                doc["text"]
            )
            for doc in retrieved_docs
        ]

        scores = model.predict(
            pairs,
            batch_size=16,
            show_progress_bar=False
        )

        ranked_docs = []

        for doc, score in zip(
            retrieved_docs,
            scores
        ):

            doc_copy = doc.copy()

            doc_copy[
                "rerank_score"
            ] = float(score)

            ranked_docs.append(
                doc_copy
            )

        ranked_docs.sort(
            key=lambda x:
            x["rerank_score"],
            reverse=True
        )

        return ranked_docs[:top_k]
