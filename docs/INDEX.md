# Global Architecture Documentation Index

This index provides a complete, structured overview of all architecture documents in the repository.  
Each section corresponds to one architectural layer and lists all documents contained within it.

---

## 1. Interaction Layer  
Documents describing user intent interpretation, dialogue management, response generation, and interaction safety.

- [conversation-lifecycle.md](interaction/conversation-lifecycle.md)
- [conversation-summarization-model.md](interaction/conversation-summarization-model.md)
- [dialogue-management-architecture.md](interaction/dialogue-management-architecture.md)
- [intent-interpretation-and-goal-formulation.md](interaction/intent-interpretation-and-goal-formulation.md)
- [intent-interpretation-model.md](interaction/intent-interpretation-model.md)
- [interaction-layer-overview.md](interaction/interaction-layer-overview.md)
- [interaction-layer-v2-overview.md](interaction/interaction-layer-v2-overview.md)
- [interaction-observability-and-auditing.md](interaction/interaction-observability-and-auditing.md)
- [interaction-safety-and-boundary-enforcement.md](interaction/interaction-safety-and-boundary-enforcement.md)
- [llm-interaction-model.md](interaction/llm-interaction-model.md)
- [llm-output-schema-specification.md](interaction/llm-output-schema-specification.md)
- [llm-prompt-construction-model.md](interaction/llm-prompt-construction-model.md)
- [perspective-modeling-and-user-state-representation.md](interaction/perspective-modeling-and-user-state-representation.md)
- [response-generation-and-communication-model.md](interaction/response-generation-and-communication-model.md)
- [response-generation-framework.md](interaction/response-generation-framework.md)
- [socially-aware-communication-and-adaptive-dialogue-strategies.md](interaction/socially-aware-communication-and-adaptive-dialogue-strategies.md)
- [social-intelligence-and-theory-of-mind-overview.md](interaction/social-intelligence-and-theory-of-mind-overview.md)
- [social-intelligence-observability-and-behavior-auditing.md](interaction/social-intelligence-observability-and-behavior-auditing.md)
- [user-intent-handling-and-context-management.md](interaction/user-intent-handling-and-context-management.md)

---

## 2. Cognitive & Planning Layer  
Documents covering reasoning, planning, meta‑reasoning, cognitive strategies, and decision‑making.

- [adaptive-planning-model.md](cognitive-planning/adaptive-planning-model.md)
- [agent-learning-and-improvement-model.md](cognitive-planning/agent-learning-and-improvement-model.md)
- [clarification-strategy.md](cognitive-planning/clarification-strategy.md)
- [cognitive-action-selection-and-behavior-control.md](cognitive-planning/cognitive-action-selection-and-behavior-control.md)
- [cognitive-architecture-overview.md](cognitive-planning/cognitive-architecture-overview.md)
- [cognitive-observability-and-meta-reasoning.md](cognitive-planning/cognitive-observability-and-meta-reasoning.md)
- [cognitive-reasoning-and-deliberation-engine.md](cognitive-planning/cognitive-reasoning-and-deliberation-engine.md)
- [creative-synthesis-and-idea-generation-engine.md](cognitive-planning/creative-synthesis-and-idea-generation-engine.md)
- [creativity-and-generative-reasoning-overview.md](cognitive-planning/creativity-and-generative-reasoning-overview.md)
- [generative-reasoning-modes-and-cognitive-strategies.md](cognitive-planning/generative-reasoning-modes-and-cognitive-strategies.md)
- [long-horizon-reasoning-model.md](cognitive-planning/long-horizon-reasoning-model.md)
- [meta-reasoning-model.md](cognitive-planning/meta-reasoning-model.md)
- [planner-decision-model.md](cognitive-planning/planner-decision-model.md)
- [planner-llm-interaction-protocol.md](cognitive-planning/planner-llm-interaction-protocol.md)
- [planning-and-reasoning-overview.md](cognitive-planning/planning-and-reasoning-overview.md)
- [planning-architecture.md](cognitive-planning/planning-architecture.md)
- [planning-engine-and-plan-generation.md](cognitive-planning/planning-engine-and-plan-generation.md)
- [planning-observability-and-auditing.md](cognitive-planning/planning-observability-and-auditing.md)
- [proactivity-and-initiative-model.md](cognitive-planning/proactivity-and-initiative-model.md)
- [reasoning-and-planning-optimization.md](cognitive-planning/reasoning-and-planning-optimization.md)
- [reasoning-model-and-multi-step-reasoning.md](cognitive-planning/reasoning-model-and-multi-step-reasoning.md)
- [reasoning-trace-model.md](cognitive-planning/reasoning-trace-model.md)

