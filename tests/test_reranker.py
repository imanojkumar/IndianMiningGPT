from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)


from src.retrieval.retrieve import retrieve
from src.reranking.rerank import Reranker

query = (
    "What is star rating of mines?"
)

docs = retrieve(
    query,
    top_k=20
)

reranker = Reranker()

results = reranker.rerank(
    query,
    docs,
    top_k=5
)

for i, r in enumerate(
    results,
    start=1
):

    print(
        f"\n{i}"
    )

    print(
        r["rerank_score"]
    )

    print(
        r["source_file"]
    )

    print(
        r["text"][:200]
    )
