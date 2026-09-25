# Was ist OpenStreetMap (OSM)?

> Englisch: OpenStreetMap · Wortherkunft: englisch open (offen) + street (Straße) + map (Karte)

**Kategorie:** Data  
**Letzte Aktualisierung:** 2026-09-22

OpenStreetMap (OSM) ist eine freie, kollaborative und quelloffene weltweite Geodatenbank, die von Millionen ehrenamtlichen Kartografen und Helfern weltweit aufgebaut und täglich gepflegt wird.

## Definition und Wortherkunft
Im Jahr 2004 von Steve Coast als Reaktion auf restriktive Lizenzierungsmodelle kommerzieller Kartenanbieter ins Leben gerufen, gilt OpenStreetMap als die Wikipedia der Kartografie. Statt Kartendaten hinter teuren API-Schranken zu verbergen, stellt OSM rohe Geodaten unter der Open Database License (ODbL) uneingeschränkt zur Verfügung.

## Alltägliche Anwendung und Praxis
Einsatzbereiche von OpenStreetMap im Alltag:
- **Offline-Navigation:** Apps wie Organic Maps, MAPS.ME oder OsmAnd navigieren zuverlässig ohne Internetverbindung im Funkloch.- **Fitness und Outdoor:** Plattformen wie Strava und Komoot setzen auf das unübertroffen detaillierte Wegenetz von OSM.- **Humanitäre Hilfe:** Das Humanitarian OpenStreetMap Team (HOT) erfasst nach Erdbeben binnen Stunden Straßen, um Rettungskräfte zu leiten.

## Technische Tiefe und Architektur
Das räumliche Datenmodell von OSM beruht auf drei Primitiven:
- **Knoten (Node):** Ein einzelner Geopunkt mit genauen Breiten- und Längengraden.- **Weg (Way):** Eine geordnete Kette von Knoten zur Modellierung von Straßen oder geschlossenen Flächen (Gebäude, Wälder).- **Relation:** Übergeordnete Struktur zur Definition von Buslinien, Abbiegebeschränkungen oder Landesgrenzen.- **Tags (Schlüssel-Wert-Paare):** Standardisierte semantische Beschreibungen (z. B. highway=footway, building=yes).

## Interdisziplinäre Perspektiven
Verwandte Initiativen digitaler Gemeingüter:
- **Digitale Enzyklopädien:** Das frei zugängliche Gemeinschaftsmodell von Wikipedia.- **Open-Source-Software:** Die weltweite Zusammenarbeit am Linux-Betriebssystemkern.- **Bürgerwissenschaften:** Gemeinschaftliche Wetter- und Feinstaubmessnetze engagierter Bürger.

## Als Analogie
Es ist wie die Wikipedia der Weltkarten: Jeder kann einen neuen Waldweg eintragen, Schreibfehler in Straßennamen korrigieren und damit einen frei zugänglichen Weltatlas für die Allgemeinheit perfektionieren.

## Häufige Fragen

**Ist OpenStreetMap für gewerbliche Zwecke kostenlos?**  
Ja; die ODbL-Lizenz gestattet die uneingeschränkte kommerzielle Nutzung unter der Voraussetzung der korrekten Namensnennung.

**Wie wird die Qualität ohne amtliche Vermesser sichergestellt?**  
Durch automatische Plausibilitätsprüfungen und die gegenseitige Kontrolle der aktiven lokalen Mapper-Community.

**Können Entwickler eigene OSM-Kartenserver betreiben?**  
Ja; mit freier Software (PostGIS, Mapnik) lassen sich unabhängige Kachelserver aufbauen, die teure externe Karten-Abos überflüssig machen.

**Was unterscheidet OSM von kommerziellen Kartendiensten?**  
Kommerzielle Dienste verkaufen fertige, geschlossene Bildkacheln; OSM liefert die unverfälschten Vektorrohdaten zum freien Download.

## Verwandte Begriffe
- [Data Pipeline](/de/dictionary/data-pipeline/)
- [Open Source](/de/dictionary/open-source/)
- [API](/de/dictionary/api/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/openstreetmap/
