from typing import Dict, Any
from utils.validators import ensure_not_empty
from utils.timing import measure_time
from utils.json_safe import json_safe


class LLMPipeline:
    """
    Abstract interface for LLM providers.
    Concrete implementations must override `generate()`.
    """

    async def generate(self, prompt: str) -> Dict[str, Any]:
        raise NotImplementedError


class OpenAILLMPipeline(LLMPipeline):
    """
    Example implementation using OpenAI-compatible API.
    """

    def __init__(self, client, model: str):
        self.client = client
        self.model = model

    @measure_time
    async def generate(self, prompt: str) -> Dict[str, Any]:
        ensure_not_empty(prompt)

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )

        text = response.choices[0].message["content"]

        return {
            "text": text,
            "raw": json_safe(response),
        }
