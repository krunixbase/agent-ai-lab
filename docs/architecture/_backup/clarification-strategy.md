# Clarification Strategy

## Overview

The clarification strategy determines when the agent should ask questions to resolve ambiguity, missing parameters, conflicting instructions, or unsafe requests. It ensures correctness while minimizing user burden.

---

## When Clarification Is Needed

### Missing Parameters
Essential details are absent.

### Ambiguous Instructions
Multiple interpretations are possible.

### Conflicting Goals
User requests contradict each other.

### Safety Concerns
Request may violate safety rules.

### Unclear Intent
User message lacks actionable meaning.

---

## Clarification Types

- direct questions,
- multiple-choice disambiguation,
- parameter confirmation,
- safety-oriented clarification,
- scope narrowing.

---

## Clarification Workflow

1. Detect ambiguity or missing information.  
2. Identify minimal clarifying question.  
3. Ask concise, targeted question.  
4. Update intent and context based on user reply.  

---

## Design Principles

- minimalism,
- precision,
- user comfort,
- safety,
- conversational flow preservation.

---

## Integration with Other Systems

- intent interpretation triggers clarification,
- planning adjusts based on clarified intent,
- memory updates context after clarification,
- safety validates clarified requests.

---

## Future Extensions

- adaptive clarification styles,
- multi-step clarification chains,
- preference-based clarification behavior.
