# Central management for Grok services

Developed for Grok Build, Grok Web and Grok Console platforms, this gateway (API gateway) gathers multi-account management in a single center. Written in Go language, the tool offers a manageable interface by standardizing users' access to different Grok services.

- ★ 7,840
- Go
- GitHub Trending · 2026-07-15

## Updates

- **October 22, 2026:** Stars 7,817 → 7,840, latest release v3.1.8 (October 22, 2026).
- **October 18, 2026:** Stars 7,669 → 7,817, latest release v3.1.7 (October 18, 2026).
- **September 16, 2026:** Stars 7,543 → 7,669, latest release v3.1.6 (September 16, 2026).
- **August 27, 2026:** Stars 7,459 → 7,543, latest release v3.1.5 (August 25, 2026).

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

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I completed the Grok2API installation and logged in to the admin panel. Now, how can I define my Grok Build, Web or Console accounts to the system, how do I make model matches, and what steps can I follow to generate the API key for external use? Please explain this process step by step.

Repository: https://github.com/chenyme/grok2api. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

If an API key is required, do not ask me to type it into the chat. Show me how to add it to the .env file and ensure this file is not pushed to Git.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

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

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-15: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/grok2api/
