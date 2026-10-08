# App deployment on your own server

OpenShip offers an application distribution platform that users can host on their own servers. This tool, developed with the TypeScript language, facilitates self-hosting processes as an alternative to cloud-based infrastructure services.

- ★ 14,584
- TypeScript
- GitHub Trending · 2026-07-21

## Updates

- **October 7, 2026:** Stars 14,558 → 14,584, latest release v0.8.2 (October 6, 2026).
- **October 6, 2026:** Stars 13,545 → 14,558, latest release v0.8.0 (September 27, 2026).
- **September 29, 2026:** Stars 12,541 → 13,545, latest release v0.8.0 (September 27, 2026).
- **September 27, 2026:** Stars 12,135 → 12,541, latest release v0.8.0 (September 27, 2026).

## What you get

- Automated CI/CD processes
- Quick transition from code to container
- Database and SSL management

## Installation

**Quick installation via CLI**

```
npm i -g openship     # or: curl -fsSL https://get.openship.io | sh
openship up           # installs Openship as a background service (starts on boot, auto-restarts)
```

**Installation with Docker**

```
git clone https://github.com/oblien/openship.git && cd openship
cp .env.example .env
docker compose up -d
```

## Running it

**Start project deployment**

```
cd your-project
openship init         # link this directory to a project
openship deploy
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to publish a project using Openship. While in the project directory, is it enough to connect the directory to the project with the openship init command and then run the openship deploy command? Can you explain step by step how the database and SSL configuration are automatically managed in this process?

## Related dictionary terms

- [Deployment Platform](https://trescout.com/en/dictionary/deployment-platform/)
- [Deployment](https://trescout.com/en/dictionary/deployment/)
- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [CI/CD](https://trescout.com/en/dictionary/ci-cd/)
- [CLI](https://trescout.com/en/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for software developers who want to host applications on their own servers and want to deploy quickly without dealing with complex configuration files.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/oblien/openship)
- [Read in Turkish →](https://trescout.com/discover/openship/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-21: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/openship/
