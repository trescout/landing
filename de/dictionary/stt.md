# Was ist STT?

*Glossar · AI · Zuletzt aktualisiert: 19. September 2026*

> Speech-to-Text

STT (Speech-to-Text) ist eine künstliche Intelligenz und Signalverarbeitungstechnologie, die menschliche Sprache in analogen oder digitalen Schallwellen analysiert und sie mit hoher Genauigkeit in geschriebenen Text umwandelt.

## Begrifflicher Ursprung, Etymologie und historische Entwicklung

STT steht für die Anfangsbuchstaben des englischen Begriffs Speech-to-Text. Im Türkischen wird es als Konuşmadan Metne, Ses Tanıma oder Ses Transkripsiyonu verwendet.

Die Geschichte der Spracherkennungsforschung ist eines der anspruchsvollsten Probleme der Informatik:

- 1952 (Audrey-System): Das in den Bell Laboratories entwickelte erste System konnte ausschließlich die von einem einzigen Sprecher ausgesprochenen Ziffern von 0 bis 9 erkennen.
- 1970er – 1990er Jahre (Statistische Modelle & HMM): Mit Hidden Markov Models (HMM) und n-Gramm-Sprachmodellen begannen Schallwellen in Phoneme (kleinste Lauteinheiten) unterteilt und analysiert zu werden. Die Genauigkeitsrate war in lauten Umgebungen und bei verschiedenen Akzenten jedoch recht gering.
- 2010er (Deep Learning & Hybride Modelle): Tiefe neuronale Netze (DNN, CNN, RNN) wurden mit HMM kombiniert, was zur Geburtsstunde von Sprachassistenten in Smartphones (Siri, Google Assistant) führte.
- 2020er (End-to-End-Transformer-Revolution): End-to-End-Architekturen, die rohe Schallwellen direkt in Spektrogramme und anschließend in Text umwandeln (OpenAI Whisper, Google Chirp, Conformer), betraten die Bühne. Diese Modelle, die mit Hunderttausenden Stunden an mehrsprachigen Daten trainiert wurden, können selbst Flüstern, starke Akzente und laute Umgebungen fehlerfrei transkribieren.

***Analogie:** STT ist wie ein perfekter Chefsekretär, der neben Ihnen sitzt, während Sie in einem Konferenzsaal sprechen, und jedes Ihrer Wörter, jede Atempause und Tonhöhenänderung mit der Geschwindigkeit des Lichts auf einer Stenografiemaschine fehlerfrei aufzeichnet; zudem erkennt er die gesprochene Sprache sofort und wendet die Grammatikregeln automatisch an.*

## Akustische Modellierung und Funktionsarchitektur

Eine moderne STT-Engine durchläuft die folgenden Schichten, während sie analoge Schallwellen in digitalen Text umwandelt:

1. Audio-Vorverarbeitung und Spektrogramm-Transformation: Das rohe Audiosignal (im PCM-Format) wird mittels Kurzzeit-Fourier-Transformation (STFT · Short-Time Fourier Transform) analysiert. Es wird in Log-Mel-Spektrogramme umgewandelt, die der Frequenzwahrnehmung des menschlichen Ohrs entsprechen. Dieser Prozess verwandelt den Ton in eine visuelle Frequenzkarte.
2. Audio-Encoder: Das Spektrogramm wird in ein Transformer-basiertes tiefes neuronales Netz eingespeist. Das Modell filtert das Rauschen in den Schallwellen heraus und ermittelt, welchem Phonem oder welcher akustischen Repräsentation (im latenten Raum / latent space) jedes 20 bis 30 Millisekunden lange Sprach- bzw. Audiosegment entspricht.
3. Autoregressive Decoder (Sprachdecoder und Kontextvorhersage): Die Signale des akustischen Modells werden mit dem trainierten Sprachmodell kombiniert. In phonetisch reichen Sprachen wie Türkisch werden homophone Wörter (Homophone; zum Beispiel die Zahl "yüz" und das Verb "yüz") anhand des Satzkontexts korrekt erkannt.
4. Interpunktion und Formatierung: Dem Rohtext werden Groß- und Kleinschreibung, Kommas, Punkte und Fragezeichen hinzugefügt, und Zahlenausdrücke („fünfzehn“ → „15“) werden in das Textformat konvertiert.

