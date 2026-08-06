# App deployment on your own server

OpenShip offers an application distribution platform that users can host on their own servers. This tool, developed with the TypeScript language, facilitates self-hosting processes as an alternative to cloud-based infrastructure services.

- ★ 10,135
- TypeScript
- GitHub Trending · 2026-07-21

## Update
- August 2, 2026: Star 5,130 → 10,135, latest version v0.5.0 (July 31, 2026).

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
I want to publish a project using Openship. While in the project directory, is it enough to connect the directory to the project with the openship init command and then run the openship deploy command? Can you explain step by step how the database and SSL configuration are automatically managed in this process?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/openship/
