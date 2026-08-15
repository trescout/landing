# Intelligente Daten mit künstlicher Intelligenz bereitstellen

Der Production-Agentic-Rag-Kurs bietet praktische Schulungen in der Entwicklung agentenbasierter Fetch-Assisted Production (Agentic RAG)-Systeme, die die Prozesse des Abrufs von Informationen aus komplexen Datenquellen automatisieren. Basierend auf der Python-Sprache vermittelt diese Ressource die technische Architektur, die zum Erstellen skalierbarer Anwendungen für künstliche Intelligenz auf Produktionsebene erforderlich ist.

- ★ 8.216
- GitHub Trending · 2026-06-03

## Was es bringt
- Aufbau der notwendigen Infrastruktur für RAG-Systeme auf Produktionsebene.
- Anwendung hybrider Such- und intelligenter Datenverarbeitungsmethoden.
- Entwicklung agentenbasierter Entscheidungsmechanismen mit LangGraph.

## Installation
**Klonen und Installieren des Repositorys**

```
git clone <repository-url>
cd arxiv-paper-curator

# 2. Configure environment (IMPORTANT!)
cp .env.example .env
# The .env file contains all necessary configuration for OpenSearch, 
# arXiv API, and service connections. Defaults work out of the box.
# You need to add Jina embeddings free api key and langfuse keys (check the blogs)

# 3. Install dependencies
uv sync

# 4. Start all services
docker compose up --build -d

# 5. Verify everything works
curl http://localhost:8000/api/v1/health
```


## Ausführung
**Spielen Sie Inhalte einer bestimmten Woche ab**

```
git clone --branch <WEEK_TAG> https://github.com/jamwithai/arxiv-paper-curator
cd arxiv-paper-curator
uv sync
docker compose down -v
docker compose up --build -d

# Replace <WEEK_TAG> with: week1.0, week2.0, etc.
```


## Wenn Sie nicht programmieren
Ich möchte mithilfe des Production-Agentic-Rag-Course-Projekts einen wissenschaftlichen Mitarbeiter entwickeln. Für die Basisinstallation des Projekts muss ich nach dem Herunterladen des Repositorys mit dem Befehl „git clone“ die .env-Datei konfigurieren und die Abhängigkeiten mit UV-Sync installieren. Dann möchte ich überprüfen, ob das System unter http://localhost:8000/api/v1/health funktioniert, indem ich alle Dienste mit dem Befehl docker compose up --build -d starte. Können Sie mir Hinweise zu den API-Schlüsseln und Dienstkonfigurationen geben, auf die ich in diesem Prozess achten sollte?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/production-agentic-rag-course/
