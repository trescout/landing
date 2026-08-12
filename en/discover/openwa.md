# Open source gateway for WhatsApp

OpenWA offers a free and open source API gateway solution for the WhatsApp messaging protocol. This tool, developed with TypeScript language, allows users to manage WhatsApp integrations on their own servers (self-hosted).

- ★ 12,674
- TypeScript
- GitHub Trending · 2026-06-17

## Update
- 12 August 2026: Star 12.605 → 12.674, latest version v0.16.0 (11 August 2026).
- August 10, 2026: Star 12,552 → 12,605, last version v0.15.0 (August 9, 2026).
- August 8, 2026: Star 12,544 → 12,552, latest version v0.14.6 (August 8, 2026).
- August 8, 2026: Star 12,503 → 12,544, latest version v0.14.5 (August 8, 2026).

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
I want to automate my messaging processes via WhatsApp using the OpenWA tool. Walk me through the basic configuration steps required to create a new session, send messages, and listen to incoming messages via webhook using REST API endpoints. Tell me what I need to pay attention to, especially regarding multi-session management and API key security.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/openwa/
