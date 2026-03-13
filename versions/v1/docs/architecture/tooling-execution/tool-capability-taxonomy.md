# Tool Capability Taxonomy

## Overview

The tool capability taxonomy defines a structured classification system for all tools available to the agent. It organizes tools by functional domain, operational characteristics, safety level, and planner relevance. The taxonomy enables the planner to reason about tool selection, capability matching, and safe execution strategies without relying on tool‑specific heuristics.

A consistent taxonomy improves discoverability, modularity, and extensibility across the entire tool ecosystem.

---

## Top‑Level Categories

### Information Retrieval Tools
Tools that fetch external or internal information.  
Examples:
- search engines,
- document retrievers,
- database query tools.

Characteristics:
- stateless,
- read‑only,
- often low‑risk.

### Computational Tools
Tools that perform calculations or transformations.  
Examples:
- math engines,
- data processors,
- format converters.

Characteristics:
- deterministic,
- no external side effects,
- medium safety requirements.

### Environment Interaction Tools
Tools that interact with external systems or environments.  
Examples:
- file system tools,
- automation tools,
- system control interfaces.

Characteristics:
- may have side effects,
- require strict safety validation.

### External API Tools
Tools that call third‑party services.  
Examples:
- weather APIs,
- financial APIs,
- communication APIs.

Characteristics:
- network‑dependent,
- may require authentication,
- medium to high safety constraints.

### Data Manipulation Tools
Tools that modify or generate structured data.  
Examples:
- JSON transformers,
- schema validators,
- data cleaning utilities.

Characteristics:
- deterministic,
- require schema validation,
- low to medium safety risk.

### Agent‑Internal Tools
Tools that operate within the agent’s internal architecture.  
Examples:
- memory read/write tools,
- summarization utilities,
- planner state tools.

Characteristics:
- tightly coupled with agent state,
- high safety requirements,
- must follow memory safety rules.

---

## Capability Dimensions

Each tool is classified along multiple dimensions:

### Functional Domain
Defines what the tool does:
- retrieval,
- computation,
- transformation,
- interaction,
- control.

### Safety Level
Indicates risk profile:
- safe,
- restricted,
- dangerous.

### Side‑Effect Profile
Describes whether the tool:
- is read‑only,
- modifies internal state,
- modifies external systems.

### Determinism
Indicates whether the tool:
- produces consistent outputs,
- depends on external factors,
- may fail unpredictably.

### Planner Relevance
Defines how the planner uses the tool:
- primary action tool,
- supporting tool,
- fallback tool.

---

## Tool Classification Schema

Each tool is represented as:

```
{
"name": "string",
"category": "retrieval | computation | environment | api | data | internal",
"capabilities": [ "string", ... ],
"safety_level": "safe | restricted | dangerous",
"side_effects": "none | internal | external",
"deterministic": true | false,
"planner_role": "primary | supporting | fallback"
}
```

---

## Taxonomy Usage

### Planner Tool Selection
The planner uses the taxonomy to:
- filter tools by capability,
- avoid unsafe tools in restricted contexts,
- prioritize deterministic tools,
- select fallback tools when needed.

### Safety Enforcement
Safety layers use the taxonomy to:
- block dangerous tools,
- validate side‑effect profiles,
- enforce permission rules.

### Tool Discovery
The agent uses the taxonomy to:
- list available tools,
- group tools by domain,
- expose capabilities to developers.

### Capability Expansion
New tools automatically extend:
- the capability model,
- planner decision space,
- orchestration strategies.

---

## Taxonomy Diagram

```
┌──────────────────────────┐
│     Tool Capability       │
│        Taxonomy           │
└─────────────┬────────────┘
│
▼
┌──────────────────────┐
│  Functional Domain    │
└─────────────┬────────┘
│
▼
┌──────────────────────┐
│    Safety Level       │
└─────────────┬────────┘
│
▼
┌──────────────────────┐
│  Side-Effect Profile  │
└─────────────┬────────┘
│
▼
┌──────────────────────┐
│     Determinism       │
└─────────────┬────────┘
│
▼
┌──────────────────────┐
│    Planner Role       │
└──────────────────────┘
```

---

## Design Principles

### Consistency
All tools follow the same classification structure.

### Safety Alignment
Taxonomy integrates directly with safety layers.

### Planner Compatibility
The taxonomy is optimized for planner decision‑making.

### Extensibility
New categories or dimensions can be added without breaking existing tools.

### Clarity
Developers can easily understand tool capabilities and constraints.

---

## Future Extensions

- capability scoring based on reliability,
- dynamic taxonomy updates,
- cross‑tool capability inference,
- taxonomy‑driven planner optimization,
- automated tool clustering using embeddings.


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
