# Perspective Modeling and User State Representation

## Purpose

Perspective Modeling and User State Representation define how the agent maintains structured models of what users (and other actors) know, want, and assume. These models support socially aware reasoning, clarification, and explanation.

---

## User State Components

- **Knowledge State** — what the user likely knows or does not know.
- **Goal State** — inferred goals, subgoals, and priorities.
- **Preference State** — tone, detail level, format, and interaction style.
- **Constraint State** — time, risk tolerance, domain constraints.
- **Emotional Context (Non‑Clinical)** — coarse‑grained interaction tone (e.g., frustrated, curious, neutral).

---

## Perspective Modeling Capabilities

- **Epistemic Modeling** — distinguishing agent knowledge from user knowledge.
- **Uncertainty Modeling** — representing ambiguity about user state.
- **Role‑Based Modeling** — adapting state representation to user roles.
- **Multi‑Actor Modeling** — tracking separate states for multiple participants.

---

## Representation Structures

- **User Profiles** — stable preferences and long‑term patterns (where allowed).
- **Session State Models** — transient goals and context for the current interaction.
- **Perspective Graphs** — relationships between actors, goals, and knowledge.
- **Assumption Annotations** — explicit markers for inferred vs. stated information.

---

## Modeling Workflow

1. Parse interaction signals (content, questions, corrections, preferences).
2. Update user state components with new evidence.
3. Mark inferred elements as assumptions, not facts.
4. Use perspective models to guide explanations, clarifications, and plans.
5. Periodically validate assumptions via lightweight clarification.

---

## Safety & Ethics Integration

- Avoid over‑personalization or intrusive inference.
- Do not infer sensitive attributes (e.g., health, demographics) beyond policy.
- Respect privacy and data minimization constraints.
- Use perspective modeling to reduce, not increase, user vulnerability.

---

## Integration with Other Systems

- **Interaction Layer v2** — uses user state to adapt responses.
- **Clarification Strategy Model** — uses uncertainty signals for questions.
- **Planning & Reasoning Architecture** — tailors plans to user goals and constraints.
- **Memory Architecture v2** — stores allowed long‑term preferences.
- **Ethics Architecture v2** — constrains what can be inferred or stored.

---

## Design Principles

- User state must be approximate, not absolute.
- Assumptions must be revisable and clearly separated from facts.
- Perspective models must remain lightweight and privacy‑preserving.

---

## Future Extensions

- Domain‑specific user state schemas.
- Multi‑party conversation state modeling.
- Adaptive epistemic modeling based on interaction history.
