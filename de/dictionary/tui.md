# Was ist TUI?

> Text User Interface

TUI (Text User Interface / Text-Benutzeroberfläche) ist eine tastaturorientierte Benutzeroberfläche, die auf Terminalbildschirmen mit Text- und Zeichenblöcken arbeitet, ohne eine Grafikkarte zu benötigen.

## Konzeptioneller Rahmen, Etymologie und die Evolution des Terminals
Der Begriff TUI ist eine Abkürzung für den englischen Ausdruck Text User Interface (oder gelegentlich Terminal User Interface). In der Geschichte der Computerschnittstellen handelt es sich um ein hybrides visuelles Paradigma, das eine Brücke zwischen CLI (Command Line Interface) und GUI (Graphical User Interface) schlägt:

## Technische Architektur: Raw Mode, ANSI-Escape-Sequenzen und Double Buffering
Wie eine TUI-Anwendung im Hintergrund funktioniert, basiert auf drei grundlegenden Mechanismen auf Betriebssystemebene:

## Die moderne TUI-Renaissance und Entwicklertools
In den letzten Jahren gab es im Entwickler-Ökosystem eine enorme TUI-Renaissance als Reaktion auf den massiven Speicherverbrauch von Webtechnologien (Electron-basierte aufgeblähte Anwendungen):

## Häufig verwechselt mit

## Häufige Fragen
**Was bedeutet TUI und wofür steht die Abkürzung?**
TUI ist die Abkürzung für Text User Interface oder Terminal User Interface. Es beschreibt visuelle und interaktive Schnittstellen, die auf dem Zeichenraster des Terminals ohne grafischen Fenster-Manager laufen.

**Was sind die grundlegenden Unterschiede zwischen CLI, GUI und TUI?**
CLI arbeitet mit einzeiligen Textbefehlen; GUI wird über Pixel, Fenster und Maus gesteuert; TUI ist ein hybrides Format, das innerhalb des Terminals mit tastaturorientierten Menüs, Panels und Boxen arbeitet.

**Wie zeichnen Terminal-Benutzeroberflächen den Bildschirm?**
Durch ANSI-Escape-Sequenzen und Terminal-Steuercodes wird der Cursor in die gewünschte Zeile und Spalte des Bildschirms bewegt, Farbcodes werden zugewiesen und Unicode-Box-Zeichen werden gezeichnet.

**Welches sind die beliebtesten Bibliotheken für die Entwicklung moderner TUIs?**
Im Rust-Ökosystem sind ratatui, in der Sprache Go bubbletea und lipgloss sowie auf der Python-Seite die Bibliotheken Textual und rich der Industriestandard.


## Verwandte Begriffe
- [CLI](/de/dictionary/cli/)
- [Terminal](/de/dictionary/terminal/)
- [Terminal Control](/de/dictionary/terminal-control/)
- [Runtime](/de/dictionary/runtime/)
- [Assembly](/de/dictionary/assembly/)
- [Tech Stack](/de/dictionary/tech-stack/)

## Verwandte Werkzeuge
- [PI](/de/discover/pi/)
- [Witr](/de/discover/witr/)
- [Hister](/de/discover/hister/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/tui/
