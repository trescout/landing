# Open source customer support platform

Chatwoot is an open source platform that offers live chat, email support and omni-channel desk management. Developed as an alternative to commercial software such as Intercom and Zendesk, this tool allows you to manage customer interactions from a single center.

- ★ 38,153
- GitHub Trending · 2026-06-12

**TreScout note:** It collects messages from customers on a single screen: Site chat, e-mail, WhatsApp. Ready-made services that do the same job charge a monthly fee per person, but since it runs on your own server, there is no such fee, in return the server and maintenance become your job. Its installation is not monolithic, requires several utilities, and has difficulty with the cheapest server packages.

## Updates

- **October 24, 2026:** Stars 38,048 → 38,153, latest release v4.19.1 (October 24, 2026).
- **October 21, 2026:** Stars 36,927 → 38,048, latest release v4.19.0 (October 20, 2026).
- **September 18, 2026:** Stars 36,253 → 36,927, latest release v4.18.0 (September 18, 2026).
- **August 27, 2026:** Stars 36,001 → 36,253, latest release v4.17.1 (August 27, 2026).

## What you get

- It combines all customer channels into a single inbox.
- Automatically answers routine questions with an artificial intelligence-supported assistant.
- It gives you full control over your customer data by hosting it on your own server.

## Installation

**Download environment file**

```
wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example
```

**Download Docker Compose file**

```
wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml
```

**Prepare Database**

```
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
```

## Running it

**Start services**

```
docker compose up -d
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

Answer questions by pretending to be a customer support representative. As the Captain AI assistant on Chatwoot, automatically resolve frequently asked questions and direct complex issues to relevant teammates. Improve customer support experience by always providing courteous, prompt and accurate information.

Repository: https://github.com/chatwoot/chatwoot. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Omni-channel Desk](https://trescout.com/en/dictionary/omni-channel-desk/)
- [Omni-channel](https://trescout.com/en/dictionary/omni-channel/)
- [Deployment](https://trescout.com/en/dictionary/deployment/)
- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for businesses that want to manage customer interactions from a single center and automate support processes.

## Links

- [GitHub repository →](https://github.com/chatwoot/chatwoot)
- [Read in Turkish →](https://trescout.com/discover/chatwoot/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-12: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/chatwoot/
