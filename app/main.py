"""FastAPI app entrypoint. Wires together the API routers and serves the Web UI."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app.api.review import router as review_router
from app.infra.logging import configure_logging
from app.ui.html import INDEX_HTML

configure_logging()

app = FastAPI(
    title="ReviewCrew - Multi-Agent Code Review Assistant",
    description="Autonomous multi-agent system powered by LangGraph, specialized Style, Security, and Test Coverage agents, and Redis caching.",
    version="1.0.0",
)

# Enable CORS for cross-origin requests and SSE streaming
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review_router)


@app.get("/", response_class=HTMLResponse)
def index():
    """Serves the interactive ReviewCrew Web UI."""
    return HTMLResponse(content=INDEX_HTML)


@app.get("/health")
def health_check():
    return {"status": "ok"}

