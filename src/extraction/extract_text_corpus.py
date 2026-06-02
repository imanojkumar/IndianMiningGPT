from pathlib import Path

from pypdf import PdfReader

import pandas as pd


INPUT_CSV = Path(
    "data/metadata/raw_inventory.csv"
)

OUTPUT_DIR = Path(
    "data/interim/text"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def extract_text(pdf_path):

    try:

        reader = PdfReader(pdf_path)

        pages = []

        for page in reader.pages:

            try:

                text = page.extract_text()

                if text:
                    pages.append(text)

            except Exception:
                pass

        return "\n".join(pages)

    except Exception:

        return ""


def main():

    inventory = pd.read_csv(INPUT_CSV)

    total = len(inventory)

    for idx, row in inventory.iterrows():

        file_name = row["file_name"]

        pdf_path = row["file_path"]

        txt_name = (
            Path(file_name).stem + ".txt"
        )

        output_file = (
            OUTPUT_DIR / txt_name
        )

        text = extract_text(pdf_path)

        output_file.write_text(
            text,
            encoding="utf-8"
        )

        print(
            f"[{idx+1}/{total}] "
            f"{txt_name}"
        )

    print()
    print("Corpus extraction complete")


if __name__ == "__main__":
    main()
