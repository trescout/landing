# Router that manages artificial intelligence traffic

Developed by NVIDIA, Switchyard is a high-performance artificial intelligence inference engine written in Rust language. It offers an optimized runtime environment to run large language models (LLM) efficiently on different hardware infrastructures.

- ★ 2,617
- Rust
- GitHub Trending · 2026-08-13

## What you get
- Routing traffic between different artificial intelligence models
- Translation between OpenAI and Anthropic API formats
- Track transaction metrics and error logs

## Installation
**Installation as command line tool**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv tool install --python 3.10 "nemo-switchyard[cli]"
```

**Installation as server**

```
cargo install --locked switchyard-server
switchyard-server --help
```


## Running it
**Check server status**

```
curl http://localhost:4000/health
```


## If you don't write code
Act as an AI traffic router for me. Using Switchyard, I want you to distribute the requests of my coding agents like Claude Code or Codex between different models, automatically translate between OpenAI and Anthropic API formats, and monitor all operational metrics. Manage incoming requests with structured routing algorithms and perform A/B testing or load balancing between different models when necessary.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/switchyard/
