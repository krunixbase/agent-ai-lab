# CONTRIBUTING.md

## Introduction

Thank you for your interest in contributing to **agent‑ai‑lab**.  
This repository defines a comprehensive, modular architecture for advanced AI agents.  
To maintain clarity, consistency, and long‑term stability, all contributions must follow the guidelines below.

The goal is to ensure that every new document, module, or architectural extension integrates cleanly into the existing system and remains aligned with safety, governance, and design principles.

## Contribution Principles

### Consistency
All new documents must follow the structure, tone, and formatting conventions used throughout the `docs/architecture` directory. Each architecture module typically consists of:
- 4–5 documents
- Clear section headers
- Commit message + commit description
- English language
- Modular, self‑contained content

### Modularity
Each document must describe a single subsystem, model, or architectural layer.  
Cross‑layer interactions should be referenced but not duplicated.

### Safety & Governance Alignment
All contributions must respect:
- Safety constraints  
- Ethical guidelines  
- Governance and oversight models  
- Privacy and data‑minimization principles  

Architectural changes must not weaken safety guarantees.

### Determinism & Auditability
Architectural descriptions must:
- Define clear boundaries  
- Avoid ambiguity  
- Support traceability and auditing  
- Preserve deterministic behavior across layers  

## Adding a New Architecture Module

1. Create a new folder under `docs/architecture/` using a descriptive name.
2. Add 4–5 Markdown documents covering:
   - Overview  
   - Models and workflows  
   - Safety and governance integration  
   - Observability and auditing  
   - Future extensions  
3. Include a commit message and commit description for each file.
4. Ensure the module integrates with:
   - Interaction  
   - Cognitive & Planning  
   - Memory & Knowledge  
   - Tooling & Execution  
   - Runtime & Orchestration  
   - Safety, Ethics & Governance  
   - Deployment & Performance  
   - Evaluation & Meta‑Learning  
5. Cross‑reference related modules where appropriate.

## Updating an Existing Module

### Minor Updates
Allowed without additional review:
- Typos  
- Clarifications  
- Formatting fixes  
- Non‑breaking wording improvements  

### Major Updates
Require architectural consistency review:
- New sections  
- Changes to workflows  
- Changes to safety or governance logic  
- Cross‑layer dependency changes  
- New responsibilities or capabilities  

Major updates must include:
- Rationale for the change  
- Impact analysis  
- Updated commit message and description  

## File Naming and Structure

- Use lowercase, hyphen‑separated filenames.
- Keep filenames descriptive (e.g., `memory-consolidation-model.md`).
- Avoid abbreviations unless widely understood.
- Each file must begin with a top‑level `#` header matching the filename.

## Writing Standards

### Language
- English only  
- Clear, technical, and concise  
- No marketing language  
- No speculative claims  

### Structure
Each document should include:
- Purpose  
- Responsibilities  
- Workflows  
- Integration points  
- Safety & governance considerations  
- Design principles  
- Future extensions  

### Formatting
- Use Markdown headers (`#`, `##`, `###`)  
- Use lists for clarity  
- Avoid nested lists unless necessary  
- Keep paragraphs short  
- No inline HTML  

## Commit Requirements

Each new document must include:
- A **commit message** summarizing the change  
- A **commit description** explaining the purpose and scope  

Commit messages should follow this pattern:

```
Add <module> defining <key responsibilities or purpose>
```

Commit descriptions should:
- Be 2–5 lines  
- Mention the file path  
- Summarize the content  

## Review Process

1. Validate architectural consistency.
2. Check alignment with safety, ethics, and governance layers.
3. Ensure cross‑layer dependencies are correct.
4. Confirm formatting and naming conventions.
5. Approve or request revisions.

## Roadmap Contributions

Contributors may propose:
- New architecture modules  
- Extensions to existing layers  
- Cross‑layer models  
- Tooling for visualization or analysis  

Proposals should include:
- Motivation  
- High‑level design  
- Expected integration points  
- Safety and governance considerations  

## Questions

If anything in the architecture is unclear or you want guidance on where a new module fits, feel free to open a discussion or issue.
