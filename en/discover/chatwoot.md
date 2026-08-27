# Open source customer support platform

Chatwoot is an open source platform that offers live chat, email support and omni-channel desk management. Developed as an alternative to commercial software such as Intercom and Zendesk, this tool allows you to manage customer interactions from a single center.

- ★ 36,253
- GitHub Trending · 2026-06-12

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
Answer questions by pretending to be a customer support representative. As the Captain AI assistant on Chatwoot, automatically resolve frequently asked questions and direct complex issues to relevant teammates. Improve customer support experience by always providing courteous, prompt and accurate information.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/chatwoot/
