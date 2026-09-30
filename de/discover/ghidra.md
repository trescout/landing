# Analyse-Framework für Software-Reverse-Engineering

Ghidra ist ein umfassendes Software-Reverse-Engineering-Framework (SRE), das von der National Security Agency (NSA) entwickelt und als Open Source geteilt wird. Plattform entwickelt mit Java- und C++-Kern; Es konvertiert kompilierte Binärdateien in Quellcode und bietet Sicherheitsforschern erweiterte Dekompilierungen, symbolische Analysen und Unterstützung für mehrere Architekturen.

- ★ 79.733
- Java
- GitHub Trending · 2026-08-28

## Was es bringt
- Integrierte leistungsstarke C-Decompiler: Konvertieren von Maschinencode und Assembleranweisungen in lesbare, C-ähnliche High-Level-Syntax.
- Große Auswahl an Prozessoren und Architekturen: Unterstützung für x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC und Hunderte eingebetteter Mikrocontroller-Architekturen.
- Kollaborative Mehrbenutzeranalyse: Gleichzeitige Annotation, Funktionsbenennung und Versionskontrolle in derselben Binärdatei mit der Ghidra-Server-Infrastruktur.
- Automatisierung und Headless-Analyse: Automatisches Scannen von Tausenden von Malware auf dem Server über die Befehlszeile, ohne die grafische Benutzeroberfläche aufrufen zu müssen.
- Erweiterbarkeit mit Java und Python: Passen Sie die Analyse mit benutzerdefinierten Skripten, Plug-Ins und Datentypbibliotheken an.

## Installations- und Systemanforderungen
**JDK 21 und Ghidra-Installation**

```
# macOS Homebrew ile kurulum:
brew install --cask ghidra

# Linux / Windows (Manuel arşivden başlatma):
# JDK 21 64-bit kurulu olmalıdır.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```


## Ausführung und Headless-Befehlszeilenanalyse
**Starten der grafischen Oberfläche**

```
./ghidraRun
```

**Ausführen einer kopflosen automatischen Analyse**

```
analyzeHeadless /proje/dizini ProjeAdi -import hedef_dosya.bin -postScript GuvenlikAnalizi.py
```


## Technische Architektur: Schlitten- und Dekompiler-Engine
- Sleigh-Prozessor-Modellierungssprache: Deklarative Beschreibungssprache, die zur Einführung eines neuen Prozessors oder einer neuen Befehlssatzarchitektur (ISA) in Ghidra verwendet wird.
- P-Code-Zwischendarstellungsschicht (IR): Durchführung einer architekturunabhängigen Datenfluss- und Kontrollflussanalyse durch Übersetzung aller Prozessoranweisungen in eine gemeinsame Zwischensprache (P-Code).
- C++-basierte Dekompilierungs-Engine: Leistungsstarke native Engine, die Kontrollflussdiagramme vereinfacht, Variablentypen extrahiert und komplexe Schleifen auf C-Code reduziert.

## Arbeitsabläufe für Reverse Engineering und Schwachstellenanalyse
- Malware-Analyse (Malware-Triage): Verdächtige ausführbare Dateien isoliert öffnen und versteckte API-Aufrufe, C2-Domänen und Verschlüsselungsschlüssel aufdecken.
- Binärdateivergleich (Program Diff): Erkennen der geschlossenen Schwachstelle durch Visualisieren der Unterschiede zwischen zwei Dateien vor und nach dem Sicherheitspatch.
- Firmware-Analyse: Roh-Flash-Speicher-Dumps von IoT-Geräten in die Speicherzuordnung einfügen und Bootloader- und Kernel-Funktionen analysieren.

## Wenn Sie nicht programmieren
Ich möchte eine verdächtige Binärdatei mit Ghidra untersuchen. Können Sie Schritt für Schritt erklären, wie Sie ein neues Projekt in Ghidra öffnen, die Datei importieren, die automatische Analyse ausführen, Funktionen im Decompiler-Fenster untersuchen und aufgerufene verdächtige API-Funktionen erkennen?

## Häufig gestellte Fragen
- Was sind die Hauptunterschiede zwischen Ghidra und IDA Pro? Während für IDA Pro kommerzielle und hohe Lizenzgebühren anfallen, ist Ghidra völlig kostenlos und Open Source. Ghidra bietet integrierte Dekompiler für alle Architekturen und umfasst einen Multi-User-Collaboration-Server.
- Ist Ghidra bei der Analyse von Malware sicher? Ja, während der statischen Analyse wird die Datei nicht ausgeführt, sondern nur dekodiert. Aus Sicherheitsgründen ist es jedoch unerlässlich, dass die Analyse in einer isolierten virtuellen Maschine (VM) durchgeführt wird.
- Wie installiere ich Ghidra Server? Mit dem im Ghidra-Paket enthaltenen svrAdmin-Skript im Serververzeichnis kann in wenigen Minuten ein Teamserver im lokalen Netzwerk geöffnet und Benutzerrechte vergeben werden.
- Können Python 3-Skripte in Ghidra ausgeführt werden? Obwohl Ghidra standardmäßig mit Jython (Python 2.7) ausgeliefert wird, können moderne Python 3-Umgebungen und externe Bibliotheken (NumPy, Capstone) dank des PyGhidra-Plugins direkt verwendet werden.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ghidra/
