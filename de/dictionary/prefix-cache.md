# Was ist Prefix Cache?

Eine Beschleunigungsmethode, die verhindert, dass künstliche Intelligenz dieselben Vorgänge wiederholt, indem sie die zuvor verarbeiteten Textanfänge im Speicher behält.

## Definition
Modelle der künstlichen Intelligenz können bei der Verarbeitung langer Texte jedes Mal von Anfang an lesen. Der Präfix-Cache speichert den unveränderlichen Anfangsteil dieses Textes im Speicher. Daher verwendet das Modell die wörtlichen Informationen, anstatt diesen Teil bei seiner nächsten Anfrage erneut zu lesen.

## So funktioniert es
Das System speichert die Präfixe der vom Modell verarbeiteten Texte zwischen. Wenn eine ähnliche Anfrage eingeht, verwendet das System sofort diesen Teil des Caches und verarbeitet nur die neu hinzugefügten Teile.

## Wo es eingesetzt wird
Es wird in LLM-Diensten, Gesprächen, die einen langen Kontext erfordern, und Anwendungen der künstlichen Intelligenz mit hohem Datenverkehr verwendet.

## Häufig verwechselt mit
Es kann mit dem KV-Cache verwechselt werden; Während der KV-Cache den internen Zustand des Modells speichert, enthält der Präfix-Cache Textblöcke.

## Häufige Fragen
**Wie viel Geschwindigkeit bietet es?**
Dies verkürzt die Reaktionszeit erheblich, insbesondere bei der Arbeit an langen Dokumenten.

**Ist es immer verfügbar?**
Ja, aber da es Speicherplatz beansprucht, muss es entsprechend der Kapazität des Systems verwaltet werden.


## Verwandte Begriffe
- [KV Cache](/de/dictionary/kv-cache/)
- [Context Window](/de/dictionary/context-window/)
- [Inference](/de/dictionary/inference/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/prefix-cache/
