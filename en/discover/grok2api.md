# Central management for Grok services

Developed for Grok Build, Grok Web and Grok Console platforms, this gateway (API gateway) gathers multi-account management in a single center. Written in Go language, the tool offers a manageable interface by standardizing users' access to different Grok services.

- ★ 7,543
- Go
- GitHub Trending · 2026-07-15

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
I completed the Grok2API installation and logged in to the admin panel. Now, how can I define my Grok Build, Web or Console accounts to the system, how do I make model matches, and what steps can I follow to generate the API key for external use? Please explain this process step by step.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/grok2api/
