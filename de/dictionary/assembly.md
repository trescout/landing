# Assembly: Definition, Register und Systemarchitektur

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Assembly bezeichnet zwei Kernkonzepte der Informatik: die hardwarenächste symbolische Programmiersprache zur direkten CPU-Steuerung und kompilierte Bereitstellungspakete (.NET Assemblies).

## 1. Hardwarenahe Programmiersprache (Assembly Language)

Prozessoren verarbeiten ausschließlich binäre Maschinencodes (Opcodes). Die Assemblersprache ersetzt diese Bitfolgen durch lesbare Mnemonics:

- `MOV`: Überträgt Daten zwischen Registern oder Hauptspeicheradressen.
- `ADD` / `SUB`: Führt arithmetische Berechnungen direkt im Prozessor aus.
- `PUSH` / `POP`: Schreibt oder liest Werte auf dem Aufruf-Stack.
- `JMP` / `JE` / `JNE`: Verzweigt den Programmablauf anhand gesetzter Prozessor-Flags.

Der Quellcode wird von Assemblern wie NASM oder GAS ohne zwischengeschaltete Virtual Machine unmittelbar in Maschinencode übersetzt.

## 2. CPU-Register und x86-64-Architektur

Moderne 64-Bit-Prozessoren der x86-64-Familie verfügen über spezialisierte und universelle Register:

- **Allzweckregister:** `RAX` (Akkumulator und Rückgabewert), `RBX` (Basisregister), `RCX` (Schleifenzähler), `RDX` (I/O-Daten), `RDI` und `RSI` (Ziel- und Quellindizes für Pufferoperationen).
- **Spezialregister:** `RSP` (Stack Pointer), `RBP` (Frame Base Pointer), `RIP` (Instruction Pointer für den nächsten Befehl) sowie `RFLAGS` (Statusflags wie Carry, Sign und Zero).

## 3. CISC vs. RISC: Unterschiede zwischen x86-64 und ARM64

Die x86-64-Architektur basiert auf dem **CISC**-Prinzip (komplexer Befehlssatz) mit variabler Befehlslänge und direkten Speicheroperationen. ARM64 (Apple Silicon, moderne Mobilprozessoren) nutzt hingegen **RISC** (reduzierter Befehlssatz) mit festen 32-Bit-Befehlen und strikter Load-Store-Architektur für höchste Energieeffizienz.

## 4. Systemaufrufe (Syscalls) und Linux-x86-64-Beispiel

```
section .text
global _start

_start:
    ; 1. Ausgabe auf stdout (sys_write = syscall 1)
    mov rax, 1          ; Syscall-Nummer: 1 (sys_write)
    mov rdi, 1          ; Dateideskriptor: 1 (stdout)
    mov rsi, msg        ; Pufferadresse im Speicher
    mov rdx, 14         ; Textlänge
    syscall             ; Wechsel in den Kernel-Modus

    ; 2. Programm beenden (sys_exit = syscall 60)
    mov rax, 60         ; Syscall-Nummer: 60 (sys_exit)
    xor rdi, rdi        ; Exit-Code 0
    syscall

section .data
    msg db "Hallo, Welt!", 10
```

## 5. .NET Assemblies und WebAssembly (WASM)

- **.NET Assembly:** Beim Kompilieren von C#-Projekten entsteht eine Einheit aus Zwischencode (CIL) und Metadaten als `.dll`- oder `.exe`-Datei.
- **WebAssembly (WASM):** Ein portables Binärformat, das hardwarenahen Code aus Sprachen wie Rust oder C++ sicher und performant im Webbrowser ausführt.

*Assembler-Programmierung gleicht dem präzisen Einsetzen mikroskopisch kleiner Zahnräder und Federn in ein mechanisches Uhrwerk: Sie liefert maximale Kontrolle und Effizienz, verlangt jedoch höchste Genauigkeit.*

## Häufig gestellte Fragen

**Was bedeutet Assembly und wofür wird es verwendet?**

Es ist die hardwarenächste symbolische Sprache, die Prozessorbefehle direkt abbildet und vor allem für Betriebssysteme, Treiber und IT-Sicherheitsanalysen genutzt wird.

**Was unterscheidet einen Assembler von einem Compiler?**

Ein Compiler übersetzt komplexe, abstrakte Programmiersprachen in Maschinencode, während ein Assembler einfache Mnemonics eins zu eins in Prozessor-Opcodes überführt.

**Wo kommt Assembly heute noch zum Einsatz?**

In Bootloadern, Echtzeit-Betriebssystemen, Reverse-Engineering, Firmware für Mikrocontroller und hochoptimierten Kryptografie-Bibliotheken.

## Verwandte Begriffe

- [Memory Management](https://trescout.com/de/dictionary/memory-management/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Compilation](https://trescout.com/de/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/de/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/de/dictionary/emulator/)

## Verwandte Werkzeuge

- [Apollo-11](https://trescout.com/de/discover/apollo-11/)

Diese Erklärung wurde in einfacher Sprache für TreScout verfasst und aus dem türkischen Original **automatisch übersetzt** · maßgeblich ist die türkische Fassung. Wenn etwas fehlerhaft oder unvollständig erscheint, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/assembly/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/assembly/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/assembly/
