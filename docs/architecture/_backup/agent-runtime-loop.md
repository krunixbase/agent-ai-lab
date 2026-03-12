# Agent Runtime Loop

## Overview

The agent runtime loop defines how the agent processes each user message from start to finish. It orchestrates memory retrieval, planning, tool execution, LLM interaction, and state updates. The loop ensures that every turn follows a predictable sequence while remaining flexible enough to support multi-step reasoning and long-term context.

The runtime loop is the core operational cycle of the agent.

---

## Runtime Loop Stages

### 1. Receive User Input
The loop begins when a new user message arrives.  
The agent:
- normalizes the input,
- updates the user input state,
- attaches metadata such as timestamps.

### 2. Retrieve Memory
The agent retrieves relevant context from:
- episodic memory,
- vector memory,
- summary memory.

This ensures continuity and grounding in previous interactions.

### 3. Planner Selection
Based on the message and context, the agent selects:
- **SingleStepPlanner** for simple tasks,
- **MultiStepPlanner** for complex or tool-driven tasks.

### 4. Planning Phase
The planner generates:
- a direct response,
- a multi-step plan,
- or a tool call.

For multi-step plans, the planner may iterate several times.

### 5. Action Execution
The agent executes the planner’s chosen action:
- LLM generation,
- tool execution,
- or continuation of a multi-step plan.

Tool results or LLM outputs may trigger additional planning cycles.

### 6. State Update
After executing an action, the agent updates:
- episodic memory,
- vector memory embeddings,
- summary memory (if thresholds are reached),
- planner state,
- tool execution state,
- LLM interaction state.

### 7. Produce Output
The agent constructs the final response for the user.  
This may include:
- generated text,
- tool-derived information,
- reasoning results.

The loop then waits for the next user message.

---

## Runtime Loop Diagram

```
┌──────────────────────────┐
│    Receive User Input     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Retrieve Memory       │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Planner Selection     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│      Planning Phase       │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│    Action Execution       │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│       State Update        │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│      Produce Output       │
└──────────────────────────┘
```

---

## Design Principles

### Deterministic Flow
Each turn follows the same high-level sequence, ensuring predictability.

### Planner-Centric Control
The planner drives decisions about tool usage, LLM calls, and multi-step reasoning.

### Memory-Aware Execution
Memory retrieval and updates occur at consistent points in the loop.

### Extensibility
New planners, tools, or memory backends can be added without modifying the loop.

### Transparency
The runtime loop exposes clear state transitions, aiding debugging and observability.

---

## Future Extensions

- parallel tool execution,
- adaptive planner selection based on context,
- runtime performance profiling,
- distributed runtime loops for multi-agent systems,
- interruptible or resumable planning cycles.


---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)

---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)
