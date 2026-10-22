# Was ist PPTX?

*Daten und Infrastruktur · Zuletzt aktualisiert: 19. September 2026*

> PowerPoint Presentation

PPTX (PowerPoint Presentation) ist ein von Microsoft entwickeltes Dateiformat auf Basis des offenen Standards (Office Open XML – OOXML), das zum Speichern von folienbasierten visuellen Präsentationen, Vorlagen, Grafiken, Multimedia-Elementen und Übergangseffekten verwendet wird.

## 1. Die innere Anatomie einer PPTX-Datei: ZIP- und XML-Architektur

Viele Nutzer betrachten PPTX als ein einzelnes Dokument; technisch gesehen ist eine .pptx-Datei jedoch ein komprimiertes ZIP-Archiv mit einer spezifischen Ordnerhierarchie.

Wenn Sie die Dateiendung einer beliebigen .pptx-Datei in .zip ändern und diese entpacken, kommt folgende Struktur zum Vorschein:

- [Content_Types].xml: Listet die MIME-Typen aller Komponenten (Medientypen, XML-Schemata) im Archiv auf.
- _rels/: Beziehungskatalog, der die Verknüpfungen zwischen Dateien und Komponenten (.rels) definiert.
- ppt/slides/: Jede Folie ist eine eigenständige XML-Datei (slide1.xml, slide2.xml). Die Texte, Formkoordinaten und Formatierungen der Folie werden hier gespeichert.
- ppt/media/: Alle in die Präsentation eingebetteten hochauflösenden Bilder, Audioaufnahmen und Videos befinden sich in diesem Ordner in ihrer Rohfassung. Um ein Bild verlustfrei aus der Präsentation zu extrahieren, ist das Öffnen der Datei als ZIP-Archiv die praktischste Methode.
- ppt/slideLayouts/ und ppt/slideMasters/: Enthalten die Gestaltungsvorlagen und Folienlayouts.

Dank dieser offenen Architektur können Präsentationsdateien selbst bei Beschädigung auf XML-Ebene repariert oder die darin enthaltenen Medienressourcen problemlos wiederhergestellt werden.

***Analogie:** Es ist wie ein digitales Diashow-Album; beim Umblättern der Seiten werden Texte, Grafiken und der Präsentationsfluss nacheinander angezeigt.*

## 2. Wie öffnet man eine PPTX-Datei? (Kostenlose und kostenpflichtige Optionen)

Es ist möglich, PPTX-Dateien auch ohne Microsoft PowerPoint anzuzeigen, zu bearbeiten oder zu präsentieren:

### Cloud- und browserbasierte Lösungen (ohne Installation)

- Google Slides: Sie können PPTX-Dateien, die in Google Drive hochgeladen wurden, direkt im Browser bearbeiten, in Echtzeit im Team zusammenarbeiten und sie wieder als PPTX herunterladen.
- Microsoft 365 Web (PowerPoint Online): Funktioniert über den Browser mit einem kostenlosen Microsoft-Konto und bietet Unterstützung für Originalschriftarten und Animationen.
- Canva und Pitch: Bieten Unterstützung für den Import von PPTX-Dateien für moderne, visuell ausgerichtete Präsentationen.

### Desktop-Office-Pakete

- LibreOffice Impress: Eine quelloffene und komplett kostenlose, fortschrittliche Desktop-Alternative.
- Apple Keynote: macOS- und iOS-Nutzer erhalten ein natives, leistungsstarkes und PPTX-kompatibles Tool.
- OnlyOffice ist eine Open-Source-Bürosoftware, die die höchste Kompatibilität mit Microsoft Office-Dateistandards bietet.

## 3. PPTX-Konvertierung und programmgesteuerte Erstellung

- PPTX zu PDF: Der sicherste Weg, um beim Öffnen von Präsentationen auf anderen Geräten verschobene Schriftarten oder ein zerstörtes Layout zu vermeiden, ist die Konvertierung in das PDF-Format.
- Programmgesteuerte PPTX-Erstellung: Python (python-pptx): Datenbankberichte, Analyse-Diagramme oder automatisierte Briefings können direkt per Code in Folien umgewandelt werden.
- Node.js (pptxgenjs): Wird verwendet, um dynamische Präsentationsdateien aus Webanwendungen zu erstellen.
- Erstellung mit Künstlicher Intelligenz: Generative KI-Tools wie Gamma oder Beautiful.ai können innerhalb von Minuten aus Texteingaben professionelle PPTX-Dateien erstellen.

