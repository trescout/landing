# Bypass censorship blocks with DNS tunneling

MasterDnsVPN is a low-load domain name system tunneling (DNS tunneling) virtual private network (VPN) solution developed to bypass censorship barriers. Written in Go language, the tool offers high packet loss stability and resolver load balancing features in data transmission.

- ★ 6,870
- Go
- GitHub Trending · 2026-06-11

## Updates

- **August 2, 2026:** Stars 5,411 → 6,870, latest release v2026.06.13.234407-7de2476 (June 13, 2026).

## What you get

- It provides data transmission in censored networks via DNS tunneling method.
- It offers multipathing and load balancing for low packet loss and high speed.
- Optimized for stable connection even under restricted network conditions.

## Installation

**Automatic Server Setup**

```
bash <(curl -Ls https://raw.githubusercontent.com/masterking32/MasterDnsVPN/main/server_linux_install.sh)
```

**Running with Docker**

```
docker run -d \
  --name masterdnsvpn \
  --restart unless-stopped \
  -e DOMAIN=v.example.com \
  -v $(pwd)/data:/data \
  -p 53:53/tcp \
  -p 53:53/udp \
  ghcr.io/masterking32/masterdnsvpn:latest
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to establish a secure connection via DNS tunneling in a censored network using the MasterDnsVPN tool. How can I configure the server side using the shared auto-install script and what basic steps should I follow to ensure the connection on the client side? Please detail the network requirements I should pay attention to during the installation process and the method of running it via Docker.

Repository: https://github.com/masterking32/MasterDnsVPN. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [DNS Tunneling](https://trescout.com/en/dictionary/dns-tunneling/)
- [Resolver Load Balancing](https://trescout.com/en/dictionary/resolver-load-balancing/)
- [DNS](https://trescout.com/en/dictionary/dns/)
- [VPN](https://trescout.com/en/dictionary/vpn/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for researchers and advanced users who want to provide high stability internet access in restricted network conditions.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/masterking32/MasterDnsVPN)
- [Read in Turkish →](https://trescout.com/discover/masterdnsvpn/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-11: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/masterdnsvpn/
