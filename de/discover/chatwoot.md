# Open-Source-Kundensupportplattform

Chatwoot ist eine Open-Source-Plattform, die Live-Chat, E-Mail-Support und Omni-Channel-Desk-Management bietet. Dieses Tool wurde als Alternative zu kommerzieller Software wie Intercom und Zendesk entwickelt und ermöglicht Ihnen die Verwaltung von Kundeninteraktionen von einem einzigen Zentrum aus.

- ★ 36.927
- GitHub Trending · 2026-06-12

**Hinweis von TreScout:** Es sammelt Nachrichten von Kunden auf einem einzigen Bildschirm: Site-Chat, E-Mail, WhatsApp. Für vorgefertigte Dienste, die die gleiche Aufgabe erfüllen, wird eine monatliche Gebühr pro Person erhoben. Da sie jedoch auf Ihrem eigenen Server ausgeführt werden, fällt keine solche Gebühr an. Im Gegenzug werden der Server und die Wartung zu Ihrer Aufgabe. Die Installation ist nicht monolithisch, erfordert mehrere Dienstprogramme und hat mit den günstigsten Serverpaketen Schwierigkeiten.

## Aktualisierungen

- **18. September 2026:** Sterne 36,253 → 36,927, neueste Version v4.18.0 (18. September 2026).
- **27. August 2026:** Sterne 36,001 → 36,253, neueste Version v4.17.1 (27. August 2026).
- **20. August 2026:** Sterne 35,290 → 36,001, neueste Version v4.17.0 (20. August 2026).
- **1. August 2026:** Sterne 30,493 → 35,290, neueste Version v4.16.2 (27. Juli 2026).

## Was es bringt

- Es vereint alle Kundenkanäle in einem einzigen Posteingang.
- Beantwortet automatisch Routinefragen mit einem durch künstliche Intelligenz unterstützten Assistenten.
- Sie haben die volle Kontrolle über Ihre Kundendaten, indem Sie diese auf Ihrem eigenen Server hosten.

## Installation

**Umgebungsdatei herunterladen**

```
wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example
```

**Docker Compose-Datei herunterladen**

```
wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml
```

**Datenbank vorbereiten**

```
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
```

## Ausführung

**Dienste starten**

```
docker compose up -d
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Beantworten Sie Fragen, indem Sie sich als Kundendienstmitarbeiter ausgeben. Lösen Sie als Captain AI-Assistent auf Chatwoot automatisch häufig gestellte Fragen und leiten Sie komplexe Probleme an relevante Teamkollegen weiter. Verbessern Sie die Erfahrung des Kundensupports, indem Sie stets höfliche, schnelle und genaue Informationen bereitstellen.

## Verwandte Begriffe aus dem Glossar

- [Omni-channel Desk](https://trescout.com/de/dictionary/omni-channel-desk/)
- [Omni-channel](https://trescout.com/de/dictionary/omni-channel/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)
- [Self-hosted](https://trescout.com/de/dictionary/self-hosted/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Unternehmen, die Kundeninteraktionen von einem einzigen Zentrum aus verwalten und Supportprozesse automatisieren möchten.

## Links

- [GitHub-Repository →](https://github.com/chatwoot/chatwoot)
- [Auf Türkisch lesen →](https://trescout.com/discover/chatwoot/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-12 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/chatwoot/
