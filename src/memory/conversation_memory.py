"""
IndianMiningGPT
Phase 8.2

Conversation Memory
"""


class ConversationMemory:

    def __init__(
        self,
        max_turns=10
    ):

        self.max_turns = max_turns

        self.history = []

    def add_turn(
        self,
        question,
        answer
    ):

        self.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        if len(
            self.history
        ) > self.max_turns:

            self.history = (
                self.history[
                    -self.max_turns:
                ]
            )

    def get_history(self):

        return self.history

    def get_history_text(self):

        if not self.history:
            return ""

        sections = []

        for i, turn in enumerate(
            self.history,
            start=1
        ):

            section = f"""
Question {i}:
{turn["question"]}

Answer {i}:
{turn["answer"]}
"""

            sections.append(
                section.strip()
            )

        return "\n\n".join(
            sections
        )

    def clear(self):

        self.history = []

    def size(self):

        return len(
            self.history
        )
