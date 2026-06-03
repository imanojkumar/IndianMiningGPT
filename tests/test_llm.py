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

from src.llm.answer_generator import (
    AnswerGenerator
)


generator = AnswerGenerator()

prompt = """
Answer briefly.

Question:
What is mining?
"""

answer = generator.answer(
    prompt
)

print("\nANSWER\n")
print(answer)
