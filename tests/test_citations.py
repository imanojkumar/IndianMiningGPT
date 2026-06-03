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

result = bot.ask(
    "What is star rating of mines?"
)

print(
    "\nANSWER\n"
)

print(
    result["answer"]
)
