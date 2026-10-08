# Open-Source-Gateway für WhatsApp

OpenWA bietet eine kostenlose und Open-Source-API-Gateway-Lösung für das WhatsApp-Messaging-Protokoll. Dieses mit der TypeScript-Sprache entwickelte Tool ermöglicht es Benutzern, WhatsApp-Integrationen auf ihren eigenen Servern (selbst gehostet) zu verwalten.

- ★ 14.976
- TypeScript
- GitHub Trending · 2026-06-17

## Aktualisierungen

- **3. Oktober 2026:** Sterne 14,622 → 14,976, neueste Version v0.24.0 (3. Oktober 2026).
- **27. September 2026:** Sterne 14,197 → 14,622, neueste Version v0.23.7 (25. September 2026).
- **16. September 2026:** Sterne 13,775 → 14,197, neueste Version v0.23.5 (15. September 2026).
- **5. September 2026:** Sterne 13,239 → 13,775, neueste Version v0.23.4 (5. September 2026).

## Was es bringt

- Volle Kontrolle über die WhatsApp-Messaging-Infrastruktur
- Sitzungs- und Webhook-Management mit moderner Oberfläche
- Schnelle und einfache Installation mit Docker-Unterstützung

## Installation

**Schnelle Installation mit Docker**

```
# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

**Lokale Entwicklungsumgebung**

```
# Clone repository
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA

# Install dependencies (includes dashboard)
npm install

# Start API + Dashboard (config is auto-generated on first run)
npm run dev

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

## Ausführung

**Starten in einer Produktionsumgebung**

```
# Basic production (SQLite, local storage)
docker compose up -d

# With PostgreSQL database
docker compose --profile postgres up -d

# Full stack (PostgreSQL, Redis, Dashboard, Traefik)
docker compose --profile full up -d
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte meine Messaging-Prozesse über WhatsApp mit dem OpenWA-Tool automatisieren. Führen Sie mich durch die grundlegenden Konfigurationsschritte, die zum Erstellen einer neuen Sitzung, zum Senden von Nachrichten und zum Abhören eingehender Nachrichten über einen Webhook mithilfe von REST-API-Endpunkten erforderlich sind. Sagen Sie mir, worauf ich achten muss, insbesondere in Bezug auf Multisession-Management und API-Schlüsselsicherheit.

## Verwandte Begriffe aus dem Glossar

- [API Gateway](https://trescout.com/de/dictionary/api-gateway/)
- [Gateway](https://trescout.com/de/dictionary/gateway/)
- [Self-hosted](https://trescout.com/de/dictionary/self-hosted/)
- [API](https://trescout.com/de/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die ihre eigenen WhatsApp-Integrationen entwickeln möchten und die volle Kontrolle über die Messaging-Infrastruktur haben möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/rmyndharis/OpenWA)
- [Auf Türkisch lesen →](https://trescout.com/discover/openwa/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-17 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openwa/
