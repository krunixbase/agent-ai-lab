import os
from typing import Optional, Dict, Any

import httpx


class LLMPipeline:
    """
    Unified interface for interacting with different LLM providers.
    Supports:
    - OpenAI
    - Anthropic
    - Local models (Ollama, LM Studio, vLLM)
    """

    def __init__(
        self,
        provider: str = "openai",
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_tokens: int = 512,
        system_prompt: Optional[str] = None,
    ):
        self.provider = provider.lower()
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt

        self.api_key = os.getenv("OPENAI_API_KEY") if provider == "openai" else None
        self.anthropic_key = os.getenv("ANTHROPIC_API_KEY") if provider == "anthropic" else None

    # -------------------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------------------

    async def generate(self, prompt: str) -> Dict[str, Any]:
        """
        Main entry point for generating text from an LLM.
        """

        if self.provider == "openai":
            return await self._generate_openai(prompt)

        if self.provider == "anthropic":
            return await self._generate_anthropic(prompt)

        if self.provider in ["ollama", "local"]:
            return await self._generate_local(prompt)

        raise ValueError(f"Unsupported provider: {self.provider}")

    # -------------------------------------------------------------------------
    # PROVIDER IMPLEMENTATIONS
    # -------------------------------------------------------------------------

    async def _generate_openai(self, prompt: str) -> Dict[str, Any]:
        """
        OpenAI Chat Completions API.
        """

        if not self.api_key:
            raise RuntimeError("Missing OPENAI_API_KEY")

        url = "https://api.openai.com/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})

        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

        return {
            "provider": "openai",
            "model": self.model,
            "text": data["choices"][0]["message"]["content"],
            "raw": data,
        }

    async def _generate_anthropic(self, prompt: str) -> Dict[str, Any]:
        """
        Anthropic Claude API.
        """

        if not self.anthropic_key:
            raise RuntimeError("Missing ANTHROPIC_API_KEY")

        url = "https://api.anthropic.com/v1/messages"

        headers = {
            "x-api-key": self.anthropic_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "messages": [
                {"role": "user", "content": prompt}
            ],
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

        return {
            "provider": "anthropic",
            "model": self.model,
            "text": data["content"][0]["text"],
            "raw": data,
        }

    async def _generate_local(self, prompt: str) -> Dict[str, Any]:
        """
        Local model (Ollama / LM Studio / vLLM).
        Assumes a local endpoint at http://localhost:11434/api/generate
        """

        url = "http://localhost:11434/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()

        return {
            "provider": "local",
            "model": self.model,
            "text": data.get("response", ""),
            "raw": data,
        }
