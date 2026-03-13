from typing import Any, Dict, List, Optional

from .memory import Memory
from .tools import ToolRegistry


class BaseAgent:
    """
    Core agent orchestrating:
    - planning (via pipeline)
    - tool execution (via ToolRegistry)
    - memory updates
    Supports both single-step and multi-step plans.
    """

    def __init__(self, pipeline, tools: Optional[ToolRegistry] = None, memory: Optional[Memory] = None):
        self.pipeline = pipeline
        self.tools = tools or ToolRegistry()
        self.memory = memory or Memory()

    def _execute_action(self, action: str, tool_input: str) -> str:
        """
        Executes a single tool action using the ToolRegistry.
        """
        tool = self.tools.get(action)
        if tool is None:
            return f"Error: unknown tool '{action}'."

        try:
            return tool(tool_input)
        except Exception as e:
            return f"Error while executing tool '{action}': {e}"

    def _run_single_step(self, plan: Dict[str, Any], user_input: str) -> str:
        """
        Backwards-compatible single-step execution:
        { "action": "...", "input": "..." }
        """
        action = plan.get("action", "echo")
        tool_input = plan.get("input", user_input)

        result = self._execute_action(action, tool_input)

        self.memory.add(
            {
                "user": user_input,
                "plan": plan,
                "result": result,
            }
        )

        return result

    def _run_multi_step(self, steps: List[Dict[str, Any]], user_input: str) -> str:
        """
        Executes a multi-step plan:
        { "steps": [ { "action": "...", "input": "..." }, ... ] }
        """
        execution_trace: List[Dict[str, Any]] = []
        last_result: str = ""

        for idx, step in enumerate(steps):
            action = step.get("action", "echo")
            tool_input = step.get("input", "")

            # Optionally allow referring to previous result
            if tool_input == "" and last_result:
                tool_input = last_result

            result = self._execute_action(action, tool_input)
            last_result = result

            execution_trace.append(
                {
                    "step": idx,
                    "action": action,
                    "input": tool_input,
                    "result": result,
                }
            )

        self.memory.add(
            {
                "user": user_input,
                "plan": {"steps": steps},
                "trace": execution_trace,
                "final_result": last_result,
            }
        )

        return last_result

    def run(self, user_input: str) -> str:
        """
        Main entrypoint for the agent.

        1. Ask the pipeline for a plan.
        2. If the plan contains `steps`, run multi-step execution.
        3. Otherwise, fall back to single-step execution.
        """
        plan = self.pipeline.plan(user_input)

        # Multi-step plan: { "steps": [ ... ] }
        if isinstance(plan, dict) and "steps" in plan and isinstance(plan["steps"], list):
            return self._run_multi_step(plan["steps"], user_input)

        # Single-step plan: { "action": "...", "input": "..." }
        return self._run_single_step(plan, user_input)

