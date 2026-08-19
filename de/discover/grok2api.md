# Zentrales Management für Grok-Dienste

Dieses Gateway (API-Gateway) wurde für die Plattformen Grok Build, Grok Web und Grok Console entwickelt und vereint die Verwaltung mehrerer Konten in einem einzigen Zentrum. Das in der Go-Sprache geschriebene Tool bietet eine verwaltbare Benutzeroberfläche, indem es den Benutzerzugriff auf verschiedene Grok-Dienste standardisiert.

- ★ 7.459
- Go
- GitHub Trending · 2026-07-15

## Was es bringt
- Grok Build vereint Web- und Konsolenkonten in einem Panel
- Bietet eine Standard-API-Schnittstelle, die mit OpenAI und Anthropic kompatibel ist
- Bietet erweiterte Kontoverwaltung, Modellrouting und Fehlerbehandlung

## Installation
**Schnelle Installation mit Docker**

```
git clone https://github.com/chenyme/grok2api.git
cd grok2api
cp config.example.yaml config.yaml
```

**Starten Sie den Dienst**

```
docker compose pull
docker compose up -d
```


## Ausführung
**Servicemanagement**

```
docker compose logs -f grok2api
docker compose restart grok2api
docker compose down
```


## Wenn Sie nicht programmieren
Ich habe die Grok2API-Installation abgeschlossen und mich beim Admin-Panel angemeldet. Wie kann ich nun meine Grok Build-, Web- oder Konsolenkonten für das System definieren, wie mache ich Modellübereinstimmungen und welche Schritte kann ich befolgen, um den API-Schlüssel für die externe Verwendung zu generieren? Bitte erklären Sie diesen Vorgang Schritt für Schritt.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/grok2api/
