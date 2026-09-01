# Modern and Open Source CRM

Twenty is an open source Salesforce alternative that allows technical teams to build a modern CRM that can be customized to their business processes. You can host this system, which focuses on artificial intelligence-supported workflows, on your own server.

- ★ 55,953
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## What you get
- A free and open source alternative to Salesforce.
- Full control over your data with the self-host option.
- Modern workflows powered by AI.
- Flexible building blocks that can be adapted to your business needs.

## Installation
**Download environment template**

```
curl -o .env https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/.env.example
```

**Download Compose file**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/docker-compose.yml
```

**Generate encryption key**

```
openssl rand -base64 32
```

**Start services**

```
docker compose up -d
```


## Running it
**Access Local UI**

```
http://localhost:3000
```


## How to install?
It is usually installed on your own server with Docker; installation steps are in the documentation. It requires some technical knowledge to manage.

## How to install, how to use?
I want to install an open source CRM called Twenty; create a new app in the terminal with the command 'npx create-twenty-app my-app', then publish it to my workspace with 'npx twenty app:publish --private'. Also tell me how to run it with Docker Compose for self-hosting.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/twenty/
