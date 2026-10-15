# Was ist Assembly?

*Entwicklung · Zuletzt aktualisiert: 19. September 2026*

Assembler bezieht sich auf zwei grundlegende Konzepte in der Informatik: Erstens die symbolische Programmiersprache der niedrigsten Ebene (Assemblersprache), die den Hardwareprozessor (CPU) direkt steuert; Die zweite besteht darin, kompilierte Softwaremodule (.NET-Assembly) in ein einziges verteilbares Paket umzuwandeln.

## 1. Programmiersprache auf niedriger Ebene (Assemblersprache)

Der Computerprozessor versteht nur die binären Signale 0 und 1 (Maschinencode/Opcodes). Die Assemblersprache besteht aus für Menschen lesbaren symbolischen Abkürzungen (Mnemoniken), die diesen rohen Maschinencodes entsprechen:

- MOV: Kopiert Daten von einem Register in ein anderes oder in eine andere Speicheradresse.
- ADD/SUB: Führt mathematische Additions- und Subtraktionsoperationen aus.
- PUSH/POP: Fügt Daten zum Aufrufstapel hinzu oder ruft ihn ab.
- JMP / JE / JNE: Verzweigt den Programmablauf entsprechend dem Vergleichsergebnis auf eine andere Speicheradresse.

Geschriebene Assembler-Codes werden durch Konverter namens Assembler (nasm, gas) direkt in Maschinencode übersetzt. Dazwischen gibt es keine virtuelle Maschinenschicht.

***Analogie:** Die Assemblersprache ist so, als würde man die Zahnräder, Federn und Wellen einer Uhr nacheinander mit einer Pinzette unter dem Mikroskop platzieren; Es bietet höchste Präzision und Leistung, erfordert jedoch große Sorgfalt. Bei der Software-Montage wird dieser empfindliche Mechanismus in das Gehäuse eingebaut und als funktionierende Armbanduhr verpackt.*

## 2. Prozessorregister und x86-64-Architektur

Die kritischsten Register auf einem modernen 64-Bit-x86-64-Prozessor sind:

- Allzweckregister: RAX (Akkumulator und Funktionsrückgabe), RBX (Basisdatenzeiger), RCX (Schleifenzähler), RDX (Eingabe-/Ausgabedaten), RDI und RSI (Ziel- und Quellzeiger).
- Spezialregister: RSP (Stapelzeiger – Oberseite des Stapels), RBP (Basiszeiger – Basis des Funktionsrahmens), RIP (Befehlszeiger – Adresse des nächsten auszuführenden Befehls) und RFLAGS (Null-, Übertragsflags).

## 3. CISC vs. RISC: Unterschied zwischen x86-64 und ARM64

Die x86-64-Architektur arbeitet mit der CISC-Philosophie (Complex Instruction Set). Es verfügt über variable Befehlsgrößen und umfangreiche Befehle, die direkt im Speicher ausgeführt werden können. ARM64 (Apple Silicon, Mobile) basiert auf RISC (Reduced Instruction Set); Mit seiner festen 32-Bit-Befehlslänge und der Load-Store-Architektur bietet es eine hervorragende Energieeffizienz.

## 4. Beispiel für Systemaufrufe (Syscall) und Linux x86-64

```
section .text
global _start

_start:
    ; 1. Ekrana "Merhaba" yazdır (sys_write = syscall 1)
    mov rax, 1          ; syscall numarası: 1 (sys_write)
    mov rdi, 1          ; dosya tanıtıcı: 1 (stdout)
    mov rsi, mesaj      ; metnin bellek adresi
    mov rdx, 8          ; metin uzunluğu
    syscall             ; çekirdeğe geçiş yap

    ; 2. Programı güvenle sonlandır (sys_exit = syscall 60)
    mov rax, 60         ; syscall numarası: 60 (sys_exit)
    xor rdi, rdi        ; çıkış kodu 0
    syscall

section .data
    mesaj db "Merhaba", 10
```

## 5. .NET Assembly und WebAssembly (WASM)

- .NET-Assembly: Beim Kompilieren von C#-Code wird ein logisches Assemblypaket (Assembly) im DLL- oder EXE-Format erstellt, das CIL/MSIL-Bytecodes und Metadaten enthält.
- WebAssembly (WASM): Ein portabler Stack-Bytecode für virtuelle Maschinen, der die Ausführung von C-, C++- und Rust-Code im Browser mit nahezu nativer Leistung ermöglicht.

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

- [Memory Management](https://trescout.com/de/dictionary/memory-management/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Compilation](https://trescout.com/de/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/de/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/de/dictionary/emulator/)

## Verwandte Werkzeuge

- [Ghidra](https://trescout.com/de/discover/ghidra/)
- [Apollo-11](https://trescout.com/de/discover/apollo-11/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/assembly/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/assembly/
