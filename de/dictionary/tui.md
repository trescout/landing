# Was ist TUI?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

> Text User Interface

TUI (Text User Interface / Text-Benutzeroberfläche) ist eine tastaturorientierte Benutzeroberfläche, die auf Terminalbildschirmen mit Text- und Zeichenblöcken arbeitet, ohne eine Grafikkarte zu benötigen.

## Konzeptioneller Rahmen, Etymologie und die Evolution des Terminals

Der Begriff TUI ist eine Abkürzung für den englischen Ausdruck Text User Interface (oder gelegentlich Terminal User Interface). In der Geschichte der Computerschnittstellen handelt es sich um ein hybrides visuelles Paradigma, das eine Brücke zwischen CLI (Command Line Interface) und GUI (Graphical User Interface) schlägt:

- CLI (Command-Line Interface): Ein eindimensionaler Datenstrom, bei dem der Benutzer einen einzeiligen Befehl eingibt und das System mit einer Textausgabe antwortet.
- GUI (Grafische Benutzeroberfläche): Eine reichhaltige visuelle Schnittstelle, die Pixel, Fenster, Mauszeiger und Grafikbeschleunigerkarten (GPU) verwendet.
- TUI (Text User Interface): Statt Pixeln ein zweidimensionales Zeichenraster aus Zeilen und Spalten auf dem Terminalbildschirm verwendende, menübasierte Benutzeroberfläche, die Fenster, Schaltflächen, Statusleisten und Formulare enthält.

Die Wurzeln von TUI reichen bis in die 1970er Jahre zu physischen Textterminals wie TeleType (TTY) und DEC VT100 zurück. Für diese Terminals wurden ANSI-Escape-Sequenzen entwickelt, um farbigen Text an bestimmte Koordinaten des Bildschirms zu schreiben und den Cursor zu bewegen (z. B. löscht \033[2J den Bildschirm, \033[31m färbt den Text rot).

***Analogie:** Anstelle des hochauflösenden OLED-Touchscreens eines modernen Smartphones (GUI) ist es eher mit mechanischen Fallblattanzeigen (Split-Flap-Displays) an Flughäfen oder digitalen Anzeigetafeln vergleichbar. In jedem Feld kann nur ein einzelner Buchstabe oder ein Symbol stehen, aber durch die organisierte Anordnung dieser Symbole entsteht ein perfektes und sofort reagierendes Bedienfeld.*

## Technische Architektur: Raw Mode, ANSI-Escape-Sequenzen und Double Buffering

Wie eine TUI-Anwendung im Hintergrund funktioniert, basiert auf drei grundlegenden Mechanismen auf Betriebssystemebene:

1. Raw-Modus des Terminals: Die Standard-Terminalumgebung arbeitet im „Cooked Mode“; das bedeutet, das Betriebssystem hält Zeichen zurück und puffert sie, bis der Benutzer die Eingabetaste drückt. Wenn eine TUI-Anwendung startet, versetzt sie das Terminal über einen termios-Aufruf in den „Raw Mode“. Auf diese Weise wird jeder vom Benutzer gedrückte Tastendruck (j, k, Strg+C, Pfeiltasten) sofort und ohne Warten auf die Eingabetaste erfasst.
2. Alternativer Bildschirmpuffer (Alternate Screen Buffer): Dass Ihr Terminalverlauf beim Öffnen von htop oder vim nicht verloren geht und Sie nach dem Schließen des Programms zu Ihrer ursprünglichen Befehlszeile zurückkehren können, wird durch den alternativen Puffer (tput smcup / rmcup) ermöglicht. Die TUI öffnet eine eigene virtuelle Leinwand und kehrt beim Beenden zum Hauptbildschirm zurück.
3. Double Buffering und Diff-Rendering: Um Bildschirmflackern zu vermeiden, halten moderne TUI-Engines zwei Zeichenmatrizen im Speicher: den aktuellen und den nächsten Bildschirmzustand. Es werden nur die geänderten Zellen berechnet und lediglich diese Differenzen (Diffs) mittels ANSI-Codes an das Terminal ausgegeben, wodurch Animationen mit einer Flüssigkeit von 60 FPS möglich sind.

## Die moderne TUI-Renaissance und Entwicklertools

In den letzten Jahren gab es im Entwickler-Ökosystem eine enorme TUI-Renaissance als Reaktion auf den massiven Speicherverbrauch von Webtechnologien (Electron-basierte aufgeblähte Anwendungen):

- Geringer Ressourcenverbrauch: Während eine grafische Benutzeroberfläche Hunderte von Megabyte an Arbeitsspeicher beansprucht, verbraucht eine TUI-Anwendung nur wenige Megabyte RAM.
- Null-Latenz über SSH: Die Übertragung grafischer Oberflächen (VNC / RDP) bei der Verwaltung eines Remote-Servers in der Cloud erfordert eine hohe Bandbreite; TUI hingegen läuft selbst bei langsamen Mobilfunkverbindungen innerhalb eines SSH-Tunnels blitzschnell.
- Tastatur-Flow-State: Das Arbeiten mit Vim-Tastenkürzeln (h, j, k, l), ohne die Hand von der Maus zu nehmen, steigert die Konzentration und Produktivität von Entwicklern um ein Vielfaches.

Hervorragende moderne Frameworks und Tools:

- Die Rust-Welt: Die Bibliotheken ratatui (ehemals tui-rs) und crossterm sind mit ihrer Speichersicherheit und ultrahohen Performance zum grundlegenden Standard für moderne TUI-Projekte geworden.
- Die Welt von Go: bubbletea (ein reaktives Framework, das das The Elm Architecture-Muster auf das Terminal überträgt), lipgloss (eine Styling-Engine) und bubbles, entwickelt vom Charm-Team.
- Die Welt von Python: Textual und rich, geschrieben von Will McGugan.
- Kult-TUI-Tools: lazygit für die Git-Verwaltung, k9s für Kubernetes-Cluster, lazydocker für Docker, btop und htop für die Systemüberwachung, ncdu für die Festplattenanalyse.

## Häufig verwechselt mit

- CLI vs. TUI: CLI ein einzeiliges Frage-Antwort-Modell (git status, ls -la). TUI hingegen ist ein zweidimensionales visuelles Panel, das das Terminalfenster ausfüllt und über Registerkarten, Listen sowie Tastenkürzel verfügt (lazygit, k9s).
- TUI besteht nicht nur aus einfachem Text: Moderne Terminals unterstützen Nerd Fonts (Icons), 24-Bit-TrueColor, UTF-8-Box-Drawing-Zeichen und dank Protokollen wie Kitty Graphics oder Sixel sogar die Darstellung echter Grafiken direkt im Terminal.

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

- [CLI](https://trescout.com/de/dictionary/cli/)
- [Terminal](https://trescout.com/de/dictionary/terminal/)
- [Terminal Control](https://trescout.com/de/dictionary/terminal-control/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Assembly](https://trescout.com/de/dictionary/assembly/)
- [Tech Stack](https://trescout.com/de/dictionary/tech-stack/)

## Verwandte Werkzeuge

- [PI](https://trescout.com/de/discover/pi/)
- [Witr](https://trescout.com/de/discover/witr/)
- [Hister](https://trescout.com/de/discover/hister/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/tui/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/tui/
