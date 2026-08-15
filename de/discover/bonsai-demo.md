# KI-Modelle auf lokalem Gerät

Das Bonsai-Demoprojekt bietet ein Toolset, das die Bereitstellungsprozesse von Modellen für maschinelles Lernen vereinfachen soll. Die Software hilft Entwicklern, ihre Anwendungsprozesse zu optimieren, indem sie komplexe Modellarchitekturen in überschaubare Arbeitsabläufe umwandelt.

- ★ 1.587
- Shell
- GitHub Trending · 2026-07-17

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
Ich möchte mithilfe des Bonsai-Demo-Projekts KI-Modelle auf meinem lokalen Gerät ausführen. Nachdem ich das für die Installation erforderliche Git-Repository geklont habe, muss ich meine HuggingFace-Token-Informationen definieren und die Abhängigkeiten und Modelle mit dem Befehl ./setup.sh herunterladen. Dann kann ich mit dem Befehl ./scripts/start_llama_server.sh den lokalen Server hochfahren und über Port 8080 über meinen Browser mit der KI interagieren.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/bonsai-demo/
