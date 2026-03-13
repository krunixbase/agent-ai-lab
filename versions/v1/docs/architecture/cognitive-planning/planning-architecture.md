
# Planning Architecture Overview

The planning subsystem is responsible for transforming user input and retrieved memory into actionable steps the agent can execute.
It acts as the reasoning core of the system, deciding how the agent should respond, which tools to use, and whether multi-step reasoning is required.

The architecture is designed to support both simple, direct responses and complex, multi-step workflows involving external tools, iterative reasoning, and memory updates.

---

# Planner Types and Responsibilities

SingleStepPlanner
The SingleStepPlanner handles straightforward interactions where the agent can respond immediately without executing a sequence of actions.

## Key characteristics:

- minimal reasoning overhead,

- no iterative loops,

- no intermediate tool calls unless explicitly required,

- optimized for speed and low complexity.

## Typical use cases:

- conversational responses,

- simple factual queries,

- tasks that do not require external data or multi-step logic.

---

# MultiStepPlanner

The MultiStepPlanner supports advanced reasoning workflows where the agent must break down a task into multiple steps, call tools, evaluate
intermediate results, and continue planning.

## Key characteristics:

- iterative planning loop,

- dynamic decision-making based on intermediate outputs,

- tool-aware reasoning,

- ability to revise or extend the plan mid-execution.

## Typical use cases:

- tasks requiring external API calls,

- multi-tool workflows,

- reasoning chains with dependencies between steps,

- long-horizon tasks that require memory updates during execution.

---

# Planning Flow

1. Input Interpretation

The planner receives:

- the user message,

- retrieved memory (episodic, vector, summary),

- optional system instructions.

It constructs an internal representation of the task and identifies whether the problem requires single-step or multi-step reasoning.

2. Plan Generation

The planner generates a plan that may include:

- direct LLM responses,

- tool calls,

- conditional branches,

- iterative loops.

Plans may be:

- static (generated once and executed),

- dynamic (updated after each step based on results).

3. Action Execution

Each step in the plan is executed in sequence. Steps may involve:

- generating text,

- calling external tools,

- updating internal state,

- evaluating tool outputs.

The MultiStepPlanner may re-enter the planning phase after each step to refine the next action.

4. Termination and Output

The planner determines when the task is complete. Termination conditions include:

- plan fully executed,

- user goal achieved,

- no further actions required,

- error or fallback conditions.

The final output is returned to the agent loop for memory updates and user delivery.

---

# Planner Architecture Diagram

```
┌──────────────────────────┐
│      User Message        │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   Memory + Context Load   │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     Planner Selection     │
│ SingleStep / MultiStep    │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│      Plan Generation      │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     Step Execution        │
│ (LLM / Tools / Logic)     │
└─────────────┬────────────┘
              │
              ▼
      ┌───────────────┐
      │ More Steps?    │─── Yes ──► back to Plan Generation
      └───────┬───────┘
              │ No
              ▼
┌──────────────────────────┐
│       Final Output        │
└──────────────────────────┘
```

---

# Design Principles

## Modularity

Planners are interchangeable. New planners (e.g., hierarchical planners, reactive planners) can be added without modifying the agent loop.

## Tool Awareness

Planners treat tools as first-class actions. They can:

- decide when to call a tool,

- interpret tool outputs,

- chain multiple tools together.

## Iterative Reasoning

The MultiStepPlanner supports:

- reflection loops,

- conditional branching,

- dynamic replanning.

## Memory Integration

Planners use memory both during:

- retrieval (to inform decisions),

- execution (to store intermediate results or new knowledge).

---

# Future Extensions

- hierarchical planning (subgoals, decomposition),

- tool selection heuristics based on memory and context,

- reinforcement-learning-inspired planning loops,

- multi-agent collaborative planning,

- plan caching and reuse across sessions.

---

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
