# Turn Execution Model

## Overview

The turn execution model describes how the agent processes a single user turn from input reception to final output. A “turn” is the atomic execution unit of the runtime: it begins when the user sends a message and ends when the agent returns a validated, safe, and coherent response. The model ensures deterministic execution, safe tool usage, correct planner coordination, and consistent memory integration.

Turn execution is structured as a pipeline of stages, each responsible for a specific part of the reasoning and execution flow.

---

## Turn Stages

### Input Reception
The agent receives:
- the user message,
- session metadata,
- timestamps,
- conversation identifiers.

The message is normalized and prepared for processing.

### Pre‑Processing
The agent performs:
- session boundary detection,
- initial safety filtering,
- intent classification,
- extraction of relevant metadata.

This stage ensures the turn begins in a valid and safe state.

### Context Construction
The agent assembles all information required for reasoning:
- memory retrieval (summary, vector, episodic),
- planner state,
- system instructions,
- safety constraints.

Context is prioritized and compressed to fit within the model’s context window.

### Planner Invocation
The planner determines:
- whether the turn requires a single-step or multi-step plan,
- which capabilities and tools are needed,
- the sequence of actions to execute,
- expected output schemas.

The planner produces a structured plan that the runtime will execute step by step.

### Step Execution Loop
The runtime executes each step in order. A step may involve:
- an LLM call,
- a tool invocation,
- a data transformation,
- a memory update.

For each step, the runtime:
- validates inputs,
- executes the action,
- validates outputs,
- updates the reasoning trace,
- updates planner state.

If a step fails, the runtime applies the error handling model.

### Error Handling
Errors are classified as:
- recoverable,
- non‑recoverable,
- critical.

Depending on severity, the runtime may:
- retry the step,
- regenerate LLM output,
- adjust tool arguments,
- reset the plan,
- produce a fallback response,
- isolate the session.

### Output Assembly
After all steps complete, the runtime:
- validates the final output,
- applies safety filtering,
- updates memory with new information,
- constructs the final user-facing message.

The turn ends when the output is returned to the user.

---

## Turn Execution Diagram

```
┌──────────────────────────┐
│      Input Reception      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│       Pre‑Processing      │
│ (safety, intent, session) │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│    Context Construction   │
│ (memory, planner state)   │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Planner Invocation    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Step Execution Loop     │
│ (LLM, tools, transforms)  │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│       Error Handling      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│      Output Assembly      │
└──────────────────────────┘
```

---

## Turn State Model

During a turn, the agent maintains several layers of state:

### Turn State
- current plan,
- current step index,
- reasoning trace,
- retrieved memory.

### Planner State
- active goals,
- pending actions,
- tool requirements,
- expected schemas.

### Safety State
- detected safety events,
- risk levels,
- active restrictions.

### Session State
- session summary,
- conversation history,
- user metadata.

---

## Step Execution Details

Each step follows a strict lifecycle:

1. **Input Validation**  
   Ensures arguments, schemas, and safety constraints are correct.

2. **Execution**  
   Runs the LLM call, tool call, or transformation.

3. **Output Validation**  
   Ensures the result is:
   - structurally valid,
   - safe,
   - consistent with planner expectations.

4. **State Update**  
   Updates:
   - planner state,
   - reasoning trace,
   - memory (if applicable).

5. **Transition**  
   Moves to the next step or finalization.

---

## Error Handling Strategies

### Recoverable Errors
- retrying tool calls,
- regenerating LLM output,
- adjusting arguments,
- re-running a step.

### Non‑Recoverable Errors
- resetting the plan,
- generating a fallback response,
- isolating unsafe outputs.

### Critical Errors
- terminating the turn,
- isolating the session,
- returning a safe error message.

---

## Performance Considerations

Turn execution is optimized for:

### Latency
- parallel memory retrieval,
- efficient step ordering.

### Token Usage
- context compression,
- removal of redundant information.

### Tool Efficiency
- avoiding repeated calls,
- caching stable results.

### Planner Efficiency
- minimizing unnecessary steps,
- adaptive plan shortening.

---

## Design Principles

### Deterministic Execution
Identical inputs produce identical turn behavior.

### Safety Enforcement
Every stage includes safety validation.

### Modularity
Each stage is independent and replaceable.

### Observability
The turn produces a complete reasoning trace.

### Isolation
Errors do not propagate across turns or sessions.

---

## Future Extensions

- predictive step scheduling,
- dynamic plan optimization,
- distributed turn execution,
- turn-level performance analytics,
- adaptive context shaping.

