# Open-Source-Gateway für WhatsApp

OpenWA bietet eine kostenlose und Open-Source-API-Gateway-Lösung für das WhatsApp-Messaging-Protokoll. Dieses mit der TypeScript-Sprache entwickelte Tool ermöglicht es Benutzern, WhatsApp-Integrationen auf ihren eigenen Servern (selbst gehostet) zu verwalten.

- ★ 12.674
- TypeScript
- GitHub Trending · 2026-06-17

## Aktualisieren
- 12. August 2026: Star 12.605 → 12.674, neueste Version v0.16.0 (11. August 2026).
- 10. August 2026: Star 12.552 → 12.605, letzte Version v0.15.0 (9. August 2026).
- 8. August 2026: Stern 12.544 → 12.552, neueste Version v0.14.6 (8. August 2026).
- 8. August 2026: Star 12.503 → 12.544, neueste Version v0.14.5 (8. August 2026).

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
Ich möchte meine Messaging-Prozesse über WhatsApp mit dem OpenWA-Tool automatisieren. Führen Sie mich durch die grundlegenden Konfigurationsschritte, die zum Erstellen einer neuen Sitzung, zum Senden von Nachrichten und zum Abhören eingehender Nachrichten über einen Webhook mithilfe von REST-API-Endpunkten erforderlich sind. Sagen Sie mir, worauf ich achten muss, insbesondere in Bezug auf Multisession-Management und API-Schlüsselsicherheit.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openwa/
