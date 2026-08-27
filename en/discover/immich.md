# Photo and Video Backup on Your Own Server

Immich is a high-performance solution designed for backing up your personal photos and videos, which you can host directly on your own server.

- ★ 109,538
- GitHub Trending · 2026-07-05

## What does this tool do?
Immich is a high-performance solution designed for backing up your personal photos and videos, which you can host directly on your own server. It allows you to manage your media library via mobile and web applications.

## Who it is for
Those who want to store and manage their photos and videos on their own hardware instead of third-party cloud services.

## What not to expect
Users who do not want to manage their own server or deal with technical installation processes.

## Highlights
- Backs up photos and videos in their original quality.
- Provides access via web and mobile applications.
- Ensures data privacy by being hosted on your own hardware.
- Creates spaces for family members or teams with multi-user support.

## First-use flow
- Ensure that you meet the hardware requirements specified in the official documentation.
- Start the Immich containers using Docker and Docker Compose.
- Download the mobile application to your device and connect by entering your server address.
- Create the first administrator account and start the backup process.

## Safe start

## First task prompt
How to add a new user in an Immich installation?

## Installation
**Download Docker Compose configuration**

```
mkdir immich-app && cd immich-app
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```


## Running it
**Start Docker services**

```
docker compose up -d
```


## Links
- GitHub repository →
- Official Immich README →
- Official Immich Website →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/immich/
