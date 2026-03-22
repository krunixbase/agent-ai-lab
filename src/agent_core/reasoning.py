from utils.validators import ensure_not_empty
from utils.formatting import truncate, pretty_json


class ReasoningEngine:
    """
    Builds system prompts and reasoning scaffolding for the agent.
    """

    def build_system_prompt(self, context: str = "") -> str:
        """
        Construct the system prompt used by the LLM.
        """
        if context:
            context = truncate(context, 800)

        system_prompt = (
            "You are an intelligent AI assistant.\n"
            "Use the provided context when relevant.\n\n"
            f"Context:\n{context}\n"
        )

        return system_prompt

    def debug_state(self, state: dict) -> str:
        """
        Return a readable debug dump of reasoning state.
        """
        ensure_not_empty(str(state), "state")
        return pretty_json(state)
