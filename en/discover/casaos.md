# Manage your personal cloud server

CasaOS is an open-source, lightweight, and elegant personal cloud operating system designed to manage Docker-based applications with a single click on home servers, mini PCs, and Raspberry Pi devices. Built with Go, the platform allows you to establish digital sovereignty without wrestling with complex terminal commands.

- ★ 36,953
- Go
- GitHub Trending · 2026-06-26

## Updates
- August 2, 2026: Stars 34,992 → 36,953, latest release v0.4.15 (December 19, 2024).

## What you get
- One-click rich app store: Install Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant, and over 100 popular self-hosted services in seconds.
- Clean and intuitive web dashboard: Monitor CPU load, RAM usage, storage capacity, network activity, and running containers in real time through elegant widget cards.
- Visual storage and file management: Automatically mount external HDDs and USB drives, and share folders across Windows and Mac devices via Samba (SMB).
- Custom Docker Compose support: Deploy custom containers effortlessly by pasting any Docker Compose file directly into the web interface.
- Lightweight Go core and low overhead: Operates smoothly with minimal memory footprint even on modest Raspberry Pi 4/5 units or repurposed older laptops.

## Installation

**Installation command**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Running it

**Update command**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Technical architecture and working principle

Rather than providing a standalone Linux kernel from scratch, CasaOS functions as a modern Docker orchestration layer on top of your existing Debian, Ubuntu, or Raspberry Pi OS installation. This approach ensures native hardware driver compatibility while organizing system duties through a modular microservice architecture:
- Go microservices architecture: CasaOS Core (CasaOS-Gateway, MessageBus, LocalStorage, and UserService) consists of independent lightweight Go services communicating via REST and WebSockets.
- Container lifecycle abstraction: Communicates directly with the Docker daemon to automatically resolve port conflicts and translate environment variables and volume mounts into user-friendly UI fields.
- ZimaOS and IceWhale ecosystem: Backed by IceWhale Technology (makers of ZimaBoard and ZimaBlade), the project ensures seamless synergy with local cloud hardware.
- Smart storage merging: Aggregates storage drives of different sizes into a unified logical storage pool for flexible media streaming and local backups.

## Step-by-step home server setup guide

To transform an old PC or mini PC into a full-featured personal cloud, follow these fundamental steps:
- Base Linux installation: Install a clean copy of Ubuntu Server or minimal Debian on your machine and connect it to your local network via Ethernet.
- One-line CasaOS setup: Run the official installation script in the terminal; it automatically installs and configures Docker and all dependencies.
- Browser dashboard access: Open a browser on any local device, enter your server's local IP address (e.g., http://192.168.1.100), and configure your primary admin credentials.
- Deploying applications: Navigate to the App Store tab to install Nextcloud for cloud storage or Jellyfin for home streaming with a single click.

## If you do not code
🤖 If you do not code
I have CasaOS installed on my home server. I want to set up and configure AdGuard Home (ad blocker), Jellyfin (media streaming), and Tailscale (secure remote access) for all devices in my household. Can you explain step by step how to install these services via the CasaOS App Store or custom Docker Compose, and how to configure shared storage drives?

- **Who it is for:** Homelab enthusiasts and self-hosters wanting to manage personal clouds and Docker apps without terminal friction.
- **License:** Apache-2.0 (Permissive open source license)
- **Developer:** IceWhale Technology and Open Source Community
- **Supported Systems:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7)

## Frequently asked questions
- Does CasaOS wipe my existing Linux installation or data? No. CasaOS does not delete your operating system; it installs as a desktop and Docker management layer on top of it. Existing files on your disks remain intact and accessible.
- How can I securely access CasaOS outside my home network? Rather than opening risky router ports, install Tailscale or WireGuard directly on CasaOS. This provides an encrypted VPN tunnel allowing access anywhere in the world as if on your home Wi-Fi.
- What is the difference between CasaOS, TrueNAS, and Unraid? TrueNAS and Unraid are standalone storage operating systems focused on advanced RAID pools and ZFS setups. CasaOS focuses on lightweight, user-friendly, app-centric home cloud convenience.
- Do installed apps restart automatically after a power outage? Yes. All Docker containers in CasaOS are launched with the <code>restart: unless-stopped</code> policy, resuming automatically whenever the server boots up.

## Links
- [GitHub →](https://github.com/IceWhaleTech/CasaOS)

## Related dictionary terms
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/en/discover/casaos/
