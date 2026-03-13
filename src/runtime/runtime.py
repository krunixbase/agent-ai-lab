class RuntimeLoop:
    def initialize(self, user_input):
        return AgentState(user_input=user_input)

    def update(self, state, result):
        state.last_result = result
        state.steps.append({"result": result})

        if len(state.steps) > 10:
            state.finished = True

        return state
