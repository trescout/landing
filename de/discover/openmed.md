# Open-Source-Künstliche Intelligenz im Gesundheitswesen

OpenMed ist eine Plattform, die Open-Source-Modelle für künstliche Intelligenz und Datensätze für das Gesundheitswesen zusammenführt. Diese Python-basierte Bibliothek wurde für medizinisch orientierte Anwendungen entwickelt und zielt darauf ab, Prozesse zur Verarbeitung von Gesundheitsdaten zu standardisieren.

- ★ 4.793
- Python
- GitHub Trending · 2026-06-10

## Was es bringt
- Extrahiert strukturierte medizinische Erkenntnisse aus klinischen Texten.
- Anonymisiert persönliche Gesundheitsdaten auf dem Gerät.
- Es führt mehr als 1.000 medizinische KI-Modelle offline aus.

## Installation
**Grundeinrichtung**

```
pip install "openmed[hf]"
```

**Unterstützung für Apple Silicon (MLX).**

```
pip install "openmed[mlx]"
```


## Ausführung
**Einfache Analyse mit Python**

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```


## Wenn Sie nicht programmieren
Ich möchte medizinische Texte mithilfe der OpenMed-Bibliothek analysieren. Ich habe Python auf meinem Gerät installiert. Zunächst habe ich die Installation mit dem Befehl pip install „openmed[hf]“ abgeschlossen. Welche Funktionen sollte ich nun in meinem Python-Code aufrufen, um meine klinischen Notizen zu analysieren und darin medizinische Begriffe oder personenbezogene Daten (PII) zu erkennen? Bitte erstellen Sie mir einen einfachen Beispielcodeblock zur Modellauswahl und zum Drucken der Ausgaben.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openmed/
