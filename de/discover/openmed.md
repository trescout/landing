# Open-Source-Künstliche Intelligenz im Gesundheitswesen

OpenMed ist eine Plattform, die Open-Source-Modelle für künstliche Intelligenz und Datensätze für das Gesundheitswesen zusammenführt. Diese Python-basierte Bibliothek wurde für medizinisch orientierte Anwendungen entwickelt und zielt darauf ab, Prozesse zur Verarbeitung von Gesundheitsdaten zu standardisieren.

- ★ 5.329
- Python
- GitHub Trending · 2026-06-10

## Aktualisierungen

- **16. September 2026:** Sterne 5,217 → 5,329, neueste Version v2.5.0 (15. September 2026).
- **5. September 2026:** Sterne 5,076 → 5,217, neueste Version v2.3.0 (4. September 2026).
- **21. August 2026:** Sterne 5,015 → 5,076, neueste Version v2.2.0 (21. August 2026).
- **15. August 2026:** Sterne 4,793 → 5,015, neueste Version v2.1.0 (12. August 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte medizinische Texte mithilfe der OpenMed-Bibliothek analysieren. Ich habe Python auf meinem Gerät installiert. Zunächst habe ich die Installation mit dem Befehl pip install „openmed[hf]“ abgeschlossen. Welche Funktionen sollte ich nun in meinem Python-Code aufrufen, um meine klinischen Notizen zu analysieren und darin medizinische Begriffe oder personenbezogene Daten (PII) zu erkennen? Bitte erstellen Sie mir einen einfachen Beispielcodeblock zur Modellauswahl und zum Drucken der Ausgaben.

## Verwandte Begriffe aus dem Glossar

- [Apple Silicon](https://trescout.com/de/dictionary/apple-silicon/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an medizinisches Fachpersonal und Softwareentwickler, die datenschutzorientierte Analysen auf ihrer eigenen Hardware durchführen möchten, ohne ihre medizinischen Daten an Cloud-Dienste zu senden.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/maziyarpanahi/openmed)
- [Auf Türkisch lesen →](https://trescout.com/discover/openmed/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-10 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openmed/
