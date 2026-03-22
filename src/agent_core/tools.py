from typing import Any, Dict, Callable

from utils.retry import retry
from utils.json_safe import json_safe
from utils.validators import ensure_not_empty


class ToolRegistry:
    """
    Registry for agent tools.
    Tools are simple callables that take input and return output.
    """

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    # -------------------------------------------------------------------------
    # REGISTRATION
    # -------------------------------------------------------------------------

    def register(self, name: str, func: Callable) -> None:
        ensure_not_empty(name, "tool name")
        self._tools[name] = func

    def list_tools(self):
        return list(self._tools.keys())

    # -------------------------------------------------------------------------
    # EXECUTION
    # -------------------------------------------------------------------------

    @retry((Exception,), retries=3, delay=0.2)
    def call(self, name: str, payload: Any) -> Any:
        """
        Execute a registered tool with retry and safe serialization.
        """
        ensure_not_empty(name, "tool name")

        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found")

        safe_payload = json_safe(payload)
        func = self._tools[name]

        return func(safe_payload)
