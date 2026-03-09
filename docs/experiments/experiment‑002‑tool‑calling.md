# Experiment 002 — Tool Calling

## Objective
Validate that the agent can correctly select and execute built‑in tools using the new planning pipeline and ToolRegistry. This experiment focuses on verifying the end‑to‑end flow from user input → LLM planning → tool execution → memory update.

---

## Scope
This experiment covers:
- OpenAIPipeline generating structured `{action, input}` plans
- ToolRegistry resolving and executing the selected tool
- Built‑in tools (echo, calculator, datetime)
- BaseAgent orchestrating the full loop
- Memory storing the interaction steps

---

## Setup
1. Ensure the following components are available:
   - `OpenAIPipeline` in `src/pipelines/openai_pipeline.py`
   - Built‑in tools in `src/agent_core/tools_builtin.py`
   - Registered tools in `ToolRegistry`
   - Valid `OPENAI_API_KEY` in `.env`

Run the agent through the FastAPI server or directly via Python.

---

## Test Cases

```
repeat this text
```

Expected Plan

```
json
{"action": "echo", "input": "repeat this text"}
```

Expected Output

```
repeat this text
```

---

## 2. Calculator Tool

Input:

```
what is 12 * 7 + 3?
```

Expected Plan:

```
{"action": "calculator", "input": "12 * 7 + 3"}
```

Expected Output:

```
87
```

---

## 3. Datetime Tool

Input:

```
what time is it?
```

Expected Plan:

```
{"action": "datetime", "input": ""}
```

Expected Output:  
ISO timestamp, e.g.:

```
2026-03-09T18:22:00.123456
```

---

# Expected Memory Trace

## After each run, memory should contain:

- user input

- generated plan

- executed tool name

- tool output

Example entry:

```
{
  "user": "what is 12 * 7 + 3?",
  "plan": {"action": "calculator", "input": "12 * 7 + 3"},
  "result": "87"
}
```

---

# Success Criteria

## The experiment is successful if:

- The LLM consistently produces valid {action, input} plans.

- ToolRegistry resolves and executes the correct tool.

- BaseAgent returns the tool output to the user.

- Memory stores all steps in the correct order.

- No fallback to echo occurs unless intended.

---

# Notes

This experiment establishes the foundation for more advanced tool‑augmented reasoning, including:

- multi‑step planning

- tool chaining

- external API tools

- error‑aware planning

---


### 1. Echo Tool
**Input:**  
