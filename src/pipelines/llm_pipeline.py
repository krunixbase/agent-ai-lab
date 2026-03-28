from typing import Dict, Any
from utils.json_safe import json_safe
from utils.retry import retry
from .base_pipeline import BasePipeline
from .ollama_client import OllamaClient
from typing import AsyncGenerator
from .ollama_client import OllamaClient

class LLMPipeline:
    def __init__(self, model: str = "llama3.2"):
        self.client = OllamaClient(model=model)
        self.model = model

    async def generate(self, prompt: str):
        return await self.client.generate(prompt)


    async def stream(self, prompt: str) -> AsyncGenerator[str, None]:
        async for chunk in self.client.stream(prompt):
            yield chunk
            
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
    
    class LLMPipeline:
    def __init__(self, model: str = "llama3.2"):
        self.client = OllamaClient(model=model)
        self.model = model

    async def generate(self, prompt: str):
        return await self.client.generate(prompt)

    async def stream(self, prompt: str) -> AsyncGenerator[str, None]:
        async for chunk in self.client.stream(prompt):
            yield chunk