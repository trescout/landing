# PostgreSQL mit Rust neu geschrieben

Das pgrust-Projekt, bei dem das PostgreSQL-Datenbankverwaltungssystem mit der Programmiersprache Rust neu geschrieben wurde, schließt alle Regressionstests erfolgreich ab. Diese Studie zielt darauf ab, die Datenbankarchitektur mit einer Sprache zu modernisieren, die auf Speichersicherheit ausgerichtet ist.

- ★ 5.030
- Rust
- GitHub Trending · 2026-07-12

## Aktualisierungen

- **16. September 2026:** Sterne 4,964 → 5,030, neueste Version v0.3 (15. September 2026).
- **10. September 2026:** Sterne 3,957 → 4,964, neueste Version v0.2-release (30. Juli 2026).
- **2. August 2026:** Sterne 2,171 → 3,957, neueste Version v0.2-release (30. Juli 2026).

## Was es bringt

- Festplattenkompatibilität mit Postgres 18.3
- Mehr als 46.000 Regressionstest-Erfolge
- Moderne Architektur konzentriert sich auf Speichersicherheit

## Installation

**Schneller Test mit Docker**

```
docker run -d --name pgrust -e POSTGRES_PASSWORD=secret malisper/pgrust:v0.1 && until docker exec -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres -c '\q' >/dev/null 2>&1; do sleep 1; done && docker exec -it -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres; docker rm -f pgrust
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Was ist der Hauptzweck des Pgrust-Projekts, wie wird die Festplattenkompatibilität mit bestehendem PostgreSQL sichergestellt und wie wird künstliche Intelligenz unterstützte Programmierung bei der Entwicklung des Projekts eingesetzt? Erzählen Sie uns von der Kompatibilität der aktuellen Version von Pgrust mit Postgres 18.3 und ihrem Erfolg bei Regressionstests.

## Verwandte Begriffe aus dem Glossar

- [Memory](https://trescout.com/de/dictionary/memory/)
- [Rust](https://trescout.com/de/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Entwickler und Datenbankforscher, die die PostgreSQL-Architektur mit der Rust-Sprache modernisieren möchten.
- **Lizenz:** AGPL-3.0

## Links

- [GitHub-Repository →](https://github.com/malisper/pgrust)
- [Auf Türkisch lesen →](https://trescout.com/discover/pgrust/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-12 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/pgrust/
