from pathlib import Path
import sys

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parents[1]
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from src.memory.conversation_memory import (
    ConversationMemory
)

memory = ConversationMemory()

memory.add_turn(
    "What is star rating of mines?",
    "A sustainability rating system."
)

memory.add_turn(
    "Who issues it?",
    "IBM on behalf of Ministry of Mines."
)

print(
    memory.get_history_text()
)

print(
    "\nTurns:",
    memory.size()
)
