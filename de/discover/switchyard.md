# Router, der den Datenverkehr mit künstlicher Intelligenz verwaltet

Switchyard wurde von NVIDIA entwickelt und ist eine leistungsstarke Inferenz-Engine für künstliche Intelligenz, die in der Rust-Sprache geschrieben ist. Es bietet eine optimierte Laufzeitumgebung, um große Sprachmodelle (LLM) effizient auf verschiedenen Hardware-Infrastrukturen auszuführen.

- ★ 3.227
- Rust
- GitHub Trending · 2026-08-13

## Aktualisierungen

- **27. September 2026:** Sterne 2,617 → 3,227, neueste Version v0.3.0 (22. September 2026).
- **31. August 2026:** Sterne 1,566 → 2,617, neueste Version v0.2.0 (10. August 2026).
- **15. August 2026:** Sterne 923 → 1,566, neueste Version v0.2.0 (10. August 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Fungieren Sie für mich als KI-Verkehrsrouter. Mit Switchyard möchte ich, dass Sie die Anforderungen meiner Codierungsagenten wie Claude Code oder Codex auf verschiedene Modelle verteilen, automatisch zwischen OpenAI- und Anthropic-API-Formaten übersetzen und alle Betriebsmetriken überwachen. Verwalten Sie eingehende Anfragen mit strukturierten Routing-Algorithmen und führen Sie bei Bedarf A/B-Tests oder Lastausgleich zwischen verschiedenen Modellen durch.

## Verwandte Begriffe aus dem Glossar

- [Inference](https://trescout.com/de/dictionary/inference/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [LLM](https://trescout.com/de/dictionary/llm/)
- [Rust](https://trescout.com/de/dictionary/rust/)
- [API](https://trescout.com/de/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die große Sprachmodelle über verschiedene Hardware- und Dienstanbieter hinweg effizient verwalten möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/NVIDIA-NeMo/Switchyard)
- [Auf Türkisch lesen →](https://trescout.com/discover/switchyard/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-13 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/switchyard/
