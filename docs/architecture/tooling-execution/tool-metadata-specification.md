# Tool Metadata Specification

## Overview

The tool metadata specification defines the structured information required to describe a tool within the agent architecture. Metadata ensures that tools are discoverable, validated, categorized, and safely executable. It also enables the planner to make informed decisions about which tools to use, how to call them, and under what constraints.

Metadata is stored in the tool registry and is used throughout the tool execution lifecycle.

---

## Metadata Fields

### Name
A unique identifier for the tool.

```
"name": "string"
```

### Description
A human‑readable explanation of what the tool does.

```
"description": "string"
```

### Category
A classification used for planner selection and capability grouping.

Examples:
- "search"
- "computation"
- "environment"
- "data"
- "external_api"

```
"category": "string"
```

### Input Schema
A JSON schema describing the required and optional input fields.

```
"input_schema": {
"type": "object",
"properties": { ... },
"required": [ ... ]
}
```

### Output Schema
A JSON schema describing the structure of the tool’s output.

```
"output_schema": {
"type": "object",
"properties": { ... }
}
```

### Safety Level
Indicates the risk profile of the tool.

Examples:
- "safe"
- "restricted"
- "dangerous"

```
"safety_level": "string"
```

### Permissions
Optional rules defining when the tool may be used.

Examples:
- allowed contexts,
- restricted user intents,
- rate limits.

```
"permissions": { ... }
```

### Execution Function Reference
A pointer to the function that implements the tool.

```
"execute": "function_reference"
```

### Metadata Version
Allows future schema evolution.

```
"version": "1.0"
```

---

## Metadata Validation

### Required Fields
A valid tool must include:
- name,
- description,
- category,
- input schema,
- output schema,
- execution reference.

### Schema Validation
The registry verifies:
- JSON schema correctness,
- required fields,
- type consistency.

### Safety Validation
The registry ensures:
- safety level is valid,
- restricted tools follow permission rules,
- unsafe tools cannot be executed without explicit approval.

---

## Metadata Usage

### Tool Discovery
The planner queries metadata to:
- list available tools,
- filter by category,
- check capabilities.

### Tool Selection
Metadata helps the planner decide:
- whether a tool matches the user’s intent,
- whether the tool is safe to use,
- whether the tool’s input schema fits the planned action.

### Execution Routing
The registry uses metadata to:
- validate arguments,
- dispatch execution,
- normalize results.

---

## Metadata Structure Diagram

```
┌──────────────────────────┐
│        Tool Metadata      │
└─────────────┬────────────┘
│
▼
┌──────────────────────┐
│  Validation Layer     │
└─────────────┬────────┘
│
▼
┌──────────────────────┐
│   Planner Usage       │
└─────────────┬────────┘
│
▼
┌──────────────────────┐
│ Execution Lifecycle   │
└──────────────────────┘
```

---

## Design Principles

### Consistency
All tools follow the same metadata structure.

### Transparency
Metadata clearly communicates tool capabilities and constraints.

### Safety
Metadata enforces safety rules before execution.

### Extensibility
New metadata fields can be added without breaking existing tools.

### Interoperability
Metadata integrates seamlessly with planners, memory, and the orchestration layer.

---

## Future Extensions

- metadata‑driven tool embeddings,
- automatic tool capability inference,
- dynamic metadata updates,
- versioned tool definitions,
- metadata‑based tool reliability scoring.



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