---

## 3. Memory & Knowledge Layer  
Documents describing memory systems, retrieval pipelines, knowledge representation, and memory safety.

- [episodic-memory-architecture.md](memory-knowledge/episodic-memory-architecture.md)
- [knowledge-and-retrieval-overview.md](memory-knowledge/knowledge-and-retrieval-overview.md)
- [knowledge-grounding-and-reasoning-integration.md](memory-knowledge/knowledge-grounding-and-reasoning-integration.md)
- [knowledge-integration-model.md](memory-knowledge/knowledge-integration-model.md)
- [knowledge-observability-and-auditing.md](memory-knowledge/knowledge-observability-and-auditing.md)
- [knowledge-representation-and-normalization.md](memory-knowledge/knowledge-representation-and-normalization.md)
- [memory-architecture-v2-overview.md](memory-knowledge/memory-architecture-v2-overview.md)
- [memory-architecture.md](memory-knowledge/memory-architecture.md)
- [memory-consolidation-and-lifecycle.md](memory-knowledge/memory-consolidation-and-lifecycle.md)
- [memory-consolidation-model.md](memory-knowledge/memory-consolidation-model.md)
- [memory-observability-and-auditing.md](memory-knowledge/memory-observability-and-auditing.md)
- [memory-retrieval-model.md](memory-knowledge/memory-retrieval-model.md)
- [memory-safety-and-privacy-guardrails.md](memory-knowledge/memory-safety-and-privacy-guardrails.md)
- [memory-safety-model.md](memory-knowledge/memory-safety-model.md)
- [memory-storage-and-retrieval-model.md](memory-knowledge/memory-storage-and-retrieval-model.md)
- [retrieval-and-memory-performance.md](memory-knowledge/retrieval-and-memory-performance.md)
- [retrieval-pipeline-and-ranking-model.md](memory-knowledge/retrieval-pipeline-and-ranking-model.md)
- [summary-memory-architecture.md](memory-knowledge/summary-memory-architecture.md)
- [vector-memory-architecture.md](memory-knowledge/vector-memory-architecture.md)

---

## 4. Tooling & Execution Layer  
Documents defining tool APIs, execution flow, validation, sequencing, and tool‑related observability.

- [tool-api-specification.md](tooling-execution/tool-api-specification.md)
- [tool-capability-taxonomy.md](tooling-execution/tool-capability-taxonomy.md)
- [tool-execution-and-orchestration.md](tooling-execution/tool-execution-and-orchestration.md)
- [tool-execution-flow.md](tooling-execution/tool-execution-flow.md)
- [tool-execution-lifecycle.md](tooling-execution/tool-execution-lifecycle.md)
- [tool-mastery-observability-and-learning-auditing.md](tooling-execution/tool-mastery-observability-and-learning-auditing.md)
- [tool-metadata-specification.md](tooling-execution/tool-metadata-specification.md)
- [tool-registry-and-capabilities.md](tooling-execution/tool-registry-and-capabilities.md)
- [tool-registry-architecture.md](tooling-execution/tool-registry-architecture.md)
- [tool-selection-and-validation.md](tooling-execution/tool-selection-and-validation.md)
- [tool-sequencing-composition-and-fallback-learning.md](tooling-execution/tool-sequencing-composition-and-fallback-learning.md)
- [tool-strategy-learning-and-adaptive-selection.md](tooling-execution/tool-strategy-learning-and-adaptive-selection.md)
- [tool-use-learning-and-adaptive-mastery-overview.md](tooling-execution/tool-use-learning-and-adaptive-mastery-overview.md)
- [tool-use-observation-and-outcome-model.md](tooling-execution/tool-use-observation-and-outcome-model.md)
- [tooling-layer-overview.md](tooling-execution/tooling-layer-overview.md)
- [tooling-observability-and-auditing.md](tooling-execution/tooling-observability-and-auditing.md)

