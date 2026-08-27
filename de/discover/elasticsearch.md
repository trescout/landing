# Verteilte und leistungsstarke Suchmaschine

Elasticsearch ist eine RESTful API-basierte, verteilte und hochleistungsfähige Such- und Analyse-Engine.

- ★ 77.846
- GitHub Trending · 2026-07-04

## Was macht dieses Werkzeug?
Elasticsearch ist eine RESTful API-basierte, verteilte und hochleistungsfähige Such- und Analyse-Engine. Sie bietet eine Infrastruktur für Echtzeitsuche, Protokollanalyse und Datenvisualisierung für große Mengen an Text-, numerischen und geografischen Daten.

## Für wen ist es?
Für diejenigen, die komplexe Suchen und Protokollanalysen über Millionen von Datenzeilen in Millisekunden durchführen möchten.

## Was Sie nicht erwarten sollten
Traditionelle Datenbankbenutzer, die relationale Datenmodelle und komplexe SQL-JOIN-Operationen benötigen.

## Höhepunkte
- Bietet Hochgeschwindigkeits-Volltextsuche bei großen Datenmengen.
- Dank seiner verteilten Architektur ist es horizontal leicht skalierbar.
- Beherbergt ein reichhaltiges Ökosystem für Protokollverwaltung und Systemüberwachung.

## Ablauf für die erste Nutzung
- Installieren Sie Elasticsearch gemäß den Anweisungen für Docker oder den Paketmanager in der offiziellen Dokumentation.
- Konfigurieren Sie die Standard-Sicherheitseinstellungen (Passwörter und Zertifikate).
- Überprüfen Sie den Cluster-Status, indem Sie eine Anfrage mit einem REST-Client an den Haupt-Endpunkt senden.

## Sicherer Start

## Erster Prompt
Wie erstellt man einen neuen Index in Elasticsearch?

## Installation
**Ziehen Sie das Docker-Image**

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```

**macOS (Homebrew)**

```
brew install elastic/tap/elasticsearch-full
```


## Ausführung
**Starten Sie mit Docker im Einzelknotenmodus**

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```


## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Offizielle Elasticsearch README →
- Offizielle Elasticsearch Website →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/elasticsearch/
