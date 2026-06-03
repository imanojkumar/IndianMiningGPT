"""
IndianMiningGPT
Phase 9.3

Benchmark Runner
"""

from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parents[2]
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from src.retrieval.retrieve import (
    retrieve
)

from src.evaluation.retrieval_metrics import (
    recall_at_k
)


BENCHMARK_FILE = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "benchmark_questions.csv"
)


def run():

    df = pd.read_csv(
        BENCHMARK_FILE
    )

    results = []

    total = 0
    hits = 0

    for _, row in df.iterrows():

        question = row[
            "question"
        ]

        expected = row[
            "expected_document"
        ]

        retrieved_docs = retrieve(
            question,
            top_k=5
        )

        score = recall_at_k(
            retrieved_docs,
            expected
        )

        total += 1
        hits += score

        results.append(
            {
                "question": question,
                "expected_document": expected,
                "hit": score
            }
        )

        print(
            f"{question} -> {score}"
        )

    recall = hits / total

    print(
        "\nRecall@5:",
        round(
            recall,
            4
        )
    )

    results_df = pd.DataFrame(
        results
    )

    output_file = (
        PROJECT_ROOT
        / "data"
        / "evaluation"
        / "benchmark_results.csv"
    )

    results_df.to_csv(
        output_file,
        index=False
    )

    print(
        f"\nSaved: {output_file}"
    )


if __name__ == "__main__":

    run()
