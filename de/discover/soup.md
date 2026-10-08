# Training der künstlichen Intelligenz bei geringem Gedächtnis

Soup ist eine Python-Bibliothek, die die Feinabstimmung großer Sprachmodelle über eine einzige YAML-Datei ermöglicht. Es kann Modelle mit 8 Milliarden Parametern mithilfe der Layer-Streaming-Methode auf Laptop-Grafikprozessoren mit 4 GB Speicher trainieren.

- ★ 7.988
- Python
- GitHub Trending · 2026-08-16

## Aktualisierungen

- **2. Oktober 2026:** Sterne 7,309 → 7,988, neueste Version v0.75.2 (1. Oktober 2026).
- **27. September 2026:** Sterne 6,267 → 7,309, neueste Version v0.75.1 (21. September 2026).
- **13. September 2026:** Sterne 5,332 → 6,267, neueste Version v0.75.0 (12. September 2026).
- **5. September 2026:** Sterne 4,285 → 5,332, neueste Version v0.74.0 (4. September 2026).

## Was es bringt

- Auf Laptops mit 4 GB Grafikspeicher können Sie Modelle mit 8 Milliarden Parametern trainieren.
- Mit der Layer-Flow-Methode müssen Sie sich nicht mit komplexen Installationen auseinandersetzen, indem Sie Hardwarebeschränkungen überwinden.
- Sie können den gesamten Trainingsprozess über eine einzige Konfigurationsdatei verwalten.

## Installation

**Grundeinrichtung**

```
pip install "soup-cli[train]"
```

**Setup mit allen Funktionen**

```
pip install "soup-cli[all]"
```

## Ausführung

**Beginnen Sie mit dem Training**

```
soup init --template chat
soup train
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mithilfe der Soup-Bibliothek auf meinem Computer mit 4 GB Grafikspeicher ein Modell der künstlichen Intelligenz mit 8 Milliarden Parametern trainieren. Helfen Sie mir, eine YAML-Konfigurationsdatei zu erstellen, die Layer-Streaming ermöglicht und 4-Bit-Quantisierung verwendet. Bereiten Sie den Inhalt der Datei „soup.yaml“ vor, die zum Starten des Trainingsprozesses erforderlich ist, und erklären Sie dann Schritt für Schritt, wie Sie das Training mithilfe dieser Datei starten.

## Verwandte Begriffe aus dem Glossar

- [Layer Streaming](https://trescout.com/de/dictionary/layer-streaming/)
- [Fine-tuning](https://trescout.com/de/dictionary/fine-tuning/)
- [Large Language Models](https://trescout.com/de/dictionary/large-language-models/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es ist für Entwickler gedacht, die große Sprachmodelle auf ihrem lokalen Computer ohne hohe Hardwarekosten optimieren möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/MakazhanAlpamys/Soup)
- [Auf Türkisch lesen →](https://trescout.com/discover/soup/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-16 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/soup/
