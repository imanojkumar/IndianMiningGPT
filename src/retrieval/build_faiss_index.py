"""
IndianMiningGPT
Phase 4.2

Build FAISS Index

Input:
    data/processed/embeddings/embeddings.npy
    data/processed/embeddings/embedding_registry.csv

Output:
    data/processed/faiss/faiss.index
    data/processed/faiss/faiss_metadata.csv
"""

from pathlib import Path

import faiss
import numpy as np
import pandas as pd


# --------------------------------------------------
# PATHS
# --------------------------------------------------

EMBEDDING_DIR = Path(
    "data/processed/embeddings"
)

FAISS_DIR = Path(
    "data/processed/faiss"
)

FAISS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

EMBEDDING_FILE = (
    EMBEDDING_DIR / "embeddings.npy"
)

REGISTRY_FILE = (
    EMBEDDING_DIR / "embedding_registry.csv"
)

INDEX_FILE = (
    FAISS_DIR / "faiss.index"
)

METADATA_FILE = (
    FAISS_DIR / "faiss_metadata.csv"
)


# --------------------------------------------------
# LOAD EMBEDDINGS
# --------------------------------------------------

print("\nLoading embeddings...")

if not EMBEDDING_FILE.exists():
    raise FileNotFoundError(
        EMBEDDING_FILE
    )

embeddings = np.load(
    EMBEDDING_FILE
)

print(
    "Embedding Shape:",
    embeddings.shape
)

print(
    "Embedding Dtype:",
    embeddings.dtype
)

# ensure float32
embeddings = embeddings.astype(
    np.float32
)


# --------------------------------------------------
# VALIDATE EMBEDDINGS
# --------------------------------------------------

print("\nValidating embeddings...")

if np.isnan(embeddings).any():
    raise ValueError(
        "NaN values detected."
    )

if np.isinf(embeddings).any():
    raise ValueError(
        "Infinite values detected."
    )

rows, dimensions = (
    embeddings.shape
)

print(
    f"Vectors: {rows}"
)

print(
    f"Dimensions: {dimensions}"
)

# check normalization
sample_norm = np.linalg.norm(
    embeddings[0]
)

print(
    f"Sample Vector Norm: "
    f"{sample_norm:.4f}"
)

if not (
    0.95 <= sample_norm <= 1.05
):
    print(
        "\nWARNING:"
        " vectors may not be normalized."
    )


# --------------------------------------------------
# LOAD REGISTRY
# --------------------------------------------------

print("\nLoading registry...")

registry = pd.read_csv(
    REGISTRY_FILE
)

if len(registry) != rows:
    raise ValueError(
        "Registry count does not match "
        "embedding count."
    )

print(
    f"Registry Rows: {len(registry)}"
)


# --------------------------------------------------
# BUILD INDEX
# --------------------------------------------------

print("\nBuilding FAISS index...")

index = faiss.IndexFlatIP(
    dimensions
)

index.add(
    embeddings
)

print(
    f"Index Size: {index.ntotal}"
)


# --------------------------------------------------
# SAVE INDEX
# --------------------------------------------------

print("\nSaving index...")

faiss.write_index(
    index,
    str(INDEX_FILE)
)

registry.to_csv(
    METADATA_FILE,
    index=False
)

print(
    f"Saved: {INDEX_FILE}"
)

print(
    f"Saved: {METADATA_FILE}"
)


# --------------------------------------------------
# VERIFY INDEX
# --------------------------------------------------

print("\nVerifying index...")

loaded_index = faiss.read_index(
    str(INDEX_FILE)
)

print(
    "Loaded Index Size:",
    loaded_index.ntotal
)

if loaded_index.ntotal != rows:
    raise ValueError(
        "Index verification failed."
    )


# --------------------------------------------------
# TEST SEARCH
# --------------------------------------------------

print("\nRunning test search...")

query = embeddings[0].reshape(
    1,
    -1
)

scores, ids = loaded_index.search(
    query,
    5
)

print("\nTop 5 Results")

for rank in range(
    len(ids[0])
):

    vector_id = int(
        ids[0][rank]
    )

    score = float(
        scores[0][rank]
    )

    chunk_name = registry.iloc[
        vector_id
    ]["chunk_file"]

    print(
        f"{rank+1}. "
        f"{chunk_name} "
        f"({score:.4f})"
    )

print(
    "\nPhase 4.2 Complete"
)
