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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Du bist Reiseassistent. Erstellen Sie mithilfe der MCP-Tools (Model Context Protocol) auf TREK einen dreitägigen Paris-Reiseplan für mich, passen Sie mein Budget an die täglichen Ausgabengrenzen an und erstellen Sie eine Packliste für das, was ich mitnehmen muss.

Repository: https://github.com/mauriceboe/TREK. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [PWA](https://trescout.com/de/dictionary/pwa/)
- [SSO](https://trescout.com/de/dictionary/sso/)
- [Self-hosted](https://trescout.com/de/dictionary/self-hosted/)
- [Context](https://trescout.com/de/dictionary/context/)
- [MCP](https://trescout.com/de/dictionary/mcp/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Reisende, die ihre Reisen digital organisieren, ihre Ausgaben verfolgen und die volle Kontrolle über ihre eigenen Daten haben möchten.
- **Lizenz:** AGPL-3.0

## Links

- [GitHub-Repository →](https://github.com/mauriceboe/TREK)
- [Auf Türkisch lesen →](https://trescout.com/discover/trek/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-26 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/trek/
