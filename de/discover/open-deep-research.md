# Tiefgründige Forschung mit autonomer künstlicher Intelligenz

Open-Deep-Research wurde von LangChain entwickelt und ist ein autonomes System, das mehrstufige Suchen im Internet durchführt, um komplexe Fragen zu beantworten. Es erleichtert tiefgreifende Forschungsprozesse, indem es den Forschungsprozess in den Phasen Planung, Datenerfassung und Synthese automatisiert.

- ★ 12.655
- Python
- GitHub Trending · 2026-07-22

## Was es bringt
- Mehrstufige autonome Recherche für komplexe Fragestellungen
- Kompatibilität mit verschiedenen Modellanbietern und Suchtools
- Forschungsprozesse visualisiert über LangGraph

## Installation
**Klonen des Repositorys und Vorbereiten der Umgebung**

```
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Abhängigkeiten installieren**

```
uv sync
# or
uv pip install -r pyproject.toml
```


## Ausführung
**Starten des Servers**

```
# Install dependencies and start the LangGraph server
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
```


## Wenn Sie nicht programmieren
Führen Sie mit dem Open Deep Research-Tool eine eingehende Analyse von [SCHREIBEN SIE HIER IHR FORSCHUNGSTHEMA] durch. Planen Sie Ihren Forschungsprozess, sammeln Sie Daten online und fassen Sie Ihre Ergebnisse zusammen, um einen umfassenden Bericht zu erstellen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/open-deep-research/
