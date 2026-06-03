"""
IndianMiningGPT
Phase 5.1

Semantic Search

Input:
    Natural language query

Uses:
    BGE-M3
    FAISS

Returns:
    Top-K matching chunks
"""

from pathlib import Path

import faiss
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer


# --------------------------------------------
# CONFIG
# --------------------------------------------

MODEL_NAME = "BAAI/bge-m3"

TOP_K = 5

FAISS_DIR = Path(
    "data/processed/faiss"
)

CHUNK_DIR = Path(
    "data/processed/chunks"
)

INDEX_FILE = (
    FAISS_DIR / "faiss.index"
)

METADATA_FILE = (
    FAISS_DIR / "faiss_metadata.csv"
)


# --------------------------------------------
# LOAD MODEL
# --------------------------------------------

print("Loading BGE-M3...")

model = SentenceTransformer(
    MODEL_NAME
)

print("Model Loaded")


# --------------------------------------------
# LOAD INDEX
# --------------------------------------------

print("Loading FAISS Index...")

index = faiss.read_index(
    str(INDEX_FILE)
)

metadata = pd.read_csv(
    METADATA_FILE
)

print(
    f"Vectors: {index.ntotal}"
)


# --------------------------------------------
# SEARCH FUNCTION
# --------------------------------------------

def search(query, top_k=TOP_K):

    query_embedding = model.encode(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True
    )

    scores, ids = index.search(
        query_embedding.astype(np.float32),
        top_k
    )

    results = []

    for score, idx in zip(
        scores[0],
        ids[0]
    ):

        chunk_file = metadata.iloc[
            idx
        ]["chunk_file"]

        chunk_path = (
            CHUNK_DIR /
            chunk_file
        )

        chunk_text = chunk_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        results.append(
            {
                "chunk_file": chunk_file,
                "score": float(score),
                "text": chunk_text[:500]
            }
        )

    return results


# --------------------------------------------
# CLI
# --------------------------------------------

while True:

    query = input(
        "\nQuery (exit to quit): "
    )

    if query.lower() == "exit":
        break

    results = search(query)

    print("\nResults\n")

    for i, result in enumerate(
        results,
        start=1
    ):

        print(
            f"\n{i}. "
            f"{result['chunk_file']}"
        )

        print(
            f"Score: "
            f"{result['score']:.4f}"
        )

        print(
            result["text"]
        )

        print(
            "\n" + "-" * 80
        )
