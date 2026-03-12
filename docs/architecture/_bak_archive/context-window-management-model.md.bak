# Context Window Management Model

## Overview

The context window management model defines how the agent controls, prioritizes, compresses, and injects information into the LLM’s limited context window. Because the LLM can only process a finite number of tokens per request, the agent must intelligently decide which information to include, which to compress, and which to discard. The model ensures that the agent maintains coherence, avoids context overflow, and preserves essential information across long conversations and multi‑step tasks.

Context management integrates memory retrieval, summarization, planner state, safety filtering, and prompt construction.

---

## Context Sources

### User Input
The latest user message is always included in full.

### System Instructions
Static instructions defining:
- safety rules,
- behavior constraints,
- output schemas.

### Planner Context
Includes:
- current plan,
- next required action,
- tool schemas,
- reasoning constraints.

### Memory Context
Retrieved from:
- summary memory,
- vector memory,
- episodic memory.

### Intermediate Results
Includes:
- tool outputs,
- validated LLM outputs,
- state transitions.

---

## Context Prioritization

The agent assigns priority levels to context elements:

### Priority 1 — Mandatory
Always included:
- system instructions,
- user input,
- planner-required schemas,
- safety constraints.

### Priority 2 — High
Included unless the window is critically full:
- current plan,
- tool call schemas,
- essential memory entries.

### Priority 3 — Medium
Included when space allows:
- vector memory matches,
- relevant episodic memory,
- intermediate results.

### Priority 4 — Low
Included only when abundant space exists:
- extended history,
- non-critical metadata,
- optional context.

---

## Compression Strategies

### Summarization
Long memory entries or conversation history are compressed using:
- abstractive summaries,
- key-point extraction,
- topic-level condensation.

### Relevance Filtering
Entries below a relevance threshold are removed.

### Deduplication
Redundant or overlapping content is eliminated.

### Semantic Compression
Vector memory matches may be merged into:
- topic clusters,
- semantic summaries.

### Planner-Aware Compression
The planner may request:
- step-specific compression,
- removal of irrelevant branches,
- focus on active subtask.

---

## Context Window Management Flow

### 1. Collect Context Candidates
The agent gathers:
- memory,
- planner state,
- system instructions,
- user input.

### 2. Assign Priorities
Each element is tagged with a priority level.

### 3. Estimate Token Cost
The agent estimates token usage for each element.

### 4. Fill Context Window
Elements are added in priority order until the limit is reached.

### 5. Apply Compression
If the window overflows:
- compress medium-priority items,
- summarize long entries,
- remove low-priority items.

### 6. Validate Safety
All included content is checked for:
- sensitive data,
- unsafe content,
- policy violations.

### 7. Construct Final Prompt
The prompt construction model assembles the final context.

---

## Context Window Diagram

```
┌──────────────────────────┐
│   Collect Context Data    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│    Assign Priorities      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Estimate Token Cost     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Fill Context Window     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│    Apply Compression      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Safety Validation     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Final Prompt Assembly   │
└──────────────────────────┘
```

---

## Token Budgeting Model

The agent uses a dynamic budgeting strategy:

### Hard Budget
Maximum tokens allowed by the LLM.

### Soft Budget
Target token usage to leave room for:
- LLM reasoning,
- planner-required structures.

### Budget Allocation
Tokens are allocated proportionally:
- 40–50% for system + planner context,
- 20–30% for memory,
- 20–30% for user input + task instructions.

---

## Failure Modes and Recovery

### Overflow Detected
Mitigation:
- aggressive summarization,
- removal of low-priority items.

### Missing Critical Context
Mitigation:
- re-fetch memory,
- re-evaluate priorities,
- planner may request a context reset.

### Relevance Drift
Mitigation:
- vector memory re-ranking,
- topic-based filtering.

---

## Design Principles

### Relevance Over Recency
Only context that supports the current task is included.

### Safety First
Unsafe or sensitive content is removed before inclusion.

### Deterministic Behavior
The same inputs produce the same context selection.

### Extensibility
New memory types or planner modes can extend the model.

### Efficiency
Compression minimizes token usage without losing meaning.

---

## Future Extensions

- adaptive token budgeting based on task complexity,
- ML-driven relevance scoring,
- cross-session context optimization,
- hierarchical memory compression,
- predictive context shaping for multi-step plans.


---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)
