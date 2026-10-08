# QUIC- und HTTP/3-Unterstützung mit Rust

Das von Cloudflare entwickelte Quiche bietet eine in der Programmiersprache Rust geschriebene Implementierung des QUIC-Transportprotokolls und des HTTP/3-Netzwerkstandards. Diese Bibliothek, die darauf abzielt, den Internetverkehr zu beschleunigen, stellt eine Low-Level-Infrastruktur für Entwickler bereit, die die Netzwerkleistung optimieren möchten.

- ★ 12.638
- GitHub Trending · 2026-09-20

## Aktualisierungen

- **27. September 2026:** Sterne 12,452 → 12,638, neueste Version 0.30.0 (17. September 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte QUIC-Pakete verarbeiten und Netzwerkverbindungszustände verwalten, indem ich diese in der Programmiersprache Rust geschriebene Bibliothek nutze. Welche Schritte muss ich befolgen, um den Client und den Server nach dem Klonen des Projekts auszuführen?

## Verwandte Begriffe aus dem Glossar

- [Rust](https://trescout.com/de/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Entwickler, die die Web-Leistung optimieren und HTTP/3-Unterstützung bereitstellen möchten.
- **Lizenz:** BSD-2-Clause

## Links

- [GitHub-Repository →](https://github.com/cloudflare/quiche)
- [Auf Türkisch lesen →](https://trescout.com/discover/quiche/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-20 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/quiche/
