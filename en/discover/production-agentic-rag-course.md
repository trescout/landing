# Bringing smart data with artificial intelligence

Production-agentic-rag-course offers hands-on training in the development of agent-based fetch-assisted production (agentic RAG) systems that automate the processes of retrieving information from complex data sources. Based on the Python language, this resource teaches the technical architecture required to create scalable and production-level artificial intelligence applications.

- ★ 9,265
- GitHub Trending · 2026-06-03

## Updates

- **October 3, 2026:** Stars 8,216 → 9,265, latest release week7.0 (November 26, 2025).
- **August 2, 2026:** Stars 6,536 → 8,216, latest release week7.0 (November 26, 2025).

## What you get

- Establishing the necessary infrastructure for RAG systems at the production level.
- Applying hybrid search and intelligent data processing methods.
- Developing agent-based decision mechanisms with LangGraph.

## Installation

**Cloning and installing the repository**

```
git clone <repository-url>
cd arxiv-paper-curator

# 2. Configure environment (IMPORTANT!)
cp .env.example .env
# The .env file contains all necessary configuration for OpenSearch, 
# arXiv API, and service connections. Defaults work out of the box.
# You need to add Jina embeddings free api key and langfuse keys (check the blogs)

# 3. Install dependencies
uv sync

# 4. Start all services
docker compose up --build -d

# 5. Verify everything works
curl http://localhost:8000/api/v1/health
```

## Running it

**Play content from a specific week**

```
git clone --branch <WEEK_TAG> https://github.com/jamwithai/arxiv-paper-curator
cd arxiv-paper-curator
uv sync
docker compose down -v
docker compose up --build -d

# Replace <WEEK_TAG> with: week1.0, week2.0, etc.
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to develop an academic research assistant using the production-agentic-rag-course project. For the basic installation of the project, after downloading the repository with the git clone command, I need to configure the .env file and install the dependencies with uv sync. Then, I want to verify that the system is working at http://localhost:8000/api/v1/health by starting all services with the docker compose up --build -d command. Can you guide me about the API keys and service configurations I should pay attention to in this process?

## Related dictionary terms

- [Clone](https://trescout.com/en/dictionary/clone/)
- [Agentic](https://trescout.com/en/dictionary/agentic/)
- [Localhost](https://trescout.com/en/dictionary/localhost/)
- [RAG](https://trescout.com/en/dictionary/rag/)
- [API](https://trescout.com/en/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** For AI engineers and developers who want to develop production-grade, scalable, and agent-based RAG systems.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/jamwithai/production-agentic-rag-course)
- [Read in Turkish →](https://trescout.com/discover/production-agentic-rag-course/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-03: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/production-agentic-rag-course/
