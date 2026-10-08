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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Du bist Reiseassistent. Erstellen Sie mithilfe der MCP-Tools (Model Context Protocol) auf TREK einen dreitägigen Paris-Reiseplan für mich, passen Sie mein Budget an die täglichen Ausgabengrenzen an und erstellen Sie eine Packliste für das, was ich mitnehmen muss.

## Verwandte Begriffe aus dem Glossar

- [PWA](https://trescout.com/de/dictionary/pwa/)
- [SSO](https://trescout.com/de/dictionary/sso/)
- [Self-hosted](https://trescout.com/de/dictionary/self-hosted/)
- [Model Context Protocol](https://trescout.com/de/dictionary/model-context-protocol/)
- [Model Context Protocol](https://trescout.com/de/dictionary/model-context-protocol-mcp/)
- [Context](https://trescout.com/de/dictionary/context/)

- **Für wen es gedacht ist:** Es richtet sich an Reisende, die ihre Reisen digital organisieren, ihre Ausgaben verfolgen und die volle Kontrolle über ihre eigenen Daten haben möchten.
- **Lizenz:** AGPL-3.0

## Links

- [GitHub-Repository →](https://github.com/mauriceboe/TREK)
- [Auf Türkisch lesen →](https://trescout.com/discover/trek/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-26 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/trek/
