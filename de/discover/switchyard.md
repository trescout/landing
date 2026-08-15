# Router, der den Datenverkehr mit künstlicher Intelligenz verwaltet

Switchyard wurde von NVIDIA entwickelt und ist eine leistungsstarke Inferenz-Engine für künstliche Intelligenz, die in der Rust-Sprache geschrieben ist. Es bietet eine optimierte Laufzeitumgebung, um große Sprachmodelle (LLM) effizient auf verschiedenen Hardware-Infrastrukturen auszuführen.

- ★ 923
- Rust
- GitHub Trending · 2026-08-13

## Was es bringt
- Leiten des Datenverkehrs zwischen verschiedenen Modellen der künstlichen Intelligenz
- Übersetzung zwischen OpenAI- und Anthropic-API-Formaten
- Verfolgen Sie Transaktionsmetriken und Fehlerprotokolle

## Installation
**Installation als Kommandozeilentool**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv tool install --python 3.10 "nemo-switchyard[cli]"
```

**Installation als Server**

```
cargo install --locked switchyard-server
switchyard-server --help
```


## Ausführung
**Überprüfen Sie den Serverstatus**

```
curl http://localhost:4000/health
```


## Wenn Sie nicht programmieren
Fungieren Sie für mich als KI-Verkehrsrouter. Mit Switchyard möchte ich, dass Sie die Anforderungen meiner Codierungsagenten wie Claude Code oder Codex auf verschiedene Modelle verteilen, automatisch zwischen OpenAI- und Anthropic-API-Formaten übersetzen und alle Betriebsmetriken überwachen. Verwalten Sie eingehende Anfragen mit strukturierten Routing-Algorithmen und führen Sie bei Bedarf A/B-Tests oder Lastausgleich zwischen verschiedenen Modellen durch.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/switchyard/
