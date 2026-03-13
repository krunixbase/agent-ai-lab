# GLOSSARY.md

## Purpose

This glossary defines key terms used throughout the **agent‑ai‑lab** architecture.  
It provides consistent terminology across all modules, ensuring clarity for contributors, reviewers, and implementers.

---

## Core Concepts

### Agent
A modular, multi‑layer AI system capable of reasoning, planning, interacting, retrieving knowledge, using tools, and adapting over time.

### Layer
A major architectural domain (e.g., Interaction, Cognitive & Planning, Memory & Knowledge) with clear responsibilities and boundaries.

### Subsystem
A focused component within a layer (e.g., Retrieval Model, Planning Engine, Tool Selector).

### Module
A documented architectural unit within `docs/architecture/`, typically consisting of 4–5 Markdown files.

---

## Cognitive & Planning Terms

### Reasoning
Structured cognitive processes used to interpret intent, generate explanations, solve problems, and make decisions.

### Planning
Decomposing a user request into actionable steps, tool calls, or reasoning sequences.

### Social Intelligence
The agent’s ability to adapt communication, infer user perspectives, and maintain socially appropriate behavior.

### Theory‑of‑Mind
Modeling what the user knows, wants, or assumes, without inferring sensitive or private attributes.

---

## Memory & Knowledge Terms

### Episodic Memory
Short‑term, session‑scoped memory capturing recent interactions.

### Long‑Term Memory
Persistent storage of stable, non‑sensitive information (e.g., user preferences, system knowledge).

### Vector Memory
Embedding‑based memory enabling semantic retrieval.

### Knowledge Retrieval
Fetching relevant information from memory or external knowledge sources.

---

## Tooling & Execution Terms

### Tool
An external capability the agent can invoke (e.g., search, calculator, database query).

### Tool Selection
Choosing the appropriate tool based on intent, context, and safety constraints.

### Execution Plan
A structured sequence of tool calls and reasoning steps.

### Fallback
An alternative tool or strategy used when the primary one fails.

---

## Runtime & Orchestration Terms

### Turn Loop
The core execution cycle that processes user input, reasoning, tool use, and response generation.

### State Management
Tracking conversation state, execution state, and intermediate results.

### Scheduling
Coordinating concurrent or sequential tasks within the runtime.

---

## Safety, Ethics & Governance Terms

### Safety Filter
A mechanism that prevents unsafe content, actions, or tool calls.

### Governance
Oversight mechanisms ensuring compliance with policies, ethics, and system rules.

### Escalation
Redirecting a request or event to a higher‑level safety or governance process.

### Policy
A rule defining allowed and disallowed behaviors across layers.

---

## Deployment, Reliability & Performance Terms

### Environment Profile
A description of the runtime environment’s capabilities, constraints, and limits.

### Reliability
The system’s ability to operate consistently under varying conditions.

### Performance Budget
Resource constraints (e.g., latency, memory) that influence planning and execution.

---

## Evaluation, Testing & Meta‑Learning Terms

### Evaluation
Systematic measurement of quality, safety, and correctness.

### Regression
A degradation in performance, safety, or correctness compared to previous versions.

### Meta‑Learning
Controlled, safe self‑optimization based on system‑wide observations.

### Optimization Proposal
A reversible, policy‑aligned suggestion for improving reasoning, memory, tool use, or performance.

---

## Observability & Auditing Terms

### Trace
A structured record of reasoning, tool calls, or execution steps.

### Metric
A quantitative measurement used for evaluation or monitoring.

### Audit Log
A record of decisions, safety events, or governance actions.

### Impact Analysis
Assessment of how a change affects system behavior, safety, or performance.

---

## Multi‑Agent & Embodiment Terms

### Multi‑Agent Coordination
Interaction between multiple agents with shared or complementary capabilities.

### Embodiment
Integration of the agent with physical or simulated environments.

### Simulation Loop
A controlled environment for testing agent behavior under repeatable conditions.

---

## Document Structure Terms

### Overview Document
The first file in a module, describing purpose, responsibilities, and integration points.

### Model Document
Defines workflows, algorithms, or conceptual models.

### Safety Document
Describes safety, ethics, and governance integration.

### Observability Document
Defines logs, metrics, and auditing pipelines.

---

