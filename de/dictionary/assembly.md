# Assembly Definition, Register und Systemarchitektur

Assembly bezeichnet zwei Kernkonzepte der Informatik: die hardwarenächste symbolische Programmiersprache zur direkten CPU-Steuerung und kompilierte Bereitstellungspakete (.NET Assemblies).

## 1. Hardwarenahe Programmiersprache (Assembly Language)
Prozessoren verarbeiten ausschließlich binäre Maschinencodes (Opcodes). Die Assemblersprache ersetzt diese Bitfolgen durch lesbare Mnemonics:

## 2. CPU-Register und x86-64-Architektur
Moderne 64-Bit-Prozessoren der x86-64-Familie verfügen über spezialisierte und universelle Register:

## 3. CISC vs. RISC: Unterschiede zwischen x86-64 und ARM64
Die x86-64-Architektur basiert auf dem CISC-Prinzip (komplexer Befehlssatz) mit variabler Befehlslänge und direkten Speicheroperationen. ARM64 (Apple Silicon, moderne Mobilprozessoren) nutzt hingegen RISC (reduzierter Befehlssatz) mit festen 32-Bit-Befehlen und strikter Load-Store-Architektur für höchste Energieeffizienz.

## 4. Systemaufrufe (Syscalls) und Linux-x86-64-Beispiel

## 5. .NET Assemblies und WebAssembly (WASM)

## Häufig gestellte Fragen
**Was bedeutet Assembly und wofür wird es verwendet?**
Es ist die hardwarenächste symbolische Sprache, die Prozessorbefehle direkt abbildet und vor allem für Betriebssysteme, Treiber und IT-Sicherheitsanalysen genutzt wird.

**Was unterscheidet einen Assembler von einem Compiler?**
Ein Compiler übersetzt komplexe, abstrakte Programmiersprachen in Maschinencode, während ein Assembler einfache Mnemonics eins zu eins in Prozessor-Opcodes überführt.

**Wo kommt Assembly heute noch zum Einsatz?**
In Bootloadern, Echtzeit-Betriebssystemen, Reverse-Engineering, Firmware für Mikrocontroller und hochoptimierten Kryptografie-Bibliotheken.


## Verwandte Begriffe
- [Memory Management](/de/dictionary/memory-management/)
- [Runtime](/de/dictionary/runtime/)
- [Compilation](/de/dictionary/compilation/)
- [Apple Silicon](/de/dictionary/apple-silicon/)
- [Emulator](/de/dictionary/emulator/)

## Verwandte Werkzeuge
- [Apollo-11](/de/discover/apollo-11/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/assembly/
