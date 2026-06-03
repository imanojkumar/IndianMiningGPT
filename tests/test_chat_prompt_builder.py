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

from src.rag.chat_prompt_builder import (
    ChatPromptBuilder
)

builder = ChatPromptBuilder()

prompt = builder.build(
    query="Who issues it?",
    memory_text="""
Question:
What is star rating?

Answer:
A sustainability rating system.
""",
    context="""
IBM verifies star rating submissions.
"""
)

print(prompt)
