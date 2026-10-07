# Was ist Speech-to-Speech?

Speech-to-Speech (S2S / KI-gestützte Sprache-zu-Sprache) ist eine End-to-End-Deep-Learning-Technologie, die Schallwellen direkt von der Quelle zum Ziel analysiert, ohne sie in eine Zwischendisposition aus Text umzuwandeln, und dabei ein neues Audiosignal erzeugt.

## Von der traditionellen Kaskadenarchitektur zur End-to-End-Architektur
Traditionelle Sprachübersetzungs- und Dialogsysteme bestanden aus drei unabhängigen Phasen, die als „Kaskade“ (Cascade) bezeichnet werden:

## Technische Infrastruktur: Audiotokenisierung und kontinuierlicher latenter Raum
Die grundlegenden工程schritte (Engineering-Schritte) hinter Speech-to-Speech-Systemen sind folgende:

## Anwendungsbereiche und Blick in die Zukunft

## Häufige Fragen
**Was bedeutet Speech-to-Speech und wie funktioniert es?**
Speech-to-Speech (Scheide von Sprache zu Sprache) ist ein End-to-End-KI-Modell, das die Notwendigkeit der Umwandlung von Sprache in Text überflüssig macht, indem es Schallwellen direkt analysiert und wieder als Ton ausgibt.

**Was ist der Unterschied zur herkömmlichen STT-TTS-Kaskade?**
Kaskadensysteme wandeln Sprache zuerst in Text und dann wieder in Sprache um; dies führt zu sekundenlangen Verzögerungen sowie zum Verlust von Emotionen und Betonungen. S2S hingegen arbeitet mit einer sofortigen Verzögerung von 200-300 ms und bewahrt den Stimmcharakter des Sprechers.

**Kann man im S2S-System während des Sprechens unterbrechen (Interruption)?**
Ja; dank des Vollduplex-Audio-Streamings (Full-Duplex) kann das Modell die Sprachgenerierung sofort stoppen und in den Zuhörmodus wechseln, wenn der Benutzer unterbricht.

**Welche Sicherheitsrisiken gibt es bei der Sprach-zu-Sprach-Übersetzung?**
Realistische Stimmklonungstechnologie birgt das Risiko von Identitätsdiebstahl und Betrug. Aus diesem Grund werden in modernen S2S-Systemen kryptografische Wasserzeichen (Audio Watermarking), die für das menschliche Ohr nicht hörbar sind, in die synthetisierte Stimme eingebettet.


## Verwandte Begriffe
- [STT](/de/dictionary/stt/)
- [Speech-to-Text](/de/dictionary/speech-to-text/)
- [Voice Cloning](/de/dictionary/voice-cloning/)
- [Whisper](/de/dictionary/whisper/)
- [Tokenizer](/de/dictionary/tokenizer/)
- [Apple Silicon](/de/dictionary/apple-silicon/)

## Verwandte Werkzeuge
- [Speech to Speech](/de/discover/speech-to-speech/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/speech-to-speech/
