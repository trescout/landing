# Was ist Tokenizer?

*Glossar · AI · Zuletzt aktualisiert: 19. September 2026*

Ein Tokenizer ist eine grundlegende Datenverarbeitungskomponente, die Texte in natürlicher Sprache in numerische Token (Token-IDs) umwandelt, die von großen Sprachmodellen (LLMs) und neuronalen Netzen mathematisch verarbeitet werden können.

## 1. Definition und das grundlegende Problem: Warum nicht direkt Wörter?

Große Sprachmodelle (GPT-4, Claude, Llama usw.) lesen Texte nicht wie Menschen Buchstabe für Buchstabe oder Wort für Wort. Neuronale Netze können nur mit Matrizen, Tensoren und Zahlen arbeiten. Daher muss der Text zuerst in Zahlen umgewandelt werden.

Historisch gesehen wurden in der natürlichen Sprachverarbeitung (NLP) drei verschiedene Ansätze erprobt:

1. Zeichenbasierte Verarbeitung: Der Text wird in einzelne Buchstaben unterteilt (k, i, t, a, p). Die Vokabulargröße ist sehr klein (einige hundert Zeichen), aber die Sätze werden sehr lang. Da die Rechenkomplexität des Aufmerksamkeitsmechanismus (Self-Attention) in der Transformer-Architektur quadratisch mit der Sequenzlänge (O(N²)) zunimmt, erschöpft sich der Speicher des Modells schnell.
2. Wortbasierte Verarbeitung: Jedes Wort wird als eigenständige Einheit betrachtet. In diesem Fall steigt die Anzahl der Einträge im Vokabular jedoch aufgrund jedes Flexionssuffixes, jedes Tippfehlers und jedes neuen Wortes in die Millionen; jedes Wort, das nicht im Vokabular enthalten ist, wird als "unbekannt" (\<unk> - Out of Vocabulary) markiert, wodurch das Modell die Bedeutung verliert.
3. Subword-Lösung: Der heutige moderne Standard. Häufig verwendete Wörter werden als ein einziges Stück ("Buch") behandelt, während seltene oder abgeleitete Wörter in sinnvolle Wortstämme und Endungen ("Buch" + "halter" + "ei") unterteilt werden. Auf diese Weise lässt sich mit einer festen Vokabulargröße zwischen 32.000 und 128.000 eine unendliche Anzahl von Wörtern darstellen.

***Analogie:** Ein Tokenizer ist eine Sortiermaschine, die statt hunderttausende verschiedene Bücher, die in eine Bibliothek gelangen, einzeln in Buchstaben zu zerlegen, spezielle Barcodes für die am häufigsten verwendeten Silben und Wortstämme druckt. Wenn das Modell den Text liest, sieht es nicht direkt die Buchstaben, sondern speichert die Barcodenummern, die es für jedes Fragment eingelesen hat, in seinem Speicher.*

## 2. Tokenizer-Algorithmen und ihre mathematische Logik

Die wichtigsten Tokenizer-Algorithmen, die das Herzstück moderner Sprachmodelle bilden, sind:

- Byte Pair Encoding (BPE): Ursprünglich ein Datenkomprimierungsalgorithmus, bildet BPE heute die Grundlage der GPT-Serie und der Llama-Modelle. Es beginnt mit allen grundlegenden Zeichen im Text und kombiniert iterativ die am häufigsten aufeinanderfolgenden Zeichenpaare im Korpus, um sie dem Vokabular hinzuzufügen.
- WordPiece: Diese von Google im BERT-Modell populär gemachte Methode basiert auf Wahrscheinlichkeiten statt auf Häufigkeiten. Beim Zusammenführen von Paaren werden diejenigen Unterwort-Fragmente ausgewählt, die den Likelihood-Score des Sprachmodells auf den Trainingsdaten am stärksten erhöhen.
- SentencePiece und Byte-Fallback: Behandelt Leerzeichen ebenfalls als spezielles Unterzeichen und betrachtet den Text als rohen Byte-Stream. Bei Auftreten seltener Unicode-Zeichen, die nicht im Vokabular enthalten sind, wird direkt auf das UTF-8-Byte (Byte-Fallback) zurückgegriffen, wodurch der \<unk>-Fehler auf null reduziert wird.

