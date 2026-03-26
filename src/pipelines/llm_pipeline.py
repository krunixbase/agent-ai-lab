from typing import Dict, Any
from utils.json_safe import json_safe
from utils.retry import retry
from .base_pipeline import BasePipeline
from .ollama_client import OllamaClient


class LLMPipeline(BasePipeline):

    def __init__(self, model: str = "llama3.2"):
        self.client = OllamaClient(model=model)
        self.model = model

    @retry((Exception,), retries=3)
    async def generate(self, prompt: str) -> Dict[str, Any]:
        raw = await self.client.generate(prompt)
        return {
            "text": raw["text"],
            "raw": json_safe(raw),
        }

    async def run(self, prompt: str):
        return await self.generate(prompt)