---

## 5. Runtime & Orchestration Layer  
Documents covering execution loops, scheduling, concurrency, error handling, and runtime observability.

- [agent-orchestration-layer.md](runtime-orchestration/agent-orchestration-layer.md)
- [agent-state-model.md](runtime-orchestration/agent-state-model.md)
- [agent-debugging-architecture.md](runtime-orchestration/agent-debugging-architecture.md)
- [agent-runtime-architecture.md](runtime-orchestration/agent-runtime-architecture.md)
- [agent-runtime-loop.md](runtime-orchestration/agent-runtime-loop.md)
- [agent-runtime-overview.md](runtime-orchestration/agent-runtime-overview.md)
- [async-task-scheduler.md](runtime-orchestration/async-task-scheduler.md)
- [concurrency-and-scheduling.md](runtime-orchestration/concurrency-and-scheduling.md)
- [error-handling-architecture.md](runtime-orchestration/error-handling-architecture.md)
- [error-recovery-model.md](runtime-orchestration/error-recovery-model.md)
- [execution-and-runtime-performance.md](runtime-orchestration/execution-and-runtime-performance.md)
- [execution-error-handling-and-retries.md](runtime-orchestration/execution-error-handling-and-retries.md)
- [execution-layer-overview.md](runtime-orchestration/execution-layer-overview.md)
- [execution-observability-and-auditing.md](runtime-orchestration/execution-observability-and-auditing.md)
- [execution-plan-and-task-model.md](runtime-orchestration/execution-plan-and-task-model.md)
- [failure-detection-and-diagnostics.md](runtime-orchestration/failure-detection-and-diagnostics.md)
- [recovery-strategies-and-graceful-degradation.md](runtime-orchestration/recovery-strategies-and-graceful-degradation.md)
- [runtime-coordination-and-orchestration.md](runtime-orchestration/runtime-coordination-and-orchestration.md)
- [runtime-lifecycle-and-state-management.md](runtime-orchestration/runtime-lifecycle-and-state-management.md)
- [runtime-observability-and-auditing.md](runtime-orchestration/runtime-observability-and-auditing.md)
- [runtime-safety-and-policy-enforcement.md](runtime-orchestration/runtime-safety-and-policy-enforcement.md)
- [turn-execution-model.md](runtime-orchestration/turn-execution-model.md)

---

## 6. Safety, Ethics & Governance Layer  
Documents defining safety constraints, ethical guidelines, compliance, and governance mechanisms.

