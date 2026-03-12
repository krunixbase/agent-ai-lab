#!/bin/bash

README="README.md"
ARCH="docs/architecture"

echo "🚀 Starting full documentation update pipeline..."

###############################################
# 0. Backup all files
###############################################

echo "📦 Creating backups..."
cp "$README" "$README.bak"

find "$ARCH" -type f -name "*.md" | while read -r file; do
    cp "$file" "$file.bak"
done

echo "📦 Backups created."


###############################################
# 1. Add TOC to README.md
###############################################

TOC=$(cat << 'EOF'
## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Architecture Diagram](#architecture-overview)
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

sed -i "15a $TOC" "$README"


###############################################
# 2. Add link to INDEX.md
###############################################

INDEX_BLOCK=$(cat << 'EOF'

---

## Full Documentation Index

For a complete list of all architecture documents across all layers, see:

👉 **[Global Architecture Index](docs/architecture/INDEX.md)**

EOF
)

sed -i "/Repository Structure/i $INDEX_BLOCK" "$README"


###############################################
# 3. Add links to README of each layer
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

sed -i "/Goals of the Documentation/i $LAYER_LINKS" "$README"


###############################################
# 4. Add Related Documents section to all .md files
###############################################

RELATED=$(cat << 'EOF'

---

## Related Documents

- [Parent Layer Overview](../README.md)
- [Global Documentation Index](../INDEX.md)
- [Architecture Diagram](../diagram.svg)

EOF
)

echo "🔧 Adding Related Documents section to all .md files..."

find "$ARCH" -type f -name "*.md" | while read -r file; do
    echo "$RELATED" >> "$file"
done


###############################################
# 5. Commit + push
###############################################

echo "📤 Committing changes..."
git add .
git commit -m "Full automated documentation update (TOC, links, related docs)"
git push

echo "🎉 All tasks completed successfully!"
