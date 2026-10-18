# KI-Modelle auf lokalem Gerät

Das Bonsai-Demoprojekt bietet ein Toolset, das die Bereitstellungsprozesse von Modellen für maschinelles Lernen vereinfachen soll. Die Software hilft Entwicklern, ihre Anwendungsprozesse zu optimieren, indem sie komplexe Modellarchitekturen in überschaubare Arbeitsabläufe umwandelt.

- ★ 2.706
- Shell
- GitHub Trending · 2026-07-17

## Aktualisierungen

- **19. September 2026:** Sterne 1,587 → 2,706.

## Was es bringt

- Führt Hochleistungsmodelle lokal mit geringer Speichernutzung aus.
- Es bietet erweiterte Funktionen wie visuelle Verarbeitung und Ride-Hailing.
- Bietet umfassende Kompatibilität mit verschiedenen Hardwarearchitekturen.

## Installation

**macOS- und Linux-Installation**

```
git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo

# (Optional) Choose a model size: 27B (default), 8B, 4B, or 1.7B
export BONSAI_MODEL=27B

# Set your HuggingFace token (only required for 27B while its repos are private)
export BONSAI_TOKEN="hf_your_token_here"

# One command does everything: installs deps, downloads models + binaries
./setup.sh
```

## Ausführung

**Starten des lokalen Servers**

```
./scripts/start_llama_server.sh    # http://localhost:8080

# Serve a different model size
BONSAI_MODEL=4B ./scripts/start_llama_server.sh
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mithilfe des Bonsai-Demo-Projekts KI-Modelle auf meinem lokalen Gerät ausführen. Nachdem ich das für die Installation erforderliche Git-Repository geklont habe, muss ich meine HuggingFace-Token-Informationen definieren und die Abhängigkeiten und Modelle mit dem Befehl ./setup.sh herunterladen. Dann kann ich mit dem Befehl ./scripts/start_llama_server.sh den lokalen Server hochfahren und über Port 8080 über meinen Browser mit der KI interagieren.

Repository: https://github.com/PrismML-Eng/Bonsai-demo. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Falls ein API-Schlüssel erforderlich ist, fordere mich nicht auf, ihn in den Chat zu schreiben. Zeig mir, wie ich ihn zur .env-Datei hinzufüge und stelle sicher, dass diese Datei nicht an Git übertragen wird.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Machine Learning](https://trescout.com/de/dictionary/machine-learning/)
- [Shell](https://trescout.com/de/dictionary/shell/)
- [Token](https://trescout.com/de/dictionary/token/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Entwickler, die KI-Modelle mit hohem Durchsatz auf ihrer nativen Hardware ausführen möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/PrismML-Eng/Bonsai-demo)
- [Auf Türkisch lesen →](https://trescout.com/discover/bonsai-demo/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-17 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/bonsai-demo/
