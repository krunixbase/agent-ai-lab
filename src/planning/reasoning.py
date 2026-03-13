class ReasoningEngine:
    def reflect(self, state, result):
        """
        Optional reflection step for self-improvement.
        """
        return {
            "reflection": f"Agent observed result: {result}"
        }
