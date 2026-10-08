# Open source gateway for WhatsApp

OpenWA offers a free and open source API gateway solution for the WhatsApp messaging protocol. This tool, developed with TypeScript language, allows users to manage WhatsApp integrations on their own servers (self-hosted).

- ★ 14,976
- TypeScript
- GitHub Trending · 2026-06-17

## Updates

- **October 3, 2026:** Stars 14,622 → 14,976, latest release v0.24.0 (October 3, 2026).
- **September 27, 2026:** Stars 14,197 → 14,622, latest release v0.23.7 (September 25, 2026).
- **September 16, 2026:** Stars 13,775 → 14,197, latest release v0.23.5 (September 15, 2026).
- **September 5, 2026:** Stars 13,239 → 13,775, latest release v0.23.4 (September 5, 2026).

## What you get

- Full control over WhatsApp messaging infrastructure
- Session and webhook management with modern interface
- Quick and easy installation with Docker support

## Installation

**Quick installation with Docker**

```
# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

**Local development environment**

```
# Clone repository
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA

# Install dependencies (includes dashboard)
npm install

# Start API + Dashboard (config is auto-generated on first run)
npm run dev

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

## Running it

**Launching in a production environment**

```
# Basic production (SQLite, local storage)
docker compose up -d

# With PostgreSQL database
docker compose --profile postgres up -d

# Full stack (PostgreSQL, Redis, Dashboard, Traefik)
docker compose --profile full up -d
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to automate my messaging processes via WhatsApp using the OpenWA tool. Walk me through the basic configuration steps required to create a new session, send messages, and listen to incoming messages via webhook using REST API endpoints. Tell me what I need to pay attention to, especially regarding multi-session management and API key security.

## Related dictionary terms

- [API Gateway](https://trescout.com/en/dictionary/api-gateway/)
- [Gateway](https://trescout.com/en/dictionary/gateway/)
- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [API](https://trescout.com/en/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers who want to develop their own WhatsApp integrations and aim to have full control over the messaging infrastructure.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/rmyndharis/OpenWA)
- [Read in Turkish →](https://trescout.com/discover/openwa/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-17: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/openwa/