- [bias-mitigation-and-fairness-framework.md](safety-ethics-governance/bias-mitigation-and-fairness-framework.md)
- [compliance-management-and-regulatory-alignment.md](safety-ethics-governance/compliance-management-and-regulatory-alignment.md)
- [data-security-and-access-control.md](safety-ethics-governance/data-security-and-access-control.md)
- [ethical-observability-and-responsibility-auditing.md](safety-ethics-governance/ethical-observability-and-responsibility-auditing.md)
- [ethical-principles-and-behavioral-guidelines.md](safety-ethics-governance/ethical-principles-and-behavioral-guidelines.md)
- [ethics-and-responsible-ai-overview.md](safety-ethics-governance/ethics-and-responsible-ai-overview.md)
- [generative-constraints-safety-and-ethical-boundaries.md](safety-ethics-governance/generative-constraints-safety-and-ethical-boundaries.md)
- [governance-and-oversight-overview.md](safety-ethics-governance/governance-and-oversight-overview.md)
- [governance-observability-and-auditability.md](safety-ethics-governance/governance-observability-and-auditability.md)
- [governance-policies-and-decision-frameworks.md](safety-ethics-governance/governance-policies-and-decision-frameworks.md)
- [governance-risk-management-and-escalation.md](safety-ethics-governance/governance-risk-management-and-escalation.md)
- [llm-safety-architecture.md](safety-ethics-governance/llm-safety-architecture.md)
- [manual-validation-and-human-in-the-loop-review.md](safety-ethics-governance/manual-validation-and-human-in-the-loop-review.md)
- [oversight-mechanisms-and-human-review.md](safety-ethics-governance/oversight-mechanisms-and-human-review.md)
- [policy-definition-and-enforcement-model.md](safety-ethics-governance/policy-definition-and-enforcement-model.md)
- [safety-architecture-overview.md](safety-ethics-governance/safety-architecture-overview.md)
- [safety-escalation-and-fallbacks.md](safety-ethics-governance/safety-escalation-and-fallbacks.md)
- [safety-evaluation-and-auditing.md](safety-ethics-governance/safety-evaluation-and-auditing.md)
- [safety-event-pipeline.md](safety-ethics-governance/safety-event-pipeline.md)
- [safety-filtering-and-redaction.md](safety-ethics-governance/safety-filtering-and-redaction.md)
- [safety-policy-enforcement-model.md](safety-ethics-governance/safety-policy-enforcement-model.md)
- [security-and-compliance-overview.md](safety-ethics-governance/security-and-compliance-overview.md)
- [security-and-privacy-architecture.md](safety-ethics-governance/security-and-privacy-architecture.md)
- [security-observability-and-auditing.md](safety-ethics-governance/security-observability-and-auditing.md)
- [threat-detection-and-incident-response.md](safety-ethics-governance/threat-detection-and-incident-response.md)

---

## 7. Deployment, Reliability & Performance Layer  
Documents covering deployment models, scaling, environment configuration, reliability engineering, and performance optimization.

- [deployment-and-environment-overview.md](deployment-reliability-performance/deployment-and-environment-overview.md)
- [deployment-models-and-scaling-strategies.md](deployment-reliability-performance/deployment-models-and-scaling-strategies.md)
- [deployment-observability-and-auditing.md](deployment-reliability-performance/deployment-observability-and-auditing.md)
- [deployment-safety-and-isolation-model.md](deployment-reliability-performance/deployment-safety-and-isolation-model.md)
- [environment-configuration-and-capability-detection.md](deployment-reliability-performance/environment-configuration-and-capability-detection.md)
- [environment-modeling-and-virtual-world-construction.md](deployment-reliability-performance/environment-modeling-and-virtual-world-construction.md)
- [environment-profiles-and-operational-modes.md](deployment-reliability-performance/environment-profiles-and-operational-modes.md)
- [performance-observability-and-adaptive-tuning.md](deployment-reliability-performance/performance-observability-and-adaptive-tuning.md)
- [performance-optimization-model.md](deployment-reliability-performance/performance-optimization-model.md)
- [performance-optimization-overview.md](deployment-reliability-performance/performance-optimization-overview.md)
- [reliability-and-fault-tolerance-overview.md](deployment-reliability-performance/reliability-and-fault-tolerance-overview.md)
- [reliability-in-distributed-and-multi-environment-deployments.md](deployment-reliability-performance/reliability-in-distributed-and-multi-environment-deployments.md)
- [reliability-observability-and-resilience-auditing.md](deployment-reliability-performance/reliability-observability-and-resilience-auditing.md)

---

## 9. Multi-agent Layer  
Documents describing multi-agent coordination, communication, safety, and governance.

- [distributed-task-allocation-and-coordination.md](multi-agent/distributed-task-allocation-and-coordination.md)
- [inter-agent-communication-and-protocols.md](multi-agent/inter-agent-communication-and-protocols.md)
- [multi-agent-coordination-model.md](multi-agent/multi-agent-coordination-model.md)
- [multi-agent-coordination-overview.md](multi-agent/multi-agent-coordination-overview.md)
- [multi-agent-observability-and-coordination-auditing.md](multi-agent/multi-agent-observability-and-coordination-auditing.md)
- [multi-agent-safety-ethics-and-governance.md](multi-agent/multi-agent-safety-ethics-and-governance.md)
- [multi-party-interaction-and-role-aware-coordination.md](multi-agent/multi-party-interaction-and-role-aware-coordination.md)

---

