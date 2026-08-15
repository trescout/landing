# Was ist KV Cache?

> Key-Value Cache

Dabei handelt es sich um eine Beschleunigungsmethode, die verhindert, dass künstliche Intelligenz dieselben Vorgänge wiederholt, indem sie die zuvor verarbeiteten Wörter in ihrem Gedächtnis behält.

## Definition
Bei der Erstellung eines Textes speichert künstliche Intelligenz die zuvor verarbeiteten Informationen nicht jedes Wort neu, sondern speichert sie in einem Cache als „Schlüssel“- und „Wert“-Werte. Dieses System ermöglicht es dem Modell, sich schnell an die Vergangenheit zu erinnern, ohne sie bei der Vorhersage des nächsten Wortes neu berechnen zu müssen. Dadurch wird die Verarbeitungslast reduziert und die Reaktionszeiten deutlich verkürzt.

## So funktioniert es
Während das Modell ausgeführt wird, wird es automatisch im Hintergrund erstellt und im Speicher gehalten. Dieser Cache beginnt sich zu füllen, wenn der Benutzer ein langes Gespräch beginnt. Wenn der Speicher voll ist, entwickelt das System Strategien, um alte Informationen zu löschen oder Platz für neue Daten zu schaffen.

## Wo es eingesetzt wird
Es wird in den Arbeitsabläufen von LLMs und insbesondere in Chat-Oberflächen eingesetzt, in denen lange Texte produziert werden.

## Häufig verwechselt mit
Es kann mit dem Kontextfenster verwechselt werden, es handelt sich jedoch nicht um eine Kapazitätsbeschränkung, sondern um eine Methode zur effizienten Nutzung dieser Kapazität.

## Häufige Fragen
**Warum ist KV-Cache wichtig?**
Indem verhindert wird, dass die KI immer wieder denselben Satz berechnet, entlastet sie den Prozessor und beschleunigt die Antwort.

**Was passiert, wenn der Speicher voll ist?**
Das System ist möglicherweise nicht mehr in der Lage, neue Daten zu verarbeiten oder beginnt, alte Informationen zu vergessen.


## Verwandte Begriffe
- [LLM](/de/dictionary/llm/)
- [Context Window](/de/dictionary/context-window/)
- [Inference](/de/dictionary/inference/)
- [Memory Management](/de/dictionary/memory-management/)

## Verwandte Werkzeuge
- [LMCache](/de/discover/lmcache/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/kv-cache/
