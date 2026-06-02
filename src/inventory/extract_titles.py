from pathlib import Path
import pandas as pd
from pypdf import PdfReader
import re

INPUT_CSV = Path("data/metadata/enriched_inventory.csv")
OUTPUT_CSV = Path("data/metadata/document_registry.csv")


def get_first_page_text(pdf_path):

    try:

        reader = PdfReader(pdf_path)

        if len(reader.pages) == 0:
            return ""

        text = reader.pages[0].extract_text()

        if text is None:
            return ""

        return text.strip()

    except Exception:

        return ""


def infer_title(text):

    if not text:
        return ""

    lines = []

    for line in text.splitlines():

        line = line.strip()

        if len(line) > 5:
            lines.append(line)

    title = " ".join(lines[:5])

    title = re.sub(r"\s+", " ", title)

    return title[:300]


def main():

    df = pd.read_csv(INPUT_CSV)

    titles = []

    for _, row in df.iterrows():

        text = get_first_page_text(row["file_path"])

        titles.append(infer_title(text))

    df["first_page_title"] = titles

    df.to_csv(
        OUTPUT_CSV,
        index=False
    )

    print()
    print("Registry created:")
    print(OUTPUT_CSV)
    print()


if __name__ == "__main__":
    main()
