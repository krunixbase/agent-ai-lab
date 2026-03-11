#!/bin/bash

BASE="docs/architecture"
BACKUP="$BASE/_backup"
LOG="$BASE/move.log"

mkdir -p "$BACKUP"
echo "=== File Move Log ===" > "$LOG"

move() {
    FILE="$1"
    TARGET="$2"

    if [ -f "$BASE/$FILE" ]; then
        mkdir -p "$BASE/$TARGET"
        echo "Moving $FILE → $TARGET" | tee -a "$LOG"
        cp "$BASE/$FILE" "$BACKUP/$FILE"
        mv "$BASE/$FILE" "$BASE/$TARGET/"
    else
        echo "Skipping $FILE (not found)" | tee -a "$LOG"
    fi
}

###############################################
# Interaction Layer
###############################################
for f in \
interaction-layer-overview.md \
interaction-layer-v2-overview.md \
interaction-observability-and-auditing.md \
interaction-safety-and-boundary-enforcement.md \
conversation-lifecycle.md \
conversation-summarization-model.md \
llm-interaction-model.md \
llm-output-schema-specification.md \
llm-prompt-construction-model.md \
response-generation-framework.md \
response-generation-and-communication-model.md \
socially-aware-communication-and-adaptive-dialogue-strategies.md \
perspective-modeling-and-user-state-representation.md \
user-intent-handling-and-context-management.md \
intent-interpretation-model.md \
intent-interpretation-and-goal-formulation.md
do
    move "$f" "interaction"
done

###############################################
# Cognitive & Planning Layer
###############################################
for f in \
cognitive-architecture-overview.md \
cognitive-reasoning-and-deliberation-engine.md \
cognitive-action-selection-and-behavior-control.md \
cognitive-observability-and-meta-reasoning.md \
reasoning-model-and-multi-step-reasoning.md \
reasoning-trace-model.md \
long-horizon-reasoning-model.md \
generative-reasoning-modes-and-cognitive-strategies.md \
creative-synthesis-and-idea-generation-engine.md \
creativity-and-generative-reasoning-overview.md \
planner-decision-model.md \
planner-llm-interaction-protocol.md \
planning-and-reasoning-overview.md \
planning-architecture.md \
planning-engine-and-plan-generation.md \
planning-observability-and-auditing.md \
reasoning-and-planning-optimization.md \
clarification-strategy.md \
proactivity-and-initiative-model.md
do
    move "$f" "cognitive-planning"
done

###############################################
# Memory & Knowledge Layer
###############################################
for f in \
memory-architecture.md \
memory-architecture-v2-overview.md \
episodic-memory-architecture.md \
summary-memory-architecture.md \
memory-consolidation-model.md \
memory-consolidation-and-lifecycle.md \
memory-storage-and-retrieval-model.md \
memory-retrieval-model.md \
vector-memory-architecture.md \
retrieval-and-memory-performance.md \
retrieval-pipeline-and-ranking-model.md \
memory-safety-model.md \
memory-safety-and-privacy-guardrails.md \
memory-observability-and-auditing.md \
knowledge-and-retrieval-overview.md \
knowledge-representation-and-normalization.md \
knowledge-integration-model.md \
knowledge-grounding-and-reasoning-integration.md \
knowledge-observability-and-auditing.md
do
    move "$f" "memory-knowledge"
done

###############################################
# Tooling & Execution Layer
###############################################
for f in \
tool-api-specification.md \
tool-capability-taxonomy.md \
tool-registry-and-capabilities.md \
tool-registry-architecture.md \
tool-selection-and-validation.md \
tool-execution-flow.md \
tool-execution-lifecycle.md \
tool-execution-and-orchestration.md \
tool-sequencing-composition-and-fallback-learning.md \
tool-strategy-learning-and-adaptive-selection.md \
tool-use-learning-and-adaptive-mastery-overview.md \
tool-use-observation-and-outcome-model.md \
tool-metadata-specification.md \
tooling-layer-overview.md \
tooling-observability-and-auditing.md
do
    move "$f" "tooling-execution"
done

###############################################
# Runtime & Orchestration Layer
###############################################
for f in \
agent-runtime-overview.md \
agent-runtime-architecture.md \
agent-runtime-loop.md \
agent-loop.md \
runtime-coordination-and-orchestration.md \
runtime-lifecycle-and-state-management.md \
runtime-safety-and-policy-enforcement.md \
runtime-observability-and-auditing.md \
async-task-scheduler.md \
concurrency-and-scheduling.md \
execution-layer-overview.md \
execution-plan-and-task-model.md \
execution-error-handling-and-retries.md \
execution-and-runtime-performance.md \
error-handling-architecture.md \
error-recovery-model.md \
failure-detection-and-diagnostics.md \
turn-execution-model.md
do
    move "$f" "runtime-orchestration"
done

