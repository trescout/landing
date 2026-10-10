# Was ist Runtime?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Unter Laufzeit versteht man den Zeitraum, in dem ein Programm nach der Kompilierungsphase tatsächlich im Prozessor und Speicher des Computers ausgeführt wird, sowie die Software-Infrastruktur (Laufzeitumgebung), die diese Ausführung ermöglicht.

## 1. Zwei grundlegende Bedeutungen des Laufzeitbegriffs

In der Softwareentwicklung bezeichnet der Begriff „Runtime“ je nach Kontext zwei unterschiedliche Konzepte:

1. Als Zeitphase (Laufzeit): Nach der Phase, in der der Code geschrieben wird (Erstellung) und durch den Compiler geleitet wird (Kompilierungszeit), ist dies der Zeitraum vom Start des Programms durch den Endbenutzer bis zum Schließen des Programms.
2. Als Ausführungsschicht (Laufzeitumgebung): Hierbei handelt es sich um eine Reihe von Bibliotheken, Speichermanagern, Garbage Collectors und virtuellen Maschinen, die erforderlich sind, damit der geschriebene Code direkt auf dem Betriebssystem und der Hardware ausgeführt werden kann. Beispielsweise sind Node.js, JVM (Java Virtual Machine) oder Go Runtime Ausführungsumgebungen.

***Analogie:** Kompilierzeit ist die Überprüfung der Architekturzeichnungen und statischen Berechnungen eines Gebäudes durch den Ingenieur am Tisch; Wenn ein Fehler vorliegt, wird dieser korrigiert, während er auf dem Papier ist. Die Laufzeit ist der Moment, in dem das Gebäude gebaut wird und sich die Menschen darin niederlassen. Unvorhergesehene Ereignisse wie Erdbeben, Überschwemmungen oder Überlastungen stellen das Gebäude erst in diesem Stadium auf die Probe.*

## 2. Unterschied zwischen Kompilierungszeit und Laufzeit

- Kompilierungszeit: Syntaxanalyse, statische Typprüfungen und Konvertierung in Maschinencode werden durchgeführt, bevor der Code ausgeführt wird. In dieser Phase werden Syntaxfehler und Typkonfliktfehler abgefangen.
- Laufzeit: Speicherzuweisung, Systemaufrufe und die Ereignisschleife werden verwaltet, während der Benutzer das Programm tatsächlich ausführt. In dieser Phase treten NullPointerException-, Segmentation Fault (SIGSEGV)- und Stack Overflow-Fehler auf.

## 3. Verwaltete vs. nicht verwaltete Laufzeiten

- Nicht verwaltet (C, C++, Rust, Zig): Konvertiert direkt in nativen Maschinencode; Keine schwere virtuelle Maschine oder Garbage Collector läuft im Hintergrund, es genügt eine leichte C-Standardbibliothek (libc). Es bietet maximale Geschwindigkeit und keine Verzögerung.
- Verwaltet (Java, C#, Go, JavaScript, Python): Läuft im Schutz einer virtuellen Maschine (JVM, CLR) oder Laufzeit. Es umfasst JIT-Compiler, automatische Garbage Collectors und einen integrierten Scheduler, der Goroutinen verwaltet, beispielsweise in Go.

## 4. Moderne JavaScript-Laufzeitkriege: Node.js vs. Deno vs. Bun

- Node.js (2009): Industriestandard, der die Google V8-Engine mit der C++-basierten asynchronen E/A-Ereignisschleife libuv kombiniert.
- Deno (2018): Moderne Plattform, die die V8-Engine mit der Rust- und Tokio-Infrastruktur verbindet, über integriertes TypeScript und eine sichere Berechtigungs-Sandbox verfügt.
- Bun (2023): Es handelt sich um eine Arbeitsumgebung der neuen Generation, die die JavaScriptCore-Engine von Apple WebKit nutzt und komplett von Grund auf in der Zig-Sprache geschrieben wurde und Datei-/Netzwerk-I/O um ein Vielfaches schneller als Node.js bietet.

## Häufige Fragen

**Was bedeutet Laufzeit, was ist ihr türkisches Äquivalent?**

Auf Türkisch heißt es „Laufzeit“ oder „Ausführungsumgebung“. Es beschreibt den Zeitraum, in dem ein Programm seinen Quellcode verlässt und tatsächlich auf der Computerhardware und der Softwareschicht läuft, die diese Arbeit unterstützt.

**Was ist ein Laufzeitfehler?**

Es handelt sich um einen Fehler, der die Kompilierungsphase erfolgreich durchläuft, aber dazu führt, dass die Anwendung aufgrund einer unerwarteten Situation (Division durch Null, Zugriff auf ein leeres Objekt, unzureichender RAM) während der Ausführung des Programms plötzlich abstürzt.

**Ist Node.js eine Programmiersprache oder eine Laufzeitumgebung?**

Node.js ist keine Sprache; Es handelt sich um eine Open-Source-JavaScript-Laufzeitumgebung, die die Ausführung von JavaScript-Code auf Servern und Computern ermöglicht, ohne dass ein Browser erforderlich ist.

**Wie funktioniert JIT (Just-In-Time) während der Kompilierungslaufzeit?**

Der JIT-Compiler erkennt häufig verwendete Codeblöcke („Hot Paths“) sofort, während das Programm ausgeführt wird, und konvertiert diese Blöcke zur Laufzeit in nativen Maschinencode, wodurch die Leistung der Anwendung erhöht wird.

## Verwandte Begriffe

- [Memory Management](https://trescout.com/de/dictionary/memory-management/)
- [Assembly](https://trescout.com/de/dictionary/assembly/)
- [Compilation](https://trescout.com/de/dictionary/compilation/)
- [Bundler](https://trescout.com/de/dictionary/bundler/)
- [Tech Stack](https://trescout.com/de/dictionary/tech-stack/)

## Verwandte Werkzeuge

- [Andrej Karpathy Skills](https://trescout.com/de/discover/andrej-karpathy-skills/)
- [Node](https://trescout.com/de/discover/node/)
- [Deno](https://trescout.com/de/discover/deno/)
- [BUN](https://trescout.com/de/discover/bun/)
- [Svelte](https://trescout.com/de/discover/svelte/)
- [Wand-Enhancer](https://trescout.com/de/discover/wand-enhancer/)
- [Univer](https://trescout.com/de/discover/univer/)
- [Onnxruntime](https://trescout.com/de/discover/onnxruntime/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/runtime/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/runtime/
