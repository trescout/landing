# Was ist Serialisierung (Serialization)?

> Englisch: Serialization · Wortherkunft: lateinisch series (Reihe, Kette) + facere (machen)

**Kategorie:** Dev  
**Letzte Aktualisierung:** 2026-09-19

Serialisierung (Serialization) ist der Vorgang, bei dem dynamische Datenstrukturen, Objekte und Zeigergraphen aus dem Arbeitsspeicher (RAM) in einen linearen Bytestrom oder ein Textformat umgewandelt werden, um über Netzwerke übertragen oder auf Festplatten gesichert zu werden.

## Was ist Serialisierung und warum ist sie notwendig? Speichermodell
In modernen Betriebssystemen arbeitet jeder Prozess in einem eigenen virtuellen Adressraum. Heap-Objekte verweisen über Speicheradressen (Pointer) aufeinander, die außerhalb dieses konkreten Prozesses wertlos sind. Die Serialisierung löst diese Zeigerstrukturen auf und überführt sie in ein portables, plattformunabhängiges Datenformat.

## Serialisierungsformate: Textbasiert vs. Binäre Protokolle
Die Auswahl des passenden Formats ist eine Abwägung zwischen Lesbarkeit und Ressourceneffizienz:
- **Textbasierte Formate (JSON, YAML, XML):** Leicht durch Menschen lesbar und einfach per HTTP zu debuggen, verursachen jedoch spürbaren CPU-Parsingaufwand und größere Datenmengen.- **Binärformate (Protocol Buffers, MessagePack, Avro):** Extrem kompakte Repräsentationen mit starker Typisierung, die minimale Bandbreite erfordern und blitzschnell verarbeitet werden.- **Schema-Evolution:** Frameworks wie Protobuf garantieren Vorwärts- und Rückwärtskompatibilität zwischen verteilten Diensten mit unterschiedlichen Versionsständen.

## Zero-Copy-Deserialisierungsarchitektur
Klassische Deserialisierer erzeugen beim Einlesen neue Objekte im Heap-Speicher. Hochleistungsbibliotheken wie Cap'n Proto oder FlatBuffers nutzen das **Zero-Copy-Prinzip**:
- **Feste Speicherausrichtung:** Daten werden mit relativen Offsets im Bytestrom abgelegt.- **Direkter Zugriff:** Anwendungen lesen Attribute unmittelbar aus dem Speicherabbild oder Netzwerkpuffer, ohne zusätzliche Speicherallokationen vorzunehmen.

## Sicherheitsaspekt: Insecure Deserialization (CWE-502)
Wenn Serialisierungsbibliotheken nicht nur reine Datenfelder, sondern beliebige ausführbare Objektklassen rekonstruieren (wie bei Python pickle oder nativer Java-Serialisierung), drohen gravierende Sicherheitslücken:
- **Remote Code Execution (RCE):** Angreifer schleusen bösartige Objektketten (Gadget Chains) ein, die bereits beim Einlesen Systembefehle auf dem Zielserver ausführen.- **Schutzmaßnahmen:** Nicht vertrauenswürdige Schnittstellen ausschließlich mit streng typisierten Datenformaten (JSON, Protobuf) bedienen und Nachrichten via HMAC oder TLS absichern.

## Als Analogie
Es ist wie das Zerlegen eines Schranks in flache Bretter für den Transport im Umzugskarton, um ihn am Zielort anhand der Anleitung exakt wieder aufzubauen.

## Häufige Fragen

**Worin liegt der Unterschied zwischen Serialisierung und Deserialisierung?**  
Serialisierung überführt Speicherobjekte in einen linearen Bytestrom; Deserialisierung baut aus dem Bytestrom wieder lebendige Objekte im Speicher auf.

**Warum darf man Python pickle nie mit ungesicherten Daten nutzen?**  
Weil pickle beim Entpacken beliebigen Programmcode ausführen kann, was Angreifern direkte Serverübernahmen ermöglicht.

**Wie erzielt FlatBuffers Zero-Copy-Performance?**  
Durch vorab ausgerichtete Binärstrukturen, bei denen Datenfelder direkt im Puffer gelesen werden können, ohne Heap-Objekte zu erzeugen.

**Wann ist JSON gegenüber Protobuf vorzuziehen?**  
Wenn einfache Lesbarkeit, schnelles Debugging im Browser und breite Zugänglichkeit wichtiger sind als minimale Bytegrößen.

## Verwandte Begriffe
- [API](/de/dictionary/api/)
- [Data Pipeline](/de/dictionary/data-pipeline/)
- [Buffer](/de/dictionary/buffer/)

## Verwandte Tools
- [YAML Cpp](/de/discover/yaml-cpp/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/serialization/
