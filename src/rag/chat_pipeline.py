"""
IndianMiningGPT
Phase 9.2

Conversational Chat Pipeline
with Query Rewriting
"""

from src.rag.query_rewriter import (
    QueryRewriter
)

from src.retrieval.retrieve import retrieve

from src.reranking.rerank import (
    Reranker
)

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

        self.rewriter = (
            QueryRewriter()
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

        # ----------------------------------
        # Conversation Memory
        # ----------------------------------

        memory_text = (
            self.memory.get_history_text()
        )

        # ----------------------------------
        # Query Rewriting
        # ----------------------------------

        rewritten_query = (
            self.rewriter.rewrite(
                query,
                memory_text
            )
        )

        # ----------------------------------
        # Retrieval
        # ----------------------------------

        retrieved_docs = retrieve(
            rewritten_query,
            top_k=20
        )

        # ----------------------------------
        # Reranking
        # ----------------------------------

        ranked_docs = (
            self.reranker.rerank(
                rewritten_query,
                retrieved_docs,
                top_k=5
            )
        )

        # ----------------------------------
        # Context Building
        # ----------------------------------

        context = (
            self.context_builder.build(
                rewritten_query,
                ranked_docs
            )
        )

        # ----------------------------------
        # Prompt Building
        # ----------------------------------

        prompt = (
            self.prompt_builder.build(
                query,
                memory_text,
                context
            )
        )

        # ----------------------------------
        # Answer Generation
        # ----------------------------------

        answer = (
            self.answer_generator.answer(
                prompt
            )
        )

        # ----------------------------------
        # Source Citations
        # ----------------------------------

        citations = (
            self.citation_builder.build(
                ranked_docs
            )
        )

        # ----------------------------------
        # Save Conversation Turn
        # ----------------------------------

        self.memory.add_turn(
            query,
            answer
        )

        # ----------------------------------
        # Final Response
        # ----------------------------------

        return (
            answer
            + "\n"
            + citations
        )
