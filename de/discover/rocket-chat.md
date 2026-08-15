# Sichere und anpassbare Teamkommunikation

Rocket.Chat bietet ein sicheres Kommunikationsbetriebssystem, das für geschäftskritische Vorgänge entwickelt wurde. Die mit der TypeScript-Sprache entwickelte Plattform zielt darauf ab, interne Nachrichten- und Kollaborationsprozesse zu zentralisieren.

- ★ 45.941
- TypeScript
- GitHub Trending · 2026-06-18

## Aktualisieren
- 7. August 2026: Star 45.919 → 45.941, letzte Version 8.7.0 (7. August 2026).
- 2. August 2026: Star 45.649 → 45.919, letzte Version 8.6.1 (10. Juli 2026).

## Was es bringt
- Datensicherheit mit Ende-zu-Ende-Verschlüsselung
- Möglichkeit des Hostings auf Ihrem eigenen Server
- Umfassende Integrations- und Anwendungsunterstützung

## Installation
**Linux · Snap-Paket (Herausgeber von Rocket.Chat)**

```
sudo snap install rocketchat-server
```

**Offizielles Docker-Compose-Repository**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git && cd rocketchat-compose && cp .env.example .env
```


## Ausführung
**Mit Docker starten**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml -f docker.yml up -d
```


## So fangen Sie an
- Offizielle Quelle →
Um mit der Installation von Rocket.Chat zu beginnen, können Sie den Bereitstellungsleitfaden auf der offiziellen Dokumentationsseite lesen. Sie können eine der Docker-, Podman- oder Kubernetes-Methoden zum Hosten auf Ihrem eigenen Server wählen oder die Launchpad-Option für einen schnelleren Start in Betracht ziehen. Alle technischen Anforderungen und detaillierten Installationsschritte finden Sie auf der offiziellen Dokumentationsseite von Rocket.Chat.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/rocket-chat/