## 3. Die "Tokenizer-Steuer" (The Tokenizer Tax) im Türkischen

Mehr als 85 % der Trainingsdaten großer Sprachmodelle sind auf Englisch. Dies führt dazu, dass das Tokenizer-Vokabular überwiegend mit englischen Stämmen und Wörtern gefüllt ist.

In morphologisch reichen Sprachen mit vielen Anhängen wie Türkisch führt dies zu erheblichen Kosten und einer Ungleichheit im Kontext:

- Der Satz „Artificial intelligence is transforming software engineering.“ umfasst etwa 7 Token.
- Türkisch: „Künstliche Intelligenz verändert die Softwareentwicklung.“ Der Satz kann aufgrund der Fragmentierung der Anhänge 14–16 Token verbrauchen.

Aus diesem Grund können türkischsprachige Nutzer weniger Dokumente in dasselbe Kontextfenster einfügen und zahlen doppelt so hohe Gebühren für API-Dienste. Mit Llama 3 und GPT-4o hat die Erhöhung der Vokabulargröße auf über 128k die Token-Effizienz für Türkisch deutlich verbessert.

## 4. Sicherheit und Grenzfälle: Glitch Tokens

Spezielle Token, die im Tokenizer-Wörterbuch erscheinen, während des Vortrainings des Modells jedoch selten oder in bedeutungslosen Kontexten im Textkörper auftauchen, werden als „Glitch-Token“ bezeichnet.

Wenn das Modell beispielsweise nach Token wie SolidGoldMagikarp gefragt wird, die von Benutzernamen in Reddit-Foren oder Codes auf E-Commerce-Websites abgeleitet werden; Da die künstliche Intelligenz den Vektor dieses Tokens nicht richtig im Einbettungsraum positionieren kann, beginnt sie zu halluzinieren, kann bedeutungslose Flüche von sich geben oder sich verriegeln.

## Häufige Fragen

**Was bedeutet Tokenizer und was ist die deutsche Entsprechung?**

Im Deutschen wird er als „Tokenisierer“ bezeichnet. Es ist eine Software, die natürlichsprachliche Texte in die kleinsten numerischen Indizes (Token) zerlegt, die das Modell der künstlichen Intelligenz verstehen kann.

**Wie vielen Wörtern oder Buchstaben entspricht 1 Token?**

In englischen Texten entspricht 1 Token durchschnittlich 4 Zeichen oder 0,75 Wörtern (100 Wörter entsprechen etwa 130 Token). In agglutinierenden Sprachen wie Türkisch kann 1 Wort aufgrund der Zerlegung der Suffixe durchschnittlich 2 bis 3 Token umfassen.

**Wie funktioniert BPE (Byte Pair Encoding)?**

Es ist ein statistischer Algorithmus, der mit den grundlegendsten Zeichen beginnt und schrittweise die am häufigsten nebeneinander vorkommenden Zeichenpaare im Trainingsdatensatz kombiniert, um ein Unterwort-Vokabular fester Größe aufzubauen.

**Sind Tokenizer-freie Modelle möglich?**

Ja; die in letzter Zeit entwickelten neuronalen Netzwerkarchitekturen der neuen Generation wie MambaByte und MegaByte zielen darauf ab, die Tokenizer-Schicht vollständig zu entfernen und direkt auf Roh-Bytes zu arbeiten, um sprachliche Ungleichheiten zu beseitigen.

## Verwandte Begriffe

- [Token](https://trescout.com/de/dictionary/token/)
- [NLP](https://trescout.com/de/dictionary/nlp/)
- [Tokenizer-free](https://trescout.com/de/dictionary/tokenizer-free/)
- [Prompt Engineering](https://trescout.com/de/dictionary/prompt-engineering/)
- [Context](https://trescout.com/de/dictionary/context/)

## Verwandte Werkzeuge

- [AI Engineering from Scratch](https://trescout.com/de/discover/ai-engineering-from-scratch/)
- [Minimind](https://trescout.com/de/discover/minimind/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/tokenizer/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/tokenizer/
