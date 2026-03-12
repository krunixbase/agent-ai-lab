#!/bin/bash

README="README.md"

echo "🚀 Updating README.md..."

###############################################
# 1. Add TOC under badges (po liniach z obrazkami)
###############################################

TOC=$(cat << 'EOF'
## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Repository Structure](#repository-structure)
- [Goals of the Documentation](#goals-of-the-documentation)
- [Migration Notes](#migration-notes)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Full Documentation Index](#full-documentation-index)
- [Layer Documentation](#layer-documentation)

EOF
)

awk -v toc="$TOC" '
/!

\[License\]

\(https:\/\/img.shields.io\/badge\/license-MIT-blue.svg\)/ {
  print;
  print "";
  print toc;
  next;
}
{ print }
' "$README" > README.tmp && mv README.tmp "$README"

###############################################
# 2. Add Full Documentation Index before "## Repository Structure"
###############################################

INDEX_BLOCK=$(cat << 'EOF'

---

## Full Documentation Index

For a complete list of all architecture documents across all layers, see:

👉 **[Global Architecture Index](docs/architecture/INDEX.md)**

EOF
)

awk -v block="$INDEX_BLOCK" '
/## Repository Structure/ {
  print block;
  print;
  next;
}
{ print }
' "$README" > README.tmp && mv README.tmp "$README"

###############################################
# 3. Add Layer Documentation before "## Goals of the Documentation"
###############################################

LAYER_LINKS=$(cat << 'EOF'

---

## Layer Documentation

- **Interaction Layer**  
  docs/architecture/interaction/README.md

- **Cognitive & Planning Layer**  
  docs/architecture/cognitive-planning/README.md

- **Memory & Knowledge Layer**  
  docs/architecture/memory-knowledge/README.md

- **Tooling & Execution Layer**  
  docs/architecture/tooling-execution/README.md

- **Runtime & Orchestration Layer**  
  docs/architecture/runtime-orchestration/README.md

- **Safety, Ethics & Governance Layer**  
  docs/architecture/safety-ethics-governance/README.md

- **Deployment, Reliability & Performance Layer**  
  docs/architecture/deployment-reliability-performance/README.md

- **Evaluation, Testing & Meta-learning Layer**  
  docs/architecture/evaluation-testing-meta-learning/README.md

- **Multi-agent Layer**  
  docs/architecture/multi-agent/README.md

- **Embodiment & Simulation Layer**  
  docs/architecture/embodiment-simulation/README.md

- **Cross-layer Architecture**  
  docs/architecture/cross-layer/README.md

- **Backup & Migration Logs**  
  docs/architecture/_backup/

EOF
)

awk -v block="$LAYER_LINKS" '
/## Goals of the Documentation/ {
  print block;
  print;
  next;
}
{ print }
' "$README" > README.tmp && mv README.tmp "$README"

###############################################
# 4. Commit + push
###############################################

echo "📤 Committing changes..."
git add README.md
git commit -m "Add TOC, index link, and layer documentation links to README"
git push

echo "🎉 README update complete!"
