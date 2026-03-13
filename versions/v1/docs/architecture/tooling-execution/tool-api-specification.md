# Tool API Specification Overview

The Tool API defines the contract between the agent and all external tools. It ensures that tools are predictable,
composable, and easy for the planner to reason about. This specification standardizes how tools declare their capabilities, 
how they receive inputs, how they return outputs, and how errors are handled.

The goal is to create a unified interface that allows the agent to integrate new tools without modifying the core planning or memory systems.

---

# Tool Definition Model

Each tool must define a structured interface consisting of:

## Name

A unique identifier used by the planner to reference the tool.

## Description

A short explanation of what the tool does and when it should be used.

## Input Schema

A structured definition of all required and optional parameters.
Schemas include:

- parameter names,

- types (string, number, boolean, object),

- validation rules,

- default values (if applicable).

## Execution Function

A callable function that:

- validates input,

- performs the tool’s operation,

- returns a structured result.

## Output Schema

A predictable structure describing:

- success results,

- error results,

- metadata (timestamps, execution info).

This ensures that planners can interpret tool outputs deterministically.

---

# Tool Categories

Tools may fall into several categories depending on their purpose:

- Information Retrieval Tools — e.g., search, Wikipedia, weather.

- Computation Tools — e.g., math, data processing.

- Action Tools — e.g., sending messages, triggering workflows.

- Environment Tools — interacting with external systems or APIs.

Each category follows the same API contract but may differ in complexity.

---

# Execution Lifecycle

1. Input Validation

The tool validates incoming parameters against its schema.
Invalid inputs produce structured error responses.

2. Execution

The tool performs its operation.
This may involve:

- API calls,

- computation,

- data transformation.

3. Result Packaging

The tool returns a structured output containing:

- status (success or error),

- data (tool-specific result),

- error (if applicable),

- metadata (execution time, source info).

4. Planner Integration

The planner interprets the result and decides:

- whether to continue planning,

- whether to call another tool,

- whether to finalize the response.

---

# Standard Output Format

All tools must return a JSON-like structure:

```
{
  "status": "success" | "error",
  "data": { ... },        // tool-specific result
  "error": { ... },       // only present on failure
  "metadata": {
    "timestamp": "...",
    "execution_ms": 42
  }
}
```

This ensures consistency across all tools.

---

# Error Handling Model

Tools must handle errors gracefully and never throw raw exceptions.
Common error types include:

- ValidationError — invalid or missing parameters.

- ExecutionError — failure during tool operation.

- ExternalError — upstream API or network issues.

- TimeoutError — operation exceeded allowed time.

Errors must include:

- a machine-readable code,

- a human-readable message,

- optional recovery hints.

# Security and Safety Requirements

Tools must follow strict safety rules:

- No uncontrolled side effects.

- No access to unauthorized resources.

- No unvalidated external input.

- No unbounded execution loops.

- No direct modification of agent memory.

Tools operate in a sandboxed environment and must be deterministic.

---

# Extensibility Guidelines

The Tool API is designed to support future extensions:

- new tool categories,

- streaming tool outputs,

- asynchronous execution,

- tool chaining and pipelines,

- reliability scoring and fallback strategies.

Tools can be added without modifying the planner or agent loop as long as they follow the API contract.

---

# Future Enhancements

- automatic tool discovery and registration,

- tool capability negotiation,

- tool embeddings for semantic selection,

- caching of tool results,

- multi-tool orchestration with dependency graphs.

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
