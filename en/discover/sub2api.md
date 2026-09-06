# Manage AI subscriptions from a single center

Sub2API is an open source intermediary service that provides single-point access and cost sharing to Claude, OpenAI, Gemini and Grok subscriptions.

- ★ 40,573
- Go
- GitHub Trending · 2026-08-23

## What you get
- Combines different AI subscriptions in one interface
- Helps you allocate subscription costs efficiently
- Offers the opportunity to work integrated with existing tools

## Installation
**automatic installation**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

**Installation with Docker**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
```


## Running it
**Start the service**

```
docker compose up -d
```

**View administrator password**

```
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```


## If you don't write code
How can I configure different AI services such as Claude, OpenAI, Gemini and Grok through a single API gateway using the Sub2API platform? Explain the basic steps I need to follow to efficiently allocate my subscription quotas and integrate them with my existing software tools. Also, summarize the legal and technical issues I need to pay attention to in order to comply with the terms of service of providers such as Anthropic when using this platform.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/sub2api/
