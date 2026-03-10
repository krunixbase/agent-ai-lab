# LLM Prompt Construction Model

## Overview

The LLM prompt construction model defines how the agent builds structured, safe, and context‑aware prompts for the language model. Its purpose is to ensure that every LLM call receives the correct combination of system instructions, memory, user input, and planner context. A well‑constructed prompt improves reasoning quality, reduces hallucinations, and ensures consistent behavior across all tasks.

Prompt construction is deterministic, layered, and optimized for both safety and performance.

---

## Prompt Layers

### System Layer
Defines the LLM’s role, constraints, and behavior.  
Includes:
- safety instructions,
- formatting rules,
- reasoning constraints,
- tool usage rules.

This layer is static and appears at the top of every prompt.

### Context Layer
Provides relevant information from memory:
- summary memory,
- vector memory matches,
- episodic memory (recent turns),
- planner state (if applicable).

Only validated and safe memory is included.

### Task Layer
Describes what the LLM must do.  
Includes:
- planner instructions,
- tool call schemas,
- output schemas,
- reasoning requirements.

This layer changes depending on the planner’s needs.

### User Input Layer
Contains the user’s latest message, normalized and sanitized.

This is always the final section of the prompt.

---

## Prompt Construction Flow

### 1. Load System Instructions
The agent loads the base system prompt containing:
- safety rules,
- behavioral constraints,
- output format requirements.

### 2. Retrieve Memory
The agent retrieves:
- summary memory,
- vector memory results,
- recent conversation turns.

Only safe and relevant entries are included.

### 3. Insert Planner Context
If the planner is active, the prompt includes:
- current plan,
- expected output schema,
- next required action.

### 4. Insert Task Instructions
The agent adds:
- tool schemas,
- reasoning instructions,
- task-specific constraints.

### 5. Insert User Input
The final section contains the user’s message.

### 6. Final Assembly
All layers are concatenated in a strict order to form the final prompt.

---

## Prompt Structure Diagram

┌──────────────────────────┐
│     System Instructions   │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Memory Context        │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Planner Context       │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Task Instructions     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│       User Input          │
└──────────────────────────┘

---

## Design Principles

### Deterministic Ordering
Prompts always follow the same structure, reducing ambiguity.

### Safety First
Unsafe memory or user content is filtered before inclusion.

### Minimalism
Only relevant context is included to avoid prompt bloat.

### Schema Alignment
Prompts always reference the correct output schema for the task.

### Extensibility
New layers or instructions can be added without breaking existing logic.

---

## Future Extensions

- adaptive prompt compression,
- dynamic prompt shaping based on task complexity,
- multi‑model prompt routing,
- prompt caching for repeated tasks,
- automatic detection of irrelevant memory.

