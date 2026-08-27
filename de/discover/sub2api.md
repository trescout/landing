# Verwalten Sie KI-Abonnements von einem einzigen Zentrum aus

Sub2API ist ein Open-Source-Vermittlungsdienst, der Einzelpunktzugriff und Kostenteilung für Claude-, OpenAI-, Gemini- und Grok-Abonnements bietet.

- ★ 39.608
- Go
- GitHub Trending · 2026-08-23

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
Wie kann ich mithilfe der Sub2API-Plattform verschiedene KI-Dienste wie Claude, OpenAI, Gemini und Grok über ein einziges API-Gateway konfigurieren? Erklären Sie die grundlegenden Schritte, die ich befolgen muss, um meine Abonnementkontingente effizient zuzuweisen und sie in meine vorhandenen Softwaretools zu integrieren. Fassen Sie außerdem die rechtlichen und technischen Aspekte zusammen, auf die ich achten muss, um bei der Nutzung dieser Plattform die Nutzungsbedingungen von Anbietern wie Anthropic einzuhalten.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/sub2api/
