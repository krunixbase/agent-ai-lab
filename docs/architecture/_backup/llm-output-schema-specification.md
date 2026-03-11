# LLM Output Schema Specification

## Overview

The LLM output schema specification defines the structured formats that the language model must follow when returning results to the agent. These schemas ensure that planner decisions, tool calls, and final responses are predictable, machine‑readable, and safe. By enforcing strict output structures, the agent avoids malformed actions, ambiguous reasoning, and unsafe tool usage.

The schema specification applies to all LLM interactions, including planning, tool invocation, summarization, and final message generation.

---

## Goals of the Output Schema

- Ensure deterministic and parseable LLM outputs.
- Prevent malformed or unsafe tool calls.
- Provide clear separation between reasoning, actions, and final responses.
- Support multi-step planning workflows.
- Enable safe integration with the orchestration layer and tool registry.

---

## Core Output Types

### Assistant Response
Used when the LLM produces a direct natural-language reply to the user.

```
{
"type": "response",
"message": "string"
}
```

### Tool Call
Used when the LLM instructs the agent to execute a tool.

```
{
"type": "tool_call",
"tool": "tool_name",
"arguments": { ... }
}
```

### Multi-Step Plan
Used when the LLM generates a structured plan for multi-step reasoning.

```
{
"type": "plan",
"steps": [
{
"id": "string",
"action": "tool | llm | respond",
"description": "string",
"arguments": { ... }
}
]
}
```

### Planner Continuation
Used when the LLM continues an existing multi-step plan.

```
{
"type": "continue",
"next_step": "string"
}
```

### Error Output
Used when the LLM detects an internal issue or cannot produce a valid structure.

```
{
"type": "error",
"message": "string"
}
```

---

## Validation Rules

### Required Fields
Each schema type must include:
- a `type` field,
- all required fields for that type,
- valid JSON structure.

### Tool Call Validation
Tool calls must:
- reference a registered tool,
- include all required arguments,
- match the tool’s input schema.

Invalid tool calls are rejected before execution.

### Plan Validation
Plans must:
- include at least one step,
- use unique step IDs,
- specify valid actions,
- avoid unsafe or recursive loops.

### Response Validation
Responses must:
- contain only user-facing text,
- avoid tool instructions,
- avoid planner metadata.

---

## Output Flow

### 1. LLM Generates Output
The LLM produces a JSON-like structure following one of the schemas.

### 2. Schema Validation
The agent validates:
- JSON correctness,
- required fields,
- allowed types,
- tool argument structure.

### 3. Action Routing
Depending on the schema:
- responses go directly to the user,
- tool calls go to the tool registry,
- plans go to the planner,
- errors trigger fallback strategies.

### 4. State Update
The agent updates:
- planner state,
- memory,
- tool execution state.

---

## Output Schema Diagram

```
┌──────────────────────────┐
│     LLM Output (Raw)      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Schema Validation     │
└─────────────┬────────────┘
│
▼
┌───────────────┬────────────────┬────────────────┐
▼               ▼                ▼                ▼
Response       Tool Call         Plan Output        Error Output
│               │                │                │
▼               ▼                ▼                ▼
┌──────────────────────────────────────────────────────────────┐
│                 Orchestration Layer Routing                   │
└──────────────────────────────────────────────────────────────┘
```

---

## Design Principles

### Strictness
Schemas are intentionally rigid to prevent ambiguous or unsafe outputs.

### Transparency
Each output type clearly communicates the LLM’s intent.

### Safety
Unsafe or malformed outputs are rejected before reaching the planner or tools.

### Extensibility
New output types can be added without modifying existing logic.

### Predictability
The agent always knows how to interpret LLM outputs.

---

## Future Extensions

- streaming output schemas,
- confidence scoring fields,
- multi-action batching,
- schema versioning,
- hybrid symbolic‑LLM output formats.

