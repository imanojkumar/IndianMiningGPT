from pathlib import Path
import sys

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parents[1]
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from src.rag.pipeline import (
    IndianMiningGPT
)

bot = IndianMiningGPT()

query = (
    "What is star rating of mines?"
)

result = bot.ask(
    query
)

print("\nQUESTION\n")
print(query)

print("\nANSWER\n")
print(result["answer"])

print("\nTOP SOURCES\n")

for i, doc in enumerate(
    result["sources"],
    start=1
):

    print(
        f"{i}. {doc['source_file']}"
    )
