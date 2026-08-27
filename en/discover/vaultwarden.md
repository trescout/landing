# Password management on your own server

An abstract for this item could not be produced today · see the source link for details.

- ★ 65,982
- Rust
- GitHub Trending · 2026-08-24

## What you get
- Fully compatible with official Bitwarden clients
- Can be hosted on your own server with low resource consumption
- Offers two-factor authentication and emergency access

## Installation
**Download and run the container**

```
docker pull vaultwarden/server:latest
docker run --detach --name vaultwarden \
  --env DOMAIN="https://vw.domain.tld" \
  --volume /vw-data/:/data/ \
  --restart unless-stopped \
  --publish 127.0.0.1:8000:80 \
  vaultwarden/server:latest
```


## If you don't write code
Help me install Vaultwarden, a tool that provides password management on my own server. This tool is server software compatible with Bitwarden clients. Since I will be installing using Docker, explain step by step how to configure the image commands to pull and run, mounting a volume to persist my data, and taking into account HTTPS requirements.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/vaultwarden/