## 4. Sicherheit und Kompatibilität: PPTX vs. PPTM

- Makro-Gefahr: Standardmäßige .pptx-Dateien können keine eingebetteten Visual Basic for Applications (VBA)-Makros enthalten. Diese Regel wurde eingeführt, um die Verbreitung von Schadsoftware über Office-Dokumente zu verhindern.
- .pptm-Dateiendung: Wenn eine Präsentation Automatisierungen oder Makros enthält, muss die Dateiendung zwingend .pptm lauten. Bei .pptm-Dateien in E-Mail-Anhängen ist stets Vorsicht geboten.

## Vergleich von PPT und PPTX

| Eigenschaft | Altes Format (.PPT) | Modernes Format (.PPTX) |
|---|---|---|
| Struktur | Binär (Binary BIFF) | Komprimiertes XML (Zip-Container) |
| Dateigröße | Groß (geringe Komprimierung) | Klein (automatische ZIP-Komprimierung) |
| Resistenz gegen Beschädigungen | Bei Beschädigung eines einzelnen Bytes lässt sich die Datei nicht öffnen | Beschädigte Folien können übersprungen und andere gerettet werden |
| Offener Standard | Geschlossenes kommerzielles Format | Internationaler Standard ISO/IEC 29500 (OpenXML) |
| Medienzugriff | Schwierig / Erfordert einen speziellen Parser | Bilder und Videos können direkt durch Entpacken der ZIP-Datei extrahiert werden |

## Häufige Fragen

**Was ist eine PPTX-Datei?**

PPTX ist ein modernes Präsentationsdateiformat, das mit Microsoft PowerPoint 2007 eingeführt wurde, auf einer offenen XML-Struktur basiert und mit dem ZIP-Algorithmus komprimiert ist.

**Wie öffne ich eine PPTX-Datei, wenn ich kein PowerPoint auf meinem Computer habe?**

Sie können die Google Slides-Webanwendung verwenden, die kostenlosen Programme LibreOffice oder OnlyOffice herunterladen oder die kostenlose Microsoft 365-Webversion über Ihren Browser öffnen.

**Wie kann ich Bilder aus einer PPTX-Datei in höchster Qualität extrahieren?**

Ändern Sie die Dateiendung von .pptx in .zip und entpacken Sie sie mit einem Archivierungsprogramm. Im Ordner ppt/media befinden sich alle Bilder der Präsentation in ihrer Originalqualität.

**Warum sieht eine PPTX-Datei auf verschiedenen Computern manchmal fehlerhaft aus?**

Wenn die in der Präsentation verwendeten speziellen Schriftarten (Fonts) auf dem anderen Computer nicht installiert sind, wählt das System eine Standardschriftart aus, was dazu führt, dass sich der Text verschiebt. Die Lösung besteht darin, die Schriftarten beim Speichern der Präsentation in die Datei einzubetten (Embed Fonts) oder sie als PDF zu exportieren.

**Was ist der Unterschied zwischen PPTX und PDF?**

PPTX ist eine bearbeitbare, lebendige Präsentationsquelle, die Animationen und Folienübergänge enthält. PDF hingegen ist ein Format mit festem Layout, ohne Animationen und ein geräteunabhängiges Format für das finale Lesen oder Drucken.

## Verwandte Begriffe

- [PDF](https://trescout.com/de/dictionary/pdf/)
- [Document Parsing](https://trescout.com/de/dictionary/document-parsing/)
- [Design Tool](https://trescout.com/de/dictionary/design-tool/)
- [Serialization](https://trescout.com/de/dictionary/serialization/)

## Verwandte Werkzeuge

- [Ppt Master](https://trescout.com/de/discover/ppt-master/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/pptx/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/pptx/
