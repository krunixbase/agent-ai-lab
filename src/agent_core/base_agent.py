class BaseAgent:
    def __init__(self, llm, memory, tools):
        self.llm = llm
        self.memory = memory
        self.tools = tools

    def run(self, prompt: str):
        self.memory.store("user", prompt)

        plan = self.llm.plan(prompt)
        self.memory.store("plan", plan)

        result = self.tools.execute(plan)
        self.memory.store("result", result)

        return result
