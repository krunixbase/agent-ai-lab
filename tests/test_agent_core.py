import pytest
import asyncio

from agent_core.base_agent import BaseAgent
from pipelines.llm_pipeline import LLMPipeline


class DummyLLM(LLMPipeline):
    async def generate(self, prompt: str):
        return {"text": "hello", "raw": {}}


@pytest.mark.asyncio
async def test_agent_run():
    agent = BaseAgent(llm=DummyLLM())
    result = await agent.run("hi")
    assert "response" in result
