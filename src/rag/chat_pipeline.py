"""
IndianMiningGPT
Phase 8.4

Memory Aware Chat Pipeline
"""

from src.retrieval.retrieve import retrieve
from src.reranking.rerank import Reranker

from src.rag.context_builder import (
    ContextBuilder
)

from src.rag.chat_prompt_builder import (
    ChatPromptBuilder
)

from src.rag.citation_builder import (
    CitationBuilder
)

from src.llm.answer_generator import (
    AnswerGenerator
)

from src.memory.conversation_memory import (
    ConversationMemory
)


class ChatPipeline:

    def __init__(self):

        print(
            "\nInitializing Chat Pipeline...\n"
        )

        self.memory = (
            ConversationMemory()
        )

        self.reranker = (
            Reranker()
        )

        self.context_builder = (
            ContextBuilder(
                max_chunks=5,
                max_chars=12000
            )
        )

        self.prompt_builder = (
            ChatPromptBuilder()
        )

        self.answer_generator = (
            AnswerGenerator()
        )

        self.citation_builder = (
            CitationBuilder()
        )

        print(
            "\nChat Pipeline Ready\n"
        )

    def ask(
        self,
        query
    ):

        retrieved_docs = retrieve(
            query,
            top_k=20
        )

        ranked_docs = (
            self.reranker.rerank(
                query,
                retrieved_docs,
                top_k=5
            )
        )

        context = (
            self.context_builder.build(
                query,
                ranked_docs
            )
        )

        memory_text = (
            self.memory.get_history_text()
        )

        prompt = (
            self.prompt_builder.build(
                query,
                memory_text,
                context
            )
        )

        answer = (
            self.answer_generator.answer(
                prompt
            )
        )

        citations = (
            self.citation_builder.build(
                ranked_docs
            )
        )

        self.memory.add_turn(
            query,
            answer
        )

        return (
            answer
            + "\n"
            + citations
        )
