from pathlib import Path

import pandas as pd

from pypdf import PdfReader


INPUT_CSV = Path("data/metadata/raw_inventory.csv")

OUTPUT_CSV = Path("data/metadata/extraction_registry.csv")


def extract_text(pdf_path):

    try:

        reader = PdfReader(pdf_path)

        text = []

        for page in reader.pages:

            try:
                page_text = page.extract_text()

                if page_text:
                    text.append(page_text)

            except Exception:
                pass

        return "\n".join(text)

    except Exception:

        return ""


def classify_quality(page_count, char_count):

    if char_count == 0:

        return "FAILED"

    chars_per_page = char_count / max(page_count, 1)

    if chars_per_page < 100:

        return "POOR"

    if chars_per_page < 500:

        return "FAIR"

    return "GOOD"


def main():

    inventory = pd.read_csv(INPUT_CSV)

    results = []

    total_docs = len(inventory)

    print()
    print(f"Assessing {total_docs} PDFs...")
    print()

    for idx, row in inventory.iterrows():

        pdf_path = row["file_path"]

        page_count = int(row["page_count"])

        text = extract_text(pdf_path)

        char_count = len(text)

        word_count = len(text.split())

        status = classify_quality(
            page_count,
            char_count
        )

        results.append(
            {
                "file_name": row["file_name"],
                "page_count": page_count,
                "char_count": char_count,
                "word_count": word_count,
                "chars_per_page": round(
                    char_count / max(page_count, 1),
                    2
                ),
                "status": status
            }
        )

        print(
            f"[{idx+1}/{total_docs}] "
            f"{row['file_name']} -> {status}"
        )

    df = pd.DataFrame(results)

    df.to_csv(
        OUTPUT_CSV,
        index=False
    )

    print()
    print("Assessment complete.")
    print(OUTPUT_CSV)
    print()


if __name__ == "__main__":
    main()
