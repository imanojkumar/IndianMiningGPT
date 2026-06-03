"""
IndianMiningGPT
Phase 10.5

Retrieval Layer
Lazy Loaded Models
"""

from pathlib import Path

import numpy as np

from src.models.model_manager import (
    ModelManager
)

from src.models.faiss_manager import (
    FaissManager
)


# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path("data")

CHUNK_DIR = (
    BASE_DIR
    / "processed"
    / "chunks"
)


# --------------------------------------------------
# RETRIEVE
# --------------------------------------------------

def retrieve(
    query,
    top_k=5
):

    model = (
        ModelManager
        .embedding_model()
    )

    index = (
        FaissManager.index()
    )

    chunk_registry = (
        FaissManager
        .chunk_registry()
    )

    chunk_registry = (
        chunk_registry.set_index(
            "chunk_id"
        )
    )

    query_embedding = (
        model.encode(
            [query],
            normalize_embeddings=True,
            convert_to_numpy=True
        )
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

        if (
            chunk_id
            not in chunk_registry.index
        ):
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
