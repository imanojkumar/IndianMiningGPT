"""
Phase 4.1
Generate BGE-M3 Embeddings

Input:
    data/processed/chunks/*.txt

Output:
    data/processed/embeddings/embeddings.npy
    data/processed/embeddings/embedding_registry.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd
import torch

from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# CONFIG
# --------------------------------------------------

CHUNK_DIR = Path(
    "data/processed/chunks"
)

OUTPUT_DIR = Path(
    "data/processed/embeddings"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

EMBEDDING_FILE = (
    OUTPUT_DIR / "embeddings.npy"
)

REGISTRY_FILE = (
    OUTPUT_DIR / "embedding_registry.csv"
)

MODEL_NAME = "BAAI/bge-m3"

# RTX 3060 6GB safe
BATCH_SIZE = 2


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

print("\nLoading model...")
print(MODEL_NAME)

DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print(f"Device: {DEVICE}")

model = SentenceTransformer(
    MODEL_NAME,
    device=DEVICE
)

print(
    f"Embedding Dimension: "
    f"{model.get_embedding_dimension()}"
)


# --------------------------------------------------
# LOAD CHUNKS
# --------------------------------------------------

print("\nReading chunks...")

chunk_files = sorted(
    CHUNK_DIR.glob("*.txt")
)

texts = []
registry = []

for idx, file_path in enumerate(
    chunk_files
):

    try:

        text = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        texts.append(text)

        registry.append(
            {
                "vector_id": idx,
                "chunk_file": file_path.name
            }
        )

    except Exception as e:

        print(
            f"Failed: {file_path.name}"
        )

        print(e)

print(
    f"Chunks Loaded: "
    f"{len(texts)}"
)


# --------------------------------------------------
# GENERATE EMBEDDINGS
# --------------------------------------------------

print("\nGenerating embeddings...")

all_embeddings = []

total_chunks = len(texts)

for start in range(
    0,
    total_chunks,
    BATCH_SIZE
):

    end = min(
        start + BATCH_SIZE,
        total_chunks
    )

    batch_texts = texts[
        start:end
    ]

    print(
        f"[{start+1}/{total_chunks}] "
        f"to "
        f"[{end}/{total_chunks}]"
    )

    batch_embeddings = model.encode(
        batch_texts,
        batch_size=BATCH_SIZE,
        show_progress_bar=False,
        normalize_embeddings=True,
        convert_to_numpy=True
    )

    all_embeddings.append(
        batch_embeddings.astype(
            np.float32
        )
    )

    if DEVICE == "cuda":
        torch.cuda.empty_cache()

embeddings = np.vstack(
    all_embeddings
)

print(
    "\nEmbedding Matrix Shape:"
)

print(
    embeddings.shape
)


# --------------------------------------------------
# SAVE EMBEDDINGS
# --------------------------------------------------

np.save(
    EMBEDDING_FILE,
    embeddings
)

print(
    f"\nSaved: {EMBEDDING_FILE}"
)


# --------------------------------------------------
# SAVE REGISTRY
# --------------------------------------------------

registry_df = pd.DataFrame(
    registry
)

registry_df.to_csv(
    REGISTRY_FILE,
    index=False
)

print(
    f"Saved: {REGISTRY_FILE}"
)

print("\nComplete.")
"""
Phase 4.1
Generate BGE-M3 Embeddings

Input:
    data/processed/chunks/*.txt

Output:
    data/processed/embeddings/embeddings.npy
    data/processed/embeddings/embedding_registry.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd
import torch

from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# CONFIG
# --------------------------------------------------

MODEL_NAME = "BAAI/bge-m3"

CHUNK_DIR = Path(
    "data/processed/chunks"
)

OUTPUT_DIR = Path(
    "data/processed/embeddings"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

EMBEDDING_FILE = (
    OUTPUT_DIR / "embeddings.npy"
)

REGISTRY_FILE = (
    OUTPUT_DIR / "embedding_registry.csv"
)

BATCH_SIZE = 8


# --------------------------------------------------
# DEVICE
# --------------------------------------------------

DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print("\nDevice:", DEVICE)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

print("\nLoading model...")
print(MODEL_NAME)

model = SentenceTransformer(
    MODEL_NAME,
    device=DEVICE
)

print(
    "Embedding Dimension:",
    model.get_embedding_dimension()
)


# --------------------------------------------------
# LOAD CHUNK FILES
# --------------------------------------------------

chunk_files = sorted(
    CHUNK_DIR.glob("*.txt")
)

print(
    f"\nChunks Found: {len(chunk_files)}"
)


# --------------------------------------------------
# EMBEDDING LOOP
# --------------------------------------------------

all_embeddings = []

registry_rows = []

total = len(chunk_files)

for start in range(
    0,
    total,
    BATCH_SIZE
):

    end = min(
        start + BATCH_SIZE,
        total
    )

    batch_files = (
        chunk_files[start:end]
    )

    texts = []

    for f in batch_files:

        text = f.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        texts.append(text)

    embeddings = model.encode(
        texts,
        batch_size=BATCH_SIZE,
        normalize_embeddings=True,
        convert_to_numpy=True,
        show_progress_bar=False
    )

    embeddings = embeddings.astype(
        np.float32
    )

    all_embeddings.append(
        embeddings
    )

    for i, f in enumerate(
        batch_files
    ):

        registry_rows.append(
            {
                "vector_id":
                start + i,

                "chunk_file":
                f.name
            }
        )

    if DEVICE == "cuda":

        torch.cuda.empty_cache()

    if start % 100 == 0:

        print(
            f"{end}/{total}"
        )


# --------------------------------------------------
# STACK
# --------------------------------------------------

print("\nCombining embeddings...")

embedding_matrix = np.vstack(
    all_embeddings
)

print(
    embedding_matrix.shape
)


# --------------------------------------------------
# SAVE
# --------------------------------------------------

np.save(
    EMBEDDING_FILE,
    embedding_matrix
)

pd.DataFrame(
    registry_rows
).to_csv(
    REGISTRY_FILE,
    index=False
)

print(
    "\nEmbeddings saved:"
)

print(
    EMBEDDING_FILE
)

print(
    REGISTRY_FILE
)

print(
    "\nPhase 4.1 Complete"
)
