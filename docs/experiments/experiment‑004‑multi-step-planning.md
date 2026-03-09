# Experiment 004 — Multi-Step Planning

## Objective
Test whether the agent can generate and execute multi-step plans instead of single-step tool calls. This is a key capability for more advanced reasoning and autonomous workflows.

---

# Scope
This experiment evaluates:
- LLM-generated multi-step plans
- sequential tool execution
- intermediate memory updates
- error handling between steps
- final result synthesis

---

# Setup

1. Extend `OpenAIPipeline` to support multi-step outputs:

   ```
   json
   {
     "steps": [
       {"action": "search", "input": "weather in Tokyo"},
       {"action": "calculator", "input": "convert temperature to Fahrenheit"},
       {"action": "echo", "input": "final summary"}
     ]
   }
   ```
2. Modify BaseAgent to:

- iterate through steps

- execute each tool

- store intermediate results in memory

- pass results to the next step if needed

3. Add a fallback for invalid or incomplete plans.

---

# Test Cases

1. Multi-step transformation

Input:

```
take the number 42, multiply it by 3, then tell me if the result is even
```

Expected Plan:

```
steps:
  - action: calculator, input: "42 * 3"
  - action: echo, input: "126 is even"
```

2. Multi-step reasoning with memory

Input:

```
first calculate 12 * 7, then remind me what you got
```

Expected Behavior:

- Step 1: calculator → 84

- Step 2: echo → "The result was 84"

3. Error handling

If a step fails:

- agent logs the error

- continues or stops depending on configuration

- returns a clear final message

---

# Expected Memory Trace

```
{
  "steps": [
    {"action": "calculator", "result": "84"},
    {"action": "echo", "result": "The result was 84"}
  ]
}
```

# Success Criteria

- agent executes multiple steps in order

- intermediate results are correctly passed forward

- memory captures each step

- final output is coherent and correct

- invalid plans fall back gracefully

---

# Notes

This experiment lays the foundation for:

- autonomous task execution

- agent workflows

- multi-agent collaboration

- long-term planning

---

