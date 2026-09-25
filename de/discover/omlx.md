# KI-Server für Mac-Computer

Omlx ist ein lokaler Inferenzserver der nächsten Generation für große Sprachmodelle (LLMs) auf Apple Silicon (M1/M2/M3/M4) Macs, der Continuous Batching und SSD-Caching unterstützt. Er vereint das Apple MLX-Framework mit einer OpenAI-kompatiblen API und einer praktischen macOS-Menüleistensteuerung.

- ★ 21.147
- Python
- GitHub Trending · 2026-08-18

## Aktualisierungen
- 31. August 2026: Sterne 20.793 → 21.147, neueste Version v0.6.4 (29. August 2026).
- 27. August 2026: Sterne 20.069 → 20.793, neueste Version v0.6.3rc3 (24. August 2026).
- 20. August 2026: Sterne 19.758 → 20.069, neueste Version v0.6.3rc2 (20. August 2026).
- 19. August 2026: Sterne 19.519 → 19.758, neueste Version v0.6.3rc1 (19. August 2026).

## Was es bringt
- Apple MLX- und Metal-Hardwarebeschleunigung: Nutzt die Unified Memory Architecture (UMA) von Apple Silicon direkt aus, um Speicherübertragungs-Engpässe zwischen CPU und GPU vollständig zu vermeiden.
- Kontinuierliche Stapelverarbeitung (Continuous Batching): Bündelt parallele Anfragen mehrerer Benutzer und Agenten in einem Rechenzyklus und steigert den Serverdurchsatz um das bis zu Dreifache.
- SSD-Caching und Chunked Prefill: Lagert Key-Value-Caches (KV) bei langen Kontextfenstern auf die schnelle NVMe-SSD aus und verhindert so Out-of-Memory-Abstürze (OOM).
- OpenAI-kompatible Standard-API: Funktioniert ohne Konfigurationsaufwand mit Cursor, Open WebUI, Continue und LangChain über /v1/chat/completions und /v1/models Endpunkte.
- macOS-Menüleistensteuerung: Server starten, stoppen, Modelle wechseln und die Speicherauslastung in Echtzeit überwachen – ganz ohne Terminalbefehle.

## Installation

**Installation über Homebrew**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```

## Ausführung

**Hintergrunddienst starten**

```
omlx start
```

**Bestimmtes Modell herunterladen und bereitstellen**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Technische Architektur und Funktionsweise

Omlx basiert auf dem maschinellen Lern-Framework MLX von Apple. Es baut auf drei architektonischen Säulen auf, die entwickelt wurden, um klassische Inferenzgrenzen auf dem Mac (wie llama.cpp oder Ollama) zu überwinden:
- Volle Ausnutzung des einheitlichen Speichers (UMA): Anders als PCs mit separaten Grafikkarten können bei Apple Silicon die GPU-Kerne direkt auf 128 GB oder 192 GB RAM zugreifen. Omlx verarbeitet diesen Speicherpool über Metal Shading Language (MSL) Kernel verzögerungsfrei.
- Dynamisches KV-Cache-Management (PagedAttention): Verwaltet Key-Value-Tensoren in seitenbasierten Blöcken, um Speicherfragmentierung bei vielen gleichzeitigen Anfragen zu verhindern und Speicher sofort nach Abschluss freizugeben.
- SSD-Überlaufebebene: Übersteigt der KV-Cache in riesigen 32K- oder 128K-Kontextfenstern den physischen RAM, lagert Omlx automatisch auf die integrierte NVMe-SSD aus, sodass die Modellausführung stabil bleibt.

## OpenAI-kompatible lokale API-Integration

Nach dem Start stellt Omlx lokal eine OpenAI-kompatible REST-API bereit (standardmäßig unter http://localhost:8000). So binden Sie Ihre Code-Editoren und KI-Tools direkt an:

**API-Test mit cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Was ist der Hauptvorteil der Apple Silicon Architektur?"}],
    "temperature": 0.7
  }'
```

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich möchte ein lokales großes Sprachmodell mit Omlx auf meinem Apple Silicon Mac ausführen. Nach der Installation über Homebrew: Kannst du mir Schritt für Schritt erklären, wie ich den Server im Hintergrund starte, Modelle über die Menüleiste verwalte und den Cursor-Code-Editor oder ein Python-Skript über die openai-Bibliothek mit diesem lokalen Modell verbinde?

- **Für wen:** KI-Entwickler und Mac-Nutzer, die maximale Inferenzgeschwindigkeit und vollständigen Datenschutz auf Apple Silicon Hardware suchen.
- **Lizenz:** Apache-2.0 (Open-Source-Lizenz)
- **Framework:** Lokale Inferenz-Engine basierend auf Apple MLX und Python
- **Hardware:** Apple Silicon M1, M2, M3, M4 Serie (Pro, Max und Ultra unterstützt)

## Häufig gestellte Fragen
- Was ist der Hauptunterschied zwischen Omlx und Ollama? Während Ollama primär auf der C++-Basis von llama.cpp aufbaut, läuft Omlx nativ auf Apples MLX-Framework. Durch diese tiefere Integration in Metal und die Neural Engine werden höhere Token-Generierungsraten erzielt, insbesondere bei Continuous Batching und langen Kontexten.
- Welche Modelle können mit 16 GB oder 24 GB RAM betrieben werden? 4-Bit quantisierte 8B-Modelle (Llama 3, Qwen 2.5, Mistral) belegen etwa 5-6 GB Speicher und laufen auf 16 GB Macs sehr flüssig. Auf Geräten mit 24 GB oder 36 GB Unified Memory können 14B- oder 32B-Modelle geladen werden.
- Belastet das SSD-Caching die Lebensdauer der Mac-SSD? Nein. Omlx verwendet intelligentes Puffer-Management, um unnötige Schreibzyklen zu verhindern. Es wird nur dann aktiv, wenn der Kontext den physischen Arbeitsspeicher übersteigt.
- Funktioniert Omlx auf älteren Intel-Macs oder PCs mit Windows/Linux? Nein. Omlx ist konsequent auf Apple Silicon (ARM-Architektur) und Apple MLX zugeschnitten. Auf Intel- oder x86-Rechnern läuft es nicht.

## Links
- [GitHub →](https://github.com/jundot/omlx)

## Verwandte Begriffe aus dem Glossar
Apple Silicon Continuous Batching LLM Local Open Source

---
Source: TreScout Discover · https://trescout.com/de/discover/omlx/
