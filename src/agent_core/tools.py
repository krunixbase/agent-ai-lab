from typing import Callable, Dict, Any


class ToolRegistry:
    """
    Registry for agent tools.
    Tools are simple Python callables with a name and description.
    """

    def __init__(self):
        self.tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        self.tools[name] = func

    def list_tools(self):
        return list(self.tools.keys())

    async def execute(self, name: str, **kwargs) -> Any:
        if name not in self.tools:
            raise ValueError(f"Tool not found: {name}")

        tool = self.tools[name]
        return tool(**kwargs)
