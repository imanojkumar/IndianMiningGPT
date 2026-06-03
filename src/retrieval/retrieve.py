"""
IndianMiningGPT
Phase 5.2 Retrieval Layer

Purpose
-------
Convert a user query into structured retrieval results.

Inputs
------
Query Text

Uses
----
data/processed/faiss/faiss.index
data/processed/faiss/faiss_metadata.csv
data/processed/chunk_metadata/chunk_registry.csv
data/processed/chunks/*.txt

Returns
-------
[
    {
        "score": float,
        "chunk_file": str,
        "source_file": str,
        "chunk_number": int,
        "word_count": int,
        "text": str
    }
]
"""

from pathlib import Path

import faiss
import pandas as pd
import numpy as np
import torch

from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path("data")

INDEX_FILE = (
    BASE_DIR
    / "processed"
    / "faiss"
    / "faiss.index"
)

FAISS_META_FILE = (
    BASE_DIR
    / "processed"
    / "faiss"
    / "faiss_metadata.csv"
)

CHUNK_REGISTRY_FILE = (
    BASE_DIR
    / "processed"
    / "chunk_metadata"
    / "chunk_registry.csv"
)

CHUNK_DIR = (
    BASE_DIR
    / "processed"
    / "chunks"
)

MODEL_NAME = "BAAI/bge-m3"


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

print("Loading BGE-M3...")

DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

model = SentenceTransformer(
    MODEL_NAME,
    device=DEVICE
)

print(
    f"Model Loaded ({DEVICE})"
)


# --------------------------------------------------
# LOAD FAISS
# --------------------------------------------------

if not INDEX_FILE.exists():
    raise FileNotFoundError(
        INDEX_FILE
    )

print("Loading FAISS Index...")

index = faiss.read_index(
    str(INDEX_FILE)
)

print(
    f"Vectors: {index.ntotal}"
)


# --------------------------------------------------
# LOAD METADATA
# --------------------------------------------------

if not CHUNK_REGISTRY_FILE.exists():
    raise FileNotFoundError(
        CHUNK_REGISTRY_FILE
    )

chunk_registry = pd.read_csv(
    CHUNK_REGISTRY_FILE
)

chunk_registry = chunk_registry.set_index(
    "chunk_id"
)

print(
    f"Chunk Metadata Rows: "
    f"{len(chunk_registry)}"
)


# --------------------------------------------------
# RETRIEVE FUNCTION
# --------------------------------------------------

def retrieve(
    query: str,
    top_k: int = 5
):
    """
    Retrieve Top-K chunks.
    """

    query_embedding = model.encode(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True
    )

    query_embedding = (
        query_embedding.astype(
            np.float32
        )
    )

    scores, ids = index.search(
        query_embedding,
        top_k
    )

    results = []

    for score, idx in zip(
        scores[0],
        ids[0]
    ):

        if idx < 0:
            continue

        chunk_id = idx + 1

        if chunk_id not in chunk_registry.index:
            continue

        row = chunk_registry.loc[
            chunk_id
        ]

        chunk_file = row[
            "chunk_file"
        ]

        chunk_path = (
            CHUNK_DIR
            / chunk_file
        )

        text = ""

        if chunk_path.exists():

            try:

                text = (
                    chunk_path.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )

            except Exception:

                text = ""

        results.append(
            {
                "score": float(score),
                "chunk_id": int(chunk_id),
                "chunk_file": chunk_file,
                "source_file": row[
                    "source_file"
                ],
                "chunk_number": int(
                    row["chunk_number"]
                ),
                "word_count": int(
                    row["word_count"]
                ),
                "text": text
            }
        )

    return results


# --------------------------------------------------
# CLI
# --------------------------------------------------

if __name__ == "__main__":

    while True:

        query = input(
            "\nQuery (exit to quit): "
        )

        if query.lower() in [
            "exit",
            "quit",
            "q"
        ]:
            break

        results = retrieve(
            query=query,
            top_k=5
        )

        print("\nResults\n")

        for i, r in enumerate(
            results,
            start=1
        ):

            print(
                f"{i}. "
                f"{r['chunk_file']}"
            )

            print(
                f"Score: "
                f"{r['score']:.4f}"
            )

            print(
                f"Source: "
                f"{r['source_file']}"
            )

            print(
                f"Chunk: "
                f"{r['chunk_number']}"
            )

            print(
                f"Words: "
                f"{r['word_count']}"
            )

            print("\nPreview:\n")

            print(
                r["text"][:500]
            )

            print(
                "\n"
                + "-" * 80
            )
