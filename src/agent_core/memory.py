from typing import List, Dict

from utils.hashing import sha256
from utils.validators import ensure_not_empty
from utils.formatting import truncate, pretty_json


class Memory:
    """
    Simple in‑memory storage for agent interactions.
    Stores user prompts and agent responses, hashed for consistency.
    """

    def __init__(self):
        # Internal memory store: { hash: {prompt, response} }
        self._store: Dict[str, Dict[str, str]] = {}

    # -------------------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------------------

    def add_interaction(self, prompt: str, response: str) -> None:
        """
        Store a prompt/response pair in memory.
        """
        ensure_not_empty(prompt, "prompt")
        ensure_not_empty(response, "response")

        key = sha256(prompt)

        self._store[key] = {
            "prompt": prompt,
            "response": response,
        }

    def get_all(self) -> List[Dict[str, str]]:
        """
        Return all stored interactions as a list.
        """
        return list(self._store.values())

    def get_summary(self, max_len: int = 500) -> str:
        """
        Return a readable summary of memory contents.
        Useful for debugging or feeding into reasoning engines.
        """
        return truncate(
            pretty_json(self._store),
            max_len=max_len
        )

    def clear(self) -> None:
        """
        Remove all stored interactions.
        """
        self._store.clear()

