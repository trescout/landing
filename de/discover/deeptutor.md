# Künstliche Intelligenz-gestütztes personalisiertes Training

DeepTutor ist ein auf lebenslangem Lernen basierendes privates Nachhilfesystem, das personalisierte Bildungsprozesse mithilfe von Schülerdaten bietet. Das Projekt zielt darauf ab, das Lernerlebnis mit künstlicher Intelligenz unterstützten individualisierten Nachhilfemethoden zu optimieren.

- ★ 40.808
- Python
- GitHub Trending · 2026-07-16

## Aktualisierungen

- **5. Oktober 2026:** Sterne 40,358 → 40,808, neueste Version v1.6.13 (4. Oktober 2026).
- **27. September 2026:** Sterne 40,334 → 40,358, neueste Version v1.6.12 (27. September 2026).
- **27. September 2026:** Sterne 39,561 → 40,334, neueste Version v1.6.11 (24. September 2026).
- **14. September 2026:** Sterne 39,283 → 39,561, neueste Version v1.6.8 (14. September 2026).

## Was es bringt

- Privatunterrichtssystem mit Schwerpunkt auf lebenslangem Lernen
- Interaktion mit personalisierten Agenten der künstlichen Intelligenz
- Erweiterte Wissensdatenbank und RAG-Unterstützung

## Installation

**Schnelle Installation**

```
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # prompts for ports + LLM provider + optional embedding
deeptutor start    # starts backend + frontend; keep the terminal open
```

**Laufen mit Docker**

```
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

## Ausführung

**Systeminitialisierung**

```
deeptutor start    # starts backend + frontend; keep the terminal open
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Wie kann ich meinen Lernprozess mit dem DeepTutor-System personalisieren? Erklären Sie die grundlegenden Schritte, die ich befolgen muss, um meine eigenen KI-Partner zu erstellen und mein lebenslanges Lernerlebnis zu optimieren, indem ich meine benutzerdefinierten Schulungsmaterialien in dieses System integriere.

## Verwandte Begriffe aus dem Glossar

- [Lifelong Learning](https://trescout.com/de/dictionary/lifelong-learning/)
- [Personalized Tutoring](https://trescout.com/de/dictionary/personalized-tutoring/)
- [Tutoring](https://trescout.com/de/dictionary/tutoring/)
- [RAG](https://trescout.com/de/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Studierende und Lehrkräfte, die ihren eigenen privaten Bildungsassistenten erstellen und eine personalisierte Lernumgebung schaffen möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/HKUDS/DeepTutor)
- [Auf Türkisch lesen →](https://trescout.com/discover/deeptutor/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-16 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/deeptutor/
