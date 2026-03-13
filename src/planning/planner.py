class Planner:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def plan(self, state):
        """
        Delegates planning to the LLM pipeline.
        """
        return self.pipeline.plan(state.user_input)

