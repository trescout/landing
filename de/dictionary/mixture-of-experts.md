# Was ist Mixture of Experts?

> MoE

Es ist ein System, das komplexe Aufgaben löst, indem es sie in Teilbereiche unterteilt, die jeweils auf ein anderes Thema spezialisiert sind.

## Definition
In dieser Struktur antwortet nicht das gesamte Modell auf jede Frage, sondern nur die für die jeweilige Frage relevanten Bereiche (Experten) werden aktiviert. Dies ermöglicht es dem Modell, trotz seiner enormen Größe nur den notwendigen Teil zu nutzen. Das Ergebnis sind sowohl intelligentere als auch schnellere Antworten.

## So funktioniert es
Wenn eine Frage gestellt wird, bestimmt ein „Router“-Mechanismus, in welchen Fachbereich die Frage fällt. Nur diese Experten bearbeiten die Frage und generieren eine Antwort.

## Wo es eingesetzt wird
Es wird in den meisten modernen großen KI-Modellen verwendet, um die Effizienz zu steigern.

## Häufig verwechselt mit
Es könnte mit der Verarbeitung aller Daten durch ein einziges Modell verwechselt werden.

## Häufige Fragen
**Wie werden die Experten ausgewählt?**
Das Modell lernt während des Trainings, welche Experten in welchem Bereich besser sind.

**Verlangsamt diese Methode das Modell?**
Im Gegenteil, es ist schneller, da nur die relevanten Teile arbeiten.


## Verwandte Begriffe
- [LLM](/de/dictionary/llm/)
- [AI Models](/de/dictionary/ai-models/)
- [Inference](/de/dictionary/inference/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/mixture-of-experts/
