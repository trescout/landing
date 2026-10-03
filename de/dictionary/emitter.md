# Was ist Emitter?

Emitter (Sender) ist ein kritischer Begriff in der Softwaretechnik, der in zwei grundlegenden Bereichen auftaucht: Als Mechanismus, der Zustandsänderungen in ereignisgesteuerten Architekturen (Event-Driven Architecture) an Zuhörer meldet (Event Emitter), und als Codegenerierungsmodul in der Compiler-Technologie, das den analysierten Code in die Zielmaschinensprache oder in Bytecode umwandelt (Code Emitter).

## Konzeptioneller Ursprung: Von der Physik zur Softwarearchitektur
Das Wort „Emitter“ leitet sich vom lateinischen Verb emittere ab, was „hinausschleudern“ oder „freisetzen“ bedeutet. In der Elektronik werden Kathoden, die Elektronen emittieren, oder in der Telekommunikation Funksender, die Signale aussenden, als Emitter bezeichnet. Die Softwarewelt hat diesen Begriff übernommen, um eine „Quelle zu beschreiben, die einen internen Zustand oder ein erzeugtes Ergebnis an die Außenwelt weitergibt“.

## 1. Ereignisgesteuerte Architektur und Event Emitter
In der ereignisbasierten Programmierung ist der Emitter das Herzstück der Entwurfsmuster Observer und Publish-Subscribe. Er ermöglicht es den Komponenten eines Systems, über Ereignisse miteinander zu kommunizieren (lose Kopplung), anstatt sich gegenseitig direkt zu kennen (enge Kopplung).

## 2. Code Emitter (Codegenerator) in der Compiler-Architektur
Die letzte und wichtigste Stufe eines Compilers oder Transpilers ist die Emitter-Schicht (Codegenerator). Die Kompilierungskette funktioniert in der folgenden Reihenfolge: Quellcode → Lexer (Tokens) → Parser (Syntaxbaum – AST) → Semantische Analyse → Optimierung → Emitter → Zielcode

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
- [Parser](/de/dictionary/parser/)
- [Compiler](/de/dictionary/compiler/)
- [Runtime](/de/dictionary/runtime/)
- [Assembly](/de/dictionary/assembly/)
- [API](/de/dictionary/api/)
- [Bundler](/de/dictionary/bundler/)

## Verwandte Werkzeuge
- [YAML Cpp](/de/discover/yaml-cpp/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/emitter/
