class ToolRegistry:
    """
    Registry for all tools available to the agent.
    Tools are simple callables: tool(input: str) -> str
    """

    def __init__(self):
        self.tools = {}

    def register(self, name: str, tool):
        self.tools[name] = tool

    def get(self, name: str):
        return self.tools.get(name)


class ToolExecutor:
    """
    Executes tools registered in the ToolRegistry.
    Handles missing tools and exceptions gracefully.
    """

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, action: str, tool_input: str) -> str:
        tool = self.registry.get(action)
        if tool is None:
            return f"Error: unknown tool '{action}'."

        try:
            return tool(tool_input)
        except Exception as e:
            return f"Error while executing tool '{action}': {e}"
