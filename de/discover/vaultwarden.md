# Passwortverwaltung auf Ihrem eigenen Server

Vaultwarden ist eine in Rust entwickelte Open-Source-Serversoftware, die mit dem Passwort-Management-Tool Bitwarden kompatibel ist.

- ★ 68.594
- Rust
- GitHub Trending · 2026-08-24

## Aktualisierungen

- **6. Oktober 2026:** Sterne 67,398 → 68,594, neueste Version 1.37.4 (5. Oktober 2026).
- **14. September 2026:** Sterne 65,982 → 67,398, neueste Version 1.37.3 (13. September 2026).
- **24. August 2026:** Sterne 65,983 → 65,982, neueste Version 1.37.2 (22. August 2026).

## Was es bringt

- Vollständig kompatibel mit offiziellen Bitwarden-Clients
- Kann mit geringem Ressourcenverbrauch auf Ihrem eigenen Server gehostet werden
- Bietet Zwei-Faktor-Authentifizierung und Notfallzugriff

## Installation

**Laden Sie den Container herunter und führen Sie ihn aus**

```
docker pull vaultwarden/server:latest
docker run --detach --name vaultwarden \
  --env DOMAIN="https://vw.domain.tld" \
  --volume /vw-data/:/data/ \
  --restart unless-stopped \
  --publish 127.0.0.1:8000:80 \
  vaultwarden/server:latest
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Helfen Sie mir bei der Installation von Vaultwarden, einem Tool, das die Passwortverwaltung auf meinem eigenen Server ermöglicht. Dieses Tool ist eine Serversoftware, die mit Bitwarden-Clients kompatibel ist. Da ich die Installation mit Docker durchführen werde, erklären Sie mir Schritt für Schritt, wie Sie die Image-Befehle zum Abrufen und Ausführen konfigurieren, ein Volume bereitstellen, um meine Daten beizubehalten, und wie Sie HTTPS-Anforderungen berücksichtigen.

## Verwandte Begriffe aus dem Glossar

- [Rust](https://trescout.com/de/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Benutzer, die ihre eigenen Passwörter und sensiblen Daten auf ihrem eigenen Server hosten möchten, anstatt sich auf Cloud-Dienste von Drittanbietern zu verlassen.
- **Lizenz:** AGPL-3.0

## Links

- [GitHub-Repository →](https://github.com/dani-garcia/vaultwarden)
- [Auf Türkisch lesen →](https://trescout.com/discover/vaultwarden/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-24 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/vaultwarden/
