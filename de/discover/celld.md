# Persistente Datenverwaltung in verteilten Systemen

Celld wurde von Deno entwickelt und bietet eine selbst gehostete Infrastruktur für dauerhafte Objekte für verteilte Systeme. Diese in der Rust-Sprache geschriebene Technologie ermöglicht die skalierbare Verteilung der Zustandsverwaltung auf verschiedene Knoten.

- ★ 4.010
- Rust
- GitHub Trending · 2026-08-08

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
Ich möchte mit Celld ein verteiltes System aufbauen. Nachdem Sie einen S3-kompatiblen Speicherplatz erstellt haben, erklären Sie Schritt für Schritt, wie die Knoten diesen Speicherplatz nutzen und wie Wrangler-Pakete verteilt werden. Fassen Sie die technischen Details in einfacher Sprache zusammen, insbesondere darüber, wie Knoten sich gegenseitig erkennen und die Datenkonsistenz über S3 sicherstellen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/celld/
