# Was ist eine PPTX-Datei?

**Kategorie:** Entwicklung
**Last updated:** 2026-09-01

Eine PPTX-Datei ist ein modernes, XML-basiertes und ZIP-komprimiertes Präsentationsformat, das seit Microsoft PowerPoint 2007 den weltweiten Standard darstellt. Es gliedert Folien, Vektoren und Mediendateien in modulare XML-Strukturen.

## 1. Der innere Aufbau einer PPTX-Datei: ZIP- und XML-Architektur
<p>Viele Anwender halten eine PPTX-Datei für ein geschlossenes Binärdokument; technisch gesehen handelt es sich jedoch um ein <strong>ZIP-Archiv</strong> mit einer durchdachten Ordnerstruktur.</p><p>Wenn Sie die Dateiendung in <code>.zip</code> umbenennen und entpacken, sehen Sie folgenden Aufbau:</p><ul><li><strong><code>[Content_Types].xml</code>:</strong> Beschreibt die MIME-Typen aller im Container enthaltenen XML-Schemas und Dateien.</li><li><strong><code>_rels/</code>:</strong> Speichert Beziehungskataloge (<code>.rels</code>), die Folien und Mediendateien logisch miteinander verknüpfen.</li><li><strong><code>ppt/slides/</code>:</strong> Jede Folie ist eine eigenständige XML-Datei (<code>slide1.xml</code>, <code>slide2.xml</code>) mit allen Textfeldern und Koordinaten.</li><li><strong><code>ppt/media/</code>:</strong> Beherbergt alle eingebetteten Grafiken, Tondokumente und Videos im unkomprimierten Originalzustand. Das Entpacken ist der schnellste Weg, hochauflösende Bilder verlustfrei zu exportieren.</li><li><strong><code>ppt/slideLayouts/</code> &amp; <code>ppt/slideMasters/</code>:</strong> Verwaltet Master-Vorlagen und Formatierungsregeln.</li></ul><p>Dank dieses offenen Aufbaus lassen sich beschädigte Folien oft direkt im XML-Code reparieren.</p>

## 2. Wie öffnet man eine PPTX-Datei? (Kostenlose und Bezahloptionen)
<p>Sie können PPTX-Dateien problemlos ohne Microsoft PowerPoint öffnen und bearbeiten:</p><h3>Cloud- und Browser-Lösungen (Ohne Installation)</h3><ul><li><strong>Google Präsentationen (Google Slides):</strong> Kollaboratives Arbeiten im Browser mit unkompliziertem PPTX-Export.</li><li><strong>Microsoft 365 Web (PowerPoint Online):</strong> Kostenlose Browser-Version mit originalgetreuer Schrift- und Animationsdarstellung.</li><li><strong>Canva &amp; Pitch:</strong> Zeitgemäße Design-Plattformen mit direktem PPTX-Import.</li></ul><h3>Desktop-Office-Pakete</h3><ul><li><strong>LibreOffice Impress:</strong> Vollwertige, kostenlose Open-Source-Präsentationssoftware.</li><li><strong>Apple Keynote:</strong> Flüssige Präsentationssoftware für macOS und iOS mit exzellentem PPTX-Support.</li><li><strong>OnlyOffice:</strong> Quelloffene Desktop-Suite mit höchster Kompatibilität zu OpenXML-Formaten.</li></ul>

## 3. Konvertierung und automatisierte Erstellung per Code
<ul><li><strong>PPTX zu PDF:</strong> Der Export als PDF fixiert das Schriftbild und verhindert Zeilenumbrüche auf fremden Rechnern.</li><li><strong>Skriptbasierte Folienerzeugung:</strong><ul><li><strong>Python (<code>python-pptx</code>):</strong> Generiert automatisierte Folienberichte direkt aus Datenbanken und Diagrammen.</li><li><strong>Node.js (<code>pptxgenjs</code>):</strong> Erzeugt Präsentationsdateien dynamisch in Webanwendungen.</li><li><strong>Generative KI:</strong> Werkzeuge wie Gamma oder Beautiful.ai erstellen vollständige Foliendecks aus simplen Textprompts.</li></ul></li></ul>

## 4. Sicherheit und Makros: PPTX vs. PPTM
<ul><li><strong>Schutz vor Makroviren:</strong> Standardmäßige <code>.pptx</code>-Dateien können keine Visual-Basic-Makros (VBA) ausführen, was vor Schadsoftware schützt.</li><li><strong>Die Dateiendung <code>.pptm</code>:</strong> Präsentationen mit automatisierten Makros müssen zwingend die Endung <code>.pptm</code> tragen.</li></ul>

## Vergleich zwischen PPT und PPTX

## Häufig gestellte Fragen

### Was ist eine PPTX-Datei?
PPTX ist das offizielle Präsentationsformat von Microsoft PowerPoint seit Version 2007. Es basiert auf offenem XML und wird als ZIP-Container verpackt.

### Wie kann ich PPTX ohne PowerPoint öffnen?
Kostenlos über Google Präsentationen, LibreOffice Impress, OnlyOffice oder die Webversion von Microsoft 365 im Browser.

### Wie extrahiere ich Bilder aus einer PPTX-Datei in voller Qualität?
Dateiendung in .zip ändern, Archiv entpacken und im Ordner ppt/media alle Originalbilder direkt abgreifen.

### Warum verschieben sich Schriften auf anderen Computern?
Fehlen installierte Schriftarten auf dem Zielsystem, wählt das Betriebssystem Ersatzschriftarten. Abhilfe schafft das Einbetten von Schriften oder der PDF-Export.

### Was ist der Unterschied zwischen PPTX und PDF?
PPTX ist ein dynamisches, editierbares Präsentationsformat mit Animationen. PDF ist ein statisches Druck- und Leseformat mit unveränderlicher visueller Darstellung.

## Verwandte Begriffe
- [PDF](/de/dictionary/pdf/)
- [Document Parsing](/de/dictionary/document-parsing/)
- [Design Tool](/de/dictionary/design-tool/)
- [Serialization](/de/dictionary/serialization/)

---
Source: TreScout Tech Dictionary · https://trescout.com/de/dictionary/pptx/
