# Inference server for AI agents

Developed by Superlinked, SIE is an open-source inference server and production cluster used to run the models required by AI agents. This Python-based structure aims to manage complex model deployments and provide a scalable infrastructure.

- ★ 3,198
- Python
- GitHub Trending · 2026-09-03

## What you get
- Manages open-source models through a single cluster
- Provides easy integration thanks to its OpenAI-compatible interface
- Supports tasks such as search, data extraction, and text generation

## Installation
**SDK installation**

```
pip install sie-sdk                # Python
npm install @superlinked/sie-sdk   # TypeScript (pnpm and yarn work too)
```


## Running it
**First deployment attempt**

```
curl http://localhost:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model": "sentence-transformers/all-MiniLM-L6-v2", "input": "Hello world"}'
# {"object": "list", "data": [{"object": "embedding", "embedding": [-0.0344, 0.0310, ...
```


## If you don't write code
I want to run a model for an AI agent via the SIE server. How can I manage the tasks my agent needs, such as search, data extraction, and text generation, through a single API? How can I configure the embedding creation and text generation processes using the OpenAI-compatible endpoints provided by SIE?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/sie/
