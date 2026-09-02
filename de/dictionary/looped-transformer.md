# Was ist Looped Transformer?

Eine KI-Architektur, die den Speicherverbrauch reduziert, indem sie dieselben Verarbeitungsschichten wiederholt verwendet.

## Definition
Während herkömmliche Modelle für jede Schicht eine separate Verarbeitungseinheit benötigen, verwendet diese Architektur dieselbe Schicht in einer Schleife immer wieder. Dadurch verkleinert sich die Modellgröße und es wird weniger Speicher verbraucht. Ziel ist es, große Modelle auf kleineren Geräten auszuführen, ohne die Leistung zu beeinträchtigen.

## So funktioniert es
Die Daten gelangen in das Modell und durchlaufen denselben Schichtenblock mehrmals. Bei jedem Durchgang werden die Daten weiter verarbeitet, bis das Endergebnis erreicht ist.

## Wo es eingesetzt wird
Wird bei Geräten mit geringen Ressourcen oder in mobilen KI-Anwendungen bevorzugt.

## Häufig verwechselt mit
Kann mit der Standard-Transformer-Architektur verwechselt werden, jedoch ist die Anzahl der Schichten hier physisch geringer.

## Häufige Fragen
**Läuft es langsamer?**
Da die Schichten wiederverwendet werden, kann es etwas mehr Rechenzeit erfordern, spart aber Speicherplatz.

**Warum ist nicht jedes Modell so aufgebaut?**
Für einige komplexe Aufgaben führt es zu besseren Ergebnissen, wenn jede Schicht spezialisiert ist.


## Verwandte Begriffe
- [Transformer](/de/dictionary/transformer/)
- [Quantization](/de/dictionary/quantization/)
- [SLM](/de/dictionary/slm/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/looped-transformer/
