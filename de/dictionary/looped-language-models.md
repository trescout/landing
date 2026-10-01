# Was ist Looped Language Models?

Dabei handelt es sich um zirkuläre Modelle der künstlichen Intelligenz, die Schritt-für-Schritt-Schlussfolgerungen ziehen, indem sie die Ergebnisse, die sie erzeugen, wieder als Eingabe verwenden.

## Definition
Schleifenbasierte Sprachmodelle sind im Gegensatz zu herkömmlichen Single-Pass-Sprachmodellen Strukturen, die die Ausgabe zwischen Schichten oder in einem zirkulären Prozess erneut verarbeiten. Bei der Lösung eines komplexen Problems gibt das Modell nicht alle Antworten auf einmal, sondern verbessert den ersten Entwurf, den es erstellt, Schritt für Schritt, indem es Eingaben berücksichtigt. Dieser Ansatz vertieft das Urteilsvermögen, ohne die Transaktionskosten zu erhöhen.

## So funktioniert es
Im ersten Schritt generiert das Modell eine transiente Antwort und gibt diese über einen internen Speicher oder einen Schleifenmechanismus an die Eingabeschicht des Modells zurück. Dieser Vorgang wird fortgesetzt, bis die angegebene Anzahl von Zyklen oder der Konfidenzschwellenwert erreicht ist.

## Wo es eingesetzt wird
Es wird insbesondere zum Lösen komplexer mathematischer Probleme, zum Analysieren logischer Rätsel und zum Debuggen von Code verwendet. Es wird auch bei Agenten der künstlichen Intelligenz bevorzugt, die tiefes Denken erfordern.

## Häufig verwechselt mit
Nicht zu verwechseln mit herkömmlichen rekurrenten neuronalen Netzen. Während rekurrente neuronale Netze Daten über Zeitreihen hinweg verarbeiten, verstärken diese Modelle die Transformatorarchitektur durch zyklische Logik.

## Häufige Fragen
**Laufen diese Modelle langsamer?**
Ja. Da dasselbe Modell mehrere Zyklen durchläuft, kann die Antwortgenerierungszeit etwas länger dauern.

**Kann die Anzahl der Schleifen gegen unendlich gehen?**
Nein. Um den Ressourcenverbrauch in Systemen zu verhindern, wird eine maximale Zyklusbegrenzung festgelegt.


## Verwandte Begriffe
- [Transformer](/de/dictionary/transformer/)
- [LLM](/de/dictionary/llm/)
- [Looped Transformer](/de/dictionary/looped-transformer/)
- [Inference](/de/dictionary/inference/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/looped-language-models/
