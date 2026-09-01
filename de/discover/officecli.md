# Verwalten Sie Office-Dateien mit künstlicher Intelligenz

OfficeCLI bietet eine Open-Source-Office-Suite, die es KI-Agenten ermöglicht, Word-, Excel- und PowerPoint-Dateien direkt zu lesen, zu bearbeiten und zu automatisieren. Dieses mit C# entwickelte Tool ermöglicht die Ausführung von Vorgängen über eine einzige Binärdatei, ohne dass eine Office-Softwareinstallation erforderlich ist.

- ★ 29.585
- C#
- GitHub Trending · 2026-07-08

## Was es bringt
- Bearbeiten Sie Word-, Excel- und PowerPoint-Dateien mit Code
- Führen Sie Transaktionen direkt durch, ohne Office-Software installieren zu müssen
- Geben Sie KI-Agenten die Möglichkeit, Dokumente zu erstellen

## Installation
**Installation auf macOS oder Linux**

```
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
```

**Installation unter Windows**

```
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```


## Ausführung
**Erstellen Sie eine leere Präsentation**

```
officecli create deck.pptx
```

**Fügen Sie Folien zu einer Präsentation hinzu**

```
officecli add deck.pptx / --type slide --prop title="Hello, World!"
```


## Wenn Sie nicht programmieren
Sie können Word-, Excel- und PowerPoint-Dateien mit dem für Sie vorbereiteten OfficeCLI-Tool verwalten. Um dieses Tool zu verwenden, installieren Sie die erforderliche Skill-Datei, indem Sie den folgenden Befehl ausführen: curl -fsSL https://officecli.ai/SKILL.md. Nach diesem Vorgang können Sie Office-Dokumente über die Befehlszeile lesen, bearbeiten und erstellen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/officecli/
