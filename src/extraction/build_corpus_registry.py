from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

raw_inventory = pd.read_csv(
    PROJECT_ROOT / "data/metadata/raw_inventory.csv"
)

enriched_inventory = pd.read_csv(
    PROJECT_ROOT / "data/metadata/enriched_inventory.csv"
)

extraction_registry = pd.read_csv(
    PROJECT_ROOT / "data/metadata/extraction_registry.csv"
)

document_registry = pd.read_csv(
    PROJECT_ROOT / "data/metadata/document_registry.csv"
)

# ---------------------------------------------------
# Merge inventories
# ---------------------------------------------------

df = raw_inventory.merge(
    enriched_inventory,
    on="file_name",
    how="left",
    suffixes=("", "_meta")
)

df = df.merge(
    extraction_registry,
    on="file_name",
    how="left"
)

# ---------------------------------------------------
# Bring title information
# ---------------------------------------------------

if "first_page_title" in document_registry.columns:
    df = df.merge(
        document_registry[
            ["file_name", "first_page_title"]
        ],
        on="file_name",
        how="left"
    )

# ---------------------------------------------------
# Initialize future fields
# ---------------------------------------------------

df["language"] = ""
df["document_type"] = ""
df["ocr_required"] = False

# OCR candidates

df.loc[
    df["status"].isin(["FAILED", "POOR"]),
    "ocr_required"
] = True

# ---------------------------------------------------
# Save
# ---------------------------------------------------

output_file = (
    PROJECT_ROOT /
    "data/metadata/corpus_registry.csv"
)

df.to_csv(output_file, index=False)

print("\nCorpus Registry Created")
print(output_file)
print("\nDocuments:", len(df))
