from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

registry = pd.read_csv(
    PROJECT_ROOT /
    "data/metadata/corpus_registry.csv"
)

def classify(title):

    if pd.isna(title):
        return "UNKNOWN"

    t = str(title).upper()

    if "ACT" in t:
        return "ACT"

    if "RULE" in t:
        return "RULE"

    if "REGULATION" in t:
        return "REGULATION"

    if "NOTIFICATION" in t:
        return "NOTIFICATION"

    if "STANDARD" in t:
        return "STANDARD"

    if "GUIDANCE" in t:
        return "GUIDELINE"

    if "GUIDELINE" in t:
        return "GUIDELINE"

    if "MANUAL" in t:
        return "MANUAL"

    if "POLICY" in t:
        return "POLICY"

    if "ORDER" in t:
        return "ORDER"

    if "REPORT" in t:
        return "REPORT"

    return "UNKNOWN"


registry["document_type"] = (
    registry["first_page_title"]
    .apply(classify)
)

registry.to_csv(
    PROJECT_ROOT /
    "data/metadata/corpus_registry.csv",
    index=False
)

print("\nClassification Complete")
print(
    registry["document_type"]
    .value_counts()
)