## 10. Embodiment & Simulation Layer  
Documents describing embodied agents, perception, motor control, simulation environments, and sensorimotor learning.

- [agent-behavior-in-simulated-environments.md](embodiment-simulation/agent-behavior-in-simulated-environments.md)
- [embodied-and-sensorimotor-overview.md](embodiment-simulation/embodied-and-sensorimotor-overview.md)
- [embodied-observability-and-safety-auditing.md](embodiment-simulation/embodied-observability-and-safety-auditing.md)
- [motor-control-and-action-execution.md](embodiment-simulation/motor-control-and-action-execution.md)
- [multimodal-perception-and-environment-modeling.md](embodiment-simulation/multimodal-perception-and-environment-modeling.md)
- [perception-and-internal-representation-model.md](embodiment-simulation/perception-and-internal-representation-model.md)
- [sensorimotor-learning-and-adaptation.md](embodiment-simulation/sensorimotor-learning-and-adaptation.md)
- [simulation-and-virtual-environment-overview.md](embodiment-simulation/simulation-and-virtual-environment-overview.md)
- [simulation-engine-and-dynamics-framework.md](embodiment-simulation/simulation-engine-and-dynamics-framework.md)
- [simulation-environment-model.md](embodiment-simulation/simulation-environment-model.md)
- [simulation-observability-and-environment-auditing.md](embodiment-simulation/simulation-observability-and-environment-auditing.md)

---

## 11. Cross-layer Architecture  
Documents describing global mechanisms such as configuration, versioning, lifecycle management, and system-wide observability.

- [agent-capability-model.md](cross-layer/agent-capability-model.md)
- [agent-configuration-and-policy-overview.md](cross-layer/agent-configuration-and-policy-overview.md)
- [agent-configuration-model.md](cross-layer/agent-configuration-model.md)
- [agent-initialization-flow.md](cross-layer/agent-initialization-flow.md)
- [agent-lifecycle-and-version-management-overview.md](cross-layer/agent-lifecycle-and-version-management-overview.md)
- [architecture-observability-mapping-and-impact-analysis.md](cross-layer/architecture-observability-mapping-and-impact-analysis.md)
- [configuration-model-and-versioning.md](cross-layer/configuration-model-and-versioning.md)
- [configuration-observability-and-auditing.md](cross-layer/configuration-observability-and-auditing.md)
- [context-window-management-model.md](cross-layer/context-window-management-model.md)
- [cross-layer-dependency-and-contract-model.md](cross-layer/cross-layer-dependency-and-contract-model.md)
- [end-to-end-agent-lifecycle-and-scenario-flows.md](cross-layer/end-to-end-agent-lifecycle-and-scenario-flows.md)
- [generative-observability-and-creativity-auditing.md](cross-layer/generative-observability-and-creativity-auditing.md)
- [global-layer-stack-and-control-flow.md](cross-layer/global-layer-stack-and-control-flow.md)
- [lifecycle-observability-and-version-auditing.md](cross-layer/lifecycle-observability-and-version-auditing.md)
- [observability-and-logging-model.md](cross-layer/observability-and-logging-model.md)
- [rollback-recovery-and-version-reversal.md](cross-layer/rollback-recovery-and-version-reversal.md)
- [rollout-strategies-and-controlled-deployment.md](cross-layer/rollout-strategies-and-controlled-deployment.md)
- [session-boundary-detection-model.md](cross-layer/session-boundary-detection-model.md)
- [session-persistence-model.md](cross-layer/session-persistence-model.md)
- [trace-inspection-model.md](cross-layer/trace-inspection-model.md)
- [transparency-explainability-and-user-trust.md](cross-layer/transparency-explainability-and-user-trust.md)
- [unified-architecture-map-and-cross-layer-dependencies-overview.md](cross-layer/unified-architecture-map-and-cross-layer-dependencies-overview.md)
- [versioning-model-and-component-tracking.md](cross-layer/versioning-model-and-component-tracking.md)

---

## 12. Backup & Migration Logs  
Historical backups and migration logs preserved for traceability.

- [_backup/](../_backup/)
- [move.log](../move.log)
- [move2.log](../move2.log)
