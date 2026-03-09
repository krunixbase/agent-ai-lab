from src.agent_core.base_agent import BaseAgent
from src.agent_core.memory import Memory
from src.agent_core.tools import ToolRegistry
from src.pipelines.llm_pipeline import LLMPipeline

def test_agent_echo():
    llm = LLMPipeline()
    memory = Memory()
    tools = ToolRegistry()

    agent = BaseAgent(llm=llm, memory=memory, tools=tools)
    result = agent.run("hello")

    assert "hello" in result
