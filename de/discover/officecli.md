# Verwalten Sie Office-Dateien mit künstlicher Intelligenz

OfficeCLI bietet eine Open-Source-Office-Suite, die es KI-Agenten ermöglicht, Word-, Excel- und PowerPoint-Dateien direkt zu lesen, zu bearbeiten und zu automatisieren. Dieses mit C# entwickelte Tool ermöglicht die Ausführung von Vorgängen über eine einzige Binärdatei, ohne dass eine Office-Softwareinstallation erforderlich ist.

- ★ 32.795
- C#
- GitHub Trending · 2026-07-08

## Aktualisierungen

- **30. Oktober 2026:** Sterne 32,527 → 32,795, neueste Version v1.0.160 (30. Oktober 2026).
- **27. Oktober 2026:** Sterne 32,214 → 32,527, neueste Version v1.0.159 (27. Oktober 2026).
- **20. Oktober 2026:** Sterne 31,905 → 32,214, neueste Version v1.0.158 (20. Oktober 2026).
- **12. Oktober 2026:** Sterne 31,762 → 31,905, neueste Version v1.0.157 (12. Oktober 2026).

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Sie können Word-, Excel- und PowerPoint-Dateien mit dem für Sie vorbereiteten OfficeCLI-Tool verwalten. Um dieses Tool zu verwenden, installieren Sie die erforderliche Skill-Datei, indem Sie den folgenden Befehl ausführen: curl -fsSL https://officecli.ai/SKILL.md. Nach diesem Vorgang können Sie Office-Dokumente über die Befehlszeile lesen, bearbeiten und erstellen.

Repository: https://github.com/iOfficeAI/OfficeCLI. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [PowerPoint](https://trescout.com/de/dictionary/powerpoint/)
- [Binary](https://trescout.com/de/dictionary/binary/)
- [Skill](https://trescout.com/de/dictionary/skill/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die Office-Dokumente automatisieren möchten, und an Benutzer, die Agenten der künstlichen Intelligenz in ihre Büroprozesse integrieren möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/iOfficeAI/OfficeCLI)
- [Auf Türkisch lesen →](https://trescout.com/discover/officecli/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-08 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/officecli/
