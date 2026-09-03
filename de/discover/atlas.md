# Quellcodeverwaltung für KI-Agenten

Atlas ist ein Quellcodeverwaltungssystem (Source Control) für KI-Agenten, die in Softwareentwicklungsprozessen eingesetzt werden. Es ermöglicht die zentrale Überwachung und Abfrage von Änderungen, die von mehreren Programmieragenten vorgenommen wurden.

- ★ 3.058
- Rust
- GitHub Trending · 2026-09-03

## Was es bringt
- Überwacht Änderungen verschiedener Programmieragenten zentral.
- Ermöglicht durch einen gemeinsamen Speicher zwischen den Agenten, bei Aufgabenwechseln genau dort weiterzumachen, wo Sie aufgehört haben.
- Verknüpft jede Codeänderung mit der Begründung und den Befehlen des Agenten, der die Änderung vorgenommen hat.

## Installation
**Installation der erforderlichen Abhängigkeiten**

```
sudo apt install -y libglib2.0-dev libgtk-3-dev libwebkit2gtk-4.1-dev
```

**Kompilierung der Anwendung aus dem Quellcode**

```
git clone https://github.com/pacifio/atlas
cd atlas
bun install
bun run dev:app
```


## Wenn Sie nicht programmieren
Du bist ein Softwareentwicklungsassistent. Protokolliere alle Codeänderungen, die du mit Atlas vornimmst, sowie deine Entscheidungen und die verwendeten Werkzeuge zusammen mit dem Sitzungsverlauf. Wenn du während der Arbeit zwischen verschiedenen Agenten wie Claude Code oder Codex wechseln musst, lies die Pläne und Architekturhinweise aus der vorherigen Sitzung aus dem gemeinsamen Speicher. Rufe Dateien, Ordner oder vergangene Sitzungen in der Codebasis mit dem '@'-Zeichen auf, um den Kontext zu wahren, und dokumentiere den Grund für jede deiner Änderungen zusammen mit den Begründungen der jeweiligen Sitzung.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/atlas/
