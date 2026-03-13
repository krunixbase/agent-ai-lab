from src.agent.base_agent import BaseAgent
from src.pipelines.openai_pipeline import OpenAIPipeline

def test_agent_runs():
    agent = BaseAgent(pipeline=OpenAIPipeline())
    result = agent.run("hello")
    assert isinstance(result, str)
