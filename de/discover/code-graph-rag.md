# Fragen Sie Ihr Code-Repository mit künstlicher Intelligenz ab

Code-Graph-Rag kombiniert Wissensgraphen und Fetch-Assisted Generation (RAG), um komplexe Strukturen in großen Code-Repositories zu verstehen und abzufragen. Es ermöglicht Entwicklern, mithilfe künstlicher Intelligenz Codebasen in verschiedenen Sprachen zu analysieren und zu bearbeiten.

- ★ 5.303
- Python
- GitHub Trending · 2026-08-10

## Aktualisierungen

- **31. Oktober 2026:** Sterne 5,284 → 5,303, neueste Version v0.4.5 (30. Oktober 2026).
- **26. Oktober 2026:** Sterne 5,279 → 5,284, neueste Version v0.3.13 (25. Oktober 2026).
- **24. Oktober 2026:** Sterne 5,278 → 5,279, neueste Version v0.3.2 (24. Oktober 2026).
- **23. Oktober 2026:** Sterne 5,264 → 5,278, neueste Version v0.2.19 (22. Oktober 2026).

## Was es bringt

- Erkennen Sie komplexe Zusammenhänge, indem Sie die Codebasis in einen Wissensgraphen umwandeln
- Erhalten Sie Antworten zur Codestruktur, indem Sie Fragen in natürlicher Sprache stellen
- Nehmen Sie mit strukturierten Such- und Bearbeitungstools präzise Änderungen am Code vor

## Installation

**Installation mit Paketmanager**

```
uv tool install "code-graph-rag[treesitter-full,semantic]"
```

**Alternative Installationsmethode**

```
pipx install "code-graph-rag[treesitter-full,semantic]"
```

## Ausführung

**Starten der Datenbank**

```
cgr daemon up
```

**Analysieren und befragen Sie das Lager**

```
cgr start --repo-path /path/to/repo --update-graph
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Analysieren Sie mein Code-Repository mit dem Code-Graph-RAG-Tool. Beantworten Sie meine Fragen mithilfe der Beziehungen zwischen Funktionen, Klassen und Modulen in Ihrer Codebasis. Schlagen Sie Änderungen oder Optimierungen vor, die ich mithilfe der vom Tool bereitgestellten Strukturanalysefunktionen am Code vornehmen sollte.

Repository: https://github.com/vitali87/code-graph-rag. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Monorepo](https://trescout.com/de/dictionary/monorepo/)
- [RAG](https://trescout.com/de/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler, die strukturelle Zusammenhänge in großen und komplexen Code-Repositories verstehen, abfragen und mithilfe künstlicher Intelligenz sichere Änderungen vornehmen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/vitali87/code-graph-rag)
- [Auf Türkisch lesen →](https://trescout.com/discover/code-graph-rag/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-10 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/code-graph-rag/
