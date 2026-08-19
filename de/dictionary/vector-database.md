# Was ist Vector Database?

Dabei handelt es sich um eine spezielle Art von Datenbank, in der künstliche Intelligenz Daten speichert, sodass sie diese anhand ihrer Bedeutung schnell finden kann.

## Definition
Eine Vektordatenbank ist ein spezielles Speichersystem, das Daten als numerische Vektoren speichert, die ihre Bedeutung darstellen, und nicht als herkömmliche Zeilen und Spalten. Diese Struktur ermöglicht es der künstlichen Intelligenz, innerhalb von Millisekunden die relevantesten Daten aus Millionen von Daten zu finden.

## So funktioniert es
Zunächst werden die Daten mithilfe der Einbettungsmethode in numerische Vektoren umgewandelt. Wenn eine Abfrage durchgeführt wird, misst die Datenbank den Abstand zwischen dem Vektor der Abfrage und den Vektoren der Daten. Als Ergebnisse werden diejenigen mit der kürzesten Entfernung zurückgegeben, also diejenigen, die der Bedeutung am nächsten kommen.

## Wo es eingesetzt wird
Es wird in intelligenten Suchsystemen, Empfehlungsmaschinen und RAG-Systemen eingesetzt, bei denen künstliche Intelligenz ein Langzeitgedächtnis schafft.

## Häufig verwechselt mit
Es wird mit klassischen Datenbanken wie SQL verwechselt, aber klassische Datenbanken suchen nach genauen Übereinstimmungen, während Vektordatenbanken nach Ähnlichkeiten suchen.

## Häufige Fragen
**Ist es langsamer als klassische Datenbanken?**
Nein, es ist viel schneller als klassische Methoden zur Ähnlichkeitssuche in sehr großen Datensätzen.

**Welche Daten können gespeichert werden?**
Alle Daten, deren Bedeutung in Vektoren umgewandelt werden kann, wie Text, Bild, Audio oder Video, können gespeichert werden.


## Verwandte Begriffe
- [Embedding](/de/dictionary/embedding/)
- [RAG](/de/dictionary/rag/)
- [Knowledge Graph](/de/dictionary/knowledge-graph/)
- [Memory Engine](/de/dictionary/memory-engine/)

## Verwandte Werkzeuge
- [Turbovec](/de/discover/turbovec/)
- [Zvec](/de/discover/zvec/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/vector-database/
