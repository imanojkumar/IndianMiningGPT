from pathlib import Path
import pandas as pd

TEXT_DIR = Path("data/interim/text")
CHUNK_DIR = Path("data/processed/chunks")

CHUNK_SIZE = 1000
OVERLAP = 200

records = []

chunk_id = 1

for txt_file in sorted(TEXT_DIR.glob("*.txt")):

    text = txt_file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    words = text.split()

    start = 0
    chunk_num = 1

    while start < len(words):

        end = start + CHUNK_SIZE

        chunk_words = words[start:end]

        chunk_text = " ".join(chunk_words)

        chunk_name = f"chunk_{chunk_id:06d}.txt"

        (CHUNK_DIR / chunk_name).write_text(
            chunk_text,
            encoding="utf-8"
        )

        records.append({
            "chunk_id": chunk_id,
            "chunk_file": chunk_name,
            "source_file": txt_file.name,
            "chunk_number": chunk_num,
            "word_count": len(chunk_words)
        })

        chunk_id += 1
        chunk_num += 1

        start += (CHUNK_SIZE - OVERLAP)

registry = pd.DataFrame(records)

registry.to_csv(
    "data/processed/chunk_metadata/chunk_registry.csv",
    index=False
)

print("\nChunking Complete")
print("Chunks:", len(registry))
print("Registry:")
print("data/processed/chunk_metadata/chunk_registry.csv")
