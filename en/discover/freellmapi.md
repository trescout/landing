# Combine 34 free LLM providers in a single API

FreeLLMAPI brings together 34 different free large language model providers under a single REST API in OpenAI format, offering intelligent routing and fault tolerance.

- ★ 38,000
- TypeScript
- GitHub Trending · 2026-08-28

## Updates

- **October 20, 2026:** Stars 37,418 → 38,000, latest release v0.16.6 (October 20, 2026).
- **October 19, 2026:** Stars 37,306 → 37,418, latest release v0.16.5 (October 19, 2026).
- **October 19, 2026:** Stars 36,776 → 37,306, latest release v0.16.4 (October 19, 2026).
- **October 18, 2026:** Stars 35,948 → 36,776, latest release v0.16.2 (October 18, 2026).

## What you get

- 34 free model providers: Single-point access to dozens of free providers including Google Gemini, Groq, Cloudflare Workers AI and Hugging Face.
- OpenAI REST API compatibility: Ability to work with LangChain, LlamaIndex, and existing AI applications without changing code thanks to the /v1/chat/completions endpoint.
- Smart routing and failure recovery: Automatic failover to an alternative provider when a provider reaches a rate limit or encounters an error.
- Streaming (Server-Sent Events) support: The ability to receive model outputs in real-time, word by word as a stream.
- Lightweight and easy deployment: An architecture that can be set up in seconds on a local computer or server using Docker or Node.js.

## Installation

**Cloning the repository and installing dependencies**

```
git clone https://github.com/tashfeenahmed/freellmapi.git
cd freellmapi
npm install
```

## Running it

**Starting the service and querying the model**

```
npm start
# OpenAI uyumlu istek:
curl http://localhost:3000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Merhaba!"}]}'
```

## Technical architecture and working principle

- Provider Adapter Layer: An extensible architecture that normalizes different REST and WebSocket APIs into a common JSON response format.
- Dynamic Load Balancing and Quota Monitoring: Tracking each provider's real-time speed limits to route requests to the fastest-responding active model.
- Built-in Caching and Error Handling: Caching repeated queries and an automatic retry mechanism for timeouts.

## Model routing and fault tolerance mechanism

- Multi-Model Comparison: Send the same user input to different open-source models to measure response quality and latency.
- Savings During Development and Prototyping: Quickly launch AI-powered prototypes and MVP projects without defining paid API keys.
- Fallback Pipeline: Ensure your system switches to secondary models without interruption when the primary provider goes down.

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

Could you explain with code examples how to run FreeLLMAPI on my local server using Docker, how to direct the OpenAI Node.js SDK to this local endpoint, and how to enable automatic fallback model usage when a provider errors out?

Repository: https://github.com/tashfeenahmed/freellmapi. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Frequently asked questions

- Do I need to buy an API key to use FreeLLMAPI? No. The system brings together 34 artificial intelligence models that offer a free tier or provide public free inference.
- Which large language models are supported? Popular models such as Llama 3, Mistral, Gemma, open-weight models like Claude, and the Google Gemini free tier are supported.
- Is it suitable for enterprise privacy? FreeLLMAPI is open-source and runs on your local network, but the underlying free providers' own terms of use and privacy policies apply.
- Is it compatible with LangChain or CrewAI? Yes. Since it provides full OpenAI REST API emulation, it can be used directly with all LLM frameworks by setting the baseURL address to localhost:3000/v1.

## Related dictionary terms

- [Pipeline](https://trescout.com/en/dictionary/pipeline/)
- [Proxy](https://trescout.com/en/dictionary/proxy/)
- [Localhost](https://trescout.com/en/dictionary/localhost/)
- [SDK](https://trescout.com/en/dictionary/sdk/)
- [LLM](https://trescout.com/en/dictionary/llm/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)

- **Who it is for:** AI developers, open-source researchers, full-stack engineers, and prototype developers.
- **License:** MIT (Özgür açık kaynak lisansı)
- **Framework:** TypeScript / Node.js Reverse Proxy
- **Platforms:** Docker, Linux, macOS, Windows

## Links

- [GitHub repository →](https://github.com/tashfeenahmed/freellmapi)
- [Read in Turkish →](https://trescout.com/discover/freellmapi/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-28: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/freellmapi/
