# Router that manages artificial intelligence traffic

Developed by NVIDIA, Switchyard is a high-performance artificial intelligence inference engine written in Rust language. It offers an optimized runtime environment to run large language models (LLM) efficiently on different hardware infrastructures.

- ★ 3,227
- Rust
- GitHub Trending · 2026-08-13

## Updates

- **September 27, 2026:** Stars 2,617 → 3,227, latest release v0.3.0 (September 22, 2026).
- **August 31, 2026:** Stars 1,566 → 2,617, latest release v0.2.0 (August 10, 2026).
- **August 15, 2026:** Stars 923 → 1,566, latest release v0.2.0 (August 10, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Act as an AI traffic router for me. Using Switchyard, I want you to distribute the requests of my coding agents like Claude Code or Codex between different models, automatically translate between OpenAI and Anthropic API formats, and monitor all operational metrics. Manage incoming requests with structured routing algorithms and perform A/B testing or load balancing between different models when necessary.

## Related dictionary terms

- [Inference](https://trescout.com/en/dictionary/inference/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [LLM](https://trescout.com/en/dictionary/llm/)
- [Rust](https://trescout.com/en/dictionary/rust/)
- [API](https://trescout.com/en/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers who want to efficiently manage large language models across different hardware and service providers.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/NVIDIA-NeMo/Switchyard)
- [Read in Turkish →](https://trescout.com/discover/switchyard/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-13: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/switchyard/
