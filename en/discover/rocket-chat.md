# Secure and customizable team communication

Rocket.Chat offers a secure communications operating system designed for mission-critical operations. The platform, developed with the TypeScript language, aims to centralize internal messaging and collaboration processes.

- ★ 45,919
- TypeScript
- GitHub Trending · 2026-06-18

## Update
- August 2, 2026: Star 45,649 → 45,919, last version 8.6.1 (July 10, 2026).

## What you get
- Data security with end-to-end encryption
- Possibility of hosting on your own server
- Broad integration and application support

## Installation
**Linux · Snap package (publisher of Rocket.Chat)**

```
sudo snap install rocketchat-server
```

**Docker official compose repository**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git && cd rocketchat-compose && cp .env.example .env
```


## Running it
**Launch with Docker**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml -f docker.yml up -d
```


## Getting started
- Official source →
To start installing Rocket.Chat, you can review the Deployment Guide on the official documentation page. You can choose one of the Docker, Podman or Kubernetes methods to host on your own server, or consider the Launchpad option for a faster start. For all technical requirements and detailed installation steps, visit Rocket.Chat's official documentation site.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/rocket-chat/
