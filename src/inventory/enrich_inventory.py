from pathlib import Path
import pandas as pd
from pypdf import PdfReader

INPUT_CSV = Path("data/metadata/raw_inventory.csv")
OUTPUT_CSV = Path("data/metadata/enriched_inventory.csv")


def extract_metadata(pdf_path: str):

    try:
        reader = PdfReader(pdf_path)

        meta = reader.metadata

        return {
            "title": getattr(meta, "title", "") if meta else "",
            "author": getattr(meta, "author", "") if meta else "",
            "subject": getattr(meta, "subject", "") if meta else "",
            "creator": getattr(meta, "creator", "") if meta else "",
            "producer": getattr(meta, "producer", "") if meta else "",
            "creation_date": getattr(meta, "creation_date", "") if meta else "",
            "modification_date": getattr(meta, "modification_date", "") if meta else "",
        }

    except Exception as e:

        return {
            "title": "",
            "author": "",
            "subject": "",
            "creator": "",
            "producer": "",
            "creation_date": "",
            "modification_date": "",
        }


def main():

    df = pd.read_csv(INPUT_CSV)

    metadata_rows = []

    for _, row in df.iterrows():

        meta = extract_metadata(row["file_path"])

        metadata_rows.append(meta)

    metadata_df = pd.DataFrame(metadata_rows)

    output_df = pd.concat(
        [df.reset_index(drop=True), metadata_df],
        axis=1
    )

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    output_df.to_csv(
        OUTPUT_CSV,
        index=False
    )

    print()
    print(f"Enriched inventory written to:")
    print(OUTPUT_CSV)
    print()
    print(f"Records processed: {len(output_df)}")


if __name__ == "__main__":
    main()
