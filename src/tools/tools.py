class ToolRegistry:
    def __init__(self):
        self.tools = {
            "echo": self.echo
        }

    def execute(self, plan: dict):
        tool = plan.get("tool")
        input_data = plan.get("input")

        if tool in self.tools:
            return self.tools[tool](input_data)

        return "Unknown tool"

    def echo(self, text: str):
        return f"[echo] {text}"
