#!/bin/bash

BASE="docs/architecture"
BACKUP="$BASE/_backup"
LOG="$BASE/move2.log"

mkdir -p "$BACKUP"
echo "=== Second Move Log ===" > "$LOG"

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
# Cognitive / Planning
###############################################
for f in \
adaptive-planning-model.md \
meta-reasoning-model.md \
agent-learning-and-improvement-model.md
do
    move "$f" "cognitive-planning"
done

###############################################
# Tooling / Execution
###############################################
for f in \
tool-mastery-observability-and-learning-auditing.md \
execution-observability-and-auditing.md
do
    move "$f" "tooling-execution"
done

###############################################
# Runtime / Orchestration
###############################################
for f in \
agent-orchestration-layer.md \
agent-state-model.md \
recovery-strategies-and-graceful-degradation.md \
agent-debugging-architecture.md
do
    move "$f" "runtime-orchestration"
done

###############################################
# Safety / Ethics / Governance
###############################################
for f in \
llm-safety-architecture.md \
bias-mitigation-and-fairness-framework.md \
policy-definition-and-enforcement-model.md \
oversight-mechanisms-and-human-review.md \
manual-validation-and-human-in-the-loop-review.md
do
    move "$f" "safety-ethics-governance"
done

###############################################
# Evaluation / Testing / Meta-learning
###############################################
for f in \
agent-evaluation-and-metrics-model.md
do
    move "$f" "evaluation-testing-meta-learning"
done

###############################################
# Social Intelligence / Interaction
###############################################
for f in \
dialogue-management-architecture.md \
social-intelligence-and-theory-of-mind-overview.md \
social-intelligence-observability-and-behavior-auditing.md
do
    move "$f" "interaction"
done

###############################################
# Embodiment / Simulation
###############################################
for f in \
embodied-observability-and-safety-auditing.md
do
    move "$f" "embodiment-simulation"
done

###############################################
# Cross-layer
###############################################
for f in \
generative-observability-and-creativity-auditing.md
do
    move "$f" "cross-layer"
done

echo "=== Done. Backup stored in $BACKUP ==="
