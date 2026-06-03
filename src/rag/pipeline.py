"""
IndianMiningGPT
Phase 7.2
End-to-End RAG Pipeline
"""

from src.retrieval.retrieve import retrieve
from src.reranking.rerank import Reranker
from src.rag.context_builder import ContextBuilder
from src.rag.prompt_builder import PromptBuilder
from src.llm.answer_generator import AnswerGenerator


class IndianMiningGPT:

    def __init__(self):

        print("\nInitializing IndianMiningGPT...\n")

        self.reranker = Reranker()

        self.context_builder = ContextBuilder(
            max_chunks=5,
            max_chars=12000
        )

        self.prompt_builder = PromptBuilder()

        self.answer_generator = AnswerGenerator()

        print("\nIndianMiningGPT Ready\n")

    def ask(
        self,
        query,
        retrieve_k=20,
        rerank_k=5
    ):

        retrieved_docs = retrieve(
            query,
            top_k=retrieve_k
        )

        ranked_docs = self.reranker.rerank(
            query,
            retrieved_docs,
            top_k=rerank_k
        )

        context = self.context_builder.build(
            query,
            ranked_docs
        )

        prompt = self.prompt_builder.build(
            query,
            context
        )

        answer = self.answer_generator.answer(
            prompt
        )

        return {
            "query": query,
            "answer": answer,
            "sources": ranked_docs
        }
