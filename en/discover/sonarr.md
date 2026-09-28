# Automatically manage your TV series archive

Sonarr is an open source, intelligent personal video recorder (PVR) and media automation manager developed for Usenet (newsgroups) and BitTorrent users. Platform developed with C# and .NET infrastructure; keeps track of newly released episodes, communicates with download clients, renames and transfers files to Plex and Jellyfin libraries on a regular basis.

- ★ 16,274
- C#
- GitHub Trending · 2026-09-12

## What you get
- Automatic episode tracking and calendar: Track the broadcast dates of your favorite series through the integrated calendar and automatically download new episodes as soon as they are released.
- Smart quality upgrades: Automatically replace lower resolution sections (720p HDTV) with higher quality versions (1080p / 4K HDR WEB-DL) over time.
- Hardlinking support: Keeping downloaded files in torrent sharing and presenting them to the media server on the same disk without duplicating them.
- Broad client and indexer integration: zero-friction working with qBittorrent, Transmission, Deluge, SABnzbd and NZBGet.
- Customizable file naming: Automatic naming and foldering of episode files according to the standards of media servers (Plex, Jellyfin, Emby).

## Installation options: Docker and local service
**Installation with Docker Compose**

```
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```


## Operation and basic configuration
**Starting the container**

```
docker compose up -d
```

**Access to web interface**

```
http://localhost:8989
```


## Technical architecture and working principle
- Torznab and Newznab protocol bridge: Communicates with indexers (via Jackett or Prowlarr) via standard XML/JSON API over RSS feeds and search queries.
- Atomic file moving and Hardlink: Reduces disk writing load and storage waste to zero by mounting the file system inode instead of copying the file when the download is finished.
- Custom Formats scoring engine: Selects the best version by scoring preferred audio codecs (Atmos, DTS-HD), video formats (AV1, HEVC) and publisher groups.

## Media ecosystem integration (Plex, Jellyfin, Prowlarr)
- Indexer synchronization with Prowlarr: Automatically import torrent trackers and Usenet indexers to Sonarr from a single center.
- Download management with qBittorrent / SABnzbd: Control download speed and sharing rate via designated categories.
- Plex or Jellyfin library notification: Send instant notification to the media server when a new episode is written to disk and scan the library.

## If you don't write code
I want to run Sonarr, qBittorrent, Prowlarr and Jellyfin services together on Docker on my home server. Can you please explain step by step the complete docker-compose.yml file containing a single volume mount structure and the first settings I need to make in the Sonarr web panel for hardlinks to work smoothly?

## Frequently asked questions
- Does Sonarr download the file itself directly? No. Sonarr is not a download client; is a manager. It searches, pushes the torrent/NZB file to clients like qBittorrent or SABnzbd, and moves the downloaded file to the archive folder.
- What is hardlink and does it fill the disk twice as much? No. Hardlinking is putting a second path pointer to the file's physical data on disk. It appears in both the downloads and tv folders, but takes up as much space on the disk as a single file.
- What is the difference between Sonarr and Radarr? While Sonarr directs television series, seasons and episodes; Radarr offers the same architecture for feature films.
- Is it necessary to use a VPN? Since Sonarr only does RSS and metadata queries, it generally doesn't require a VPN; however, it is recommended that the torrent download client (qBittorrent) runs behind a VPN tunnel.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/sonarr/
