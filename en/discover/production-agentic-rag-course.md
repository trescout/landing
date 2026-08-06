# Bringing smart data with artificial intelligence

Production-agentic-rag-course offers hands-on training in the development of agent-based fetch-assisted production (agentic RAG) systems that automate the processes of retrieving information from complex data sources. Based on the Python language, this resource teaches the technical architecture required to create scalable and production-level artificial intelligence applications.

- ★ 8,216
- GitHub Trending · 2026-06-03

## Update
- August 2, 2026: Star 6,536 → 8,216, last version week7.0 (November 26, 2025).

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
I want to develop an academic research assistant using the production-agentic-rag-course project. For the basic installation of the project, after downloading the repository with the git clone command, I need to configure the .env file and install the dependencies with uv sync. Then, I want to verify that the system is working at http://localhost:8000/api/v1/health by starting all services with the docker compose up --build -d command. Can you guide me about the API keys and service configurations I should pay attention to in this process?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/production-agentic-rag-course/
