class LLMPipeline:
    def plan(self, prompt: str):
        return {
            "tool": "echo",
            "input": prompt
        }
