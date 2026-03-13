class SimplePipeline:
    """
    Minimalny pipeline LLM, który udaje planowanie.
    Możesz go łatwo podmienić na OpenAI, Ollama, Anthropic itd.
    """

    def plan(self, user_input: str):
        if "upper" in user_input.lower():
            return {"action": "upper", "input": user_input}

        if "steps" in user_input.lower():
            return {
                "steps": [
                    {"action": "echo", "input": user_input},
                    {"action": "upper", "input": ""}
                ]
            }

        return {"action": "echo", "input": user_input}
