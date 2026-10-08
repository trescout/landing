# Was ist Emitter?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Emitter (Sender) ist ein kritischer Begriff in der Softwaretechnik, der in zwei grundlegenden Bereichen auftaucht: Als Mechanismus, der Zustandsänderungen in ereignisgesteuerten Architekturen (Event-Driven Architecture) an Zuhörer meldet (Event Emitter), und als Codegenerierungsmodul in der Compiler-Technologie, das den analysierten Code in die Zielmaschinensprache oder in Bytecode umwandelt (Code Emitter).

## Konzeptioneller Ursprung: Von der Physik zur Softwarearchitektur

Das Wort „Emitter“ leitet sich vom lateinischen Verb emittere ab, was „hinausschleudern“ oder „freisetzen“ bedeutet. In der Elektronik werden Kathoden, die Elektronen emittieren, oder in der Telekommunikation Funksender, die Signale aussenden, als Emitter bezeichnet. Die Softwarewelt hat diesen Begriff übernommen, um eine „Quelle zu beschreiben, die einen internen Zustand oder ein erzeugtes Ergebnis an die Außenwelt weitergibt“.

In der Software ist ein "Emitter" keine einzelne Struktur, sondern repräsentiert je nach Kontext zwei riesige Disziplinen: Ereignisströme und Compiler-Design.

***Analogie:** Event Emitter: Ist ein Feuermelder. Wenn der Knopf gedrückt wird (emit), weiß der Knopf nicht, wie viele Personen sich im Gebäude befinden oder welche Sirenen ertönen; er sendet lediglich ein Signal aus und alle angeschlossenen Alarmsysteme (listeners) werden aktiviert.

Code Emitter: Ist der leitende Ingenieur, der die detaillierten technischen Pläne (AST) eines Architekten entgegennimmt und sie in Anweisungen für Schalungen und Bewehrungen umwandelt, die von den Bauarbeitern direkt umgesetzt werden können.*

## 1. Ereignisgesteuerte Architektur und Event Emitter

In der ereignisbasierten Programmierung ist der Emitter das Herzstück der Entwurfsmuster Observer und Publish-Subscribe. Er ermöglicht es den Komponenten eines Systems, über Ereignisse miteinander zu kommunizieren (lose Kopplung), anstatt sich gegenseitig direkt zu kennen (enge Kopplung).

Die reaktive und asynchrone I/O-Struktur von Node.js basiert auf der EventEmitter-Klasse innerhalb des events-Moduls:

**emit(event, [...args]):** Löst das Ereignis mit dem angegebenen Namen aus und benachrichtigt alle registrierten Listener.

**on(event, listener):** Registriert die Callback-Funktion, die ausgeführt wird, wenn das angegebene Ereignis eintritt.

**einmal(Ereignis, Zuhörer):** Fängt das Ereignis nur beim ersten Auftreten einmalig ab und löscht die Registrierung anschließend automatisch.

**Wichtiger technischer Hinweis:** Entgegen der landläufigen Meinung führt Node.js EventEmitter Ereignis-Listener standardmäßig synchron aus. Wenn ein Listener blockiert, warten nachfolgende Listener. Für die asynchrone Ausführung wird setImmediate() oder process.nextTick() verwendet.

Der häufigste Fehler in der Event Emitter-Architektur besteht darin, die Listener (removeListener oder off) von Objekten, deren Lebenszyklus beendet ist, nicht zu entfernen. Dies verhindert, dass Objekte vom Garbage Collector bereinigt werden, und führt zu einer MaxListenersExceededWarning-Warnung in Node.js.

## 2. Code Emitter (Codegenerator) in der Compiler-Architektur

Die letzte und wichtigste Stufe eines Compilers oder Transpilers ist die Emitter-Schicht (Codegenerator). Die Kompilierungskette funktioniert in der folgenden Reihenfolge: Quellcode → Lexer (Tokens) → Parser (Syntaxbaum – AST) → Semantische Analyse → Optimierung → Emitter → Zielcode

Der Emitter durchläuft den optimierten abstrakten Syntaxbaum (AST) oder die Zwischenrepräsentation (IR - Intermediate Representation) von Anfang bis Ende (meist mit dem Visitor-Pattern). Er übersetzt jeden Knoten in Anweisungen, die die Zielplattform versteht: Diese Ausgabe kann roher Maschinencode (x86/ARM-Assembly), virtueller Maschinen-Bytecode (JVM, V8-Bytecode) oder eine andere Hochsprache (wie die Kompilierung von TypeScript zu JavaScript) sein.

## Häufige Fragen

**Was bedeutet Emitter und was ist die türkische Entsprechung?**

Emitter bedeutet im Englischen „Sender“ oder „Emittent“. In der Softwareentwicklung wird es meist als „Event Emitter“ (Ereignissender) oder in Compilern als „Code Emitter“ (Code-Generator/Sender) verwendet.

**Was ist der größte Vorteil der Verwendung eines Event Emitters?**

Er reduziert die Abhängigkeit (Coupling) zwischen Komponenten auf null. Ein Modul löst ein Ereignis aus; es kümmert sich nicht darum, wer, wann oder wie das Ereignis verarbeitet. Dies erhöht die Modularität und Testbarkeit.

**Welche Aufgabe übernimmt der Emitter in Compilern?**

Er ist die letzte Komponente, die die analysierte und optimierte Baumstruktur (AST) des Quellcodes entgegennimmt und die Zielausgabe (Assembly, Maschinencode, Bytecode oder transformierten Quellcode) generiert.

**Was ist der Unterschied zwischen einem RxJS Observable und einem Event Emitter?**

Ein Event Emitter führt in der Regel Multicasting durch und wird für sofortige Ereignisbenachrichtigungen verwendet. Ein RxJS Observable hingegen bietet die Möglichkeit, umfangreiche Datenströme über die Zeit hinweg mit funktionalen Operatoren wie Filtern, Mapping und Verzögerungen zu transformieren.

## Verwandte Begriffe

- [Parser](https://trescout.com/de/dictionary/parser/)
- [Compiler](https://trescout.com/de/dictionary/compiler/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Assembly](https://trescout.com/de/dictionary/assembly/)
- [API](https://trescout.com/de/dictionary/api/)
- [Bundler](https://trescout.com/de/dictionary/bundler/)

## Verwandte Werkzeuge

- [YAML Cpp](https://trescout.com/de/discover/yaml-cpp/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/emitter/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/emitter/
