# Conversation Summarization Model

## Overview

The conversation summarization model defines how the agent compresses long conversational histories into concise, reusable summaries. Summaries allow the agent to maintain context across long interactions without exceeding token limits or losing important information. The model integrates with memory retrieval, session persistence, and the runtime loop to ensure that summaries remain accurate, relevant, and up to date.

Summarization is designed to be incremental, context-aware, and optimized for LLM consumption.

---

## Goals of the Summarization Model

- Preserve essential information from long conversations.
- Reduce memory footprint while maintaining context.
- Enable fast retrieval of relevant details.
- Prevent context drift during multi-turn interactions.
- Support long-term continuity across sessions.

---

## Types of Summaries

### Episodic Summaries
Short summaries generated after each turn or small group of turns.  
They capture:
- user intent,
- agent actions,
- tool usage,
- key outcomes.

### Rolling Summaries
Medium-length summaries that replace older episodic entries once thresholds are reached.  
They capture:
- topic transitions,
- resolved tasks,
- important facts,
- user preferences.

### Long-Term Summaries
High-level summaries stored across sessions.  
They capture:
- stable user preferences,
- recurring topics,
- long-term goals,
- important facts extracted from multiple conversations.

---

## Summarization Flow

### 1. Triggering Summarization
Summaries may be generated when:
- the episodic memory buffer reaches a size limit,
- a conversation topic concludes,
- the session ends,
- the agent detects redundant or outdated memory.

### 2. Memory Extraction
The agent selects relevant memory entries:
- recent turns,
- tool results,
- planner decisions,
- user-provided facts.

### 3. Summary Generation
The LLM produces a structured summary that:
- removes redundancy,
- preserves meaning,
- maintains chronological clarity,
- highlights important details.

### 4. Summary Storage
The summary is stored in:
- summary memory,
- persistent memory (if configured),
- vector memory (as an embedding).

### 5. Replacement and Pruning
Older episodic entries are removed or compressed once the summary is stored.

---

## Summarization Diagram

```
┌──────────────────────────┐
│   Episodic Memory Grows   │
└─────────────┬────────────┘
│ Threshold reached
▼
┌──────────────────────────┐
│    Extract Key Entries    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Generate LLM Summary    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     Store in Summary      │
│   + Vector Memory (opt.)  │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Prune Episodic Memory   │
└──────────────────────────┘
```

---

## Design Principles

### Relevance
Summaries focus on information that will matter in future turns.

### Compression
Redundant or low-value details are removed to reduce memory load.

### Stability
Long-term summaries avoid volatile or ephemeral details.

### LLM Optimization
Summaries are formatted to be easily consumed by the LLM during prompt construction.

### Privacy Awareness
Sensitive or personal data is excluded unless explicitly allowed.

---

## Future Extensions

- topic-aware summarization,
- hierarchical summaries,
- user-editable summaries,
- automatic detection of summary-worthy events,
- multi-agent shared summarization models.


---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)
