# Was ist Experts Streamed from Disk?

Dies ist eine Methode, bei der Teile riesiger KI-Modelle bei Bedarf von der Festplatte geladen werden, wenn sie nicht in den Arbeitsspeicher passen.

## Definition
KI-Modelle sind manchmal so groß, dass sie nicht in die RAM-Kapazität des Computers passen. Bei dieser Technik werden nur die Teile des Modells (die Experten), die in diesem Moment benötigt werden, schnell von der Festplatte gelesen und in den Arbeitsspeicher geladen. Dadurch können sehr große Modelle auch auf Hardware mit begrenzten Ressourcen ausgeführt werden.

## So funktioniert es
Das System unterteilt die Gewichte des Modells in kleine Stücke und speichert diese auf der Festplatte. Wenn ein Benutzer eine Frage stellt, werden die relevanten Teile des Modells sehr schnell von der Festplatte in den Arbeitsspeicher übertragen, verarbeitet und anschließend wird der Arbeitsspeicher wieder geleert.

## Wo es eingesetzt wird
Es wird insbesondere von Entwicklern verwendet, die sehr große Sprachmodelle auf Heimcomputern ausführen möchten, sowie auf Servern mit Hardwarebeschränkungen.

## Häufig verwechselt mit
Es könnte mit dem Laden des gesamten Modells in den Arbeitsspeicher verwechselt werden; hier findet das Laden jedoch nur bei Bedarf statt.

## Häufige Fragen
**Verringert diese Methode die Geschwindigkeit?**
Ja, da das Lesen von der Festplatte langsamer ist als vom RAM, kann es zu einer gewissen Verzögerung bei der Antwortzeit des Modells kommen.

**Kann jedes Modell auf diese Weise funktionieren?**
Das Modell muss mit dieser Architektur entworfen worden sein; das heißt, es muss zwingend eine modulare Struktur (Mixture of Experts) aufweisen.


## Verwandte Begriffe
- [Mixture of Experts](/de/dictionary/mixture-of-experts/)
- [RAM](/de/dictionary/ram/)
- [Inference Engine](/de/dictionary/inference-engine/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/experts-streamed-from-disk/
