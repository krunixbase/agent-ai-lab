# agent-ai-lab

A modular, extensible framework for building AI agents with reasoning, planning, tool execution, and memory.  
Designed for experimentation, research, and production‑grade agent architectures.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg)
![LLM](https://img.shields.io/badge/LLM-Agents-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

---

## Overview

**agent-ai-lab** provides a clean foundation for experimenting with AI agents powered by LLMs.  
The project focuses on:

- structured reasoning loops  
- LLM-based planning  
- tool calling and execution  
- memory systems  
- modular pipelines  
- FastAPI server for agent interaction  

The goal is to create a transparent, debuggable, and extensible environment for building intelligent agents.

---

## Features

- **BaseAgent** with a multi-step reasoning loop  
- **OpenAIPipeline** for LLM-based planning  
- **ToolRegistry** for dynamic tool execution  
- **Built-in tools** (echo, calculator, datetime)  
- **Memory system** for storing interaction traces  
- **FastAPI server** for running agents via HTTP  
- **Experiments** documenting agent behavior and evolution  
- **Docker support** for containerized deployment  

---

## Project Structure

```
agent-ai-lab/
│
├── src/
│   ├── agent_core/
│   │   ├── base_agent.py
│   │   ├── memory.py
│   │   ├── tools.py
│   │   └── reasoning.py
│   │
│   ├── pipelines/
│   │   ├── llm_pipeline.py
│   │   └── retrieval_pipeline.py
│   │
│   └── server/
│       └── api.py
│
├── docs/
│   ├── architecture.md
│   └── experiments/
│       └── experiment-001-agent-loop.md
│
├── tests/
│   └── test_agent_core.py
│
├── README.md
├── LICENSE
└── .gitignore
```

---

---

## Getting Started

### 1. Clone the repository

```
bash
git clone https://github.com/krunixbase/agent-ai-lab
cd agent-ai-lab
```

### 2. Create your environment file

```
bash
cp .env.example .env
```

Add your OpenAI API key:

```
OPENAI_API_KEY=your-key-here
```

### 3. Install dependencies

```
bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```
bash
uvicorn src.server.api:app --reload
```

Server will be available at:

```
http://localhost:8000
```
---

## Running with Docker

- Build the image:

```
bash
docker build -t agent-ai-lab .
```

- Run the container:

```
bash
docker run -p 8000:8000 --env-file .env agent-ai-lab
```
---

## Experiments

The project includes a growing set of documented experiments:

- Experiment 001 — Basic agent loop

- Experiment 002 — Tool calling

- (Upcoming) Experiment 003 — Memory summarization

- (Upcoming) Experiment 004 — Multi-step planning

Experiments live in:

```
docs/experiments/
```

---

# Roadmap

## The full roadmap is available in:

```
ROADMAP.md
```

## It covers short‑term, mid‑term, and long‑term goals including:

- multi-agent collaboration

- persistent memory

- RAG pipelines

- external API tools

- orchestration and distributed execution

---

# Contributing

Contributions are welcome.Please open an issue or submit a pull request.

---

# License

This project is licensed under the MIT License.

---
