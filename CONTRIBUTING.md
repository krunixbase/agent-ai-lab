# Contributing Guidelines

Thank you for your interest in contributing to **Agent AI Lab — System Architecture Documentation**.  
This repository aims to maintain a clean, consistent, and high‑quality architectural knowledge base.  
To keep the structure coherent, please follow the guidelines below.

---

## 1. Repository Structure

All documentation lives under:

docs/architecture/

Each architectural layer has its own folder and its own `README.md`.  
Do not place files outside the appropriate layer unless explicitly required.

---

## 2. Adding New Documents

When adding a new document:

1. Place it in the correct layer directory.
2. Use **kebab-case** for filenames.
3. Add a short description at the top of the file.
4. Update:
   - the layer’s `README.md`
   - the global `INDEX.md`

---

## 3. Writing Standards

- Use **clear, technical English**.
- Prefer **short sections**, **structured headers**, and **lists**.
- Avoid redundancy across documents.
- Keep terminology consistent with existing architecture.
- Include diagrams (Mermaid or textual) when helpful.
- Do not include implementation-specific details — this repo documents architecture, not code.

---

## 4. Versioning & Backups

- Do not delete old documents; move them to `_backup/` if deprecated.
- Add a note in the migration log (`move.log` or `move2.log`) when reorganizing files.

---

## 5. Pull Requests

Each PR should include:

- A clear description of the change.
- Updated references in `INDEX.md`.
- No unrelated formatting changes.
- No broken links.

PRs that modify multiple layers must explain cross-layer impact.

---

## 6. Issues

Use GitHub Issues for:

- Proposing new architectural concepts
- Reporting inconsistencies
- Suggesting improvements
- Requesting clarifications

---

## 7. Style Guide Summary

- English only  
- Kebab-case filenames  
- Markdown only  
- Mermaid diagrams preferred  
- No trailing whitespace  
- No empty placeholder files  

---

Thank you for helping improve the Agent AI Lab architecture!

