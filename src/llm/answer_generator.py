"""
IndianMiningGPT
Answer Generator
"""

from src.llm.ollama_client import (
    OllamaClient
)


class AnswerGenerator:

    def __init__(self):

        self.client = OllamaClient()

    def answer(
        self,
        prompt
    ):

        return self.client.generate(
            prompt=prompt,
            temperature=0.1
        )
