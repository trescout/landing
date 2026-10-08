# Was ist Specification?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Eine Spezifikation (kurz Spec, deutsch Lastenheft oder Pflichtenheft) ist ein technisches Dokument, das beschreibt, was ein Produkt leisten soll und welche Regeln dabei gelten.

## Definition und Wortherkunft

Es ist wie der architektonische Entwurf eines Gebäudes: Bevor der Entwickler mit dem Programmieren beginnt, schaut er sich das Dokument an und versteht, was er bauen soll. Es reduziert Fehler und klärt Erwartungen. In der API-Welt übernimmt OpenAPI diese Aufgabe, in der Hardware sind es Datenblätter (Datasheets).

***Analogie:** Es ist wie die Zutatenliste und die Kochschritte in einem Rezept; Wenn Sie sich nicht an das Rezept halten, schmeckt das Essen anders.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Software:** Dokument für Funktionen und Regeln.
**Ausschreibung:** Technische Spezifikationsdatei.
**Produkt:** Design- und Abnahmekriterien.

## Technische Tiefe und Architektur

Eine gute Spezifikation enthält:

**Umfang:** Was enthalten ist und was nicht.
**Abnahmekriterium:** Testbare Bedingungen für den Status 'Fertig'.
**Grenzen:** Leistung, Sicherheit, Kompatibilität.
**Release:** Änderungshistorie.

Entsprechung des API-Endpunkts zur Spezifikation:

```
paths:
  /siparis:
    post:
      summary: Yeni sipariş oluşturur
```

Regel: Was nicht messbar ist, ist keine Spezifikation, sondern ein Wunsch. Jeder Punkt muss testbar geschrieben werden.

## Häufig gemischte Dinge

Ähnlich wie eine Anforderung (Requirement). Eine Anforderung besagt, was gewünscht ist, eine Spezifikation erklärt, wie es umzusetzen ist. Das eine ist das Ziel, das andere der Plan.

## Einsatz in verschiedenen Disziplinen

**Rezept:** Material- und Schrittliste.
**Montageanleitung:** Teile- und Reihenfolgeschema.
**Ausschreibung:** Administrative und technische Spezifikation.

## Häufig gestellte Fragen

**Kann sich die Spezifikation ändern?**

Ja, aber jede Änderung muss mit ihren Auswirkungen auf Kosten und Zeitplan genehmigt werden.

**Wer schreibt die Spec-Datei?**

Der Produktmanager, Ingenieur oder Analyst schreibt sie. Wichtig sind ein einzelner Verantwortlicher und eine Versionsdisziplin.

**Wie viel Detail ist erforderlich?**

Genug, um Unklarheiten zu beseitigen. Zu viel ermüdet den Autor, zu wenig blockiert den Entwickler.

**Gibt es Specs in Agile?**

Ja, in schlanker Form. User Stories mit Akzeptanzkriterien und API-Verträge fungieren als Spezifikationen.

## Verwandte Begriffe

- [Spec-driven Development](https://trescout.com/de/dictionary/spec-driven-development/)
- [Framework](https://trescout.com/de/dictionary/framework/)
- [Tech Stack](https://trescout.com/de/dictionary/tech-stack/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/specification/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/specification/
