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

from src.rag.chat_pipeline import (
    ChatPipeline
)

bot = ChatPipeline()

print(
    "\nQUESTION 1\n"
)

answer1 = bot.ask(
    "What is star rating of mines?"
)

print(answer1)

print(
    "\nQUESTION 2\n"
)

answer2 = bot.ask(
    "Who issues it?"
)

print(answer2)
