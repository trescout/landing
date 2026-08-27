# Centralize Your Game Library

Romm is a game library manager that allows you to organize your retro game collection through a modern and stylish web interface.

- ★ 12,170
- GitHub Trending · 2026-07-04

## What does this tool do?
Romm is a self-hosted game library manager that allows you to organize your retro game collection through a modern and stylish web interface. It automatically fetches game metadata via IGDB integration.

## Who it is for
Retro gaming enthusiasts who want to turn scattered game files into a centralized, visually rich archive.

## What not to expect
Those looking to make digital game purchases or those seeking a client to manage current platforms.

## Highlights
- Offers a modern library interface accessible via a browser.
- Automatically downloads information such as game covers, release dates, and descriptions.
- Provides multi-user support and play history tracking.

## First-use flow
- Download the Docker and Docker Compose files required for Romm.
- Generate the necessary keys for API access and add them to the configuration file.
- Start the service by mounting the directory where your game files are located.
- Log in to the web interface and initiate the first library scan.

## Safe start

## First task prompt
How to add a new platform (e.g., SNES) to the Romm library?

## Installation
**Get sample compose file**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/rommapp/romm/master/examples/docker-compose.example.yml
```


## Running it
**start**

```
docker compose up -d
```


## Links
- GitHub repository →
- Official Romm README →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/romm/
