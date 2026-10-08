# Was ist Full Text Search?

*Glossar · Data · Zuletzt aktualisiert: 22. September 2026*

Full-Text-Suche ist die Suchmethode, mit der Wörter gefunden werden, die im gesamten Inhalt von Dokumenten vorkommen.

## Definition und Wortherkunft

Während die einfache Suche den Dateinamen prüft, durchsucht die Volltextsuche jeden Satz im Dokument. Sie ist der effektivste Weg, um in großen Archiven an Informationen zu gelangen. Ihre moderne Infrastruktur basiert auf einer Struktur namens invertierter Index (inverted index).

***Analogie:** Es ist vergleichbar damit, nicht nur das Inhaltsverzeichnis eines Buches anzusehen, sondern alle Seiten zu durchsuchen, um den gesuchten Satz zu finden.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Internetsuche:** Nach einem Thema im Blog suchen.
**E-Mail:** Einen Beitrag von vor Jahren finden.
**Code:** Nach einer Funktion im Repository suchen.
**Recht:** Ein Rechtsprechungarchiv durchsuchen.

## Technische Tiefe und Architektur

Die Zeile lautet wie folgt:

**Tokenisierung:** Der Text wird in Wörter unterteilt, die Endungen auf den Wortstamm zurückgeführt.
**Inverser Index:** Es wird im Voraus festgehalten, in welchen Dokumenten jedes Wort vorkommt.
**Ranking:** Algorithmen wie BM25 ordnen nach Titel- und Häufigkeitsgewichtung.

Beispiel mit Postgres:

```
SELECT baslik FROM yazilar
WHERE to_tsvector('turkish', icerik) @@ to_tsquery('turkish', 'yapay & zeka');
```

Wenn Bedeutungsähnlichkeit gewünscht ist (z. B. dass bei der Eingabe von „Automobil“ das Wort „Auto“ erscheint), ist eine Vektorsuche erforderlich. Beide werden auch zusammen verwendet: Zuerst grenzt das Schlüsselwort ein, dann sortiert der Vektor.

## Häufig gemischte Dinge

Kann mit Metadatensuche verwechselt werden. Die Metadatensuche betrachtet Dateidateien (Name, Datum, Größe), während die Volltextsuche den Inhalt betrachtet. Die Vektorsuche hingegen betrachtet nicht das Wort, sondern die Bedeutung.

## Einsatz in verschiedenen Disziplinen

**Bibliothek:** Volltextsuche anstelle von Zettelkatalogen.
**Buch:** Das Register (Index) am Ende.
**Archiv:** Suche nach einem Thema in einer Zeitungsausschnittsammlung.

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

- [RAG](https://trescout.com/de/dictionary/rag/)
- [Vector Index](https://trescout.com/de/dictionary/vector-index/)
- [Document Parsing](https://trescout.com/de/dictionary/document-parsing/)

## Verwandte Werkzeuge

- [Karakeep](https://trescout.com/de/discover/karakeep/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/full-text-search/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/full-text-search/
