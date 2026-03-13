class Memory:
    """
    Minimal memory module for the agent.
    Stores interaction history and allows retrieving recent entries.
    Designed to be simple, predictable, and fully compatible with BaseAgent.
    """

    def __init__(self):
        # List of memory entries (dicts)
        self.entries = []

    def add(self, item):
        """
        Adds a new memory entry.
        Each entry can contain:
        - user input
        - plan
        - tool execution trace
        - final result
        - agent state snapshot
        """
        self.entries.append(item)

    def get_recent(self, n=5):
        """
        Returns the last N memory entries.
        Useful for providing context to the LLM pipeline.
        """
        return self.entries[-n:]

    def clear(self):
        """
        Clears all stored memory.
        Useful for resetting the agent between sessions.
        """
        self.entries = []
