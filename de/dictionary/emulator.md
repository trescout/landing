# Was ist ein Emulator?

> Englisch: Emulator · Wortherkunft: lateinisch aemulari (nachahmen, wetteifern)

**Kategorie:** Dev  
**Letzte Aktualisierung:** 2026-09-19

Ein Emulator ist eine Software, welche die Hardware-Architektur, Registerstrukturen und den Befehlssatz eines fremden Computersystems nachbildet, sodass darauf ausgelegte Gastprogramme unverändert auf moderner Host-Hardware laufen.

## Konzeptioneller Rahmen, Wortherkunft und Simulator-Abgrenzung
Das Wort leitet sich vom lateinischen aemulari ab, was nachahmen bedeutet. Während ein Simulator lediglich das äußere Verhalten eines Systems abbildet (wie ein Flugsimulator die Flugphysik nachahmt, ohne den Bordcomputer nachzubilden), rekonstruiert der Emulator die inneren elektronischen Schaltkreise: CPU-Register, Speicherverwaltung und Grafik-Chipsätze.

## Rechnerarchitektur und der Befehlszyklus: Fetch-Decode-Execute
Im Zentrum jedes Emulators arbeitet eine virtuelle CPU mit Befehlsübersetzung:
- **Interpreter-Emulation:** Jeder Befehl des Gastsystems wird einzeln eingelesen, dekodiert und ausgeführt. Sehr präzise, jedoch rechenintensiv.- **Dynamische Übersetzung (JIT-Recompiler):** Ganze Befehlsblöcke einer fremden Architektur (z. B. ARM oder MIPS) werden zur Laufzeit in nativen Host-Code (x86-64) übersetzt und im Cache gehalten.- **Zyklengenaue Emulation (Cycle-Accurate):** Taktgenaue Synchronisation aller Chips, um zeitkritische Hardware-Effekte historischer Konsolen originalgetreu zu erhalten.

## Einsatzgebiete in Entwicklung, IT-Sicherheit und Unternehmen
Wichtige Einsatzbereiche von Emulatoren:
- **App-Entwicklung:** Testen von Android- und iOS-Apps auf Desktop-Rechnern ohne physische Smartphones.- **Schadsoftware-Analyse:** Gefahrlose Ausführung verdächtiger Dateien in abgeschirmten virtuellen QEMU-Umgebungen.- **Altsystem-Erhalt:** Weiterbetrieb historischer Kernbankensysteme auf moderner Cloud-Hardware.

## Rechtliche Aspekte und Urheberrecht
Historische Gerichtsentscheidungen (wie Sony vs. Connectix) haben bestätigt, dass die Entwicklung von Emulatoren durch sauberes Reverse Engineering legal ist. Urheberrechtsverletzungen entstehen erst durch die unbefugte Weitergabe geschützter BIOS-Dateien oder urheberrechtlich geschützter Spiele-ROMs.

## Als Analogie
Das Lesen eines Buchs in einer Fremdsprache: Ein Simulator ist eine grobe Zusammenfassung der Handlung; ein Interpreter-Emulator schlägt jedes Wort mühsam im Wörterbuch nach; ein JIT-Recompiler übersetzt ganze Kapitel vorab in Ihre Muttersprache, sodass Sie flüssig lesen können.

## Häufige Fragen

**Worin unterscheidet sich ein Emulator von einer virtuellen Maschine?**  
Eine virtuelle Maschine führt Code direkt auf derselben CPU-Architektur aus; ein Emulator übersetzt Befehle einer völlig fremden Prozessorarchitektur vollständig per Software.

**Ist die Programmierung von Emulatoren legal?**  
Ja; das Nachbauen von Hardwarefunktionen mittels Clean-Room-Verfahren ist rechtlich zulässig, solange kein herstellereigener BIOS-Code mitgeliefert wird.

**Warum erfordert die Emulation alter Konsolen oft schnelle PCs?**  
Weil zyklengenaue Emulatoren Millionen Rechenschritte des Host-PCs benötigen, um einen einzigen Taktzyklus historischer Spezialbausteine exakt abzubilden.

**Was ist QEMU?**  
Ein weltweit etablierter Open-Source-Maschinenemulator, der vollständige PC- und Serverarchitekturen für ARM, x86 und RISC-V nachbildet.

## Verwandte Begriffe
- [ROM](/de/dictionary/rom/)
- [Virtual Machines](/de/dictionary/virtual-machines/)
- [Apple Silicon](/de/dictionary/apple-silicon/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/emulator/
