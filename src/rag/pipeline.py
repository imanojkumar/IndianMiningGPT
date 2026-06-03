"""
IndianMiningGPT
Phase 7.4
End-to-End RAG Pipeline
with Source Citations and Validation
"""

from src.retrieval.retrieve import retrieve
from src.reranking.rerank import Reranker
from src.rag.context_builder import ContextBuilder
from src.rag.prompt_builder import PromptBuilder
from src.rag.citation_builder import CitationBuilder
from src.rag.answer_validator import AnswerValidator
from src.llm.answer_generator import AnswerGenerator


class IndianMiningGPT:

    def __init__(self):

        print(
            "\nInitializing IndianMiningGPT...\n"
        )

        self.reranker = Reranker()

        self.validator = AnswerValidator()

        self.context_builder = ContextBuilder(
            max_chunks=5,
            max_chars=12000
        )

        self.prompt_builder = PromptBuilder()

        self.citation_builder = CitationBuilder()

        self.answer_generator = AnswerGenerator()

        print(
            "\nIndianMiningGPT Ready\n"
        )

    def ask(
        self,
        query,
        retrieve_k=20,
        rerank_k=5
    ):

        # --------------------------------------------------
        # Retrieve
        # --------------------------------------------------

        retrieved_docs = retrieve(
            query,
            top_k=retrieve_k
        )

        # --------------------------------------------------
        # Rerank
        # --------------------------------------------------

        ranked_docs = self.reranker.rerank(
            query,
            retrieved_docs,
            top_k=rerank_k
        )

        # --------------------------------------------------
        # Build Context
        # --------------------------------------------------

        context = self.context_builder.build(
            query,
            ranked_docs
        )

        # --------------------------------------------------
        # Build Prompt
        # --------------------------------------------------

        prompt = self.prompt_builder.build(
            query,
            context
        )

        # --------------------------------------------------
        # Generate Answer
        # --------------------------------------------------

        answer = self.answer_generator.answer(
            prompt
        )

        # --------------------------------------------------
        # Validate Answer
        # --------------------------------------------------

        validation = self.validator.validate(
            answer,
            context
        )

        # --------------------------------------------------
        # Build Citations
        # --------------------------------------------------

        citations = self.citation_builder.build(
            ranked_docs
        )

        # --------------------------------------------------
        # Validation Summary
        # --------------------------------------------------

        validation_text = "\n\nVALIDATION\n"

        if validation["issues"]:

            validation_text += "\n".join(
                validation["issues"]
            )

        else:

            validation_text += (
                "No issues detected"
            )

        # --------------------------------------------------
        # Final Answer
        # --------------------------------------------------

        final_answer = (
            answer
            + validation_text
            + "\n"
            + citations
        )

        return {
            "query": query,
            "answer": final_answer,
            "sources": ranked_docs,
            "validation": validation
        }
