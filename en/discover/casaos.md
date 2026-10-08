# Manage your personal cloud server

CasaOS is an open-source, lightweight, and elegant personal cloud operating system that enables one-click management of Docker-based applications on home servers, mini PCs, and Raspberry Pi devices. Developed in the Go programming language, the platform allows you to establish your own digital sovereignty without the need for complex terminal commands.

- ★ 36,953
- Go
- GitHub Trending · 2026-06-26

## Updates

- **August 2, 2026:** Stars 34,992 → 36,953, latest release v0.4.15 (December 19, 2024).

## What you get

- Rich app store with a single click: Install Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant and over 100 popular self-hosted services in seconds.
- Elegant and intuitive web control panel: Live-track CPU, RAM load, disk usage rates, network activity, and running containers through stylish widget cards.
- Visual storage and file management: Automatically mount external hard drives and USB drives, and share your folders over the local network with your Windows/Mac devices using the Samba (SMB) protocol.
- Custom Docker Compose support: Effortlessly bring your custom containers to life by pasting any Docker Compose file not found in the official store directly into the web interface.
- Lightweight Go core and zero system overhead: Delivering smooth performance even on the most modest Raspberry Pi 4/5 or older laptops by consuming minimal memory in the background.

## Installation

**installation command**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Running it

**update command**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Technical architecture and working principle

- Go microservice architecture: The CasaOS Core (CasaOS-Gateway, MessageBus, LocalStorage, and UserService) consists of lightweight Go services operating independently. Inter-service communication takes place via REST and WebSocket.
- Container lifecycle abstraction: By communicating directly with the Docker daemon, it automatically detects port conflicts and translates environment variables and persistent volume mount paths into user-friendly forms.
- The ZimaOS and IceWhale ecosystem: Backed by IceWhale Technology, the manufacturer of ZimaBoard and ZimaBlade hardware, the project ensures full compatibility with local cloud hardware.
- Smart disk pooling: Combines hard drives of different sizes into a single logical storage pool, creating flexible space for home media and backup.

## Step-by-step guide to setting up your own home server

- Basic Linux installation: Install a clean Ubuntu Server or Debian minimal on your device and connect it to your local network via an Ethernet cable.
- Single-line CasaOS installation: Run the official installation script via the terminal; the script automatically configures Docker and dependencies.
- Accessing the interface from the browser: Create your first administrator account by typing your server's IP address (e.g., http://192.168.1.100) into your browser from any computer on the network.
- Deploying applications: Go to the App Store tab and install your personal cloud with Nextcloud and your movie/TV show library with Jellyfin with a single click.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

CasaOS is installed on my personal home server. I want to install and configure AdGuard Home (ad blocker), Jellyfin (media streaming), and Tailscale (secure remote access) services for all devices in my home. Could you explain step by step how to install these services via custom Docker Compose or the app store from the CasaOS web panel, and how to set up disk sharing?

## Frequently asked questions

- Does CasaOS delete my existing Linux operating system or data? No. CasaOS does not delete your existing operating system; it is installed on top of it as a desktop and Docker management layer. Existing files on your disks are preserved and made accessible via the panel.
- How can I safely access my CasaOS server when I am away from home? Instead of insecure port forwarding, you can install Tailscale or WireGuard on CasaOS with a single click. This way, you can access the dashboard from anywhere in the world via an encrypted VPN tunnel as if you were on your home network.
- What is the difference between CasaOS and TrueNAS or Unraid? TrueNAS and Unraid are standalone operating systems focused on deep storage management and RAID configurations. CasaOS, on the other hand, offers a lightweight, extremely easy-to-use, and application-centric home cloud experience.
- Do installed applications start automatically after a power outage? Yes. All Docker containers on CasaOS are started with the restart: unless-stopped policy by default. When your server restarts, all your services automatically continue running from where they left off.

## Related dictionary terms

- [VPN](https://trescout.com/en/dictionary/vpn/)
- [RAM](https://trescout.com/en/dictionary/ram/)
- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [CPU](https://trescout.com/en/dictionary/cpu/)
- [Terminal](https://trescout.com/en/dictionary/terminal/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)

- **Who it is for:** It is intended for users who want to set up a home server (Homelab) or a personal cloud, avoiding terminal complexity and aiming to manage Docker applications with a single click.
- **License:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı)
- **Developer:** IceWhale Technology and Open Source Community
- **Supported Systems:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7)

## Links

- [GitHub repository →](https://github.com/IceWhaleTech/CasaOS)
- [Read in Turkish →](https://trescout.com/discover/casaos/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-26: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/casaos/
