# Serienarchiv und Heim-Streaming automatisch verwalten

Sonarr ist ein quelloffener, intelligenter Videorekorder (PVR) und Medienautomatisierungs-Manager für Usenet- und BitTorrent-Nutzer. Entwickelt in C# und .NET, überwacht er neue Episoden, steuert Download-Clients, benennt Dateien um und integriert sie nahtlos in Plex- und Jellyfin-Bibliotheken.

- ★ 16.274
- C#
- GitHub Trending · 2026-09-12

## Aktualisierungen
- 17. September 2026: Sterne 16.274, neueste Version v4.0.20.3014 (.NET 8 Runtime-Optimierungen und Upgrades für Custom Formats Scoring).

## Was es bringt
- Automatische Episodenverfolgung & Kalender: Behält Ausstrahlungstermine im integrierten Kalender im Blick und startet Downloads bei Veröffentlichung.
- Intelligente Qualitäts-Upgrades: Ersetzt niedrig aufgelöste Episoden (720p HDTV) im Laufe der Zeit automatisch durch Spitzenversionen (1080p / 4K HDR WEB-DL).
- Speicherschonende Hardlinks: Ermöglicht weiteres Torrent-Seeding ohne zusätzlichen Speicherplatzbedarf auf dem Medienserver.
- Umfassende Client- & Indexer-Anbindung: Nahtlose Zusammenarbeit mit qBittorrent, Transmission, Deluge, SABnzbd und NZBGet.
- Standardisierte Dateiorganisation: Benennt Episoden und Staffelordner automatisch nach den Anforderungen von Plex, Jellyfin und Emby.

## Installationsoptionen: Docker und lokaler Dienst

**Docker Compose Einrichtung**

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Berlin
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```

## Ausführung und Ersteinrichtung

**Container starten**

```
docker compose up -d
```

**Weboberfläche öffnen**

```
http://localhost:8989
```

## Technische Architektur und Funktionsweise

Sonarr fungiert als Orchestrierungszentrale in modernen Self-Hosted-Medienumgebungen:
- Torznab- und Newznab-Protokollbrücke: Kommuniziert über Prowlarr oder Jackett via standardisierte XML- und JSON-Schnittstellen mit Indexern.
- Atomare Dateioperationen und Hardlinks: Verknüpft Dateisystem-Inodes direkt, statt Gigabytes an Videodaten zu kopieren – null zusätzliche Festplattenabnutzung.
- Custom Formats Scoring-Engine: Bewertet Releases nach bevorzugten Audioformaten (Atmos, DTS-HD), Videocodecs (AV1, HEVC) und Releasegruppen.

## Integration ins Medien-Ökosystem (Plex, Jellyfin, Prowlarr)

Im perfekten Homelab arbeitet Sonarr im Verbund mit ergänzenden Diensten:
- Indexer-Abgleich mit Prowlarr: Verwalten Sie Tracker zentral und übertragen Sie Konfigurationen automatisch nach Sonarr.
- Downloadsteuerung mit qBittorrent / SABnzbd: Setzen Sie Uploadlimits und trennen Sie Medienpfade über Kategorien.
- Sofortige Bibliotheksaktualisierung: Benachrichtigt Plex oder Jellyfin per Webhook, sobald eine Datei fertig einsortiert wurde.

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich möchte Sonarr zusammen mit qBittorrent, Prowlarr und Jellyfin per Docker Compose betreiben. Kannst du mir eine vollständige docker-compose.yml mit konsistenter Volume-Struktur für funktionierende Hardlinks bereitstellen und die ersten Einrichtungsschritte in Sonarr erklären?

- **Für wen:** Homelab-Enthusiasten, Serienfans und Nutzer, die ihre Mediensammlung ohne manuellen Aufwand pflegen wollen.
- **Lizenz:** GPL-3.0 (Freie Open-Source-Lizenz)
- **Technologie:** C# und .NET basierte Webanwendung
- **Web-Port:** Standard 8989

## Häufig gestellte Fragen
- Lädt Sonarr Mediendateien selbst herunter? Nein. Sonarr ist kein Download-Client, sondern der Manager. Er durchsucht Indexer, übergibt Aufträge an qBittorrent oder SABnzbd und verschiebt die fertigen Dateien in die Bibliothek.
- Was ist ein Hardlink und belegt er doppelten Speicher? Nein. Ein Hardlink ist ein zweiter Verweis auf dieselben physischen Datenblöcke der Festplatte. Die Datei erscheint in zwei Ordnern, belegt den Speicherplatz aber nur einmal.
- Was ist der Unterschied zwischen Sonarr und Radarr? Sonarr ist auf Serien und Staffeln spezialisiert, während Radarr dasselbe Konzept für Spielfilme umsetzt.
- Muss Sonarr über ein VPN laufen? Sonarr fragt nur Metadaten ab und benötigt in der Regel kein VPN. Es wird jedoch dringend empfohlen, den Download-Client (qBittorrent) über einen VPN-Tunnel zu betreiben.

## Links
- [GitHub →](https://github.com/Sonarr/Sonarr)

## Verwandte Begriffe aus dem Glossar
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/de/discover/sonarr/
