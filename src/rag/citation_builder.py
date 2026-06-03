"""
IndianMiningGPT
Phase 7.3 Citation Builder
"""


class CitationBuilder:

    def build(
        self,
        ranked_docs,
        max_sources=5
    ):

        if not ranked_docs:
            return ""

        lines = []

        lines.append(
            "\nSOURCES\n"
        )

        for idx, doc in enumerate(
            ranked_docs[:max_sources],
            start=1
        ):

            source = doc.get(
                "source_file",
                "unknown"
            )

            chunk = doc.get(
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

            lines.append(
                f"[{idx}] {source}"
            )

            lines.append(
                f"    Chunk: {chunk}"
            )

            lines.append(
                f"    Score: {score}"
            )

            lines.append("")

        return "\n".join(lines)
