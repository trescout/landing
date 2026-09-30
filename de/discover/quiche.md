# QUIC- und HTTP/3-Unterstützung mit Rust

Das von Cloudflare entwickelte Quiche bietet eine in der Programmiersprache Rust geschriebene Implementierung des QUIC-Transportprotokolls und des HTTP/3-Netzwerkstandards. Diese Bibliothek, die darauf abzielt, den Internetverkehr zu beschleunigen, stellt eine Low-Level-Infrastruktur für Entwickler bereit, die die Netzwerkleistung optimieren möchten.

- ★ 12.638
- GitHub Trending · 2026-09-20

## Was es bringt
- Das QUIC-Transportprotokoll implementieren
- Am HTTP/3-Netzwerkstandard arbeiten
- Low-Level-Netzwerkpakete verarbeiten

## Installation
**Das Projekt klonen**

```
git clone https://github.com/cloudflare/quiche
```


## Ausführung
**Den Client ausführen**

```
cargo run --bin quiche-client -- https://cloudflare-quic.com/
```

**Den Server ausführen**

```
cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key
```


## Wenn Sie nicht programmieren
Ich möchte QUIC-Pakete verarbeiten und Netzwerkverbindungszustände verwalten, indem ich diese in der Programmiersprache Rust geschriebene Bibliothek nutze. Welche Schritte muss ich befolgen, um den Client und den Server nach dem Klonen des Projekts auszuführen?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/quiche/
