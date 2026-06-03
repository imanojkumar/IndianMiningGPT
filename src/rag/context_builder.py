"""
IndianMiningGPT
Phase 6.1 Context Builder
"""


class ContextBuilder:

    def __init__(
        self,
        max_chunks=5,
        max_chars=12000
    ):

        self.max_chunks = max_chunks
        self.max_chars = max_chars

    def build(
        self,
        query,
        ranked_docs
    ):

        if not ranked_docs:
            return ""

        context_sections = []

        current_chars = 0

        docs_used = 0

        for doc in ranked_docs:

            if docs_used >= self.max_chunks:
                break

            source_file = doc.get(
                "source_file",
                "unknown"
            )

            chunk_number = doc.get(
                "chunk_number",
                "?"
            )

            score = round(
                doc.get(
                    "rerank_score",
                    doc.get(
                        "score",
                        0
                    )
                ),
                4
            )

            text = (
                doc.get(
                    "text",
                    ""
                )
                .replace(
                    "\n\n",
                    "\n"
                )
                .strip()
            )

            section = f"""
==================================================
SOURCE FILE: {source_file}
CHUNK NUMBER: {chunk_number}
RELEVANCE SCORE: {score}
==================================================

{text}
"""

            section_size = len(
                section
            )

            if (
                current_chars
                + section_size
                > self.max_chars
            ):
                break

            context_sections.append(
                section
            )

            current_chars += (
                section_size
            )

            docs_used += 1

        context = "\n\n".join(
            context_sections
        )

        return context
