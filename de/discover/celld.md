# Persistente Datenverwaltung in verteilten Systemen

Celld wurde von Deno entwickelt und bietet eine selbst gehostete Infrastruktur für dauerhafte Objekte für verteilte Systeme. Diese in der Rust-Sprache geschriebene Technologie ermöglicht die skalierbare Verteilung der Zustandsverwaltung auf verschiedene Knoten.

- ★ 4.937
- Rust
- GitHub Trending · 2026-08-08

## Aktualisierungen

- **2. Oktober 2026:** Sterne 4,817 → 4,937, neueste Version v0.6.1 (1. Oktober 2026).
- **27. September 2026:** Sterne 4,630 → 4,817, neueste Version v0.6.0 (26. September 2026).
- **15. September 2026:** Sterne 4,521 → 4,630, neueste Version v0.5.0 (15. September 2026).
- **6. September 2026:** Sterne 4,405 → 4,521, neueste Version v0.4.1 (5. September 2026).

## Was es bringt

- Bietet skalierbares Zustandsmanagement in Ihrer eigenen Infrastruktur.
- Es speichert jedes Objekt als unabhängige SQLite-Datenbank.
- Es stellt eine knotenübergreifende Koordination mit S3-kompatiblem Speicher her.

## Installation

**Laden Sie das Tool auf Ihren Computer herunter**

```
curl -fsSL https://celld.dev/install.sh | sh
```

## Ausführung

**Ressourcenbeschränkter Knoten**

```
CELLD_MAX_RESIDENT_CELLS=1000 \
CELLD_RESIDENT_LOW_WATER=800 \
celld --bucket s3://my-cells-bucket --listen 0.0.0.0:8080 \
  --advertise node-a.internal:8080
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mit Celld ein verteiltes System aufbauen. Nachdem Sie einen S3-kompatiblen Speicherplatz erstellt haben, erklären Sie Schritt für Schritt, wie die Knoten diesen Speicherplatz nutzen und wie Wrangler-Pakete verteilt werden. Fassen Sie die technischen Details in einfacher Sprache zusammen, insbesondere darüber, wie Knoten sich gegenseitig erkennen und die Datenkonsistenz über S3 sicherstellen.

## Verwandte Begriffe aus dem Glossar

- [State Management](https://trescout.com/de/dictionary/state-management/)
- [Durable Objects](https://trescout.com/de/dictionary/durable-objects/)
- [Self-hosted](https://trescout.com/de/dictionary/self-hosted/)
- [Rust](https://trescout.com/de/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Entwickler, die auf verteilten Systemen arbeiten und ein skalierbares Zustandsmanagement auf ihren eigenen Servern etablieren möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/denoland/celld)
- [Auf Türkisch lesen →](https://trescout.com/discover/celld/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-08 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/celld/
