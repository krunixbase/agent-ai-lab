# Planner–LLM Interaction Protocol

## Overview

The planner–LLM interaction protocol defines how the planner communicates with the language model, how instructions are encoded, how outputs are interpreted, and how multi‑step reasoning is coordinated. The protocol ensures that planner requests are unambiguous, LLM outputs follow strict schemas, and the reasoning loop remains deterministic and safe.

This protocol is central to orchestrating complex tasks that require iterative reasoning, tool usage, or structured plans.

---

## Interaction Goals

- Provide the LLM with clear, structured instructions.
- Ensure outputs follow strict schemas for safe parsing.
- Support multi‑step planning workflows.
- Maintain deterministic behavior across turns.
- Prevent hallucinated tool calls or malformed plans.
- Enable the planner to refine or continue reasoning based on LLM output.

---

## Interaction Stages

### 1. Planner Prepares Context
The planner gathers:
- user input,
- memory context,
- current plan state,
- required output schema.

This context is passed to the prompt construction model.

### 2. Prompt Construction
The prompt includes:
- system instructions,
- memory context,
- planner context,
- output schema,
- user input.

The LLM receives a fully structured prompt.

### 3. LLM Generates Structured Output
The LLM returns one of the allowed schema types:
- response,
- tool_call,
- plan,
- continue,
- error.

Outputs must be valid JSON-like structures.

### 4. Schema Validation
The agent validates:
- JSON correctness,
- required fields,
- allowed types,
- tool argument structure.

Invalid outputs trigger fallback or regeneration.

### 5. Planner Interpretation
The planner interprets the validated output:
- tool_call → execute tool,
- plan → begin multi-step reasoning,
- continue → execute next step,
- response → finalize output,
- error → fallback or regenerate.

### 6. Iteration or Completion
The planner may:
- continue the plan,
- refine the plan,
- request another LLM call,
- or finalize the response.

---

## Interaction Diagram

```
┌──────────────────────────┐
│     Planner Prepares      │
│         Context           │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Prompt Construction     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     LLM Generation        │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Schema Validation     │
└─────────────┬────────────┘
│
▼
┌───────────────┬────────────────┬────────────────┬──────────────┐
▼               ▼                ▼                ▼              ▼
Response       Tool Call         Plan Output      Continue Output   Error
│               │                │                │              │
▼               ▼                ▼                ▼              ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     Planner Interpretation & Routing                    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Design Principles

### Deterministic Protocol
The planner always knows how to interpret LLM outputs.

### Strict Schema Enforcement
Only valid structured outputs are accepted.

### Safety Integration
Unsafe or malformed outputs are rejected before execution.

### Iterative Reasoning Support
The protocol supports multi-step plans and refinement loops.

### Extensibility
New output types or planner modes can be added without breaking the protocol.

---

## Future Extensions

- planner confidence scoring,
- multi-model routing,
- hybrid symbolic–LLM reasoning steps,
- introspective planner feedback loops,
- schema versioning for evolving capabilities.


---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)
