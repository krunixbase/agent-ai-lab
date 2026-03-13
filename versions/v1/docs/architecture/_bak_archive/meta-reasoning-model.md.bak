# Meta‑Reasoning Model

## Overview

The meta‑reasoning model defines how the agent evaluates, critiques, and adjusts its own reasoning during execution. Meta‑reasoning operates above the standard planning and step‑execution layers, enabling the agent to detect flawed logic, identify uncertainty, refine intermediate outputs, and choose better strategies. This layer improves reliability, coherence, and adaptability without allowing unsafe self‑modification.

Meta‑reasoning is applied both *within a turn* (in‑turn meta‑reasoning) and *after a turn* (post‑turn reflection). It influences planning, tool usage, safety decisions, and long‑horizon reasoning.

---

## Meta‑Reasoning Capabilities

### Self‑Evaluation During Execution
The agent evaluates:
- whether its reasoning is coherent,
- whether steps align with the plan,
- whether assumptions are justified,
- whether uncertainty is high enough to require alternative strategies.

### Strategy Selection
The agent chooses between:
- direct reasoning,
- tool‑assisted reasoning,
- multi‑step planning,
- fallback strategies,
- regeneration with stricter constraints.

### Error Anticipation
The agent predicts:
- likely failure points,
- ambiguous instructions,
- unsafe or incomplete outputs,
- tool call risks.

### Confidence Assessment
The agent estimates:
- confidence in intermediate reasoning,
- reliability of retrieved knowledge,
- stability of the plan,
- need for additional validation.

---

## Meta‑Reasoning Layers

### In‑Turn Meta‑Reasoning
Occurs during step execution:
- evaluates LLM outputs,
- checks for contradictions,
- identifies missing information,
- adjusts reasoning paths.

### Planner‑Level Meta‑Reasoning
Occurs when generating or revising plans:
- evaluates plan complexity,
- detects redundant or unsafe steps,
- chooses between alternative strategies,
- shortens or restructures plans.

### Post‑Turn Reflection
Occurs after producing the final output:
- identifies weaknesses in reasoning,
- updates memory with distilled insights,
- prepares for future turns,
- refines long‑horizon goals.

---

## Meta‑Reasoning Flow

```
┌──────────────────────────┐
│   Generate Initial Plan   │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│  Evaluate Plan Coherence  │
│ (meta‑reasoning layer)    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Execute Step with       │
│   In‑Turn Meta‑Checks     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│  Adjust Reasoning Path    │
│ (if contradictions found) │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   Final Output +          │
│   Post‑Turn Reflection    │
└──────────────────────────┘
```

---

## Meta‑Reasoning Techniques

### Consistency Checking
The agent checks:
- whether steps contradict earlier reasoning,
- whether tool outputs align with expectations,
- whether assumptions remain valid.

### Counterfactual Reasoning
The agent evaluates:
- alternative interpretations of the user request,
- alternative plan structures,
- alternative tool sequences.

### Uncertainty Handling
The agent identifies:
- ambiguous instructions,
- missing information,
- low‑confidence reasoning,
- unclear tool results.

When uncertainty is high, the agent may:
- ask clarifying questions,
- choose safer strategies,
- regenerate reasoning with constraints.

### Self‑Critique
The agent critiques:
- logical gaps,
- unsupported claims,
- excessive assumptions,
- unnecessary complexity.

### Strategy Switching
The agent may switch strategies when:
- the current plan is inefficient,
- a tool is unnecessary,
- a simpler approach exists,
- safety risk increases.

---

## Meta‑Reasoning Triggers

### Logical Triggers
- contradictions in reasoning,
- incomplete steps,
- invalid assumptions.

### Safety Triggers
- potential policy violations,
- sensitive content,
- unsafe tool usage.

### Performance Triggers
- overly long plans,
- redundant steps,
- unnecessary LLM calls.

### Uncertainty Triggers
- ambiguous user intent,
- conflicting memory entries,
- unreliable tool outputs.

---

## Meta‑Reasoning Outputs

### Revised Plans
- shorter,
- safer,
- more efficient.

### Revised Steps
- corrected arguments,
- improved reasoning,
- validated assumptions.

### Clarifying Questions
- when uncertainty is too high,
- when user intent is unclear.

### Reflection Notes
- distilled insights,
- memory updates,
- long‑term improvements.

---

## Design Principles

### Safety‑Aligned Reasoning
Meta‑reasoning must always prioritize safety over efficiency.

### Deterministic Behavior
Meta‑reasoning should produce consistent results for identical inputs.

### Non‑Self‑Modifying
The agent cannot alter its core behavior or safety rules.

### Transparency (Internal)
Meta‑reasoning decisions are logged for debugging and analysis.

### Minimal Intrusion
Meta‑reasoning should refine reasoning without overwhelming the main execution flow.

---

## Future Extensions

- probabilistic reasoning models,
- ML‑based uncertainty estimation,
- multi‑agent meta‑coordination,
- long‑term meta‑learning (non‑self‑modifying),
- dynamic strategy optimization.


---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)
