"""HTML template for the ReviewCrew Multi-Agent Code Reviewer Web UI."""

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ReviewCrew | Multi-Agent AI Code Reviewer</title>
  <meta name="description" content="Autonomous Multi-Agent Code Review System orchestrated with LangGraph, specialized Style, Security, and Test Coverage agents, and Redis caching.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-base: #0b0f19;
      --bg-surface: #111827;
      --bg-surface-elevated: #1f2937;
      --bg-glass: rgba(17, 24, 39, 0.75);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-focus: rgba(99, 102, 241, 0.5);
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --text-dim: #6b7280;
      --primary: #6366f1;
      --primary-light: #818cf8;
      --primary-dark: #4f46e5;
      --secondary: #06b6d4;
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --accent: #ec4899;
      --card-radius: 16px;
      --inner-radius: 10px;
      --transition-smooth: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-base);
      color: var(--text-main);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
      line-height: 1.5;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(6, 182, 212, 0.10) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.05) 0%, transparent 60%);
      background-attachment: fixed;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-base);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--bg-surface-elevated);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--text-dim);
    }

    /* Container */
    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 24px 20px 60px;
    }

    /* Navbar / Header */
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 24px;
      background: var(--bg-glass);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: 20px;
      margin-bottom: 28px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      color: inherit;
    }

    .brand-icon {
      width: 42px;
      height: 42px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }

    .brand-icon svg {
      width: 24px;
      height: 24px;
      color: white;
    }

    .brand-text h1 {
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, #ffffff, #c7d2fe);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-text p {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .status-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 100px;
      font-size: 0.8rem;
      font-weight: 600;
      color: #34d399;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      background-color: var(--success);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--success);
      animation: pulse-dot 2s infinite;
    }

    @keyframes pulse-dot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.5; transform: scale(0.85); }
    }

    .btn-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--text-main);
      text-decoration: none;
      transition: var(--transition-smooth);
    }

    .btn-link:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-1px);
    }

    /* Hero Banner */
    .hero {
      text-align: center;
      margin-bottom: 32px;
      padding: 10px 0;
    }

    .hero-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 5px 14px;
      background: rgba(99, 102, 241, 0.12);
      border: 1px solid rgba(99, 102, 241, 0.25);
      border-radius: 100px;
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--primary-light);
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .hero h2 {
      font-size: 2.2rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      margin-bottom: 10px;
      background: linear-gradient(135deg, #ffffff 40%, #a5b4fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero p {
      max-width: 680px;
      margin: 0 auto;
      font-size: 0.98rem;
      color: var(--text-muted);
    }

    /* Multi-Agent Architecture Ribbon */
    .agent-pipeline-overview {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
      margin-bottom: 28px;
    }

    .agent-card-mini {
      background: var(--bg-glass);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--inner-radius);
      padding: 14px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: var(--transition-smooth);
    }

    .agent-card-mini:hover {
      border-color: var(--border-focus);
      background: rgba(31, 41, 55, 0.7);
      transform: translateY(-2px);
    }

    .agent-mini-icon {
      width: 36px;
      height: 36px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .agent-mini-icon.router { background: rgba(99, 102, 241, 0.2); color: #818cf8; }
    .agent-mini-icon.style { background: rgba(236, 72, 153, 0.2); color: #f472b6; }
    .agent-mini-icon.security { background: rgba(239, 68, 68, 0.2); color: #f87171; }
    .agent-mini-icon.test { background: rgba(16, 185, 129, 0.2); color: #34d399; }
    .agent-mini-icon.supervisor { background: rgba(6, 182, 212, 0.2); color: #22d3ee; }

    .agent-mini-info h4 {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-main);
    }

    .agent-mini-info p {
      font-size: 0.72rem;
      color: var(--text-muted);
    }

    /* Main Workspace Grid */
    .workspace-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    @media (max-width: 1024px) {
      .workspace-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Cards */
    .glass-panel {
      background: var(--bg-glass);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--card-radius);
      padding: 24px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
      position: relative;
    }

    .panel-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border-subtle);
    }

    .panel-title {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 1.1rem;
      font-weight: 700;
    }

    .panel-title svg {
      width: 20px;
      height: 20px;
      color: var(--primary-light);
    }

    /* Preset Chips */
    .presets-row {
      margin-bottom: 18px;
    }

    .presets-label {
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .presets-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .chip-btn {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition-smooth);
    }

    .chip-btn:hover {
      background: var(--bg-surface-elevated);
      color: var(--text-main);
      border-color: rgba(255, 255, 255, 0.2);
    }

    .chip-btn.active {
      background: rgba(99, 102, 241, 0.15);
      border-color: var(--primary);
      color: #c7d2fe;
    }

    /* Form Fields */
    .form-group {
      margin-bottom: 16px;
    }

    .form-row {
      display: flex;
      gap: 12px;
      margin-bottom: 16px;
    }

    .form-col {
      flex: 1;
    }

    label {
      display: block;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 6px;
    }

    select, input[type="text"] {
      width: 100%;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 10px 14px;
      border-radius: var(--inner-radius);
      font-size: 0.88rem;
      font-family: inherit;
      outline: none;
      transition: var(--transition-smooth);
    }

    select:focus, input[type="text"]:focus, textarea:focus {
      border-color: var(--primary-light);
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
    }

    textarea {
      width: 100%;
      background: #090d16;
      border: 1px solid var(--border-subtle);
      color: #e5e7eb;
      padding: 14px;
      border-radius: var(--inner-radius);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.84rem;
      line-height: 1.6;
      resize: vertical;
      min-height: 240px;
      outline: none;
      transition: var(--transition-smooth);
    }

    .collapsible-details {
      margin-bottom: 18px;
      border: 1px solid var(--border-subtle);
      border-radius: var(--inner-radius);
      overflow: hidden;
      background: rgba(0, 0, 0, 0.2);
    }

    .collapsible-summary {
      padding: 10px 14px;
      cursor: pointer;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
    }

    .collapsible-content {
      padding: 12px;
      border-top: 1px solid var(--border-subtle);
    }

    .collapsible-content textarea {
      min-height: 120px;
    }

    /* Submit Button */
    .btn-submit {
      width: 100%;
      padding: 14px 20px;
      background: linear-gradient(135deg, var(--primary) 0%, #4338ca 100%);
      color: white;
      border: none;
      border-radius: var(--inner-radius);
      font-size: 0.96rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 8px 24px rgba(99, 102, 241, 0.35);
      transition: var(--transition-smooth);
      position: relative;
      overflow: hidden;
    }

    .btn-submit:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 12px 30px rgba(99, 102, 241, 0.5);
      background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%);
    }

    .btn-submit:active:not(:disabled) {
      transform: translateY(0);
    }

    .btn-submit:disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }

    .spinner {
      width: 20px;
      height: 20px;
      border: 2.5px solid rgba(255, 255, 255, 0.3);
      border-top-color: white;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      display: none;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    /* Live Pipeline Visualizer Card */
    .pipeline-status-container {
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid var(--border-subtle);
      border-radius: var(--inner-radius);
      padding: 16px;
      margin-bottom: 20px;
    }

    .pipeline-status-title {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .pipeline-nodes {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 6px;
      position: relative;
    }

    .node-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      flex: 1;
      text-align: center;
      position: relative;
      z-index: 2;
    }

    .node-icon-circle {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--bg-surface-elevated);
      border: 2px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-dim);
      font-size: 0.9rem;
      transition: var(--transition-smooth);
    }

    .node-item.active .node-icon-circle {
      border-color: var(--primary);
      color: white;
      background: var(--primary);
      box-shadow: 0 0 16px var(--primary);
      animation: pulse-ring 1.5s infinite;
    }

    .node-item.complete .node-icon-circle {
      border-color: var(--success);
      color: white;
      background: var(--success);
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
    }

    @keyframes pulse-ring {
      0% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.6); }
      70% { box-shadow: 0 0 0 8px rgba(99, 102, 241, 0); }
      100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }
    }

    .node-label {
      font-size: 0.72rem;
      font-weight: 500;
      color: var(--text-muted);
    }

    .node-item.active .node-label {
      color: var(--primary-light);
      font-weight: 600;
    }

    .node-item.complete .node-label {
      color: #34d399;
    }

    /* Live Output Tabs */
    .tabs-header {
      display: flex;
      gap: 6px;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 16px;
      overflow-x: auto;
      padding-bottom: 2px;
    }

    .tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 8px 14px;
      font-size: 0.85rem;
      font-weight: 500;
      border-radius: 8px 8px 0 0;
      cursor: pointer;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition-smooth);
      position: relative;
    }

    .tab-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.04);
    }

    .tab-btn.active {
      color: white;
      font-weight: 600;
      background: rgba(99, 102, 241, 0.12);
    }

    .tab-btn.active::after {
      content: '';
      position: absolute;
      bottom: -3px;
      left: 0;
      right: 0;
      height: 2px;
      background: var(--primary);
      border-radius: 2px;
    }

    .tab-content {
      display: none;
    }

    .tab-content.active {
      display: block;
    }

    /* Result Display Box */
    .result-box {
      background: #090d16;
      border: 1px solid var(--border-subtle);
      border-radius: var(--inner-radius);
      padding: 18px;
      min-height: 260px;
      max-height: 480px;
      overflow-y: auto;
      font-size: 0.88rem;
      line-height: 1.6;
    }

    .empty-state {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 240px;
      color: var(--text-dim);
      text-align: center;
      gap: 12px;
    }

    .empty-state svg {
      width: 44px;
      height: 44px;
      opacity: 0.4;
    }

    .empty-state p {
      font-size: 0.9rem;
    }

    /* Review Render styling */
    .review-markdown {
      white-space: pre-wrap;
      font-family: inherit;
      color: #e5e7eb;
    }

    .review-markdown code {
      font-family: 'JetBrains Mono', monospace;
      background: rgba(255, 255, 255, 0.08);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.82rem;
      color: #a5b4fc;
    }

    .cache-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 600;
      margin-bottom: 12px;
    }

    .cache-pill.hit {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .cache-pill.miss {
      background: rgba(99, 102, 241, 0.15);
      color: #a5b4fc;
      border: 1px solid rgba(99, 102, 241, 0.3);
    }

    .actions-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 14px;
    }

    .btn-copy {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 500;
      cursor: pointer;
      transition: var(--transition-smooth);
    }

    .btn-copy:hover {
      background: rgba(255, 255, 255, 0.1);
      color: var(--text-main);
    }

    /* Live Stream Log */
    .stream-log {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 12px;
      padding: 8px 12px;
      background: rgba(0, 0, 0, 0.4);
      border-radius: 6px;
      border: 1px solid var(--border-subtle);
      max-height: 80px;
      overflow-y: auto;
    }

    .stream-log-entry {
      line-height: 1.4;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .stream-log-time {
      color: var(--text-dim);
    }

    /* Footer */
    footer {
      margin-top: 48px;
      text-align: center;
      padding-top: 24px;
      border-top: 1px solid var(--border-subtle);
      color: var(--text-dim);
      font-size: 0.82rem;
    }

    footer a {
      color: var(--primary-light);
      text-decoration: none;
    }

    footer a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Header -->
    <header>
      <a href="/" class="brand">
        <div class="brand-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="16 18 22 12 16 6"></polyline>
            <polyline points="8 6 2 12 8 18"></polyline>
          </svg>
        </div>
        <div class="brand-text">
          <h1>ReviewCrew AI</h1>
          <p>Multi-Agent Code Review & PR Assistant</p>
        </div>
      </a>
      <div class="nav-actions">
        <div class="status-badge" id="systemStatus">
          <span class="status-dot"></span>
          <span id="statusText">System Online</span>
        </div>
        <a href="/docs" target="_blank" class="btn-link">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
          </svg>
          API Docs (/docs)
        </a>
      </div>
    </header>

    <!-- Hero -->
    <div class="hero">
      <div class="hero-pill">Autonomous LangGraph Multi-Agent Architecture</div>
      <h2>Intelligent Code Reviews at Team Scale</h2>
      <p>Routes code changes through specialized Style, Security, and Test Coverage agents with AST tool calling, synthesized by an intelligent supervisor graph.</p>
    </div>

    <!-- Agent Pipeline Overview -->
    <div class="agent-pipeline-overview">
      <div class="agent-card-mini">
        <div class="agent-mini-icon router">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
        </div>
        <div class="agent-mini-info">
          <h4>Router Node</h4>
          <p>Diff hunk classification & routing</p>
        </div>
      </div>
      <div class="agent-card-mini">
        <div class="agent-mini-icon style">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
        </div>
        <div class="agent-mini-info">
          <h4>Style Agent</h4>
          <p>Ruff linter & PEP 8 tool calling</p>
        </div>
      </div>
      <div class="agent-card-mini">
        <div class="agent-mini-icon security">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        </div>
        <div class="agent-mini-info">
          <h4>Security Agent</h4>
          <p>Pattern detector & secret scanner</p>
        </div>
      </div>
      <div class="agent-card-mini">
        <div class="agent-mini-icon test">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="9 15 12 18 15 15"></polyline></svg>
        </div>
        <div class="agent-mini-info">
          <h4>Test Coverage</h4>
          <p>Test ratio & test framework check</p>
        </div>
      </div>
      <div class="agent-card-mini">
        <div class="agent-mini-icon supervisor">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
        </div>
        <div class="agent-mini-info">
          <h4>Supervisor</h4>
          <p>Merged synthesis & PR comment</p>
        </div>
      </div>
    </div>

    <!-- Main Workspace -->
    <div class="workspace-grid">
      <!-- Left Panel: Input & Settings -->
      <div class="glass-panel">
        <div class="panel-header">
          <div class="panel-title">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
            </svg>
            Submit Code Change
          </div>
        </div>

        <!-- Presets -->
        <div class="presets-row">
          <div class="presets-label">
            <span>Quick Presets (Click to load)</span>
          </div>
          <div class="presets-chips">
            <button type="button" class="chip-btn active" onclick="loadPreset('security')">
              🛡️ SQL Injection & Secret
            </button>
            <button type="button" class="chip-btn" onclick="loadPreset('style')">
              🎨 PEP 8 Style Violations
            </button>
            <button type="button" class="chip-btn" onclick="loadPreset('test')">
              🧪 Missing Unit Tests
            </button>
            <button type="button" class="chip-btn" onclick="loadPreset('clean')">
              ⚡ Clean Refactoring
            </button>
          </div>
        </div>

        <form id="reviewForm" onsubmit="handleReviewSubmit(event)">
          <div class="form-row">
            <div class="form-col">
              <label for="langSelect">Language</label>
              <select id="langSelect" required>
                <option value="py">Python (.py)</option>
                <option value="js">JavaScript (.js)</option>
                <option value="ts">TypeScript (.ts)</option>
                <option value="go">Go (.go)</option>
                <option value="php">PHP (.php)</option>
                <option value="java">Java (.java)</option>
                <option value="rb">Ruby (.rb)</option>
                <option value="rs">Rust (.rs)</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label for="diffHunk">Git Diff Hunk (Unified Format)</label>
            <textarea id="diffHunk" spellcheck="false" required placeholder="Paste unified git diff here..."></textarea>
          </div>

          <details class="collapsible-details">
            <summary class="collapsible-summary">
              <span>Original File Content (Optional Context)</span>
              <span>▼</span>
            </summary>
            <div class="collapsible-content">
              <textarea id="oldFile" spellcheck="false" placeholder="Optional: full original file before change..."></textarea>
            </div>
          </details>

          <button type="submit" id="submitBtn" class="btn-submit">
            <div class="spinner" id="btnSpinner"></div>
            <span id="btnText">🚀 Start Multi-Agent Review</span>
          </button>
        </form>
      </div>

      <!-- Right Panel: Live Pipeline & Output -->
      <div class="glass-panel">
        <div class="panel-header">
          <div class="panel-title">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
            </svg>
            Live Agent Pipeline & Results
          </div>
          <span id="runBadge" style="font-size: 0.75rem; color: var(--text-dim); font-family: monospace;">Ready</span>
        </div>

        <!-- Real-time Pipeline Progress Nodes -->
        <div class="pipeline-status-container">
          <div class="pipeline-status-title">
            <span>LangGraph Pipeline State</span>
            <span id="pipelineStepText" style="color: var(--text-muted); font-size: 0.75rem;">Idle</span>
          </div>
          <div class="pipeline-nodes">
            <div class="node-item" id="node-router">
              <div class="node-icon-circle">🔀</div>
              <span class="node-label">Router</span>
            </div>
            <div class="node-item" id="node-style">
              <div class="node-icon-circle">🎨</div>
              <span class="node-label">Style</span>
            </div>
            <div class="node-item" id="node-security">
              <div class="node-icon-circle">🛡️</div>
              <span class="node-label">Security</span>
            </div>
            <div class="node-item" id="node-test">
              <div class="node-icon-circle">🧪</div>
              <span class="node-label">Test</span>
            </div>
            <div class="node-item" id="node-merge">
              <div class="node-icon-circle">✨</div>
              <span class="node-label">Merge</span>
            </div>
          </div>
        </div>

        <!-- Output Tabs -->
        <div class="tabs-header">
          <button type="button" class="tab-btn active" onclick="switchTab('final')">
            🏆 Final Review
          </button>
          <button type="button" class="tab-btn" onclick="switchTab('security')">
            🛡️ Security
          </button>
          <button type="button" class="tab-btn" onclick="switchTab('style')">
            🎨 Style
          </button>
          <button type="button" class="tab-btn" onclick="switchTab('test')">
            🧪 Test Coverage
          </button>
          <button type="button" class="tab-btn" onclick="switchTab('raw')">
            📋 Raw JSON
          </button>
        </div>

        <!-- Tab Contents -->
        <div id="tab-final" class="tab-content active">
          <div id="cacheIndicator"></div>
          <div class="result-box" id="finalResultBox">
            <div class="empty-state">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
              <p>Submit a code change to view the unified review generated by the Supervisor Agent.</p>
            </div>
          </div>
        </div>

        <div id="tab-security" class="tab-content">
          <div class="result-box" id="securityResultBox">
            <div class="empty-state"><p>No security findings yet.</p></div>
          </div>
        </div>

        <div id="tab-style" class="tab-content">
          <div class="result-box" id="styleResultBox">
            <div class="empty-state"><p>No style findings yet.</p></div>
          </div>
        </div>

        <div id="tab-test" class="tab-content">
          <div class="result-box" id="testResultBox">
            <div class="empty-state"><p>No test coverage findings yet.</p></div>
          </div>
        </div>

        <div id="tab-raw" class="tab-content">
          <div class="result-box" id="rawResultBox" style="font-family: 'JetBrains Mono', monospace; font-size: 0.78rem;">
            <div class="empty-state"><p>Raw JSON response will appear here.</p></div>
          </div>
        </div>

        <!-- Live Log / SSE status -->
        <div class="stream-log" id="streamLog" style="display: none;">
          <div class="stream-log-entry">
            <span class="stream-log-time">00:00:00</span>
            <span class="stream-log-msg">SSE Stream initialized.</span>
          </div>
        </div>

        <div class="actions-footer">
          <button type="button" class="btn-copy" onclick="copyCurrentReview()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
              <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
            </svg>
            <span id="copyBtnText">Copy Review</span>
          </button>
          <span id="runTiming" style="font-size: 0.75rem; color: var(--text-dim);"></span>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer>
      <p>ReviewCrew Multi-Agent Code Review System &bull; Powered by LangGraph, FastAPI, Redis & Langfuse</p>
    </footer>
  </div>

  <script>
    // Sample Presets
    const PRESETS = {
      security: {
        lang: "py",
        diff: `@@ -12,6 +12,12 @@ def authenticate_user(db_conn, username, password_attempt):
+    # Query user directly from input string
+    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password_attempt}'"
+    cursor = db_conn.cursor()
+    cursor.execute(query)
+    user = cursor.fetchone()
+    
+    JWT_SECRET = "super_secret_jwt_key_12345_production_do_not_leak!"
     return user`,
        old: `def authenticate_user(db_conn, username, password_attempt):
    pass`
      },
      style: {
        lang: "py",
        diff: `@@ -1,5 +1,11 @@
+from math import *
+import sys, os
+
+def Calculate_Discount(Price, discount_rate):
+    try:
+        final_price = Price - (Price * discount_rate)
+        UNUSED_VAR = 42
+        return final_price
+    except:
+        print("error")
+        return None`,
        old: `# Utility calculations`
      },
      test: {
        lang: "py",
        diff: `@@ -45,6 +45,21 @@ class PaymentGateway:
+    def process_refund(self, transaction_id: str, amount_cents: int) -> bool:
+        \"\"\"Process full or partial refund for a customer transaction.\"\"\"
+        if amount_cents <= 0:
+            raise ValueError("Refund amount must be positive")
+        
+        tx = self.store.get_transaction(transaction_id)
+        if not tx or tx.status != "settled":
+            return False
+            
+        refund_id = self.gateway_client.issue_refund(
+            charge_id=tx.charge_id,
+            amount=amount_cents
+        )
+        self.store.record_refund(transaction_id, refund_id, amount_cents)
+        return True`,
        old: `class PaymentGateway:
    def __init__(self, store, client):
        self.store = store
        self.gateway_client = client`
      },
      clean: {
        lang: "py",
        diff: `@@ -15,7 +15,10 @@ def calculate_tax(subtotal: float, tax_rate: float) -> float:
+    \"\"\"Calculate total sales tax with proper precision validation.\"\"\"
+    if subtotal < 0 or tax_rate < 0:
+        raise ValueError("Subtotal and tax rate must be non-negative")
+    return round(subtotal * tax_rate, 2)`,
        old: `def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate`
      }
    };

    let currentReviewData = null;
    let activeTab = 'final';

    function loadPreset(key) {
      const p = PRESETS[key];
      if (!p) return;
      document.getElementById('langSelect').value = p.lang;
      document.getElementById('diffHunk').value = p.diff;
      document.getElementById('oldFile').value = p.old;

      // Update chip states
      document.querySelectorAll('.chip-btn').forEach(btn => btn.classList.remove('active'));
      event.currentTarget.classList.add('active');
    }

    function switchTab(tabId) {
      activeTab = tabId;
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      
      event.currentTarget.classList.add('active');
      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.add('active');
    }

    function logStream(msg) {
      const log = document.getElementById('streamLog');
      log.style.display = 'block';
      const time = new Date().toLocaleTimeString();
      const entry = document.createElement('div');
      entry.className = 'stream-log-entry';
      entry.innerHTML = `<span class="stream-log-time">${time}</span><span class="stream-log-msg">${msg}</span>`;
      log.appendChild(entry);
      log.scrollTop = log.scrollHeight;
    }

    function setNodeStatus(nodeId, status) {
      const el = document.getElementById('node-' + nodeId);
      if (!el) return;
      el.classList.remove('active', 'complete');
      if (status) el.classList.add(status);
    }

    function resetPipelineNodes() {
      ['router', 'style', 'security', 'test', 'merge'].forEach(id => {
        setNodeStatus(id, null);
      });
      document.getElementById('streamLog').innerHTML = '';
      document.getElementById('streamLog').style.display = 'none';
      document.getElementById('cacheIndicator').innerHTML = '';
      document.getElementById('runTiming').innerText = '';
    }

    async function handleReviewSubmit(e) {
      e.preventDefault();
      const submitBtn = document.getElementById('submitBtn');
      const btnText = document.getElementById('btnText');
      const btnSpinner = document.getElementById('btnSpinner');
      const runBadge = document.getElementById('runBadge');
      const pipelineStepText = document.getElementById('pipelineStepText');

      const payload = {
        diff_hunk: document.getElementById('diffHunk').value.trim(),
        old_file: document.getElementById('oldFile').value.trim(),
        lang: document.getElementById('langSelect').value
      };

      if (!payload.diff_hunk) {
        alert("Please provide a diff hunk.");
        return;
      }

      // UI Loading state
      submitBtn.disabled = true;
      btnSpinner.style.display = 'block';
      btnText.innerText = 'Analyzing Diff...';
      runBadge.innerText = 'Submitting...';
      runBadge.style.color = 'var(--primary-light)';
      resetPipelineNodes();

      const startTime = performance.now();

      try {
        setNodeStatus('router', 'active');
        pipelineStepText.innerText = 'Routing diff to specialists...';
        logStream('Posting diff to /review endpoint...');

        const resp = await fetch('/review', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (!resp.ok) {
          throw new Error('API returned ' + resp.status + ': ' + (await resp.text()));
        }

        const data = await resp.json();
        const runId = data.run_id;
        runBadge.innerText = 'Run ID: ' + runId.slice(0, 8);
        logStream('Run registered: ' + runId);
        setNodeStatus('router', 'complete');

        // Connect to SSE stream
        connectSseStream(runId, startTime);
      } catch (err) {
        console.error(err);
        alert('Error submitting review: ' + err.message);
        submitBtn.disabled = false;
        btnSpinner.style.display = 'none';
        btnText.innerText = '🚀 Start Multi-Agent Review';
        runBadge.innerText = 'Error';
        runBadge.style.color = 'var(--danger)';
      }
    }

    function connectSseStream(runId, startTime) {
      const pipelineStepText = document.getElementById('pipelineStepText');
      const eventSource = new EventSource('/review/' + runId + '/stream');

      // Pre-activate specialist nodes
      setNodeStatus('style', 'active');
      setNodeStatus('security', 'active');
      setNodeStatus('test', 'active');
      pipelineStepText.innerText = 'Specialist agents running in parallel...';

      eventSource.addEventListener('status', (e) => {
        try {
          const payload = JSON.parse(e.data);
          logStream('Status update: ' + payload.status + (payload.cached ? ' (Cache Hit)' : ''));
          if (payload.cached) {
            document.getElementById('cacheIndicator').innerHTML = 
              `<div class="cache-pill hit">⚡ Redis Cache Hit &bull; 0 LLM calls consumed</div>`;
          }
          if (payload.status === 'complete') {
            eventSource.close();
            onReviewComplete(runId, startTime);
          }
        } catch (err) {}
      });

      eventSource.addEventListener('style', (e) => {
        try {
          const payload = JSON.parse(e.data);
          setNodeStatus('style', 'complete');
          logStream('Style Agent finished.');
          if (payload.style_review) renderReviewItem('styleResultBox', payload.style_review);
        } catch (err) {}
      });

      eventSource.addEventListener('security', (e) => {
        try {
          const payload = JSON.parse(e.data);
          setNodeStatus('security', 'complete');
          logStream('Security Agent finished.');
          if (payload.security_review) renderReviewItem('securityResultBox', payload.security_review);
        } catch (err) {}
      });

      eventSource.addEventListener('test_coverage', (e) => {
        try {
          const payload = JSON.parse(e.data);
          setNodeStatus('test', 'complete');
          logStream('Test Coverage Agent finished.');
          if (payload.test_review) renderReviewItem('testResultBox', payload.test_review);
        } catch (err) {}
      });

      eventSource.addEventListener('merge', (e) => {
        try {
          const payload = JSON.parse(e.data);
          setNodeStatus('merge', 'active');
          pipelineStepText.innerText = 'Supervisor synthesizing review...';
          logStream('Supervisor synthesis node reached.');
          if (payload.final_review) renderReviewItem('finalResultBox', payload.final_review);
        } catch (err) {}
      });

      eventSource.onerror = (err) => {
        console.warn('SSE stream closed or error, polling final result...');
        eventSource.close();
        setTimeout(() => onReviewComplete(runId, startTime), 1000);
      };
    }

    async function onReviewComplete(runId, startTime) {
      setNodeStatus('merge', 'complete');
      document.getElementById('pipelineStepText').innerText = 'All Agents Complete';
      const submitBtn = document.getElementById('submitBtn');
      const btnText = document.getElementById('btnText');
      const btnSpinner = document.getElementById('btnSpinner');
      const runBadge = document.getElementById('runBadge');

      submitBtn.disabled = false;
      btnSpinner.style.display = 'none';
      btnText.innerText = '🚀 Run Another Review';
      runBadge.innerText = 'Completed';
      runBadge.style.color = '#34d399';

      const duration = ((performance.now() - startTime) / 1000).toFixed(2);
      document.getElementById('runTiming').innerText = 'Completed in ' + duration + 's';

      try {
        const resp = await fetch('/review/' + runId);
        if (resp.ok) {
          const fullResult = await resp.json();
          currentReviewData = fullResult;
          document.getElementById('rawResultBox').innerHTML = `<pre>${JSON.stringify(fullResult, null, 2)}</pre>`;
          
          if (fullResult.final_review) renderReviewItem('finalResultBox', fullResult.final_review);
          if (fullResult.security_review) renderReviewItem('securityResultBox', fullResult.security_review);
          if (fullResult.style_review) renderReviewItem('styleResultBox', fullResult.style_review);
          if (fullResult.test_review) renderReviewItem('testResultBox', fullResult.test_review);
        }
      } catch (e) {
        console.error('Failed to fetch full result', e);
      }
    }

    function renderReviewItem(containerId, text) {
      const box = document.getElementById(containerId);
      if (!box) return;
      box.innerHTML = `<div class="review-markdown">${escapeHtml(text)}</div>`;
    }

    function escapeHtml(str) {
      return str.replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
    }

    function copyCurrentReview() {
      let textToCopy = "";
      if (activeTab === 'final' && currentReviewData && currentReviewData.final_review) {
        textToCopy = currentReviewData.final_review;
      } else if (activeTab === 'security' && currentReviewData && currentReviewData.security_review) {
        textToCopy = currentReviewData.security_review;
      } else if (activeTab === 'style' && currentReviewData && currentReviewData.style_review) {
        textToCopy = currentReviewData.style_review;
      } else if (activeTab === 'test' && currentReviewData && currentReviewData.test_review) {
        textToCopy = currentReviewData.test_review;
      } else if (currentReviewData) {
        textToCopy = JSON.stringify(currentReviewData, null, 2);
      }

      if (!textToCopy) {
        alert("No review to copy yet.");
        return;
      }

      navigator.clipboard.writeText(textToCopy).then(() => {
        const copyBtnText = document.getElementById('copyBtnText');
        copyBtnText.innerText = 'Copied!';
        setTimeout(() => { copyBtnText.innerText = 'Copy Review'; }, 2000);
      });
    }

    // Health check ping
    setInterval(async () => {
      try {
        const res = await fetch('/health');
        if (res.ok) {
          document.getElementById('statusText').innerText = 'System Online';
        } else {
          document.getElementById('statusText').innerText = 'System Degraded';
        }
      } catch (e) {
        document.getElementById('statusText').innerText = 'Offline';
      }
    }, 30000);

    // Initial load
    window.addEventListener('DOMContentLoaded', () => {
      loadPreset('security');
    });
  </script>
</body>
</html>
"""
