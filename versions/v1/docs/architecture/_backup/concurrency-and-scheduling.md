# Concurrency and Scheduling

## Purpose

The Concurrency and Scheduling system controls how tasks are ordered, parallelized, and executed over time. It ensures efficient use of resources while preserving determinism, safety, and predictable behavior.

---

## Scheduling Model

### Scheduling Units
Tasks are the primary units of scheduling. Each task has:

- priority (optional),
- dependencies,
- resource requirements,
- safety constraints.

### Scheduling Policies

- **Sequential** — strict ordering for dependent or safety-critical tasks.
- **Parallel** — concurrent execution for independent tasks.
- **Batch** — grouped execution for similar or low-priority tasks.

Policies can be configured per plan or per environment.

---

## Concurrency Model

- **Task-Level Concurrency** — multiple independent tasks may run in parallel.
- **Resource-Aware Concurrency** — concurrency is limited by resource constraints (e.g., tool limits, environment limits).
- **Safety-Aware Concurrency** — tasks with safety-sensitive operations may be serialized or restricted.

---

## Constraints

- Maximum concurrent tasks.
- Per-tool concurrency limits.
- Timeouts and global execution windows.
- Safety-driven serialization for high-risk operations.

---

## Scheduling Pipeline

1. Identify tasks that are **ready** (dependencies satisfied).
2. Filter tasks based on resource and safety constraints.
3. Apply scheduling policy to select tasks for execution.
4. Dispatch tasks to the Execution Layer.
5. Update task states and re-evaluate readiness.

---

## Integration with Other Systems

- **Execution Plan and Task Model** — provides task metadata and dependencies.
- **Tooling Layer v2** — enforces tool-specific concurrency limits.
- **Safety Architecture** — influences serialization and ordering for sensitive tasks.
- **Observability** — exposes scheduling decisions and concurrency metrics.

---

## Design Principles

- Predictable and explainable scheduling decisions.
- Safety-aware concurrency control.
- Efficient resource utilization.
- Deterministic behavior under the same conditions.

---

## Future Extensions

- Priority-based scheduling.
- Dynamic throttling based on runtime load.
- Adaptive concurrency based on historical performance.

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
