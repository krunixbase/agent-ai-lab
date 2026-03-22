class ReasoningEngine:
    """
    Responsible for:
    - building system prompts
    - injecting memory/context
    - future: chain-of-thought planning
    """

    def build_system_prompt(self, context: str = "") -> str:
        base = (
            "You are an AI agent. Use the provided context to answer the user.\n"
            "If context is empty, answer normally.\n\n"
        )

        if context:
            base += f"Context:\n{context}\n\n"

        return base
