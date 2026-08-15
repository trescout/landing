# PostgreSQL mit Rust neu geschrieben

Das pgrust-Projekt, bei dem das PostgreSQL-Datenbankverwaltungssystem mit der Programmiersprache Rust neu geschrieben wurde, schließt alle Regressionstests erfolgreich ab. Diese Studie zielt darauf ab, die Datenbankarchitektur mit einer Sprache zu modernisieren, die auf Speichersicherheit ausgerichtet ist.

- ★ 3.957
- Rust
- GitHub Trending · 2026-07-12

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
Was ist der Hauptzweck des Pgrust-Projekts, wie wird die Festplattenkompatibilität mit bestehendem PostgreSQL sichergestellt und wie wird künstliche Intelligenz unterstützte Programmierung bei der Entwicklung des Projekts eingesetzt? Erzählen Sie uns von der Kompatibilität der aktuellen Version von Pgrust mit Postgres 18.3 und ihrem Erfolg bei Regressionstests.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/pgrust/
