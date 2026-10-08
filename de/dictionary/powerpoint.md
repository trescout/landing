# Was ist PowerPoint?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

PowerPoint ist die folienbasierte Präsentationsanwendung von Microsoft.

## Definition und Wortherkunft

Das Programm wurde 1987 von der Firma Forethought ins Leben gerufen und bald darauf von Microsoft übernommen. Es ist die digitale Bühne, auf der Sie einem Publikum Ihre Ideen, Daten oder Ihr Projekt erklären: Sie kombinieren Texte, Bilder und Grafiken zu organisierten Folien. Das Dateiformat .pptx ist eigentlich ein komprimiertes XML-Paket.

***Analogie:** Es ist wie ein Stapel illustrierter Karten, die ein Geschichtenerzähler in der Hand hält, um seine Erzählung zu unterstützen.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Geschäftstreffen:** Vierteljährliche Berichte und Projektstatuspräsentationen.
**Schule:** Hausaufgaben und Verteidigung der Abschlussarbeit.
**Konferenzen:** Keynote-Vorträge und Panels.
**Training:** Vorlesungssets.

## Technische Tiefe und Architektur

Bestandteile einer wirkungsvollen Präsentation:

**Folienmaster (Folienmaster):** Vorlage, bei der Schriftart, Farbe und Logo von einem Ort aus verwaltet werden. Anstatt jede Folie einzeln zu formatieren, bearbeiten Sie das Original.
**Serveransicht:** Sie sehen Ihre Notizen, das Publikum sieht nur die Folie.
**Export:** Die Präsentation kann als PDF oder Video gespeichert werden.
**Automatisierung:** Wiederholte Darstellungen können mit Code generiert werden. Das Öffnen einer leeren Präsentation mit Python geht wie folgt:

```
from pptx import Presentation
sunum = Presentation()
slayt = sunum.slides.add_slide(sunum.slide_layouts[5])
slayt.shapes.title.text = "Merhaba"
sunum.save("ornek.pptx")
```

In der Regel gibt es pro Folie nur eine Idee. Den Text mit Bildern zu unterstützen ist effektiver als das Schreiben von Wandtexten.

## Einsatz in verschiedenen Disziplinen

**Unterrichtstafel:** Board-Layout, das das Thema Schritt für Schritt erklärt.
**Fotoalbum:** Der visuelle Fluss, der die Erzählung ausrichtet.
**Theater:** Der Phasenplan schreitet Schritt für Schritt voran.

## Häufig gestellte Fragen

**Kann ich mir während einer Präsentation Notizen machen?**

Ja. In der Moderatorenansicht sehen Sie Ihre Notizen, das Publikum sieht nur die Folie.

**Kann es in andere Formate konvertiert werden?**

Ja. Sie können Ihre Präsentation als PDF oder Video speichern.

**Gibt es eine kostenlose Alternative?**

Ja. LibreOffice Impress und das webbasierte Google Slides leisten ähnliche Arbeit. Beachten Sie die Schriftart- und Animationsunterschiede beim Übergang.

**Was tun, wenn die Datei zu groß wird?**

Komprimieren Sie Bilder, verknüpfen Sie Videos (nicht einbetten) und löschen Sie nicht verwendete Originale. Das Speichern in Abschnitten statt in einzelnen Dateien funktioniert ebenfalls.

## Verwandte Begriffe

- [Design Tool](https://trescout.com/de/dictionary/design-tool/)
- [User Interface](https://trescout.com/de/dictionary/user-interface/)
- [Dashboard](https://trescout.com/de/dictionary/dashboard/)

## Verwandte Werkzeuge

- [MarkItDown](https://trescout.com/de/discover/markitdown/)
- [Ppt Master](https://trescout.com/de/discover/ppt-master/)
- [OfficeCLI](https://trescout.com/de/discover/officecli/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/powerpoint/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/powerpoint/
