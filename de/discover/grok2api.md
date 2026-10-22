# Zentrales Management für Grok-Dienste

Dieses Gateway (API-Gateway) wurde für die Plattformen Grok Build, Grok Web und Grok Console entwickelt und vereint die Verwaltung mehrerer Konten in einem einzigen Zentrum. Das in der Go-Sprache geschriebene Tool bietet eine verwaltbare Benutzeroberfläche, indem es den Benutzerzugriff auf verschiedene Grok-Dienste standardisiert.

- ★ 7.840
- Go
- GitHub Trending · 2026-07-15

## Aktualisierungen

- **22. Oktober 2026:** Sterne 7,817 → 7,840, neueste Version v3.1.8 (22. Oktober 2026).
- **18. Oktober 2026:** Sterne 7,669 → 7,817, neueste Version v3.1.7 (18. Oktober 2026).
- **16. September 2026:** Sterne 7,543 → 7,669, neueste Version v3.1.6 (16. September 2026).
- **27. August 2026:** Sterne 7,459 → 7,543, neueste Version v3.1.5 (25. August 2026).

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich habe die Grok2API-Installation abgeschlossen und mich beim Admin-Panel angemeldet. Wie kann ich nun meine Grok Build-, Web- oder Konsolenkonten für das System definieren, wie mache ich Modellübereinstimmungen und welche Schritte kann ich befolgen, um den API-Schlüssel für die externe Verwendung zu generieren? Bitte erklären Sie diesen Vorgang Schritt für Schritt.

Repository: https://github.com/chenyme/grok2api. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Falls ein API-Schlüssel erforderlich ist, fordere mich nicht auf, ihn in den Chat zu schreiben. Zeig mir, wie ich ihn zur .env-Datei hinzufüge und stelle sicher, dass diese Datei nicht an Git übertragen wird.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [API Gateway](https://trescout.com/de/dictionary/api-gateway/)
- [Gateway](https://trescout.com/de/dictionary/gateway/)
- [API](https://trescout.com/de/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die mehrere Grok-Konten verwalten möchten und diese Dienste in ihren Anwendungen über eine Standard-API nutzen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/chenyme/grok2api)
- [Auf Türkisch lesen →](https://trescout.com/discover/grok2api/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-15 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/grok2api/
