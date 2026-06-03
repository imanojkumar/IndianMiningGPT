"""
IndianMiningGPT
Phase 5.3 Reranker
"""

import torch
from sentence_transformers import CrossEncoder

MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"


class Reranker:

    def __init__(self):

        print(
            "Loading Cross Encoder..."
        )

        device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        print(
            f"Device: {device}"
        )

        self.model = CrossEncoder(
            MODEL_NAME,
            device=device
        )

        print(
            "Cross Encoder Loaded"
        )

    def rerank(
        self,
        query,
        retrieved_docs,
        top_k=5
    ):

        if not retrieved_docs:
            return []

        pairs = [
            (query, doc["text"])
            for doc in retrieved_docs
        ]

        scores = self.model.predict(
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
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return ranked_docs[:top_k]
