# Was ist PDF Inspector?

*Daten und Infrastruktur · Zuletzt aktualisiert: 19. September 2026*

PDF Inspector (PDF-Prüf- und -Analyse-Tool) ist eine technische Analysesoftware, die die innere Struktur, die Objekthierarchie (Object Tree), eingebettete Schriftarten, Farbräume, Metadaten und potenzielle Sicherheitsrisiken von PDF-Dokumenten auf Code- und Byte-Ebene untersucht.

## 1. Die Innenarchitektur einer PDF-Datei

Ein Inspector, der ein PDF-Dokument eingehend untersucht, analysiert die 4 Hauptkomponenten der Datei:

- Gibt die PDF-Version an, mit der das Dokument kompatibel ist (z. B. %PDF-1.7, %PDF-2.0).
- Body (Inhalt / Objekte): Dies sind die grundlegenden Datenblöcke, aus denen Seiten, Texte, Vektorgrafiken und Bilder bestehen (Wörterbücher, Arrays, Streams).
- Xref-Tabelle (Cross-Reference Table): Ein Verzeichnis, das speichert, bei welchem Byte am Dateianfang jedes einzelne Objekt (indirektes Objekt) in der Datei beginnt. Ein schneller wahlfreier Zugriff wird durch diese Tabelle ermöglicht.
- Trailer: Verweist auf das Stammverzeichnis des Dokuments (Katalog/Root) und die Verschlüsselungsparameter.

***Analogie:** Es ist wie die Lupe eines Experten, der nicht nur aus der Ferne auf den Einband und die Seiten eines Buches blicks, sondern die Heftung des Einbands, das Papiergewicht, die Tintenart und die Reihenfolge der Seiten untersucht.*

## 2. Was prüft der PDF Inspector?

Ein PDF-Inspector-Tool liest nicht nur Text; es untersucht die technische Gesundheit des Dokuments in folgenden Dimensionen:

### A. Font- und Typografievalidierung

- Schrifteinbettung (Font Embedding): Erkennt, ob die Schriften im Dokument (TrueType, OpenType, Type 1) vollständig oder nur mit den verwendeten Zeichen (Subsetting) eingebettet sind. Nicht eingebaute Schriften führen auf verschiedenen Geräten zu Fehldarstellungen des Designs.
- ToUnicode CMap: Überprüft, ob die Zeichenglyphen auf der Seite den korrekten Unicode-Zeichen zugeordnet sind. Wenn diese Zuordnung fehlerhaft ist, verwandeln sich Texte beim Kopieren oder Suchen in bedeutungssynonyme Symbole, selbst wenn sie auf dem Bildschirm korrekt angezeigt werden.

### B. Druck- und Farbstandards (Prepress)

- Farbräume: Überprüft die Farbtrennungen für RGB, CMYK und Sonderfarben (Pantone).
- Seitenboxen (Page Boxes): Anschnittbereich (BleedBox), Endformat (TrimBox) und Medienbegrenzung (MediaBox) werden mit millimetergenauer Präzision kontrolliert.

### C. Standardkonformität (PDF/A und PDF/UA)

- Archivierungskompatibilität (PDF/A): Überprüft die Regeln (ISO 19005), die externe Links, Verschlüsselung und nicht eingebettete Schriftarten verbieten, damit das Dokument auch nach Jahren noch exakt gleich angezeigt werden kann.
- Barrierefreiheit (PDF/UA): Überprüft für sehbehinderte Nutzer und Screenreader das Vorhandensein einer Tag-Hierarchie (Tagged PDF) und alternativer Bildbeschreibungen (Alt-Text).

### D. Sicherheits- und Schadsoftwareanalyse

- Schadcode-Injektion: Erkennt verdächtigen JavaScript-Code (/JS, /JavaScript), Befehle zum Ausführen externer Programme (/Launch) oder beschädigte Datenströme, die Pufferüberläufe zu Exploitzwecken auslösen, versteckt in PDFs.
- Versteckte Metadaten: Bringt Autoreninformationen, den Revisionsverlauf, GPS-Standorte und angeblich gelöschte, verborgene Ebenen ans Licht.

