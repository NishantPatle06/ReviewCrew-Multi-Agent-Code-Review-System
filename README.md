# ReviewCrew: Multi-Agent Code Review System

## About

ReviewCrew is an autonomous multi-agent system designed to review code changes (diffs) similarly to a team of human senior reviewers. Powered by **LangGraph**, it orchestrates specialized agents—each focusing on a distinct concern such as code style & conventions, security vulnerabilities, or test coverage. A supervisor agent then synthesizes their findings into a single, cohesive, human-grade pull request review.

### Key Features
- **Multi-Agent Orchestration**: Built with **LangGraph** where specialized reviewer agents (Style, Security, Test Coverage) run with tool calling (Ruff linter AST analysis, security vulnerability detectors, test suite ratio checkers).
- **Intelligent Supervisor Synthesis**: A supervisor node merges all specialist findings, deduplicates issues, and generates a unified, constructive code review comment.
- **Interactive Web Interface**: A modern, glassmorphic dark-mode web console served at the root URL with quick preset diffs (SQL injection, PEP 8 style, missing test coverage), language selection, and real-time pipeline visualization.
- **FastAPI Backend & SSE Streaming**: Real-time Server-Sent Events (SSE) streaming review output as each agent finishes its analysis.
- **Redis Caching & Pub/Sub**: Normalized diff hashing stores previous review runs in Redis, delivering immediate sub-millisecond responses on identical diffs without consuming LLM quotas.
- **Observability**: Full tracing and scoring across every agent step with Langfuse.
- **Containerized Stack**: Complete Docker Compose setup running the FastAPI app and Redis container.

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

## Quick Start (Docker Compose)

1. **Clone the repository and set up environment variables**:
   ```bash
   cp .env.example .env
   # Add your GEMINI_API_KEY (Google AI Studio)
   ```

2. **Start the stack**:
   ```bash
   docker compose up -d --build
   ```

3. **Open the Web UI**:
   - Web UI: [http://localhost:8000/](http://localhost:8000/)
   - Interactive Swagger API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health check: [http://localhost:8000/health](http://localhost:8000/health)

---

## Cloud Deployment (Render / Railway)

This repository includes a `render.yaml` blueprint:
1. Connect this GitHub repository to [Render.com](https://render.com).
2. Choose **Blueprints** and select `render.yaml`.
3. Provide your `GEMINI_API_KEY` in the environment settings.
4. Render will automatically spin up the Docker web service and private Redis instance!