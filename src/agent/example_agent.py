from .base_agent import BaseAgent
from ..pipelines.simple_pipeline import SimplePipeline
from ..tools.tools import ToolRegistry
from ..tools.tools_builtin import EchoTool, UppercaseTool
from ..memory.memory import Memory


def build_example_agent():
    tools = ToolRegistry()
    tools.register("echo", EchoTool())
    tools.register("upper", UppercaseTool())

    pipeline = SimplePipeline()
    memory = Memory()

    return BaseAgent(
        pipeline=pipeline,
        tools=tools,
        memory=memory
    )
