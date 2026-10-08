# Was ist Open Source AI?

*Glossar · AI · Zuletzt aktualisiert: 22. September 2026*

Open-Source-KI (auf Türkisch Open-Source-Künstliche Intelligenz) sind Modelle, deren Gewichte und Codes von jedem untersucht und ausgeführt werden können.

## Definition und Wortherkunft

Im Gegensatz zu geschlossenen Modellen sind diese Modelle transparent: Jeder, der möchte, kann sie herunterladen, mit den eigenen Daten untersuchen und Änderungen daran vornehmen. Bekannte Beispiele sind Llama, Mistral und DeepSeek. Es lässt sich argumentieren, dass auch Trainingsdaten offen sein sollten; OSI führt zu diesem Thema eine separate Definitionsstudie durch.

***Analogie:** Anstatt das Geheimrezept eines Gerichts zu bewahren, ist es so, als würde man das Rezept teilen, damit jeder experimentieren und es verbessern kann.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Lokaler Chat:** Persönlicher Assistent, der ohne Internet funktioniert.
**Forschung:** Basismodell getestet.
**Institutionell:** Inhouse-Lösung ohne Datenauslagerung.

## Technische Tiefe und Architektur

Komponenten:

**Gewichte:** Dateien trainierter Modelle werden über Hugging Face verteilt.
**Lizenz:** Apache und MIT gelten als freizügig. Einige Community-Lizenzen schränken die kommerzielle Nutzung ein. Sie müssen den Text lesen.
**Quantisierung:** Die reduzierte Version des Modells (GGUF) läuft mit wenig Speicher.
**Betrieb:** Tools wie Ollama öffnen Modelle mit einem einzigen Befehl:

```
ollama run llama3
```

Hardware-Regel: Wenn der Parameter wächst, benötigt er Speicher. Kleinere Modelle laufen auf dem Laptop, größere auf dem Server.

## Häufig gemischte Dinge

Kann mit offenen Gewichten gemischt werden. „Offene Gewichte“ bedeutet nur, dass die Gewichte offen sind. Open-Source-KI hingegen umfasst auch Code- und Prozesstransparenz, ihr Anwendungsbereich ist breiter.

## Einsatz in verschiedenen Disziplinen

**Rezept:** Rezept mit Zutaten und Maßangaben geteilt.
**Lehrbuch:** Open Source, das jeder lesen und bearbeiten kann.
**Samenbank:** Von Landwirten geteilter Ahnensamen.

## Häufig gestellte Fragen

**Sind Open-Source-Modelle schwächer?**

Früher war das so, aber heute konkurrieren viele offene Modelle mit ihren geschlossenen Konkurrenten. Geschlossene Modelle haben im Rennen um die Spitze die Nase vorn, doch in der Praxis hat sich der Abstand verringert.

**Warum sollte ich Open Source verwenden?**

Für Datenschutz, Kosten und vollständige Integration. Ihre Daten gehen nicht raus und Sie zahlen keine Lizenzgebühr.

**Ist eine kommerzielle Nutzung erlaubt?**

Es variiert je nach Lizenz. Apache und MIT sind kostenlos, einige Community-Lizenzen sehen eine Benutzerzahl- oder Umsatzbegrenzung vor.

**Womit sollte man beginnen?**

Beginnen Sie lokal mit kleinen, quantisierten Modellen. Wenn der Bedarf wächst, verschieben Sie es auf den Server.

## Verwandte Begriffe

- [Open Weights](https://trescout.com/de/dictionary/open-weights/)
- [Self-Hosting](https://trescout.com/de/dictionary/self-hosting/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/open-source-ai/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/open-source-ai/
