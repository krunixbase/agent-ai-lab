# Memory Retrieval Model

## Overview

The memory retrieval model defines how the agent selects, filters, and ranks memory entries to provide relevant context for each turn. Retrieval spans episodic memory, vector memory, and summary memory, combining symbolic and semantic signals to reconstruct the most useful context for reasoning. The model ensures that retrieved content is safe, relevant, and optimized for LLM consumption.

Retrieval is deterministic, multi-layered, and tightly integrated with the runtime loop and prompt construction model.

---

## Retrieval Layers

### Summary Memory Retrieval
Provides high-level, long-term context.  
Used to:
- recall stable user preferences,
- maintain continuity across sessions,
- provide topic-level summaries.

### Vector Memory Retrieval
Provides semantic matches using embeddings.  
Used to:
- retrieve conceptually related content,
- surface older but relevant information,
- support long-range contextual recall.

### Episodic Memory Retrieval
Provides recent conversational history.  
Used to:
- maintain short-term continuity,
- preserve turn-by-turn context,
- support immediate reasoning.

---

## Retrieval Flow

### 1. Query Construction
The agent constructs a retrieval query using:
- the user’s latest message,
- planner context,
- task requirements.

This query is used for vector search and episodic filtering.

### 2. Summary Memory Load
Summary memory is always loaded first because it provides stable, high-level context.

### 3. Vector Memory Search
The agent performs semantic retrieval:
- embedding similarity search,
- relevance scoring,
- safety filtering.

Top matches are selected based on relevance thresholds.

### 4. Episodic Memory Filtering
Recent turns are filtered by:
- recency,
- relevance to the query,
- safety constraints.

Only the most relevant entries are included.

### 5. Consolidation
The agent merges:
- summary memory,
- vector memory matches,
- episodic memory entries.

Duplicates and redundant content are removed.

### 6. Safety Filtering
Before injection into prompts, all retrieved entries undergo:
- sensitive data filtering,
- unsafe content removal,
- structural validation.

### 7. Prompt Injection
Only validated entries are included in the prompt construction model.

---

## Retrieval Diagram

```
┌──────────────────────────┐
│     Construct Query       │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│  Load Summary Memory      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│ Vector Memory Retrieval   │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│ Episodic Memory Filter    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Consolidate Results   │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Safety Filtering      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Prompt Injection      │
└──────────────────────────┘
```

---

## Ranking Model

Memory entries are ranked using a weighted combination of:

- **semantic similarity** (vector memory),
- **recency** (episodic memory),
- **topic relevance** (summary memory),
- **task alignment** (planner context),
- **safety score** (filtered content).

The ranking ensures that the most relevant and safe entries appear first.

---

## Design Principles

### Relevance First
Only memory that directly supports the current task is retrieved.

### Safety Integration
Unsafe or sensitive content is filtered at multiple stages.

### Multi-Layer Retrieval
Combining summary, vector, and episodic memory provides both breadth and depth.

### Deterministic Behavior
Retrieval follows a strict order and consistent thresholds.

### Extensibility
New memory types or ranking strategies can be added without modifying core logic.

---

## Future Extensions

- adaptive retrieval thresholds,
- cross-session semantic linking,
- topic clustering for improved relevance,
- retrieval caching for repeated tasks,
- hybrid symbolic–semantic retrieval models.


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
