from typing import List, Dict, Any


class Memory:
    """
    Simple in-memory storage for agent interactions.
    Future extensions:
    - episodic memory
    - vector memory
    - long-term memory persistence
    """

    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def add_interaction(self, user_input: str, agent_output: str):
        self.history.append(
            {
                "user": user_input,
                "agent": agent_output,
            }
        )

    def get_history(self) -> List[Dict[str, Any]]:
        return self.history
