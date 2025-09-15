Multi-Tool Agents (LM Studio, Ollama) — Setup Guide

### Overview
This repo contains two minimal Google ADK agents that expose simple tools (`get_weather`, `get_current_time`) and differ only by the backing local LLM provider:
- `multi_tool_agent_lm_studio`: targets an LM Studio OpenAI-compatible endpoint
- `multi_tool_agent_ollama`: targets an Ollama endpoint

Both agents define a `root_agent` you can import and invoke in your own code, or use with ADK tooling.

### Prerequisites
- Python 3.11+
- macOS/Linux shell
- One of the following local LLM runtimes installed and running:
  - LM Studio with the OpenAI-compatible server enabled
  - Ollama with a model pulled locally

### 1) Clone and install
```bash
cd /Users/lt68905/Dev_Playground/LearnPython/sample-adk
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### 2) Configure environment

You only need to set variables for the agent you intend to use.

- LM Studio agent (`multi_tool_agent_lm_studio`):
  - `LM_STUDIO_MODEL`: the model identifier as seen in LM Studio
  - `OPENAI_API_BASE`: base URL of LM Studio’s OpenAI-compatible server (e.g., `http://localhost:1234/v1`)

```bash
export LM_STUDIO_MODEL="your-lmstudio-model-name"
export OPENAI_API_BASE="http://localhost:1234/v1"
```

- Ollama agent (`multi_tool_agent_ollama`):
  - `OLLAMA_MODEL`: the Ollama model name (e.g., `llama3.1`)
  - If you have an OpenAI-compatible endpoint proxy for Ollama, set `OPENAI_API_BASE` accordingly; otherwise omit.

```bash
export OLLAMA_MODEL="llama3.1"
# Optional if using an OpenAI-compatible proxy for Ollama
# export OPENAI_API_BASE="http://localhost:11434/v1"
```

### 3) Start your local LLM runtime
- LM Studio: open LM Studio, download a chat/instruct model, then start the server (OpenAI-compatible) and note the Base URL.
- Ollama: `ollama pull llama3.1` (or your model), then `ollama run llama3.1` at least once to ensure it’s available.

### 4) Quick usage (Python)

Run one of the following from an interactive shell or a short script.

- Using LM Studio agent:
```python
from multi_tool_agent_lm_studio.agent import root_agent

user_question = "What's the weather in New York and the current time?"
response = root_agent.run(user_question)  # Requires LM Studio env vars
print(response)
```

- Using Ollama agent:
```python
from multi_tool_agent_ollama.agent import root_agent

user_question = "What's the weather in New York and the current time?"
response = root_agent.run(user_question)  # Requires OLLAMA_MODEL env var
print(response)
```

Notes:
- The provided tools are intentionally simple. Weather is only implemented for "New York"; time is only implemented for "New York".
- The agent’s behavior depends on the local LLM you configure via environment variables.

### 5) Optional: ADK Web UI
Google ADK includes a simple web UI. After setting the appropriate environment for the agent you want to try, you can launch:
```bash
adk web
```
If your ADK install requires selecting the agent entry-point, set your Python path to include this folder or run from the repo root so the packages `multi_tool_agent_lm_studio` and `multi_tool_agent_ollama` are importable.

### Troubleshooting
- If requests fail, verify your local LLM endpoint is up and that `OPENAI_API_BASE` (if used) matches it.
- Ensure the model names in `LM_STUDIO_MODEL` or `OLLAMA_MODEL` exactly match what your runtime expects.
- Recreate your virtual environment if dependencies conflict.