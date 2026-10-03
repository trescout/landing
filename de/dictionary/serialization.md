# Was ist Serialization?

Unter Serialisierung versteht man die dynamische Zuordnung von Objekten, Datenstrukturen und Zeigergrafiken im Arbeitsspeicher (RAM) einer Programmiersprache; Dabei handelt es sich um den Prozess der Konvertierung von Daten in einen flachen, linearen Bytestrom oder ein Textformat, das über das Netzwerk übertragen oder auf der Festplatte gespeichert werden kann.

## Was bedeutet Serialisierung und warum ist sie notwendig? Speichermodell
In modernen Betriebssystemen läuft jeder Prozess in seinem eigenen isolierten virtuellen Adressraum. Ein Objekt zur Laufzeit; Es enthält lokale Variablen auf dem Stapel, dynamisch zugewiesene Speicherblöcke auf dem Heap, Funktionszeiger (vtable) und Referenzadressen (0x7ffee4b2...).

## Serialisierungsformate: textbasiert vs. binär
Auswahl des richtigen Serialisierungsformats in der Softwarearchitektur; Es erfordert ein Gleichgewicht zwischen menschlicher Lesbarkeit, CPU-Parsing-Kosten, Netzwerkbandbreite und Typsicherheit.

## Zero-Copy-Deserialisierungsarchitektur
In klassischen Serialisierungsbibliotheken (JSON-Parser oder Standard-Protobuf) wird der Deserialisierungsprozess mit diesen Schritten durchgeführt:

## Sicherheitsdimension: Unsichere Deserialisierung (CWE-502)
Es entstehen katastrophale Sicherheitslücken, wenn bei der Serialisierung versucht wird, Objektklassen und Laufzeitverhalten zu serialisieren, anstatt nur reine Daten zu verschieben. Unsichere Deserialisierung (Insecure Reverse Serialization), die in der OWASP-Top-10-Liste steht, ermöglicht es dem Angreifer, beliebigen Code (Remote Code Execution – RCE) auf dem System auszuführen.

## Häufige Fragen
**Was ist der Hauptunterschied zwischen Serialisierung und Deserialisierung?**
Bei der Serialisierung werden lebende Objekte im Speicher in einen Byte-/Textstrom umgewandelt, der gespeichert oder übertragen werden kann. Bei der Deserialisierung wird diese Bytesequenz gelesen, analysiert und in ein Objekt umgewandelt, das im Speicher des Zielsystems funktioniert.

**Wann sollten Protobuf oder FlatBuffers anstelle von JSON in Webprojekten verwendet werden?**
Für öffentliche Web-Clients und öffentliche APIs ist JSON aufgrund seiner Browserkompatibilität und einfachen Debugging ideal. Für interne Microservices, mobile Anwendungs-Backends oder Echtzeit-Datenströme sollten jedoch Protobuf oder FlatBuffers bevorzugt werden, um die Netzwerkbandbreite zu drosseln und die Kosten für die CPU-Zerlegung zu senken.

**Wie funktioniert der Angriff „Insecure Deserialization“ und wie kann man ihn verhindern?**
Der Angreifer fügt schädliche Funktionen oder Klassenstrukturen in die serialisierten Daten ein, die während der Deserialisierung ausgeführt werden sollen. Wenn der Server diese Daten analysiert, können Systembefehle ausgelöst werden. To prevent this, formats that carry class logic should be abandoned and only schema formats that carry pure data (Protobuf, JSON Schema) should be used.

**Was bedeutet Zero-Copy-Deserialisierung?**
Dabei handelt es sich um eine Technik, bei der Daten direkt mit Zeigeroffsets im Pufferspeicher gelesen werden, anstatt den eingehenden Bytestrom durch Zuweisung neuer Speicherbereiche zu kopieren. Es entlastet den Prozessor und den Garbage Collector, indem es die Speicherzuweisung zurücksetzt.

**Was ist Schema-Evolution? Wie kann die Abwärts- und Vorwärtskompatibilität sichergestellt werden?**
Datenmodelle ändern sich, wenn die Software aktualisiert wird. Systeme wie Protobuf und Avro geben Feldern eindeutige numerische IDs, sodass alte Clients neue Felder ignorieren können (Abwärtskompatibilität) und neue Clients alte Daten mit Standardwerten lesen können (Vorwärtskompatibilität).


## Verwandte Begriffe
- [API](/de/dictionary/api/)
- [Data Pipeline](/de/dictionary/data-pipeline/)
- [Memory Management](/de/dictionary/memory-management/)
- [Network Stack](/de/dictionary/network-stack/)

## Verwandte Werkzeuge
- [YAML Cpp](/de/discover/yaml-cpp/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/serialization/