**Leistungsmetrik (WER · Word Error Rate):** Die Genauigkeit eines STT-Modells wird anhand der Wortfehlerrate (Word Error Rate – WER) gemessen. Die Formel lautet WER = (S + D + I) / N (S: Substitution, D: Löschung, I: Insertion, N: Gesamtzahl der Wörter). Bei modernen Modellen ist die englische WER auf 3–5 % und bei agglutinierenden Sprachen wie Türkisch auf 7–10 % gesunken.

## Anwendungsbereiche und Open-Source-Ökosystem

- Meeting- und Notizassistenten: Echtzeit-Transkription und Zusammenfassung von Zoom-, Google Meet- oder Teams-Besprechungen (Otter.ai, Fireflies).
- Untertitelung und Übersetzung: Automatische Erstellung zeitgestempelter (timestamp) Untertitel im .srt- und .vtt-Format für Video- und Podcast-Inhalte.
- Gesundheit und Recht: Ärzte können ihre klinischen Untersuchungsnotizen oder Sitzungsprotokolle freihändig diktieren.
- Open-Source-Spitzenreiter (Whisper & Whisper.cpp): Das Open-Source-Modell Whisper von OpenAI und die von Georgi Gerganov vollständig in C/C++ optimierte Bibliothek whisper.cpp bieten die Möglichkeit, STT (Speech-to-Text) lokal auf eigener Hardware (Mac M-Serie, Raspberry Pi, Consumer-GPUs) und unter Wahrung der vollständigen Privatsphäre ohne Serverabhängigkeit auszuführen.

## Häufige Fragen

**Was bedeutet STT und wofür steht die Abkürzung?**

STT ist die Abkürzung für „Speech-to-Text“ (Sprache zu Text). Es handelt sich dabei um eine Technologie der künstlichen Intelligenz, die Audiosignale analysiert, Wörter entschlüsselt und sie in ein Textformat umwandelt.

**Was ist der Unterschied zwischen STT und Spracherkennung (Voice Recognition)?**

Spracherkennung (Voice Recognition / Speaker Identification) konzentriert sich darauf, festzustellen, wer spricht (biometrische Identität). STT hingegen transkribiert den Inhalt der gesprochenen Wörter unabhängig von der Identität des Sprechers.

**Verstehen STT-Modelle türkische Laute korrekt?**

Whisper und moderne modelle auf Conformer-Basis wurden mit umfangreichen türkischen Audiodatensätzen trainiert; sie sind in der Lage, Transkriptionen und Zeichensetzungen im phonetisch reichen Türkisch mit hoher Genauigkeit durchzuführen.

**Ist es möglich, STT lokal (Local) auszuführen?**

Ja; dank optimierter Engines wie whisper.cpp oder faster-whisper können Sie Ihre Audiodaten offline auf Ihrem eigenen Computer und mit vollständigem Datenschutz ausführen, ohne sie an einen Cloud-Server zu senden.

## Verwandte Begriffe

- [Speech-to-Text](https://trescout.com/de/dictionary/speech-to-text/)
- [Speech-to-Speech](https://trescout.com/de/dictionary/speech-to-speech/)
- [Voice Cloning](https://trescout.com/de/dictionary/voice-cloning/)
- [Whisper](https://trescout.com/de/dictionary/whisper/)
- [Tokenizer](https://trescout.com/de/dictionary/tokenizer/)
- [Apple Silicon](https://trescout.com/de/dictionary/apple-silicon/)

## Verwandte Werkzeuge

- [Agents](https://trescout.com/de/discover/agents/)
- [Speech to Speech](https://trescout.com/de/discover/speech-to-speech/)
- [Transcribe.cpp](https://trescout.com/de/discover/transcribe-cpp/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/stt/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/stt/
