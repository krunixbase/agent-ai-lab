#!/bin/bash

set -e

echo "=============================================="
echo " Agent AI Lab — Update README + Add Diagrams"
echo "=============================================="
echo ""

###############################################
# 1. Create assets directory
###############################################

echo "[1/5] Ensuring assets/ directory exists..."
mkdir -p assets
echo "✔ assets/ ready"
echo ""

###############################################
# 2. Backup existing README.md
###############################################

echo "[2/5] Backing up existing README.md..."
if [ -f README.md ]; then
    cp README.md README.md.bak
    echo "✔ README.md backed up as README.md.bak"
else
    echo "⚠ README.md not found — creating a new one"
fi
echo ""

###############################################
# 3. Create SVG diagrams
###############################################

echo "[3/5] Creating SVG diagrams..."

# Banner
cat << 'EOF' > assets/readme_banner.svg
<svg width="1200" height="250" xmlns="http://www.w3.org/2000/svg">
  <rect width="1200" height="250" fill="#1a1a1a"/>
  <text x="600" y="130" font-size="48" fill="#ffffff" text-anchor="middle" font-family="Arial">
    Agent AI Lab — System Architecture
  </text>
</svg>
EOF

# Runtime loop
cat << 'EOF' > assets/runtime_loop.svg
<svg width="900" height="500" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="500" fill="#f5f5f5"/>
  <text x="450" y="40" font-size="28" text-anchor="middle">Runtime Loop — Agent AI Lab</text>

  <g font-size="16">
    <rect x="50" y="100" width="200" height="60" fill="#d9eaff" stroke="#000"/>
    <text x="150" y="135" text-anchor="middle">Input / Observation</text>

    <rect x="350" y="100" width="200" height="60" fill="#ffe6cc" stroke="#000"/>
    <text x="450" y="135" text-anchor="middle">Cognition / Reasoning</text>

    <rect x="650" y="100" width="200" height="60" fill="#e6ffd9" stroke="#000"/>
    <text x="750" y="135" text-anchor="middle">Planning</text>

    <rect x="350" y="250" width="200" height="60" fill="#fff2cc" stroke="#000"/>
    <text x="450" y="285" text-anchor="middle">Tool Execution</text>

    <rect x="50" y="250" width="200" height="60" fill="#ffd9d9" stroke="#000"/>
    <text x="150" y="285" text-anchor="middle">Memory Update</text>

    <rect x="650" y="250" width="200" height="60" fill="#e6e6ff" stroke="#000"/>
    <text x="750" y="285" text-anchor="middle">Output / Action</text>

    <line x1="250" y1="130" x2="350" y2="130" stroke="#000" marker-end="url(#arrow)"/>
    <line x1="550" y1="130" x2="650" y2="130" stroke="#000" marker-end="url(#arrow)"/>
    <line x1="750" y1="160" x2="750" y2="250" stroke="#000" marker-end="url(#arrow)"/>
    <line x1="450" y1="160" x2="450" y2="250" stroke="#000" marker-end="url(#arrow)"/>
    <line x1="250" y1="280" x2="350" y2="280" stroke="#000" marker-end="url(#arrow)"/>
    <line x1="150" y1="250" x2="150" y2="160" stroke="#000" marker-end="url(#arrow)"/>
  </g>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#000"/>
    </marker>
  </defs>
</svg>
EOF

# Memory architecture
cat << 'EOF' > assets/memory_architecture.svg
<svg width="900" height="500" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="500" fill="#fafafa"/>
  <text x="450" y="40" font-size="28" text-anchor="middle">Memory Architecture — Agent AI Lab</text>

  <g font-size="16">
    <rect x="100" y="120" width="250" height="80" fill="#e6f7ff" stroke="#000"/>
    <text x="225" y="165" text-anchor="middle">Episodic Memory</text>

    <rect x="550" y="120" width="250" height="80" fill="#fff0f6" stroke="#000"/>
    <text x="675" y="165" text-anchor="middle">Semantic Memory</text>

    <rect x="100" y="300" width="250" height="80" fill="#f9f0ff" stroke="#000"/>
    <text x="225" y="345" text-anchor="middle">Vector Memory</text>

    <rect x="550" y="300" width="250" height="80" fill="#f6ffed" stroke="#000"/>
    <text x="675" y="345" text-anchor="middle">Long-term Knowledge</text>

    <line x1="225" y1="200" x2="225" y2="300" stroke="#000" marker-end="url(#arrow)"/>
    <line x1="675" y1="200" x2="675" y2="300" stroke="#000" marker-end="url(#arrow)"/>
  </g>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#000"/>
    </marker>
  </defs>
</svg>
EOF

echo "✔ SVG diagrams created"
echo ""

###############################################
# 4. Generate new README.md (English)
###############################################

echo "[4/5] Writing new README.md..."

cat << 'EOF' > README.md
<p align="center">
  <img src="assets/readme_banner.svg" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/krunixbase/agent-ai-lab/ci.yml" />
  <img src="https://img.shields.io/badge/docs-complete-brightgreen" />
  <img src="https://img.shields.io/badge/version-v1.0.0-blue" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
</p>

# Agent AI Lab — System Architecture Documentation

A comprehensive, modular, and deeply structured documentation set describing the full architecture of an advanced AI agent system. The goal of the project is to provide a clear, layered, and extensible blueprint for building, evaluating, and deploying intelligent agents capable of reasoning, interacting, learning, and acting safely in complex environments.

The documentation is organized into twelve architectural layers, each representing a major subsystem of the agent. Every layer includes conceptual overviews, detailed specifications, observability models, safety considerations, and cross‑layer dependencies.

---

## Status Overview

| Category | Status |
|---------|--------|
| Architecture Docs | Complete (v1 snapshot available) |
| Backend | In development |
| Last Commit | See GitHub |
| Issues | Open |
| License | MIT |
| Version | v1.0.0 |
| Release | Planned |

---

## Quick Links

- **Architecture Overview** → `ARCHITECTURE.md`
- **Architecture Diagram** → `ARCHITECTURE_DIAGRAM.md`
- **Documentation Index** → `INDEX.md`
- **System Design** → `SYSTEM_DESIGN.md`
- **Glossary** → `GLOSSARY.md`
- **Governance Model** → `GOVERNANCE_MODEL.md`
- **Risk Model** → `RISK_MODEL.md`
- **Security Model** → `SECURITY_MODEL.md`
- **Roadmap** → `ROADMAP.md`
- **Contributing Guide** → `CONTRIBUTING.md`

---

## Architecture Overview

The system is divided into **twelve major layers**, covering the full lifecycle of an intelligent agent:

1. Interaction Layer  
2. Cognitive & Planning Layer  
3. Memory & Knowledge Layer  
4. Tooling & Execution Layer  
5. Runtime & Orchestration Layer  
6. Safety, Ethics & Governance Layer  
7. Deployment, Reliability & Performance Layer  
8. Evaluation, Testing & Meta‑learning Layer  
9. Multi‑agent Layer  
10. Embodiment & Simulation Layer  
11. Cross‑layer Architecture  
12. Backup & Migration Logs  

Each layer is located under:

