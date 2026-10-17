# What is Self-hosted?

*Development · Last updated: September 19, 2026*

Self-hosted (self-hosting or local hosting) is an architecture for running and managing software, a database, or a digital service on a physical server, local hardware (homelab), or a virtual private server (VPS) entirely under your own control, without depending on a third-party cloud company (SaaS).

## Etymology and Turkish Equivalent

Formed by combining the English words self and host, the term is referred to in Turkish as öz barındırma, kendi sunucusunda barındırma, or yerel barındırma.

In the traditional SaaS (Software as a Service) model, users are merely tenants; data and infrastructure are locked in the data centers of foreign companies. In the self-hosted approach, you are the direct system administrator and owner: the database, storage disks, network rules, and encryption keys are entirely your physical or logical property.

## 1. From SaaS Fatigue to Cloud Repatriation

In the last decade, the shift of every software to a monthly recurring subscription model has created significant subscription fatigue among individuals and organizations:

- The Cost Trap: SaaS tools costing $10–$50 per user per month escalate into hundreds of thousands of dollars in uncontrolled costs as teams grow. Indeed, the move by global tech leaders like 37signals (Basecamp) to leave the cloud and return to their own hardware (Cloud Repatriation) has proven the economic rationality of the self-hosted approach.
- Data Sovereignty and Privacy: Self-hosting is the strongest shield against the risk of companies unilaterally changing terms of use, using data to train AI models, or suddenly closing accounts. Keeping sensitive customer data within your own borders in accordance with KVKK and GDPR standards also ensures legal compliance.

## 2. Hardware Architecture and the Homelab Ecosystem

The self-hosted world has moved from expensive enterprise server racks to living rooms and home laboratories (Homelab):

- Low-Power Hardware: Intel N100-based mini PCs, Raspberry Pi 5, or older laptops can run 24/7 uninterrupted with an electricity consumption of only a few hundred liras per year.
- Storage and Data Security (ZFS & RAID): RAID arrays where multiple hard drives are mirrored and the ZFS file system make data loss impossible, even if a drive physically burns out. Operating systems like TrueNAS and unRAID turn this hardware into professional storage pools.
- Cloud VPS Alternative: For those who do not want to host hardware at home, cheap virtual private servers (VPS) rented from providers like Hetzner or OVH combine self-hosted freedom with cloud reliability.

## 3. Modern Self-Hosted Software Stack

Gone are the days when it was necessary to manually compile PHP and MySQL on Linux. Modern architecture is built on three pillars:

- Containerization (Docker & Docker Compose): Each service (Nextcloud, Vaultwarden, Jellyfin) runs inside an isolated Docker container with its own libraries. Thanks to the docker-compose.yml file, dozens of services can be spun up with a single command.
- Reverse Proxy: Nginx, Traefik, or Caddy handles incoming web requests, routes domain names to the correct container, and automatically renews free SSL/TLS certificates via Let's Encrypt.
- Secure Network Tunnels (Zero-Trust & Mesh VPN): Opening ports to the outside on a home router invites cyberattacks. Modern self-hosted users safely run their systems in an internal network (Mesh VPN) closed to the outside world and open only to authorized devices by using Tailscale, WireGuard, or Cloudflare Tunnels.

## 4. Popular Self-Hosted Solutions

- Personal Cloud and Photos: Nextcloud instead of Google Drive, Immich with AI face recognition instead of Google Photos.
- Password Management: Open-source and lightweight Vaultwarden (Bitwarden compatible) instead of 1Password.
- Media Streaming: Jellyfin and Plex, where you manage your own archive instead of Netflix and Spotify.
- Local AI: Ollama and Open WebUI running on your own graphics card instead of a ChatGPT subscription.
- Smart Home: Home Assistant, which runs entirely locally instead of cloud-dependent manufacturers.

## 5. Responsibilities: The 3-2-1 Backup Rule

Freedom brings responsibility. There is no cloud company behind you to open a support ticket with in the event of a hardware failure. Therefore, the 3-2-1 Backup Rule is mandatory:

- Keep at least 3 copies of your data.
Store these copies in 2 different physical media (for example, internal disk and external USB).
- Host at least 1 of the copies in a different physical location (encrypted remote server or external storage) against fire and theft.

## Frequently Asked Questions

**What is self-hosted and what does it mean in Turkish?**

It is a concept of English origin that means 'self-hosting' or 'hosting on one's own server' in Turkish. It refers to running software on the user's own hardware or server instead of third-party cloud providers.

**Is advanced coding knowledge required to set up self-hosted?**

No, you do not need to write code. Basic knowledge of the Linux command line and an understanding of Docker logic are sufficient. Furthermore, modern systems like CasaOS and Umbrel offer one-click installation capabilities similar to an app store.

**Is it safe to run self-hosted services on a home server (homelab)?**

When configured correctly, it is more secure than commercial clouds because your data is not shared with companies. However, it is essential to use VPN tunnels like Tailscale instead of opening ports directly on the modem and to keep up with security updates.

**Why is the 3-2-1 backup rule vital?**

In self-hosted systems, there is no customer service to recover data when hardware fails. The 3-2-1 backup rule·3 copies, 2 different media, and 1 off-site location·prevents data loss in the event of hardware fires or malfunctions.

## Related terms

- [Local](https://trescout.com/en/dictionary/local/)
- [Offline](https://trescout.com/en/dictionary/offline/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Deployment](https://trescout.com/en/dictionary/deployment/)

## Related tools

- [Immich](https://trescout.com/en/discover/immich/)
- [CasaOS](https://trescout.com/en/discover/casaos/)
- [Chatwoot](https://trescout.com/en/discover/chatwoot/)
- [Open-Generative-AI](https://trescout.com/en/discover/open-generative-ai/)
- [OpenWA](https://trescout.com/en/discover/openwa/)
- [Openship](https://trescout.com/en/discover/openship/)
- [Instatic](https://trescout.com/en/discover/instatic/)
- [TREK](https://trescout.com/en/discover/trek/)

This explanation was written in plain language for TreScout with AI and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/self-hosted/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/self-hosted/
