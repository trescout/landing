# Zentralisieren Sie Ihre Spielebibliothek

Romm ist ein Spielebibliotheks-Manager, mit dem Sie Ihre Retro-Spielesammlung über eine moderne und elegante Weboberfläche organisieren können.

- ★ 12.170
- GitHub Trending · 2026-07-04

## Was macht dieses Werkzeug?
Romm ist ein Spielebibliotheks-Manager, den Sie direkt auf Ihrem eigenen Server hosten können und mit dem Sie Ihre Retro-Spielesammlung über eine moderne und elegante Weboberfläche organisieren können. Dank der IGDB-Integration werden Spiel-Metadaten automatisch abgerufen.

## Für wen ist es?
Für Retro-Gaming-Enthusiasten, die ihre verstreuten Spieldateien in ein zentrales, visuell ansprechendes Archiv verwandeln möchten.

## Was Sie nicht erwarten sollten
Für diejenigen, die digitale Spiele kaufen möchten oder einen Client zur Verwaltung aktueller Plattformen suchen.

## Höhepunkte
- Bietet eine moderne Bibliotheks-Oberfläche, die über den Browser zugänglich ist.
- Lädt automatisch Informationen wie Spielcover, Veröffentlichungsdatum und Beschreibung herunter.
- Bietet Unterstützung für mehrere Benutzer und die Nachverfolgung des Spielverlaufs.

## Ablauf für die erste Nutzung
- Laden Sie die für Romm erforderlichen Docker- und Docker-Compose-Dateien herunter.
- Erstellen Sie die für den API-Zugriff erforderlichen Schlüssel und fügen Sie diese der Konfigurationsdatei hinzu.
- Starten Sie den Dienst, indem Sie das Verzeichnis einbinden (mount), in dem sich Ihre Spieldateien befinden.
- Melden Sie sich bei der Weboberfläche an und starten Sie den ersten Bibliotheks-Scan.

## Sicherer Start

## Erster Prompt
Wie füge ich der Romm-Bibliothek eine neue Plattform (z. B. SNES) hinzu?

## Installation
**Holen Sie sich eine Beispiel-Kompositionsdatei**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/rommapp/romm/master/examples/docker-compose.example.yml
```


## Ausführung
**beginnen**

```
docker compose up -d
```


## Links
- GitHub-Repository →
- Offizielle Romm README →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/romm/
