from typing import Any, Dict, List, Optional

from .state import AgentState
from .memory import Memory
from .tools import ToolRegistry, ToolExecutor
from ..planning.planner import Planner
from ..runtime.runtime import RuntimeLoop


class BaseAgent:
    """
    Full agent architecture:
    - stateful execution
    - planning
    - tool execution
    - memory updates
    - runtime loop
    """

    def __init__(self, pipeline, tools=None, memory=None):
        self.pipeline = pipeline
        self.tools = tools or ToolRegistry()
        self.executor = ToolExecutor(self.tools)
        self.memory = memory or Memory()
        self.planner = Planner(pipeline)
        self.runtime = RuntimeLoop()

    def run(self, user_input: str) -> str:
        state = self.runtime.initialize(user_input)

        plan = self.planner.plan(state)
        state.plan = plan

        if "steps" in plan:
            return self._run_multi_step(state, plan["steps"])

        return self._run_single_step(state, plan)

    def _run_single_step(self, state: AgentState, plan: Dict[str, Any]) -> str:
        action = plan.get("action", "echo")
        tool_input = plan.get("input", state.user_input)

        result = self.executor.execute(action, tool_input)
        state = self.runtime.update(state, result)

        self.memory.add({"state": state, "result": result})
        return result

    def _run_multi_step(self, state: AgentState, steps: List[Dict[str, Any]]) -> str:
        last_result = ""

        for step in steps:
            action = step.get("action", "echo")
            tool_input = step.get("input", last_result or state.user_input)

            result = self.executor.execute(action, tool_input)
            last_result = result

            state = self.runtime.update(state, result)

        self.memory.add({"state": state, "final_result": last_result})
        return last_result

