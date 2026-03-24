# agent-ai-lab — Backend Overview

This document describes the backend environment for building AI agents, LLM pipelines, autonomous workflows, and cryptographically verifiable reasoning systems.  
It complements the main architecture documentation located in the root README.md and in the `docs/architecture/` directory.

---

## 🚀 Overview

The backend provides:

- a modular Agent Core  
- LLM pipelines  
- retrieval pipelines (RAG)  
- tool execution  
- memory management  
- FastAPI server  
- deterministic execution foundations  
- cryptographic extension points  

It is designed to be production-ready, testable, and extensible.

---

## 🧱 Architecture (Backend)

```
┌──────────────────────────────────────────────┐
│                  API Layer                   │
│              (FastAPI / server/)             │
└──────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│                Agent Core                    │
│  base_agent.py • memory.py • tools.py        │
│           reasoning.py • planning            │
└──────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│                Pipelines                     │
│   llm_pipeline.py • retrieval_pipeline.py     │
│   embeddings • vector search • RAG            │
└──────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│             External Integrations             │
│  LLM providers • vector DBs • tools • APIs    │
└──────────────────────────────────────────────┘
```

---

## 🌐 API Layer

FastAPI backend exposes:

- `POST /agent/run` — run agent with a prompt  
- `GET /agent/tools` — list available tools  
- `GET /health` — health check  

---

## 🧠 Agent Core

The Agent Core manages:

- reasoning loop  
- planning  
- memory  
- tool execution  
- deterministic execution (optional)  

Core modules:

- `base_agent.py`  
- `memory.py`  
- `tools.py`  
- `reasoning.py`  

---

## 🔌 Pipelines

### LLM Pipeline
Supports:

- OpenAI  
- Anthropic  
- Local models (Ollama, vLLM)  
- structured outputs  
- streaming  

### Retrieval Pipeline
Supports:

- embeddings  
- vector search  
- RAG  
- Pinecone / Chroma / pgvector  

---

## 🐳 Running with Docker

```
bash
docker build -t agent-ai-lab .
docker run -p 8000:8000 agent-ai-lab
```
Backend will be available at:
```
http://localhost:8000
```

---

## 🧪 Running Locally

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

---

## 🔐 Environment Variables

```
cp .env.example .env
```
Fill in your API keys as needed.

---

## 📁 Repository Structure (Backend)

```
server/
agent/
pipelines/
tools/
config/
tests/
```

---

## 🧭 Roadmap (Backend)
- deterministic execution
- plan hashing
- cryptographic signing episodes
- Shamir secret sharing module
- distributed agent workflows
- advanced RAG
- multi-agent workflows
- plugin system for tools

---

## 📄 License

MIT License — see LICENSE.

---

## 📚 Related Documentation
- Full architecture: docs/architecture/
- System design: docs/architecture/system-design/
- Risk model: docs/architecture/risk-model/
- Governance: docs/architecture/governance-model/

