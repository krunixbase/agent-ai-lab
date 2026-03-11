```mermaid
flowchart TD

    A[Interaction Layer] --> B[Cognitive & Planning]
    B --> C[Memory & Knowledge]
    B --> D[Tooling & Execution]
    D --> E[Runtime & Orchestration]
    E --> F[Deployment, Reliability & Performance]
    B --> G[Evaluation, Testing & Meta-learning]
    A --> H[Safety, Ethics & Governance]
    B --> H
    D --> H
    E --> H

    B --> I[Multi-agent]
    E --> I

    C --> J[Cross-layer Architecture]
    D --> J
    E --> J
    H --> J
    F --> J

    B --> K[Embodiment & Simulation]
    E --> K
