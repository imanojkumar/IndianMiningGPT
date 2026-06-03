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

from src.retrieval.retrieve import retrieve
from src.reranking.rerank import Reranker
from src.rag.context_builder import ContextBuilder


query = (
    "What is star rating of mines?"
)

results = retrieve(
    query,
    top_k=20
)

reranker = Reranker()

ranked = reranker.rerank(
    query,
    results,
    top_k=5
)

builder = ContextBuilder()

context = builder.build(
    query,
    ranked
)

print(
    "\nCONTEXT SIZE:",
    len(context)
)

print(
    "\nCONTEXT PREVIEW\n"
)

print(
    context[:3000]
)
