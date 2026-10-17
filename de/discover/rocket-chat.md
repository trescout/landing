# Sichere und anpassbare Teamkommunikation

Rocket.Chat bietet ein sicheres Kommunikationsbetriebssystem, das für geschäftskritische Vorgänge entwickelt wurde. Die mit der TypeScript-Sprache entwickelte Plattform zielt darauf ab, interne Nachrichten- und Kollaborationsprozesse zu zentralisieren.

- ★ 46.215
- TypeScript
- GitHub Trending · 2026-06-18

## Aktualisierungen

- **6. Oktober 2026:** Sterne 46,098 → 46,215, neueste Version 8.9.0 (5. Oktober 2026).
- **10. September 2026:** Sterne 46,064 → 46,098, neueste Version 8.8.1 (9. September 2026).
- **2. September 2026:** Sterne 46,005 → 46,064, neueste Version 8.8.0 (1. September 2026).
- **19. August 2026:** Sterne 45,941 → 46,005, neueste Version 8.7.1 (19. August 2026).

## Was es bringt

- Datensicherheit mit Ende-zu-Ende-Verschlüsselung
- Möglichkeit des Hostings auf Ihrem eigenen Server
- Umfassende Integrations- und Anwendungsunterstützung

## Installation

**Offizielles compose-Repository klonen**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git
```

**Umgebungsdatei erstellen**

```
cd rocketchat-compose
cp .env.example .env
```

**MongoDB- und Rocket.Chat-Services starten**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml up -d
```

## Ausführung

**Lokale Oberfläche öffnen**

```
http://localhost:3000
```

## So fangen Sie an

Um mit der Installation von Rocket.Chat zu beginnen, können Sie den Bereitstellungsleitfaden auf der offiziellen Dokumentationsseite lesen. Sie können eine der Docker-, Podman- oder Kubernetes-Methoden zum Hosten auf Ihrem eigenen Server wählen oder die Launchpad-Option für einen schnelleren Start in Betracht ziehen. Alle technischen Anforderungen und detaillierten Installationsschritte finden Sie auf der offiziellen Dokumentationsseite von Rocket.Chat.

- [Offizielle Quelle →](https://rocket.chat/)

## Verwandte Begriffe aus dem Glossar

- [Communications Operating System](https://trescout.com/de/dictionary/communications-operating-system/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)

- **Für wen es gedacht ist:** Es wurde für Organisationen entwickelt, denen der Datenschutz am Herzen liegt und die die volle Kontrolle über ihre eigene Infrastruktur haben möchten.

## Links

- [GitHub-Repository →](https://github.com/RocketChat/Rocket.Chat)
- [Auf Türkisch lesen →](https://trescout.com/discover/rocket-chat/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-18 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/rocket-chat/
