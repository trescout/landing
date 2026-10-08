# Was ist Skill?

*Glossar · AI · Zuletzt aktualisiert: 22. September 2026*

Ein Skill (auf Türkisch „yetenek“) ist eine definierte Einheit, die es einem KI-Assistenten ermöglicht, Aufgaben mithilfe eines externen Tools auszuführen.

## Definition und Wortherkunft

Die allgemeine Unterhaltung des Assistenten reicht nicht aus; manchmal muss er Dateien lesen oder Suchen durchführen. Jede dieser speziellen Funktionen wird als Skill definiert. Das Konzept wurde von der Ära der Sprachassistenten in die Ära der Agenten übertragen: von Alexa-Skills zu heutigen Agentenfähigkeiten.

***Analogie:** Es ist wie die verschiedenen Werkzeuge in den Händen eines Küchenchefs; der Chef ist einzigartig und wählt für jede Aufgabe das richtige Werkzeug aus.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Datei:** Dokumente lesen und zusammenfassen.
**Kalender:** Besprechungen vereinbaren.
**Suche:** Aktuelle Informationen abrufen.

## Technische Tiefe und Architektur

Eine Fähigkeit wird aus drei Teilen geschrieben:

**Name:** Der Kurzname, den das Modell aufruft.
**Beschreibung:** Beschreibung, wann es verwendet werden soll. Das Modell trifft seine Auswahl anhand dieser Information.
**Parameterschema:** Eingabeformat.

Beispieldefinition:

```
{
  "name": "hava-durumu",
  "description": "Belirtilen şehrin güncel havasını verir",
  "parameters": { "sehir": "string" }
}
```

Ablauf: Der Benutzer stellt eine Anfrage, das Modell wählt die passende Fähigkeit aus, füllt die Parameter aus, das Werkzeug wird ausgeführt und das Ergebnis wird an das Modell zurückgegeben. Bei Fähigkeiten mit Schreibberechtigung ist eine Benutzerbestätigung erforderlich.

## Häufig gemischte Dinge

Es wird oft für eine allgemeine Modellfähigkeit gehalten. Gemeint ist hier jedoch die Fähigkeit des Assistenten, externe Werkzeuge zu nutzen. Das Modell versteht die Sprache, die Skill erledigt die Arbeit.

## Einsatz in verschiedenen Disziplinen

**Küche:** Das Messer in den Händen des Kochs und die Saucentechniken.
**Bohrmaschine:** Je nach Aufsatz unterschiedliche Funktion.
**Telefon:** Jede installierte Anwendung.

## Häufig gestellte Fragen

**Verfügt jedes Modell über eine Fähigkeit?**

Nein. Basismodelle generieren Text, Fähigkeiten werden erst erworben, wenn dem Assistenten ein externes Werkzeug hinzugefügt wird.

**Wie entwickelt man Fähigkeiten?**

Sie werden über eine API-Verbindung oder einen Codeblock definiert. Die Beschreibung wird klar verfasst, und das Modell wählt das richtige aus.

**Ist es sicher?**

Lesefähigkeiten bergen ein geringes Risiko. Bei Aktionen wie Schreiben und Bezahlen sind eine Bestätigung und eine Umfangsbegrenzung zwingend erforderlich.

**Wer schreibt Fähigkeiten?**

Entwickler schreiben sie, Plattformen vertreiben sie im Store. Eine gute Beschreibung zu verfassen ist die halbe Miete.

## Verwandte Begriffe

- [AI Agent](https://trescout.com/de/dictionary/ai-agent/)
- [AI Skill](https://trescout.com/de/dictionary/ai-skills/)
- [Agent Skills](https://trescout.com/de/dictionary/agent-skills/)
- [Tools](https://trescout.com/de/dictionary/tools/)
- [AI Capabilities](https://trescout.com/de/dictionary/ai-capabilities/)

## Verwandte Werkzeuge

- [Anthropic Skills](https://trescout.com/de/discover/anthropic-skills/)
- [Taste Skill](https://trescout.com/de/discover/taste-skill/)
- [Archify](https://trescout.com/de/discover/archify/)
- [Awesome Claude Skills](https://trescout.com/de/discover/awesome-claude-skills/)
- [Last30days Skill](https://trescout.com/de/discover/last30days-skill/)
- [I Have Adhd](https://trescout.com/de/discover/i-have-adhd/)
- [Reverse Skill](https://trescout.com/de/discover/reverse-skill/)
- [Book to Skill](https://trescout.com/de/discover/book-to-skill/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/skill/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/skill/
