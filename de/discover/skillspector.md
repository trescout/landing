# Sichere KI-Funktionen

SkillSpector wurde von NVIDIA entwickelt und ist ein Scan-Tool, das Schwachstellen und bösartige Muster in den Kompetenzpaketen von Agenten für künstliche Intelligenz erkennt. Diese Python-basierte Software zielt darauf ab, Sicherheitsrisiken zu analysieren, die während des Entwicklungsprozesses agentenbasierter Systeme auftreten.

- ★ 14.527
- Python
- GitHub Trending · 2026-06-12

## Aktualisieren
- 12. August 2026: Star 14.482 → 14.527, neueste Version v2.9.3 (11. August 2026).
- 11. August 2026: Star 14.370 → 14.482, neueste Version v2.9.2 (11. August 2026).
- 8. August 2026: Star 14.313 → 14.370, neueste Version v2.8.2 (8. August 2026).
- 7. August 2026: Star 14.260 → 14.313, neueste Version v2.8.1 (7. August 2026).

## Was es bringt
- KI erkennt Schwachstellen und bösartige Muster in den Fähigkeiten von Agenten.
- Es bietet zweistufige Sicherheitsscans mit statischer Analyse und optionaler KI-Bewertung.
- Es ermöglicht die Überprüfung der Sicherheit von Agenten durch Risikobewertung und detaillierte Berichterstattung.

## Installation
**Klonen des Repositorys und Erstellen einer virtuellen Umgebung**

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate
```

**Schließen Sie die Einrichtung ab**

```
# Install for production use
make install

# Or install with development dependencies
make install-dev
```


## Ausführung
**Lokales Verzeichnis scannen**

```
skillspector scan ./my-skill/
```

**Scannen Sie das Git-Repository**

```
skillspector scan https://github.com/user/my-skill
```


## Wenn Sie nicht programmieren
Ich möchte einen KI-Agenten-Skill mit dem SkillSpector-Tool einer Sicherheitsüberprüfung unterziehen. Wie verwende ich den Befehl „skillspector scan ./my-skill/“, um in einem lokalen Verzeichnis nach Talenten zu suchen, und welche Parameter sollte ich dem Befehl hinzufügen, um die Scanergebnisse in „report.json“ im JSON-Format zu speichern?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/skillspector/
