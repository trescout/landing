# Künstliche Intelligenz-gestütztes personalisiertes Training

DeepTutor ist ein auf lebenslangem Lernen basierendes privates Nachhilfesystem, das personalisierte Bildungsprozesse mithilfe von Schülerdaten bietet. Das Projekt zielt darauf ab, das Lernerlebnis mit künstlicher Intelligenz unterstützten individualisierten Nachhilfemethoden zu optimieren.

- ★ 38.364
- Python
- GitHub Trending · 2026-07-16

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
Wie kann ich meinen Lernprozess mit dem DeepTutor-System personalisieren? Erklären Sie die grundlegenden Schritte, die ich befolgen muss, um meine eigenen KI-Partner zu erstellen und mein lebenslanges Lernerlebnis zu optimieren, indem ich meine benutzerdefinierten Schulungsmaterialien in dieses System integriere.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/deeptutor/