###############################################
# Safety, Ethics & Governance Layer
###############################################
for f in \
safety-architecture-overview.md \
safety-filtering-and-redaction.md \
safety-escalation-and-fallbacks.md \
safety-event-pipeline.md \
safety-policy-enforcement-model.md \
safety-evaluation-and-auditing.md \
generative-constraints-safety-and-ethical-boundaries.md \
ethical-principles-and-behavioral-guidelines.md \
ethics-and-responsible-ai-overview.md \
ethical-observability-and-responsibility-auditing.md \
governance-and-oversight-overview.md \
governance-policies-and-decision-frameworks.md \
governance-risk-management-and-escalation.md \
governance-observability-and-auditability.md \
compliance-management-and-regulatory-alignment.md \
data-security-and-access-control.md \
security-and-privacy-architecture.md \
security-and-compliance-overview.md \
security-observability-and-auditing.md \
threat-detection-and-incident-response.md
do
    move "$f" "safety-ethics-governance"
done

###############################################
# Deployment, Reliability & Performance Layer
###############################################
for f in \
deployment-and-environment-overview.md \
deployment-models-and-scaling-strategies.md \
deployment-observability-and-auditing.md \
deployment-safety-and-isolation-model.md \
environment-configuration-and-capability-detection.md \
environment-modeling-and-virtual-world-construction.md \
environment-profiles-and-operational-modes.md \
reliability-and-fault-tolerance-overview.md \
reliability-in-distributed-and-multi-environment-deployments.md \
reliability-observability-and-resilience-auditing.md \
performance-observability-and-adaptive-tuning.md \
performance-optimization-model.md \
performance-optimization-overview.md \
execution-and-runtime-performance.md
do
    move "$f" "deployment-reliability-performance"
done

###############################################
# Evaluation, Testing & Meta-Learning Layer
###############################################
for f in \
evaluation-framework-overview.md \
evaluation-metrics-and-quality-dimensions.md \
evaluation-observability-and-reporting.md \
evaluation-pipeline-and-regression-detection.md \
automated-testing-pipeline-and-tooling.md \
benchmarking-suites-and-test-scenarios.md \
test-suite-architecture.md \
test-suite-architecture-and-scenario-design.md \
testing-and-validation-overview.md \
testing-observability-and-quality-reporting.md \
meta-learning-and-self-optimization-overview.md \
meta-learning-observability-and-optimization-auditing.md \
meta-learning-strategies-and-adaptation-model.md \
self-evaluation-and-reflection-model.md \
self-observation-and-performance-monitoring.md \
self-optimization-policies-and-boundary-controls.md \
risk-detection-and-mitigation.md
do
    move "$f" "evaluation-testing-meta-learning"
done

###############################################
# Multi-Agent Layer
###############################################
for f in \
multi-agent-coordination-model.md \
multi-agent-coordination-overview.md \
multi-agent-observability-and-coordination-auditing.md \
multi-agent-safety-ethics-and-governance.md \
inter-agent-communication-and-protocols.md \
multi-party-interaction-and-role-aware-coordination.md \
distributed-task-allocation-and-coordination.md
do
    move "$f" "multi-agent"
done

###############################################
# Embodiment & Simulation Layer
###############################################
for f in \
embodied-and-sensorimotor-overview.md \
sensorimotor-learning-and-adaptation.md \
motor-control-and-action-execution.md \
simulation-and-virtual-environment-overview.md \
simulation-engine-and-dynamics-framework.md \
simulation-environment-model.md \
simulation-observability-and-environment-auditing.md \
multimodal-perception-and-environment-modeling.md \
perception-and-internal-representation-model.md \
agent-behavior-in-simulated-environments.md
do
    move "$f" "embodiment-simulation"
done

###############################################
# Cross-Layer
###############################################
for f in \
cross-layer-dependency-and-contract-model.md \
unified-architecture-map-and-cross-layer-dependencies-overview.md \
architecture-observability-mapping-and-impact-analysis.md \
global-layer-stack-and-control-flow.md \
configuration-model-and-versioning.md \
configuration-observability-and-auditing.md \
lifecycle-observability-and-version-auditing.md \
agent-lifecycle-and-version-management-overview.md \
agent-configuration-model.md \
agent-configuration-and-policy-overview.md \
agent-capability-model.md \
agent-initialization-flow.md \
end-to-end-agent-lifecycle-and-scenario-flows.md \
rollback-recovery-and-version-reversal.md \
rollout-strategies-and-controlled-deployment.md \
observability-and-logging-model.md \
transparency-explainability-and-user-trust.md \
session-boundary-detection-model.md \
session-persistence-model.md \
context-window-management-model.md \
turn-execution-model.md \
trace-inspection-model.md \
versioning-model-and-component-tracking.md
do
    move "$f" "cross-layer"
done

echo "=== Done. Backup stored in $BACKUP ==="
