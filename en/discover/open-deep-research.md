# In-depth research with autonomous artificial intelligence

Developed by LangChain, open-deep-research is an autonomous system that performs multi-step searches on the internet to answer complex questions. It facilitates deep research processes by automating the research process through planning, data collection and synthesis stages.

- ★ 12,655
- Python
- GitHub Trending · 2026-07-22

## What you get
- Multi-step autonomous research for complex questions
- Compatibility with different model providers and search tools
- Research processes visualized via LangGraph

## Installation
**Cloning the repository and preparing the environment**

```
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Installing dependencies**

```
uv sync
# or
uv pip install -r pyproject.toml
```


## Running it
**Starting the server**

```
# Install dependencies and start the LangGraph server
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
```


## If you don't write code
Conduct an in-depth analysis of [WRITE YOUR RESEARCH TOPIC HERE] using the Open Deep Research tool. Plan your research process, collect data online, and synthesize your findings to create a comprehensive report.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/open-deep-research/
