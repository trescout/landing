# KI-Coding-Agent für Terminal

DeepSeek-Reasonix ist ein KI-Coding-Agent, der auf dem Terminal läuft und auf DeepSeek-Modellen basiert. Dieses Tool konzentriert sich auf die Stabilität des Präfix-Cache und stellt sicher, dass Entwickler über lange Sitzungen hinweg unterbrechungsfreie Codierungsunterstützung erhalten.

- ★ 35.992
- Go
- GitHub Trending · 2026-08-03

## Aktualisierungen

- **29. Oktober 2026:** Sterne 35,979 → 35,992, neueste Version studio-v2.55.0 (29. Oktober 2026).
- **28. Oktober 2026:** Sterne 35,978 → 35,979, neueste Version studio-v2.54.0 (28. Oktober 2026).
- **27. Oktober 2026:** Sterne 35,965 → 35,978, neueste Version studio-v2.53.1 (27. Oktober 2026).
- **26. Oktober 2026:** Sterne 35,956 → 35,965, neueste Version studio-v2.52.0 (26. Oktober 2026).

## Was es bringt

- Bietet langfristige, unterbrechungsfreie Codierungsunterstützung mit DeepSeek-Modellen.
- Es bietet eine kostengünstige Sitzungsverwaltung mit seiner Präfix-Caching-Funktion.
- Es ermöglicht eine flexible Nutzung über das Terminal mit konfigurierbarer Plug-in-Unterstützung.

## Installation

**Installation über NPM oder Homebrew**

```
npm i -g reasonix                  # any OS; pulls the prebuilt native binary
brew install esengine/reasonix/reasonix   # macOS
```

**Kompilieren aus Quellcode**

```
git clone https://github.com/esengine/DeepSeek-Reasonix.git
cd DeepSeek-Reasonix
make build      # -> bin/reasonix(.exe)
make cross      # -> dist/ (darwin|linux|windows × amd64|arm64)
```

## Ausführung

**Konfiguration und Initialisierung**

```
reasonix setup                      # configure a provider and model
reasonix                            # start an interactive session
reasonix run "implement the TODOs in main.go"
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Während ich mit diesem künstlichen Intelligenz-Codierungsagenten arbeite, der auf dem Terminal läuft, entwickle ich Codevorschläge unter Berücksichtigung der aktuellen Struktur und Ziele meines Projekts. Konzentrieren Sie sich auf die Erstellung konsistenter, kostengünstiger Antworten über unsere langen Sitzungen hinweg mithilfe der Präfix-Cache-Stabilität. Stellen Sie beim Schreiben oder Debuggen von Code modulare und saubere Lösungen bereit, die den Anforderungen des Projekts entsprechen.

Repository: https://github.com/esengine/DeepSeek-Reasonix. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Terminal](https://trescout.com/de/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler, die in einer Terminalumgebung arbeiten und ihre Codierungsprozesse automatisieren und in langfristigen Projekten Unterstützung durch künstliche Intelligenz erhalten möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/esengine/DeepSeek-Reasonix)
- [Auf Türkisch lesen →](https://trescout.com/discover/deepseek-reasonix/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-03 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/deepseek-reasonix/
