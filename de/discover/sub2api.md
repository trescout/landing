# Verwalten Sie KI-Abonnements von einem einzigen Zentrum aus

Sub2API ist ein Open-Source-Vermittlungsdienst, der Einzelpunktzugriff und Kostenteilung für Claude-, OpenAI-, Gemini- und Grok-Abonnements bietet.

- ★ 43.558
- Go
- GitHub Trending · 2026-08-23

## Aktualisierungen

- **9. Oktober 2026:** Sterne 43,391 → 43,558, neueste Version v0.2.15 (9. Oktober 2026).
- **7. Oktober 2026:** Sterne 43,206 → 43,391, neueste Version v0.2.14 (7. Oktober 2026).
- **2. Oktober 2026:** Sterne 43,199 → 43,206, neueste Version v0.2.13 (2. Oktober 2026).
- **2. Oktober 2026:** Sterne 43,119 → 43,199, neueste Version v0.2.12 (2. Oktober 2026).

## Was es bringt

- Kombiniert verschiedene KI-Abonnements in einer Schnittstelle
- Hilft Ihnen, die Abonnementkosten effizient zuzuordnen
- Bietet die Möglichkeit, integriert mit vorhandenen Tools zu arbeiten

## Installation

**automatische Installation**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

**Installation mit Docker**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
```

## Ausführung

**Starten Sie den Dienst**

```
docker compose up -d
```

**Administratorkennwort anzeigen**

```
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Wie kann ich mithilfe der Sub2API-Plattform verschiedene KI-Dienste wie Claude, OpenAI, Gemini und Grok über ein einziges API-Gateway konfigurieren? Erklären Sie die grundlegenden Schritte, die ich befolgen muss, um meine Abonnementkontingente effizient zuzuweisen und sie in meine vorhandenen Softwaretools zu integrieren. Fassen Sie außerdem die rechtlichen und technischen Aspekte zusammen, auf die ich achten muss, um bei der Nutzung dieser Plattform die Nutzungsbedingungen von Anbietern wie Anthropic einzuhalten.

## Verwandte Begriffe aus dem Glossar

- [API](https://trescout.com/de/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für Entwickler, die mehrere KI-Abonnements auf einer einzigen Plattform verwalten und ihre Kosten optimieren möchten.
- **Lizenz:** LGPL-3.0

## Links

- [GitHub-Repository →](https://github.com/Wei-Shaw/sub2api)
- [Auf Türkisch lesen →](https://trescout.com/discover/sub2api/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-23 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/sub2api/
