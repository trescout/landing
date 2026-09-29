# Was ist Weights?

Dies sind die numerischen Werte, die KI-Modelle während des Trainings lernen und die ihre Entscheidungen formen.

## Definition
Es handelt sich um riesige Zahlentabellen, die die Stärke der Synapsenverbindungen im Gehirn eines KI-Modells darstellen. Während das Modell trainiert wird, werden diese Zahlen kontinuierlich aktualisiert, wodurch bestimmt wird, wie wichtig bestimmte Informationen sind. Das eigentliche Fachwissen, das es dem Modell ermöglicht, eine Eingabe entgegenzunehmen und eine korrekte Ausgabe zu erzeugen, ist in diesen Werten gespeichert.

## So funktioniert es
Während das Modell mit Millionen von Daten trainiert wird, werden diese numerischen Werte bei jedem Fehler geringfügig angepasst. Wenn das Training abgeschlossen ist, werden diese Werte fixiert, und das Modell beantwortet nun neu eingehende Fragen anhand dieser optimierten Zahlen.

## Wo es eingesetzt wird
In den Dateien großer Sprachmodelle (LLMs), die heruntergeladen und auf dem Computer ausgeführt werden können – wie beispielsweise im GGUF-Format –, sind diese numerischen Daten direkt enthalten.

## Häufig verwechselt mit
Wird oft mit der Modellarchitektur verwechselt. Die Architektur ist wie der Grundriss der Räume eines leeren Gebäudes; die Gewichte hingegen sind die Möbel, die in diese Räume gestellt werden und das Gebäude bewohnbar machen.

## Häufige Fragen
**Können wir diese numerischen Werte manuell ändern?**
Theoretisch ist das möglich, aber da es Milliarden von Parametern gibt, zieht man es vor, dass Computer sie automatisch trainieren, anstatt dies manuell zu tun.

**Werden diese Werte bei Open-Source-Modellen geteilt?**
Ja, bei Modellen mit offenen Gewichten (Open Weights) werden diese numerischen Werte öffentlich zur Verfügung gestellt, damit jeder sie herunterladen und nutzen kann.


## Verwandte Begriffe
- [Open Weights](/de/dictionary/open-weights/)
- [LLM](/de/dictionary/llm/)
- [Fine-tuning](/de/dictionary/fine-tuning/)
- [GGUF](/de/dictionary/gguf/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/weights/
