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

from src.rag.query_rewriter import (
    QueryRewriter
)

rewriter = QueryRewriter()

memory = """
Question 1:
What is Star Rating of Mines?

Answer 1:
A sustainability rating system.
"""

query = (
    "Who issues it?"
)

new_query = (
    rewriter.rewrite(
        query,
        memory
    )
)

print(
    new_query
)
