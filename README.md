# ReviewCrew: Multi-Agent Code Review System

[![Live Demo](https://img.shields.io/badge/Live_Demo-ReviewCrew_AI-6366f1?style=for-the-badge&logo=render&logoColor=white)](https://reviewcrew-app.onrender.com)
[![API Docs](https://img.shields.io/badge/API_Docs-Swagger_UI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://reviewcrew-app.onrender.com/docs)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-orange?style=for-the-badge)](https://github.com/langchain-ai/langgraph)
[![Redis](https://img.shields.io/badge/Cache-Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io)

> 🚀 **Live Web Application:** [https://reviewcrew-app.onrender.com](https://reviewcrew-app.onrender.com)  
> 📖 **Interactive API Documentation:** [https://reviewcrew-app.onrender.com/docs](https://reviewcrew-app.onrender.com/docs)  
> 🩺 **Health Check Endpoint:** [https://reviewcrew-app.onrender.com/health](https://reviewcrew-app.onrender.com/health)

---

## About

ReviewCrew is an autonomous multi-agent system designed to review code changes (diffs) similarly to a team of human senior reviewers. Powered by **LangGraph**, it orchestrates specialized agents—each focusing on a distinct concern such as code style & conventions, security vulnerabilities, or test coverage. A supervisor agent then synthesizes their findings into a single, cohesive, human-grade pull request review.

### Key Features
- **Multi-Agent Orchestration**: Built with **LangGraph** where specialized reviewer agents (Style, Security, Test Coverage) run in parallel with tool calling (Ruff linter AST analysis, security vulnerability detectors, test suite ratio checkers).
- **Intelligent Supervisor Synthesis**: A supervisor node merges all specialist findings, deduplicates issues, and generates a unified, constructive code review comment.
- **Interactive Web Interface**: A modern, glassmorphic dark-mode web console served at the root URL with quick preset diffs (SQL injection, PEP 8 style, missing test coverage), language selection, and real-time pipeline visualization.
- **FastAPI Backend & SSE Streaming**: Real-time Server-Sent Events (SSE) streaming review output as each agent finishes its analysis.
- **Redis Caching & Pub/Sub**: Normalized diff hashing stores previous review runs in Redis, delivering immediate sub-millisecond responses on identical diffs without consuming LLM quotas.
- **Observability**: Full tracing and scoring across every agent step with Langfuse.
- **Containerized Stack**: Complete Docker Compose setup running the FastAPI app and Redis container.

---

## Live Demo & Screenshots

Experience the multi-agent review system in action at:  
👉 **[https://reviewcrew-app.onrender.com](https://reviewcrew-app.onrender.com)**

1. Paste any Git diff hunk or click one of the preset samples (e.g. *SQL Injection*, *Style Violations*, or *Missing Tests*).
2. Watch the live LangGraph execution pipeline stream updates via SSE as the **Style**, **Security**, and **Test Coverage** agents analyze the diff.
3. Review the merged final synthesis from the **Supervisor Agent**.

---

## Architecture

```
                    ┌─────────────────────────┐
                    │      Incoming Diff      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Router Node        │
                    └────────────┬────────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│   Style Agent    │   │  Security Agent  │   │   Test Agent     │
│   (Ruff / AST)   │   │  (Vuln Scanner)  │   │  (Test Coverage) │
└────────┬─────────┘   └─────────┬────────┘   └─────────┬────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Supervisor Node     │
                    │   (Unified Synthesis)   │
                    └────────────┬────────────┘
                                 │
                     Cached via Redis (7d TTL)
```

---

## Local Setup (Docker Compose)

1. **Clone the repository and set up environment variables**:
   ```bash
   git clone https://github.com/NishantPatle06/ReviewCrew-Multi-Agent-Code-Review-System.git
   cd ReviewCrew-Multi-Agent-Code-Review-System
   cp .env.example .env
   # Add your GEMINI_API_KEY in .env
   ```

2. **Start the stack**:
   ```bash
   docker compose up -d --build
   ```

3. **Access Locally**:
   - Web UI: [http://localhost:8000/](http://localhost:8000/)
   - Interactive Swagger API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health check: [http://localhost:8000/health](http://localhost:8000/health)

---

## Cloud Deployment (Render Blueprint)

This repository includes a `render.yaml` blueprint:
1. Fork or connect this repository to [Render.com](https://render.com).
2. Choose **Blueprints** and select `render.yaml`.
3. Provide your `GEMINI_API_KEY` in the environment variable prompt.
4. Render automatically provisions the Docker Web Service and private Redis instance.