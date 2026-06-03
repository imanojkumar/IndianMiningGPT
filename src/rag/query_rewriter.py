"""
IndianMiningGPT
Phase 9.1

Query Rewriter
"""


class QueryRewriter:

    def rewrite(
        self,
        query,
        memory_text
    ):

        query_lower = query.lower()

        followup_words = [
            "it",
            "they",
            "them",
            "this",
            "that",
            "these",
            "those"
        ]

        if not any(
            word in query_lower
            for word in followup_words
        ):
            return query

        if not memory_text:
            return query

        lines = memory_text.split(
            "\n"
        )

        questions = []

        for i, line in enumerate(lines):

            line = line.strip()

            if line.startswith(
                "Question"
            ):

                if i + 1 < len(lines):

                    candidate = (
                        lines[i + 1]
                        .strip()
                    )

                    if candidate:

                        questions.append(
                            candidate
                        )

        if not questions:
            return query

        last_question = (
            questions[-1]
        )

        return (
            f"{query} "
            f"(context: {last_question})"
        )