## 3. PDF Inspector vs PDF Parser vs PDF Viewer

| Eigenschaft | PDF-Viewer (Anzeigeprogramm) | PDF-Parser (Parser) | PDF-Inspector (Prüfer) |
|---|---|---|---|
| Ziel | Das Dokument auf dem Bildschirm rendern | Text und Tabellen extrahieren | Strukturelle Integrität und Sicherheit prüfen |
| Zielgruppe | Endbenutzer | Datenanalysten, LLM-/RAG-Entwickler | Sicherheitsforscher, Herausgeber, Ingenieure |
| Ausgabe | Pixel / Visuelle Ausgabe | JSON, CSV, Klartext | Objektbaum, Fehlerbericht, Sicherheitsbewertung |
| Typische Werkzeuge | Adobe Acrobat Reader, Chrome | PyPDF, pdfplumber, Tika | veraPDF, qpdf, pdf-parser |

## 4. Beliebte Werkzeuge für Entwickler und Systemadministratoren

- qpdf: Ein leistungsstarkes C++-Tool, das PDF-Verschlüsselungen über die Kommandozeile entschlüsseln, Objektstrukturen glätten und fehlerhafte Dateien reparieren kann.
- veraPDF: Ein von der Europäischen Kommission und der PDF Association unterstützter Open-Source-Referenz-Validator, der die Konformität mit PDF/A-Archivierungsstandards validiert.
- pdf-parser.py (Didier Stevens): Das Standard-Analysetool, das Cybersicherheitsexperten zur Analyse schädlicher und verdächtiger PDF-Dateien verwenden.
- pdfcpu ist eine moderne, in Go geschriebene Bibliothek für PDF-Optimierung und strukturelle Validierung.

## Fragen und Antworten

**Was ist der PDF Inspector und warum wird er benötigt?**

Der PDF Inspector ist ein Werkzeug, das die Objektcodes, Schriftarttabellen und Metadaten hinter PDF-Dateien analysiert. Er wird verwendet, um Dateibeschädigungen, Druckfehler und eingebettete Cybersicherheitsbedrohungen zu erkennen.

**Warum verwandelt sich aus einem PDF-Dokument kopierter Text in sinnlose Zeichen?**

Dies liegt daran, dass die „ToUnicode CMap“-Zuordnungstabelle der Schriftart im PDF fehlt oder beschädigt ist. Obwohl die Buchstabenform (Glyphe) korrekt gezeichnet wird, ist das Textäquivalent des Buchstabens unbekannt. Der PDF Inspector kann solche Mängel erkennen.

**Warum sollte die PDF/A-Konformität überprüft werden?**

Behörden und Archive möchten, dass Dokumente auch nach 20 bis 30 Jahren noch exakt gleich aussehen. Der PDF/A-Standard verbietet Audio/Video, Verschlüsselung und externe Schriftartverknüpfungen. Inspector-Werkzeuge überprüfen diese Kriterien.

**Kann eine PDF-Datei ein Werkzeug für Cyberangriffe sein?**

Ja; das PDF-Format kann JavaScript-Code, externe Links und eingebettete Binärdateien ausführen. Cyberkriminelle können diese Funktionen nutzen, um Schadsoftware unbemerkt vom Benutzer herunterzuladen.

**Sind PDF Parser und PDF Inspector dasselbe?**

Nein; während sich ein Parser darauf konzentriert, den Text und die Daten im Dokumentinhalt zu extrahieren, überprüft der Inspector die Konformität des Dokuments mit technischen Standards, Schriftartregeln und Sicherheitsrichtlinien.

## Verwandte Begriffe

- [PDF Parser](https://trescout.com/de/dictionary/pdf-parser/)
- [Document Parsing](https://trescout.com/de/dictionary/document-parsing/)
- [PDF](https://trescout.com/de/dictionary/pdf/)
- [Security Scanner](https://trescout.com/de/dictionary/security-scanner/)

## Verwandte Werkzeuge

- [PDF Inspector](https://trescout.com/de/discover/pdf-inspector/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/pdf-inspector/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/pdf-inspector/
