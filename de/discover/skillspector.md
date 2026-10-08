# Sichere KI-Funktionen

SkillSpector wurde von NVIDIA entwickelt und ist ein Scan-Tool, das Schwachstellen und bösartige Muster in den Kompetenzpaketen von Agenten für künstliche Intelligenz erkennt. Diese Python-basierte Software zielt darauf ab, Sicherheitsrisiken zu analysieren, die während des Entwicklungsprozesses agentenbasierter Systeme auftreten.

- ★ 19.418
- Python
- GitHub Trending · 2026-06-12

## Aktualisierungen

- **5. Oktober 2026:** Sterne 18,381 → 19,418, neueste Version v2.12.0 (23. September 2026).
- **27. September 2026:** Sterne 16,828 → 18,381, neueste Version v2.12.0 (23. September 2026).
- **10. September 2026:** Sterne 16,595 → 16,828, neueste Version v2.11.2 (9. September 2026).
- **8. September 2026:** Sterne 16,471 → 16,595, neueste Version v2.11.1 (7. September 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte einen KI-Agenten-Skill mit dem SkillSpector-Tool einer Sicherheitsüberprüfung unterziehen. Wie verwende ich den Befehl „skillspector scan ./my-skill/“, um in einem lokalen Verzeichnis nach Talenten zu suchen, und welche Parameter sollte ich dem Befehl hinzufügen, um die Scanergebnisse in „report.json“ im JSON-Format zu speichern?

## Verwandte Begriffe aus dem Glossar

- [AI Skills](https://trescout.com/de/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler, die KI-Agenten entwickeln und die Sicherheitsrisiken der von ihnen verwendeten Funktionspakete analysieren möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/NVIDIA/SkillSpector)
- [Auf Türkisch lesen →](https://trescout.com/discover/skillspector/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-12 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/skillspector/
