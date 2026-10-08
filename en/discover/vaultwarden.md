# Password management on your own server

Vaultwarden is an open-source server software compatible with the password management tool Bitwarden and developed in Rust.

- ★ 68,594
- Rust
- GitHub Trending · 2026-08-24

## Updates

- **October 6, 2026:** Stars 67,398 → 68,594, latest release 1.37.4 (October 5, 2026).
- **September 14, 2026:** Stars 65,982 → 67,398, latest release 1.37.3 (September 13, 2026).
- **August 24, 2026:** Stars 65,983 → 65,982, latest release 1.37.2 (August 22, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Help me install Vaultwarden, a tool that provides password management on my own server. This tool is server software compatible with Bitwarden clients. Since I will be installing using Docker, explain step by step how to configure the image commands to pull and run, mounting a volume to persist my data, and taking into account HTTPS requirements.

## Related dictionary terms

- [Rust](https://trescout.com/en/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for users who want to host their own passwords and sensitive data on their own server rather than relying on third-party cloud services.
- **License:** AGPL-3.0

## Links

- [GitHub repository →](https://github.com/dani-garcia/vaultwarden)
- [Read in Turkish →](https://trescout.com/discover/vaultwarden/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-24: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/vaultwarden/
