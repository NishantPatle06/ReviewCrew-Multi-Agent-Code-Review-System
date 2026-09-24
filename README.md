# ReviewCrew-Multi-Agent-Code-Review-System

## About

ReviewCrew is a multi-agent system designed to review code changes (diffs) similarly to a team of human reviewers. Powered by LangGraph, it orchestrates specialized agents—each focusing on a distinct concern such as code style, security vulnerabilities, or test coverage. A supervisor agent then synthesizes their findings into a single, cohesive code review.

### Key Features
- **Multi-Agent Architecture**: Built with LangGraph for orchestrating specialized reviewer agents and a supervisor.
- **FastAPI Backend**: A robust backend providing a RESTful interface to the review system.
- **Production-ready Infrastructure**: Includes caching (Redis), observability, and containerization.
- **Flexible LLM Support**: Designed to work with free-tier LLM APIs (like Gemini or Groq) using LangChain's model abstractions.

This project was built to demonstrate applied AI engineering, specifically focusing on prompting, tool calling, and workflow orchestration.