# Was ist Assembly?

Assembler bezieht sich auf zwei grundlegende Konzepte in der Informatik: Erstens die symbolische Programmiersprache der niedrigsten Ebene (Assemblersprache), die den Hardwareprozessor (CPU) direkt steuert; Die zweite besteht darin, kompilierte Softwaremodule (.NET-Assembly) in ein einziges verteilbares Paket umzuwandeln.

## 1. Programmiersprache auf niedriger Ebene (Assemblersprache)
Der Computerprozessor versteht nur die binären Signale 0 und 1 (Maschinencode/Opcodes). Die Assemblersprache besteht aus für Menschen lesbaren symbolischen Abkürzungen (Mnemoniken), die diesen rohen Maschinencodes entsprechen:

## 2. Prozessorregister und x86-64-Architektur
Die kritischsten Register auf einem modernen 64-Bit-x86-64-Prozessor sind:

## 3. CISC vs. RISC: Unterschied zwischen x86-64 und ARM64
Die x86-64-Architektur arbeitet mit der CISC-Philosophie (Complex Instruction Set). Es verfügt über variable Befehlsgrößen und umfangreiche Befehle, die direkt im Speicher ausgeführt werden können. ARM64 (Apple Silicon, Mobile) basiert auf RISC (Reduced Instruction Set); Mit seiner festen 32-Bit-Befehlslänge und der Load-Store-Architektur bietet es eine hervorragende Energieeffizienz.

## 4. Beispiel für Systemaufrufe (Syscall) und Linux x86-64

## 5. .NET Assembly und WebAssembly (WASM)

## Häufige Fragen
**Was bedeutet Montage und was bewirkt sie?**
Assembler ist die unterste symbolische Programmiersprache, die 1 zu 1 dem Hardware-Befehlssatz des Computerprozessors entspricht. Es wird zur direkten Steuerung von CPU-Registern und Speicher verwendet.

**Was ist der Unterschied zwischen Assembler und Compiler?**
Der Compiler (C, C++, Rust) analysiert und optimiert und übersetzt komplexe menschliche Logik und Schleifen in Maschinencode. Assembler hingegen wandelt Assembleranweisungen, die bereits symbolische Versionen von Maschinencode sind, direkt in binären Bytecode um.

**Wo wird Assemblersprache heute noch verwendet?**
Es wird aktiv in Betriebssystemkernen (Bootloader), Hardware-Gerätetreibern, Reverse Engineering, Malware-Analyse, Cyber-Schwachstellenerkennung und eingebetteten Systemen (IoT/Mikrocontroller) eingesetzt.

**Was ist der Unterschied zwischen CISC und RISC?**
CISC (x86-64) verfügt über einen umfangreichen Befehlssatz, der mehrere Unterprozesse und Speicherzugriffe in einem einzigen Befehl ausführen kann; RISC (ARM) hingegen ist eine vereinfachte und energieeffiziente Architektur, die jeden Befehl in einem einzigen Taktzyklus ausführt.


## Verwandte Begriffe
- [Memory Management](/de/dictionary/memory-management/)
- [Runtime](/de/dictionary/runtime/)
- [Compilation](/de/dictionary/compilation/)
- [Apple Silicon](/de/dictionary/apple-silicon/)
- [Emulator](/de/dictionary/emulator/)

## Verwandte Werkzeuge
- [Ghidra](/de/discover/ghidra/)
- [Apollo-11](/de/discover/apollo-11/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/assembly/
