# Foto- und Video-Backup auf Ihrem eigenen Server

Immich ist eine leistungsstarke Lösung für das Backup Ihrer persönlichen Fotos und Videos, die Sie direkt auf Ihrem eigenen Server hosten können.

- ★ 109.538
- GitHub Trending · 2026-07-05

## Was macht dieses Werkzeug?
Immich ist eine leistungsstarke Lösung für das Backup Ihrer persönlichen Fotos und Videos, die Sie direkt auf Ihrem eigenen Server hosten können. Es ermöglicht Ihnen die Verwaltung Ihrer Medienbibliothek über mobile und Webanwendungen.

## Für wen ist es?
Für diejenigen, die ihre Fotos und Videos auf ihrer eigenen Hardware speichern und verwalten möchten, anstatt Cloud-Dienste von Drittanbietern zu nutzen.

## Was Sie nicht erwarten sollten
Benutzer, die ihren eigenen Server nicht verwalten möchten oder sich nicht mit technischen Installationsprozessen befassen wollen.

## Höhepunkte
- Sichert Fotos und Videos in ihrer Originalqualität.
- Bietet Zugriffsmöglichkeiten über Web- und mobile Anwendungen.
- Gewährleistet Datenschutz durch Hosting auf Ihrer eigenen Hardware.
- Unterstützt mehrere Benutzer und ermöglicht die Erstellung von Bereichen für Familienmitglieder oder Teams.

## Ablauf für die erste Nutzung
- Stellen Sie sicher, dass Sie die in der offiziellen Dokumentation angegebenen Hardwareanforderungen erfüllen.
- Starten Sie die Immich-Container mit Docker und Docker Compose.
- Laden Sie die mobile App auf Ihr Gerät herunter und verbinden Sie sich durch Eingabe Ihrer Serveradresse.
- Erstellen Sie das erste Administratorkonto und starten Sie den Sicherungsvorgang.

## Sicherer Start

## Erster Prompt
Wie füge ich einer Immich-Installation einen neuen Benutzer hinzu?

## Installation
**Laden Sie die Docker Compose-Konfiguration herunter**

```
mkdir immich-app && cd immich-app
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```


## Ausführung
**Starten Sie die Docker-Dienste**

```
docker compose up -d
```


## Links
- GitHub-Repository →
- Offizielle Immich README →
- Offizielle Immich Website →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/immich/
