# Open-Source-Unternehmensressourcenplanung

Odoo ist eine Open-Source-Enterprise-Resource-Planning-Plattform, die es Unternehmen ermöglicht, alle ihre betrieblichen Prozesse unter einem Dach zu verwalten. Dieses mit der Python-Sprache entwickelte System bietet eine breite Palette modularer Geschäftsanwendungen vom Vertrieb bis zur Buchhaltung.

- ★ 52.082
- GitHub Trending · 2026-06-04

## Was es bringt
- Es verwaltet Geschäftsprozesse wie Verkauf, Buchhaltung und Lager von einer einzigen Zentrale aus.
- Es bietet modulare Geschäftsanwendungen, die untereinander kompatibel sind.
- Es stellt eine Open-Source-Infrastruktur bereit, die je nach Bedarf angepasst werden kann.

## Installation
****

```
docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=change_me postgres:15
```

****

```
docker run -d --name odoo --link odoo-db:db -p 127.0.0.1:8069:8069 odoo:latest
```


## Ausführung
****

```
http://localhost:8069
```


## So fangen Sie an
- Offizielle Quelle →

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/odoo/
