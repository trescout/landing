# Verwalten Sie Ihr Serienarchiv automatisch

Sonarr ist ein intelligenter Open-Source-Videorecorder (PVR) und Medienautomatisierungsmanager, der für Usenet- (Newsgroups) und BitTorrent-Benutzer entwickelt wurde. Plattform entwickelt mit C#- und .NET-Infrastruktur; Verfolgt neu veröffentlichte Episoden, kommuniziert mit Download-Clients, benennt Dateien um und überträgt sie regelmäßig in Plex- und Jellyfin-Bibliotheken.

- ★ 16.274
- C#
- GitHub Trending · 2026-09-12

## Aktualisierungen

- **17. September 2026:** Sterne 15,798 → 16,274, neueste Version v4.0.20.3014 (16. September 2026).
- **12. September 2026:** Sterne 15,796 → 15,798, neueste Version v4.0.19.2979 (26. Juni 2026).

## Was es bringt

- Automatische Episodenverfolgung und Kalender: Verfolgen Sie die Sendetermine Ihrer Lieblingsserien über den integrierten Kalender und laden Sie neue Episoden automatisch herunter, sobald sie veröffentlicht werden.
- Intelligente Qualitäts-Upgrades: Ersetzen Sie Abschnitte mit niedrigerer Auflösung (720p HDTV) im Laufe der Zeit automatisch durch Versionen mit höherer Qualität (1080p / 4K HDR WEB-DL).
- Hardlinking-Unterstützung: Heruntergeladene Dateien bleiben bei der Torrent-Freigabe erhalten und werden dem Medienserver auf derselben Festplatte angezeigt, ohne sie zu duplizieren.
- Umfassende Client- und Indexer-Integration: Reibungsloses Arbeiten mit qBittorrent, Transmission, Deluge, SABnzbd und NZBGet.
- Anpassbare Dateibenennung: Automatische Benennung und Ordnerierung von Episodendateien gemäß den Standards von Medienservern (Plex, Jellyfin, Emby).

## Installationsoptionen: Docker und lokaler Dienst

**Installation mit Docker Compose**

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

## Bedienung und Grundkonfiguration

**Starten des Containers**

```
docker compose up -d
```

**Zugriff auf die Weboberfläche**

```
http://localhost:8989
```

## Technische Architektur und Funktionsweise

- Torznab- und Newznab-Protokollbrücke: Kommuniziert mit Indexern (über Jackett oder Prowlarr) über die Standard-XML/JSON-API über RSS-Feeds und Suchanfragen.
- Atomare Dateiverschiebung und Hardlink: Reduziert die Schreiblast auf die Festplatte und die Speicherverschwendung auf Null, indem der Dateisystem-Inode gemountet wird, anstatt die Datei nach Abschluss des Downloads zu kopieren.
- Bewertungs-Engine für benutzerdefinierte Formate: Wählt die beste Version durch Bewertung bevorzugter Audio-Codecs (Atmos, DTS-HD), Videoformate (AV1, HEVC) und Herausgebergruppen aus.

## Integration des Medienökosystems (Plex, Jellyfin, Prowlarr)

- Indexer-Synchronisierung mit Prowlarr: Importieren Sie Torrent-Tracker und Usenet-Indexer automatisch von einem einzigen Zentrum aus in Sonarr.
- Download-Verwaltung mit qBittorrent / SABnzbd: Steuern Sie die Download-Geschwindigkeit und die Freigaberate über bestimmte Kategorien.
- Plex- oder Jellyfin-Bibliotheksbenachrichtigung: Senden Sie eine sofortige Benachrichtigung an den Medienserver, wenn eine neue Episode auf die Festplatte geschrieben wird, und scannen Sie die Bibliothek.

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die Dienste Sonarr, qBittorrent, Prowlarr und Jellyfin gemeinsam auf Docker auf meinem Heimserver ausführen. Können Sie bitte Schritt für Schritt die vollständige Datei „docker-compose.yml“ erklären, die eine Single-Volume-Mount-Struktur und die ersten Einstellungen enthält, die ich im Sonarr-Webpanel vornehmen muss, damit Hardlinks reibungslos funktionieren?

## Häufig gestellte Fragen

- Lädt Sonarr die Datei selbst direkt herunter? Nein. Sonarr ist kein Download-Client; ist Manager. Es sucht, überträgt die Torrent-/NZB-Datei an Clients wie qBittorrent oder SABnzbd und verschiebt die heruntergeladene Datei in den Archivordner.
- Was ist ein Hardlink und füllt er die Festplatte doppelt so stark aus? Nein. Beim Hardlinking wird ein zweiter Pfadzeiger auf die physischen Daten der Datei auf der Festplatte gesetzt. Es erscheint sowohl im Download- als auch im TV-Ordner, nimmt jedoch genauso viel Speicherplatz auf der Festplatte ein wie eine einzelne Datei.
- Was ist der Unterschied zwischen Sonarr und Radarr? Während Sonarr bei Fernsehserien, Staffeln und Episoden Regie führt; Radarr bietet die gleiche Architektur für Spielfilme.
- Ist die Verwendung eines VPN erforderlich? Da Sonarr nur RSS- und Metadatenabfragen durchführt, ist im Allgemeinen kein VPN erforderlich; Es wird jedoch empfohlen, dass der Torrent-Download-Client (qBittorrent) hinter einem VPN-Tunnel ausgeführt wird.

## Verwandte Begriffe aus dem Glossar

- [PVR](https://trescout.com/de/dictionary/pvr/)
- [HDR](https://trescout.com/de/dictionary/hdr/)
- [VPN](https://trescout.com/de/dictionary/vpn/)
- [Pipeline](https://trescout.com/de/dictionary/pipeline/)
- [API](https://trescout.com/de/dictionary/api/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)

- **Für wen es gedacht ist:** Besitzer von Heimservern (Homelab), Medienbegeisterte und alle, die ihre Serienarchive mühelos verwalten möchten.
- **Lizenz:** GPL-3.0 (Açık kaynak lisansı)
- **Infrastruktur:** C#- und .NET-basierter Webdienst
- **Webport:** Standard 8989

## Links

- [GitHub-Repository →](https://github.com/Sonarr/Sonarr)
- [Auf Türkisch lesen →](https://trescout.com/discover/sonarr/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-12 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/sonarr/
