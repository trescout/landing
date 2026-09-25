# Automate your TV series library and media streaming

Sonarr is an open-source, smart personal video recorder (PVR) and media automation manager built for Usenet and BitTorrent users. Powered by C# and .NET, it monitors upcoming episodes, interfaces with download clients, renames files, and routes content seamlessly into Plex and Jellyfin libraries.

- ★ 16,274
- C#
- GitHub Trending · 2026-09-12

## Updates
- September 17, 2026: Stars 16,274, latest release v4.0.20.3014 (.NET 8 runtime optimizations and custom format scoring upgrades).

## What you get
- Automated episode tracking & calendar: Tracks air dates on an integrated calendar and queues downloads the moment episodes air.
- Intelligent quality upgrades: Automatically swaps lower-res rips (720p HDTV) for pristine releases (1080p/4K HDR WEB-DL) over time.
- Zero-waste hardlinking: Preserves ongoing torrent seeding while making files instantly playable in media servers without duplicate disk space.
- Broad client & indexer support: Seamless integration with qBittorrent, Transmission, Deluge, SABnzbd, and NZBGet.
- Customizable file organization: Automatically cleans filenames, creates season folders, and standardizes formats for Plex, Jellyfin, and Emby.

## Installation options: Docker and local service

**Docker Compose setup**

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=UTC
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```

## Running it and initial setup

**Start the container**

```
docker compose up -d
```

**Access web interface**

```
http://localhost:8989
```

## Technical architecture and inner workings

Sonarr serves as the orchestration brain within a modern self-hosted media pipeline:
- Torznab and Newznab protocol bridge: Communicates with indexers via Jackett or Prowlarr using standardized XML and JSON REST endpoints.
- Atomic file operations & Hardlinks: Links filesystem inodes rather than copying gigabytes of video, reducing disk write wear to zero.
- Custom Formats scoring engine: Ranks releases using weighted attributes for preferred audio (Atmos, TrueHD), video codecs (AV1, HEVC), and release groups.

## Media ecosystem integration (Plex, Jellyfin, Prowlarr)

For a complete homelab setup, Sonarr connects seamlessly with neighboring media services:
- Indexer sync with Prowlarr: Manage Usenet and torrent trackers centrally and sync them into Sonarr automatically.
- Download handling via qBittorrent / SABnzbd: Assign dedicated categories, bandwidth caps, and seeding ratios.
- Instant library refresh: Notifies Plex or Jellyfin over Webhooks the instant a file finishes processing.

## If you do not code
🤖 If you do not code
I want to deploy Sonarr alongside qBittorrent, Prowlarr, and Jellyfin using Docker Compose. Can you provide a unified compose file configured with consistent volume mounts to support atomic hardlinks, and explain the initial configuration steps in the Sonarr web UI?

- **Who it is for:** Homelab builders, media collectors, and self-hosters wanting zero-maintenance TV archiving.
- **License:** GPL-3.0 (Open source license)
- **Framework:** C# and .NET web application
- **Web Port:** Default 8989

## Frequently asked questions
- Does Sonarr download media directly? No. Sonarr is an automation orchestrator, not a download client. It finds releases, sends them to qBittorrent or SABnzbd, and moves the finished files into your library.
- What is a hardlink and does it double disk usage? No. A hardlink creates a secondary pointer to the exact same physical disk sectors. It appears in both folders while consuming zero extra bytes.
- What is the difference between Sonarr and Radarr? Sonarr specializes in serialized episodic television shows, whereas Radarr uses the same design patterns specifically for standalone movies.
- Do I need to run Sonarr through a VPN? Sonarr only handles RSS lookups and API metadata, so it does not strictly require a VPN. However, routing your actual download client (e.g. qBittorrent) through a VPN tunnel is strongly advised.

## Links
- [GitHub →](https://github.com/Sonarr/Sonarr)

## Related dictionary terms
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/en/discover/sonarr/
