# Verwalten Sie Ihren persönlichen Cloud-Server

CasaOS ist ein quelloffenes, leichtgewichtiges und elegantes persönliches Cloud-Betriebssystem, mit dem Docker-basierte Anwendungen auf Heimservern, Mini-PCs und Raspberry Pi Geräten mit nur einem Klick verwaltet werden können. Entwickelt in Go, ermöglicht die Plattform digitale Unabhängigkeit ohne komplexe Terminalbefehle.

- ★ 36.953
- Go
- GitHub Trending · 2026-06-26

## Aktualisierungen
- 2. August 2026: Sterne 34.992 → 36.953, neueste Version v0.4.15 (19. Dezember 2024).

## Was es bringt
- Umfangreicher App Store mit 1-Klick-Installation: Installieren Sie Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant und über 100 beliebte Self-Hosted-Dienste in Sekundenschnelle.
- Elegantes und intuitives Web-Dashboard: Behalten Sie CPU- und RAM-Last, Festplattenbelegung, Netzwerkaktivität und aktive Container über Widgets in Echtzeit im Blick.
- Visuelle Speicher- und Dateiverwaltung: Binden Sie externe Festplatten und USB-Laufwerke automatisch ein und teilen Sie Ordner im lokalen Netzwerk per Samba (SMB) mit Windows und Mac.
- Eigene Docker Compose Unterstützung: Starten Sie benutzerdefinierte Container mühelos, indem Sie Docker Compose Dateien direkt in die Weboberfläche einfügen.
- Leichtgewichtiger Go-Kern ohne Systemballast: Verbraucht im Hintergrund minimalen Arbeitsspeicher und läuft selbst auf einem Raspberry Pi 4/5 oder älteren Laptops absolut flüssig.

## Installation

**Installationsbefehl**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Ausführung

**Aktualisierungsbefehl**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Technische Architektur und Funktionsweise

Anstatt ein komplett eigenes Linux bereitzustellen, fungiert CasaOS als moderne Docker-Orchestrierungsschicht auf Ihrer bestehenden Debian-, Ubuntu- oder Raspberry Pi OS-Installation. Dieser Ansatz garantiert maximale Hardwarekompatibilität bei modularer Microservice-Struktur:
- Go-Microservice-Architektur: Der Kern von CasaOS (Gateway, MessageBus, LocalStorage und UserService) besteht aus voneinander unabhängigen, schlanken Go-Diensten via REST und WebSockets.
- Abstraktion des Container-Lebenszyklus: Kommuniziert direkt mit dem Docker-Daemon, erkennt Port-Konflikte automatisch und übersetzt Umgebungsvariablen und Mount-Pfade in verständliche Eingabefelder.
- ZimaOS- und IceWhale-Ökosystem: Unterstützt von IceWhale Technology (Entwickler von ZimaBoard und ZimaBlade), bietet das System optimale Synergie mit Heim-Cloud-Hardware.
- Intelligente Festplattenzusammenführung: Verbindet Speicher unterschiedlicher Größen zu einem logischen Speicherpool für Medien und Backups.

## Schritt-für-Schritt-Anleitung für den eigenen Heimserver

Um einen alten PC oder Mini-PC in eine vollwertige persönliche Cloud zu verwandeln, genügen diese zentralen Schritte:
- Grundlegende Linux-Installation: Installieren Sie Ubuntu Server oder ein minimales Debian auf dem Gerät und verbinden Sie es per Ethernet-Kabel mit dem Heimnetzwerk.
- Einzeilige CasaOS-Installation: Führen Sie das offizielle Installationsskript im Terminal aus; Docker und alle Abhängigkeiten werden automatisch eingerichtet.
- Zugriff über den Webbrowser: Rufen Sie im Browser eines beliebigen Rechners im Netzwerk die Server-IP auf (z. B. http://192.168.1.100) und erstellen Sie Ihr Administratorkonto.
- Dienste per Klick starten: Öffnen Sie den App Store, um Nextcloud für eigene Dateien oder Jellyfin für Filme und Serien mit einem Klick zu installieren.

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich habe CasaOS auf meinem Heimserver installiert. Ich möchte AdGuard Home (Werbeblocker), Jellyfin (Medienstreaming) und Tailscale (sicherer Fernzugriff) für alle Geräte im Haus einrichten. Kannst du mir Schritt für Schritt erklären, wie ich diese Dienste über den CasaOS App Store oder per Docker Compose installiere und Festplattenfreigaben einrichte?

- **Für wen:** Homelab-Einsteiger und Nutzer, die eine private Cloud und Docker-Container ohne Terminalfrust betreiben möchten.
- **Lizenz:** Apache-2.0 (Freie Open-Source-Lizenz)
- **Entwickler:** IceWhale Technology und Open-Source-Community
- **Unterstützte Systeme:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7)

## Häufig gestellte Fragen
- Löscht CasaOS mein bestehendes Linux-Betriebssystem oder meine Daten? Nein. CasaOS formatiert Ihre Festplatten nicht, sondern setzt als Verwaltungs- und Docker-Schicht auf Linux auf. Ihre bestehenden Dateien bleiben vollständig erhalten.
- Wie kann ich von unterwegs sicher auf meinen CasaOS-Server zugreifen? Statt unsichere Portweiterleitungen am Router einzurichten, installieren Sie Tailscale oder WireGuard auf CasaOS. Dadurch entsteht ein verschlüsselter VPN-Tunnel für weltweiten Zugriff.
- Was ist der Unterschied zwischen CasaOS, TrueNAS und Unraid? TrueNAS und Unraid sind spezialisierte Speicherbetriebssysteme mit Fokus auf komplexe RAID-Verbünde und ZFS. CasaOS setzt stattdessen auf Leichtigkeit und app-zentrierte Heimanwendung.
- Starten installierte Apps nach einem Stromausfall automatisch neu? Ja. Alle Docker-Container laufen standardmäßig mit der Richtlinie <code>restart: unless-stopped</code> und setzen ihren Dienst beim Neustart des Servers selbsttätig fort.

## Links
- [GitHub →](https://github.com/IceWhaleTech/CasaOS)

## Verwandte Begriffe aus dem Glossar
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/de/discover/casaos/
