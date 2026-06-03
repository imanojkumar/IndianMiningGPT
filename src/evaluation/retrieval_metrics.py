"""
IndianMiningGPT
Phase 9.3

Retrieval Metrics
"""


def recall_at_k(
    retrieved_docs,
    expected_document
):

    for doc in retrieved_docs:

        if (
            doc["source_file"]
            == expected_document
        ):

            return 1

    return 0
