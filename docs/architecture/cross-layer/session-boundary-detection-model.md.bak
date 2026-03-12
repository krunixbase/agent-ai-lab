# Session Boundary Detection Model

## Overview

The session boundary detection model defines how the agent determines when a conversation session begins, ends, or transitions into a new context. Detecting boundaries is essential for managing memory, summarization, context resets, and long‑term continuity. The model ensures that the agent maintains coherence without carrying irrelevant or outdated context across unrelated interactions.

Session boundaries may be explicit (user signals the end) or implicit (detected through behavioral or contextual cues).

---

## Boundary Types

### Explicit Session End
Triggered when the user clearly indicates the end of a conversation.  
Examples:
- “Thanks, that’s all.”
- “Goodbye.”
- “We’re done.”

### Implicit Session End
Detected when the agent identifies signals such as:
- long inactivity,
- abrupt topic shift,
- new task unrelated to prior context,
- user returning after a long gap with a new intent.

### Session Reset
Occurs when the user explicitly requests:
- “Start over,”
- “Clear context,”
- “Forget the previous conversation.”

### Session Transition
A boundary between two distinct tasks within the same interaction.  
Example:
- User finishes a coding task and immediately starts a travel planning task.

---

## Detection Signals

### Temporal Signals
- long inactivity windows,
- user returning after hours or days,
- session timeout thresholds.

### Linguistic Signals
- explicit closing phrases,
- greetings after long gaps,
- abrupt topic changes,
- meta‑instructions (“new task”, “switch topic”).

### Behavioral Signals
- switching from one domain to another (e.g., math → cooking),
- tool usage patterns indicating a new workflow,
- planner detecting unrelated intent.

### Memory Signals
- retrieved memory does not match new user intent,
- vector similarity below relevance thresholds,
- summary memory mismatch.

---

## Boundary Detection Flow

### 1. Receive User Input
The agent receives the latest message and normalizes it.

### 2. Evaluate Explicit Signals
The agent checks for:
- closing phrases,
- reset commands,
- greetings indicating a new start.

### 3. Evaluate Implicit Signals
The agent analyzes:
- time since last message,
- topic similarity,
- planner intent classification.

### 4. Determine Boundary Type
The agent classifies the event as:
- no boundary,
- session end,
- session reset,
- session transition.

### 5. Apply Boundary Logic
Depending on classification:
- end → finalize session, trigger summarization,
- reset → clear episodic memory and planner state,
- transition → compress recent context and start new task context.

### 6. Update Memory
The agent updates:
- episodic memory,
- summary memory,
- session metadata.

---

## Detection Diagram

```
┌──────────────────────────┐
│     Receive Input         │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│  Check Explicit Signals   │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│  Check Implicit Signals   │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│ Classify Boundary Type    │
└─────────────┬────────────┘
│
▼
┌──────────────┬──────────────┬──────────────┐
▼              ▼              ▼              ▼
No Boundary   Session End   Session Reset   Transition
│              │              │              │
▼              ▼              ▼              ▼
┌──────────────────────────────────────────────────────────┐
│            Apply Boundary Logic & Update Memory           │
└──────────────────────────────────────────────────────────┘
```

---

## Design Principles

### Precision
Boundaries must be detected accurately to avoid losing relevant context.

### Safety
Resets and transitions must not leak sensitive or irrelevant information.

### Stability
Minor topic drift should not trigger unnecessary resets.

### Extensibility
New signals or heuristics can be added without modifying core logic.

### Determinism
The same input should always produce the same boundary classification.

---

## Future Extensions

- machine‑learned boundary classifiers,
- user‑configurable session timeout policies,
- domain‑aware topic segmentation,
- multi‑agent shared session boundaries,
- adaptive thresholds based on user behavior.


---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)
