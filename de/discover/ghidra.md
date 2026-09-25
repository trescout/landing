# Software-Reverse-Engineering- und Analyse-Suite

Ghidra ist eine umfassende Open-Source-Software-Reverse-Engineering-Suite (SRE), die von der National Security Agency (NSA) entwickelt und veröffentlicht wurde. Aufgebaut auf Java mit einem performanten C++ Dekompilierer, übersetzt sie kompilierte Binärdateien in verständlichen Quellcode und bietet fundierte Analysen über Dutzende Prozessorarchitekturen hinweg.

- ★ 78.142
- Java
- GitHub Trending · 2026-08-28

## Aktualisierungen
- 17. September 2026: Sterne 78.142, neueste Version Ghidra_12.1.3_build (Java 21 Unterstützung, RISC-V und ARM64 Dekompilierer-Verbesserungen).

## Was es bringt
- Leistungsfähiger integrierter C-Dekompilierer: Übersetzt Maschinencode und Assemblerbefehle direkt in lesbaren, strukturierten C-Pseudocode.
- Riesiges Multi-Architektur-Spektrum: Unterstützt x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC und Hunderte Mikrocontroller-Familien.
- Kollaborative Team-Analyse: Mehrere Analysten können über den Ghidra Server zeitgleich am selben Projekt mit Kommentaren und Versionskontrolle arbeiten.
- Automatisierte Headless-Analyse: Skripten Sie Malware-Triage und Schwachstellenprüfungen ohne grafische Oberfläche direkt über die Kommandozeile.
- Erweiterbarkeit durch Java und Python: Entwickeln Sie eigene Plugins, automatische Unpacker und Datentypen-Parser.

## Installation und Systemanforderungen

**Installation von JDK 21 und Ghidra**

```
# Auf macOS via Homebrew:
brew install --cask ghidra

# Linux / Windows (Manueller Start aus dem Release-Archiv):
# Erfordert ein installiertes 64-Bit JDK 21.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```

## Ausführung und Headless-Kommandozeilenanalyse

**Grafische Oberfläche starten**

```
./ghidraRun
```

**Headless-Analyse ohne GUI ausführen**

```
analyzeHeadless /projekt/pfad ProjektName -import datei.bin -postScript SicherheitsAudit.py
```

## Technische Architektur: Sleigh und Dekompilierer-Engine

Die architektonischen Grundlagen, die Ghidra zu einem Standard der Sicherheitsanalyse machen:
- Sleigh Prozessorspezifikationssprache: Eine deklarative Sprache zur Beschreibung von Befehlssätzen und Registerbelegungen neuer Hardwarearchitekturen.
- P-Code Zwischenrepräsentation (IR): Normalisiert unterschiedlichste Assembler-Opcodes in ein einheitliches Zwischenformat für architekturunabhängige Datenflussanalysen.
- Nativer C++ Dekompilierer: Beseitigt redundanten Code, rekonstruiert Kontrollflussstrukturen und ermittelt Variablentypen mit hoher Geschwindigkeit.

## Reverse-Engineering- und Schwachstellenanalyse-Workflows

Ghidra fungiert als zentrale Schaltstelle bei defensiven wie offensiven Sicherheitsprüfungen:
- Malware-Analyse (Triage): Untersucht verdächtige Binärdateien auf verborgene Zeichenketten, C2-Server-Adressen und verdächtige API-Aufrufe.
- Binärvergleich (Program Diff): Vergleicht Softwarestände vor und nach einem Patch, um Sicherheitslücken und Exploit-Mechanismen zu identifizieren.
- Firmware-Analyse: Liest Roh-Flash-Dumps von IoT-Geräten ein, um Bootloader, Dateisysteme und Hardware-Treiber zu untersuchen.

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich möchte eine verdächtige ausführbare Datei mit Ghidra untersuchen. Kannst du mir Schritt für Schritt erklären, wie ich ein neues Projekt anlege, die Datei importiere, die automatische Analyse (Auto Analysis) starte, im Decompiler-Fenster Funktionen lese und verdächtige Systemaufrufe identifiziere?

- **Für wen:** Malware-Analysten, Sicherheitsforscher, Reverse-Engineering-Spezialisten und Firmware-Entwickler.
- **Lizenz:** Apache-2.0 (Freie Open-Source-Lizenz)
- **Entwickler:** National Security Agency (NSA) und Open-Source-Community
- **Voraussetzungen:** Java Development Kit (JDK) 21 64-bit

## Häufig gestellte Fragen
- Was sind die wesentlichen Unterschiede zwischen Ghidra und IDA Pro? Während IDA Pro ein kommerzielles Produkt mit kostspieligen Lizenzen pro Architektur ist, ist Ghidra vollkommen kostenlos, Open Source, enthält Dekompilierer für alle Architekturen und verfügt über einen integrierten Kollaborationsserver.
- Ist die Analyse von Schadsoftware in Ghidra sicher? Ja, bei der statischen Analyse wird die Datei lediglich disassembliert und nicht ausgeführt. Dennoch sollte Malware immer in einer isolierten virtuellen Maschine analysiert werden.
- Wie wird der Ghidra Server eingerichtet? Über das Skript svrAdmin im Server-Verzeichnis lässt sich ein Team-Server im lokalen Netzwerk innerhalb weniger Minuten aufsetzen und konfigurieren.
- Können Python 3 Skripte in Ghidra genutzt werden? Standardmäßig ist Jython (Python 2.7) integriert, über das PyGhidra-Plugin können jedoch moderne Python 3 Umgebungen und Bibliotheken wie NumPy nahtlos eingebunden werden.

## Links
- [GitHub →](https://github.com/NationalSecurityAgency/ghidra)

## Verwandte Begriffe aus dem Glossar
Binary Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/de/discover/ghidra/
