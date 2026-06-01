from pathlib import Path
import csv
from datetime import datetime

from pypdf import PdfReader


RAW_PDF_DIR = Path.home() / "mining_gpt" / "data" / "raw_pdfs"

OUTPUT_CSV = (
    Path.home()
    / "projects"
    / "IndianMiningGPT"
    / "data"
    / "metadata"
    / "raw_inventory.csv"
)


def get_page_count(pdf_path: Path) -> int:
    try:
        reader = PdfReader(str(pdf_path))
        return len(reader.pages)
    except Exception:
        return -1


def get_file_size_mb(pdf_path: Path) -> float:
    return round(pdf_path.stat().st_size / (1024 * 1024), 2)


def discover_pdfs():
    return sorted(RAW_PDF_DIR.glob("*.pdf"))


def build_inventory():

    pdf_files = discover_pdfs()

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "file_name",
            "file_path",
            "file_size_mb",
            "page_count",
            "inventory_timestamp"
        ])

        for pdf in pdf_files:

            writer.writerow([
                pdf.name,
                str(pdf),
                get_file_size_mb(pdf),
                get_page_count(pdf),
                datetime.utcnow().isoformat()
            ])

    print(f"\nInventory generated:")
    print(OUTPUT_CSV)
    print(f"PDFs discovered: {len(pdf_files)}")


if __name__ == "__main__":
    build_inventory()
