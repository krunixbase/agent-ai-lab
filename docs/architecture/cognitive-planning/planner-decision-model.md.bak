# Planner Decision Model

## Overview

The planner decision model defines how the agent determines the appropriate reasoning strategy for each user message. It governs when to use single‑step reasoning, when to initiate multi‑step planning, when to call tools, and when to rely solely on the LLM. The model ensures that decisions are consistent, explainable, and optimized for accuracy, safety, and efficiency.

The planner decision model is central to the agent’s intelligence, as it controls how reasoning unfolds across turns.

---

## Decision Inputs

The planner evaluates several inputs before choosing a strategy:

### User Intent
The planner analyzes:
- complexity of the request,
- explicit instructions,
- need for multi-step reasoning,
- need for external information.

### Memory Context
The planner considers:
- retrieved episodic memory,
- vector memory matches,
- summary memory context.

### Tool Availability
The planner checks:
- whether tools are enabled,
- which tools match the user’s intent,
- tool safety constraints.

### Safety Constraints
The planner ensures:
- no unsafe tool usage,
- no policy violations,
- no unsafe reasoning loops.

### System Configuration
The planner respects:
- default planner type,
- maximum reasoning steps,
- tool usage limits.

---

## Planner Types

### SingleStepPlanner
Used for:
- simple questions,
- direct responses,
- short reasoning tasks,
- cases where no tools are needed.

### MultiStepPlanner
Used for:
- complex reasoning,
- tool-driven workflows,
- multi-stage tasks,
- iterative refinement.

The planner may switch dynamically based on context.

---

## Decision Flow

### 1. Analyze User Input
The planner inspects the message for:
- complexity,
- ambiguity,
- required actions,
- tool-related keywords.

### 2. Evaluate Memory
The planner checks whether memory provides:
- relevant facts,
- missing context,
- constraints that affect planning.

### 3. Determine Planner Type
The planner selects:
- **single-step** if the task is simple,
- **multi-step** if the task requires tools or multi-stage reasoning.

### 4. Generate Plan
Depending on the planner type:
- single-step generates a direct response,
- multi-step generates a structured plan with actions.

### 5. Execute or Iterate
The planner:
- executes the next step,
- calls tools if needed,
- refines the plan based on results.

### 6. Finalize Output
The planner produces the final response and updates state.

---

## Decision Model Diagram

```
┌──────────────────────────┐
│    Analyze User Input     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Evaluate Memory       │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│  Select Planner Strategy  │
│ (Single-Step / Multi-Step)│
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│       Generate Plan       │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│ Execute / Iterate Steps   │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│      Finalize Output      │
└──────────────────────────┘
```

---

## Design Principles

### Predictability
The planner follows a consistent decision flow, reducing ambiguity.

### Adaptivity
The planner adjusts strategy based on user intent, memory, and tool availability.

### Safety
All decisions respect safety constraints and avoid unsafe tool usage.

### Efficiency
The planner avoids unnecessary multi-step reasoning when a simple response is sufficient.

### Extensibility
New planner types or decision rules can be added without modifying core logic.

---

## Future Extensions

- dynamic planner switching mid-turn,
- planner confidence scoring,
- reinforcement learning for planner optimization,
- hybrid planners combining symbolic and LLM reasoning,
- planner introspection for debugging and transparency.


---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)
