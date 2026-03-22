from typing import Dict, Any
from utils.retry import retry
from utils.json_safe import json_safe
from utils.validators import ensure_not_empty

from .base_pipeline import BasePipeline


class OpenAIPipeline(BasePipeline):

    def __init__(self, client):
        self.client = client

    @retry((Exception,), retries=3)
    async def run(self, prompt: str) -> Dict[str, Any]:
        self.validate(prompt, "prompt")

        raw = await self.client.chat(prompt=prompt)

        return {
            "text": raw["choices"][0]["message"]["content"],
            "raw": json_safe(raw),
        }
