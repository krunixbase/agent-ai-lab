from typing import Dict, Any
from utils.validators import ensure_not_empty
from utils.json_safe import json_safe
from utils.retry import retry

from .base_pipeline import BasePipeline


class LLMPipeline(BasePipeline):

    def __init__(self, client):
        self.client = client

    @retry((Exception,), retries=3)
    async def generate(self, prompt: str) -> Dict[str, Any]:
        self.validate(prompt, "prompt")

        raw = await self.client.generate(prompt=prompt)

        return {
            "text": raw.get("text", ""),
            "raw": json_safe(raw),
        }

    async def run(self, prompt: str):
        return await self.generate(prompt)
