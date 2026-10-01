# Was ist Full Text Search?

Full-Text-Suche ist die Suchmethode, mit der Wörter gefunden werden, die im gesamten Inhalt von Dokumenten vorkommen.

## Definition und Wortherkunft
Während die einfache Suche den Dateinamen prüft, durchsucht die Volltextsuche jeden Satz im Dokument. Sie ist der effektivste Weg, um in großen Archiven an Informationen zu gelangen. Ihre moderne Infrastruktur basiert auf einer Struktur namens invertierter Index (inverted index).

## Wie kann man es kennen und im täglichen Leben anwenden?
Internetsuche: Nach einem Thema im Blog suchen.E-Mail: Einen Beitrag von vor Jahren finden.Code: Nach einer Funktion im Repository suchen.Recht: Ein Rechtsprechungarchiv durchsuchen.

## Technische Tiefe und Architektur
Die Zeile lautet wie folgt:

## Häufig gemischte Dinge
Kann mit Metadatensuche verwechselt werden. Die Metadatensuche betrachtet Dateidateien (Name, Datum, Größe), während die Volltextsuche den Inhalt betrachtet. Die Vektorsuche hingegen betrachtet nicht das Wort, sondern die Bedeutung.

## Einsatz in verschiedenen Disziplinen
Bibliothek: Volltextsuche anstelle von Zettelkatalogen.Buch: Das Register (Index) am Ende.Archiv: Suche nach einem Thema in einer Zeitungsausschnittsammlung.

## Häufig gestellte Fragen
**Wird es nicht zu langsam laufen?**
Dank des vorab erstellten Index liefert es innerhalb von Sekunden Ergebnisse. Eine Suche ohne Index ist langsam, daher ist ein Index unerlässlich.

**Funktioniert es bei allen Dateitypen?**
Ja, bei Dateien, aus denen Text extrahiert werden kann. Bei gescannten Dokumenten wird der Text zunächst mittels OCR ermittelt.

**Bereiten türkische Suffixe Probleme?**
Bei der qualifizierten Analyse werden Suffixe auf den Wortstamm zurückgeführt. Bei einer Engine mit schwacher Sprachunterstützung sinkt die Trefferquote, daher ist eine türkisch unterstützte Konfiguration erforderlich.

**Wann ist eine Vektorsuche erforderlich?**
Wenn Synonyme und Konzepte gesucht werden. Wenn keine Schlüsselwörter gefunden werden können, greift die Vektorsuche; beide zusammen sind leistungsstark.


## Verwandte Begriffe
- [RAG](/de/dictionary/rag/)
- [Vector Index](/de/dictionary/vector-index/)
- [Document Parsing](/de/dictionary/document-parsing/)

## Verwandte Werkzeuge
- [Karakeep](/de/discover/karakeep/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/full-text-search/
