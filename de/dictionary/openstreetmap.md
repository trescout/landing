# Was ist OpenStreetMap?

*Glossar · Data · Zuletzt aktualisiert: 22. September 2026*

OpenStreetMap (kurz OSM) ist eine freie und offene Weltkarte, die von Freiwilligen gemeinsam erstellt wird.

## Definition und Wortherkunft

Das Projekt wurde 2004 gestartet. Im Gegensatz zu kommerziellen Karten werden die Daten nicht von einem Unternehmen, sondern von einer Gemeinschaft Freiwilliger erstellt: Jeder kann neue Straßen, Gebäude oder wichtige Orte hinzufügen und Fehler korrigieren. Die Daten sind unter der ODbL-Lizenz für jeden frei zugänglich. Das bedeutet, dass Sie die Daten kostenlos nutzen können, bei einer Weitergabe jedoch die Quelle angeben müssen.

***Analogie:** Es ist wie die Wikipedia der Karten; Jeder kann etwas hinzufügen, Fehler beheben und dank der Community bleibt es ständig auf dem neuesten Stand.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Navigations-Apps:** Apps wie OsmAnd und MAPS.ME beziehen ihre Karten aus OSM-Daten.
**Logistik:** Routenplanung für Lieferdienste.
**Katastrophenhilfe:** Schnelle Kartierung von Krisengebieten durch Freiwillige (z. B. HOT-Community).
**Stadtplanung:** Analysen von Radwegen und Grünflächen.

## Technische Tiefe und Architektur

OSM-Daten bestehen aus drei Bausteinen:

**Knoten (Node):** Ein einzelner Punkt (z. B. Standort einer Apotheke).
**Weg (Way):** Eine Verbindung von Knoten (Straße, Gebäudeumriss).
**Relation:** Eine logische Gruppierung von Elementen (Buslinie).

Jedes Element erhält ein Tag: Schlüssel-Wert-Paare wie highway=residential. Zur Bearbeitung wird der iD-Editor im Browser oder die fortgeschrittene JOSM-Anwendung verwendet.

Die Overpass API wird abgefragt, um spezifische Daten abzurufen. Zum Beispiel eine kleine Abfrage, die Apotheken in der Umgebung findet:

```
[out:json];
node["amenity"="pharmacy"](around:1000,41.0,29.0);
out;
```

Rohdaten können aus der Planet.osm-Datei heruntergeladen werden. Kartenbilder werden hingegen stückweise von Kachel-Servern (Tile-Servern) bezogen.

## Einsatz in verschiedenen Disziplinen

**Enzyklopädie:** Das Wikipedia-Modell, bei dem jeder schreibt und korrigiert.
**Open-Source-Software:** Der Linux-Kernel, der durch freiwillige Beiträge wächst.
**Bürgerwissenschaft (Citizen Science):** Das Sammeln von Vogelbeobachtungsdaten in einer gemeinsamen Datenbank.

## Häufig gestellte Fragen

**Ist es wirklich kostenlos?**

Die Daten sind unter der ODbL-Lizenz kostenlos. Wenn Sie sie auf Ihrem eigenen Server hosten, fallen keine zusätzlichen Gebühren an. Unternehmen, die fertige Kacheldienste anbieten, können jedoch Gebühren verlangen.

**Was ist der Unterschied zu Google Maps?**

Bei Google Maps produziert das Unternehmen die Daten und bindet sie an API-Kontingente. OSM-Daten werden von der Community produziert; Sie können die Rohdaten herunterladen und unbegrenzt verarbeiten.

**Wie kann ich zur Karte beitragen?**

Sie können ein Konto erstellen und mit dem iD-Editor im Browser beginnen. Das Hinzufügen eines fehlenden Geschäfts in Ihrer Straße ist ein guter erster Schritt.

**Kann ich es für mein kommerzielles Produkt verwenden?**

Ja, aber gemäß der ODbL müssen Sie OpenStreetMap als Quelle sichtbar angeben und abgeleitete Daten unter derselben Lizenz teilen.

## Verwandte Begriffe

- [Data Pipeline](https://trescout.com/de/dictionary/data-pipeline/)
- [OSINT](https://trescout.com/de/dictionary/osint/)
- [Graph-based Investigation](https://trescout.com/de/dictionary/graph-based-investigation/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/openstreetmap/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/openstreetmap/
