# Verwalten Sie gemeinsam Ihre Reisepläne

TREK ist eine selbst gehostete Reiseplanungsanwendung, die Funktionen wie Echtzeit-Zusammenarbeit, interaktive Karten und Budgetverwaltung bietet. Mit der Unterstützung progressiver Webanwendungen (PWA) und der Integration von Single Sign-on (SSO) können Benutzer ihre Reiseprozesse digital organisieren.

- ★ 7.040
- GitHub Trending · 2026-06-26

## Was es bringt
- Erstellen Sie tägliche Reiserouten und Pläne per Drag & Drop
- Gruppenausgaben verfolgen und pro Person aufteilen
- Automatisches Reise- und Budgetmanagement mit Integration künstlicher Intelligenz

## Installation
**Schnelle Installation mit Docker**

```
ENCRYPTION_KEY=$(openssl rand -hex 32) docker run -d -p 3000:3000 \
  -e ENCRYPTION_KEY=$ENCRYPTION_KEY \
  -v ./data:/app/data -v ./uploads:/app/uploads mauriceboe/trek
```


## Wenn Sie nicht programmieren
Du bist Reiseassistent. Erstellen Sie mithilfe der MCP-Tools (Model Context Protocol) auf TREK einen dreitägigen Paris-Reiseplan für mich, passen Sie mein Budget an die täglichen Ausgabengrenzen an und erstellen Sie eine Packliste für das, was ich mitnehmen muss.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/trek/
