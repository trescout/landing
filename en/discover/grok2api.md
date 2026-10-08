# Central management for Grok services

Developed for Grok Build, Grok Web and Grok Console platforms, this gateway (API gateway) gathers multi-account management in a single center. Written in Go language, the tool offers a manageable interface by standardizing users' access to different Grok services.

- ★ 7,669
- Go
- GitHub Trending · 2026-07-15

## Updates

- **September 16, 2026:** Stars 7,543 → 7,669, latest release v3.1.6 (September 16, 2026).
- **August 27, 2026:** Stars 7,459 → 7,543, latest release v3.1.5 (August 25, 2026).
- **August 19, 2026:** Stars 7,447 → 7,459, latest release v3.1.4 (August 19, 2026).
- **August 18, 2026:** Stars 7,239 → 7,447, latest release v3.1.3 (August 17, 2026).

## What you get

- Grok Build combines Web and Console accounts in one panel
- Provides standard API interface compatible with OpenAI and Anthropic
- Provides advanced account management, model routing and error handling

## Installation

**Quick installation with Docker**

```
git clone https://github.com/chenyme/grok2api.git
cd grok2api
cp config.example.yaml config.yaml
```

**Start the service**

```
docker compose pull
docker compose up -d
```

## Running it

**service management**

```
docker compose logs -f grok2api
docker compose restart grok2api
docker compose down
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I completed the Grok2API installation and logged in to the admin panel. Now, how can I define my Grok Build, Web or Console accounts to the system, how do I make model matches, and what steps can I follow to generate the API key for external use? Please explain this process step by step.

## Related dictionary terms

- [API Gateway](https://trescout.com/en/dictionary/api-gateway/)
- [Gateway](https://trescout.com/en/dictionary/gateway/)
- [API](https://trescout.com/en/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers who want to manage multiple Grok accounts and use these services in their applications via a standard API.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/chenyme/grok2api)
- [Read in Turkish →](https://trescout.com/discover/grok2api/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-15: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/grok2api/
