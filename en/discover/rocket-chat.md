# Secure and customizable team communication

Rocket.Chat offers a secure communications operating system designed for mission-critical operations. The platform, developed with the TypeScript language, aims to centralize internal messaging and collaboration processes.

- ★ 46,064
- TypeScript
- GitHub Trending · 2026-06-18

## What you get
- Data security with end-to-end encryption
- Possibility of hosting on your own server
- Broad integration and application support

## Installation
**Clone official Compose repo**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git
```

**Create environment file**

```
cd rocketchat-compose
cp .env.example .env
```

**Start MongoDB and Rocket.Chat services**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml up -d
```


## Running it
**Access Local UI**

```
http://localhost:3000
```


## Getting started
- Official source →

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/rocket-chat/
