"""
IndianMiningGPT
Phase 7.4
Answer Validator
"""


class AnswerValidator:

    def __init__(
        self,
        min_answer_length=20,
        max_answer_length=3000
    ):

        self.min_answer_length = min_answer_length
        self.max_answer_length = max_answer_length

    def validate(
        self,
        answer,
        context
    ):

        result = {
            "valid": True,
            "issues": []
        }

        # Empty answer

        if not answer.strip():

            result["valid"] = False

            result["issues"].append(
                "Empty answer"
            )

            return result

        # Too short

        if len(answer) < self.min_answer_length:

            result["issues"].append(
                "Answer unusually short"
            )

        # Too long

        if len(answer) > self.max_answer_length:

            result["issues"].append(
                "Answer unusually long"
            )

        # Hallucination fallback

        if (
            "I don't know" in answer
            or "I do not know" in answer
            or "cannot determine" in answer.lower()
        ):

            result["issues"].append(
                "Model uncertain"
            )

        # Grounding check

        context_words = set(
            context.lower().split()
        )

        answer_words = set(
            answer.lower().split()
        )

        overlap = len(
            answer_words.intersection(
                context_words
            )
        )

        if overlap < 10:

            result["issues"].append(
                "Low context overlap"
            )

        return result
