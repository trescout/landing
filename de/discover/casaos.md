# Verwalten Sie Ihren persönlichen Cloud-Server

CasaOS ist ein Open-Source, leichtgewichtiges und elegantes persönliches Cloud-Betriebssystem, mit dem sich Docker-basierte Anwendungen auf Heimservern, Mini-PCs und Raspberry-Pi-Geräten mit nur einem Klick verwalten lassen. Die in der Programmiersprache Go entwickelte Plattform ermöglicht es Ihnen, Ihre digitale Souveränität aufzubauen, ohne komplexe Terminalbefehle zu benötigen.

- ★ 36.953
- Go
- GitHub Trending · 2026-06-26

## Was es bringt
- App Store mit nur einem Klick: Installieren Sie Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant und über 100 weitere beliebte Self-Hosted-Dienste in Sekundenschnelle.
- Elegantes und intuitives Web-Control-Panel: Verfolgen Sie CPU- und RAM-Auslastung, Festplattenbelegung, Netzwerkaktivität und laufende Container live über elegante Widget-Karten.
- Visueller Speicher und Dateiverwaltung: Bindet externe Festplatten und USB-Laufwerke automatisch ein und teilt Ihre Ordner im lokalen Netzwerk über das Samba (SMB)-Protokoll mit Ihren Windows/Mac-Geräten.
- Spezielle Docker-Compose-Unterstützung: Erwecken Sie Ihre benutzerdefinierten Container mühelos zum Leben, indem Sie eine beliebige Docker-Compose-Datei, die nicht im offiziellen Store enthalten ist, in die Weboberfläche einfügen.
- Leichter Go-Kern und null Systemlast: Dank minimalem Speicherverbrauch im Hintergrund bietet es selbst auf den bescheidensten Raspberry Pi 4/5 oder älteren Laptops eine flüssige Leistung.

## Installation
**Installationsbefehl**

```
curl -fsSL https://get.casaos.io | sudo bash
```


## Ausführung
**Update-Befehl**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```


## Technische Architektur und Funktionsweise
- Go-Mikroservice-Architektur: Der CasaOS-Kern (CasaOS-Gateway, MessageBus, LocalStorage und UserService) besteht aus unabhängigen, leichtgewichtigen Go-Diensten. Die Kommunikation zwischen den Diensten erfolgt über REST und WebSocket.
- Abstraktion des Container-Lebenszyklus: Kommuniziert direkt mit dem Docker-Daemon, um Portkonflikte automatisch zu erkennen, und wandelt Umgebungsvariablen sowie Pfade für permanente Datenträgerbindungen (Volume Mounts) in benutzerfreundliche Formulare um.
- ZimaOS und das IceWhale-Ökosystem: Das vom ZimaBoard- und ZimaBlade-Hardwarehersteller IceWhale Technology unterstützte Projekt bietet volle Kompatibilität mit lokaler Cloud-Hardware.
- Intelligentes Festplatten-Pooling: Führt Festplatten unterschiedlicher Größe in einem einzigen logischen Speicherpool zusammen und schafft so flexiblen Speicherplatz für Heimmedien und Backups.

## Schritt-für-Schritt-Anleitung zum Einrichten Ihres eigenen Heimservers
- Grundlegende Linux-Installation: Installieren Sie ein sauberes Ubuntu Server oder Debian minimal auf Ihrem Gerät und verbinden Sie es über ein Ethernet-Kabel mit Ihrem lokalen Netzwerk.
- CasaOS-Einzeilen-Installation: Führen Sie das offizielle Installationsskript über das Terminal aus; das Skript konfiguriert Docker und Abhängigkeiten automatisch.
- Zugriff auf das Interface über den Browser: Erstellen Sie Ihr erstes Administratorkonto, indem Sie die IP-Adresse Ihres Servers (z. B. http://192.168.1.100) von einem beliebigen Computer im Netzwerk in Ihren Browser eingeben.
- Apps bereitstellen: Gehen Sie auf die Registerkarte App Store und installieren Sie Ihre persönliche Cloud mit Nextcloud und Ihre Film-/Serienbibliothek mit Jellyfin mit nur einem Klick.

## Wenn Sie nicht programmieren
Auf meinem persönlichen Heimserver ist CasaOS installiert. Ich möchte die Dienste AdGuard Home (Werbeblocker), Jellyfin (Medien-Streaming) und Tailscale (sicherer Zugriff von außerhalb des Hauses) für alle Geräte in meinem Zuhause installieren und konfigurieren. Können Sie Schritt für Schritt erklären, wie ich diese Dienste über das CasaOS-Webpanel mittels benutzerdefiniertem Docker Compose oder dem App Store installiere und wie ich die Festplattenfreigabe einrichte?

## Häufig gestellte Fragen
- Löscht CasaOS mein bestehendes Linux-Betriebssystem oder meine Daten? Nein. CasaOS löscht Ihr bestehendes Betriebssystem nicht; es wird als Desktop- und Docker-Verwaltungsschicht darüber installiert. Die vorhandenen Dateien auf Ihren Festplatten bleiben erhalten und werden über das Panel zugänglich gemacht.
- Wie kann ich von unterwegs sicher auf meinen CasaOS-Server zugreifen? Anstatt unsicheres Port-Forwarding einzurichten, können Sie mit nur einem Klick Tailscale oder WireGuard auf CasaOS installieren. Dadurch erreichen Sie das Dashboard von überall auf der Welt über einen verschlüsselten VPN-Tunnel, als wären Sie in Ihrem Heimnetzwerk.
- Was ist der Unterschied zwischen CasaOS und TrueNAS oder Unraid? TrueNAS und Unraid sind eigenständige Betriebssysteme, die sich auf tiefgehende Speicherverwaltung und RAID-Konfigurationen konzentrieren. CasaOS hingegen bietet ein leichtgewichtiges, äußerst benutzerfreundliches und anwendungszentriertes Heimwolken-Erlebnis.
- Starten installierte Anwendungen nach einem Stromausfall automatisch? Ja. Alle Docker-Container unter CasaOS werden standardmäßig mit der Richtlinie restart: unless-stopped gestartet. Sobald Ihr Server wieder eingeschaltet wird, laufen all Ihre Dienste automatisch dort weiter, wo sie aufgehört haben.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/casaos/
