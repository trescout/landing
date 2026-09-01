# Training der künstlichen Intelligenz bei geringem Gedächtnis

Soup ist eine Python-Bibliothek, die die Feinabstimmung großer Sprachmodelle über eine einzige YAML-Datei ermöglicht. Es kann Modelle mit 8 Milliarden Parametern mithilfe der Layer-Streaming-Methode auf Laptop-Grafikprozessoren mit 4 GB Speicher trainieren.

- ★ 4.285
- Python
- GitHub Trending · 2026-08-16

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
Ich möchte mithilfe der Soup-Bibliothek auf meinem Computer mit 4 GB Grafikspeicher ein Modell der künstlichen Intelligenz mit 8 Milliarden Parametern trainieren. Helfen Sie mir, eine YAML-Konfigurationsdatei zu erstellen, die Layer-Streaming ermöglicht und 4-Bit-Quantisierung verwendet. Bereiten Sie den Inhalt der Datei „soup.yaml“ vor, die zum Starten des Trainingsprozesses erforderlich ist, und erklären Sie dann Schritt für Schritt, wie Sie das Training mithilfe dieser Datei starten.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/soup/
