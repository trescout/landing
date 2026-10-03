# Was ist Speaker Diarization?

Speaker Diarization (Sprecher-Diarisierung oder Protokollierung) ist eine Technologie der künstlichen Intelligenz, die Schallwellen in einer Audioaufnahme mit mehreren Teilnehmern analysiert, um die Frage „Wer hat wann gesprochen?“ zu beantworten und Sprachsegmente den jeweiligen Sprecheridentitäten zuzuordnen.

## Definition und Ursprung des Begriffs (Diarization Definition)
Diarization, dessen etymologischer Ursprung auf das französische Verb „diariser“ (Tagebuch führen) zurückgeht, bezeichnet in der Tontechnik den Prozess, einen Audiostrom in zeitabhängige Segmente zu unterteilen und jeden Abschnitt einer bestimmten Sprecheridentität (z. B. Sprecher 1, Sprecher 2) zuzuordnen. Unabhängig vom Inhalt des Gesprochenen erfolgt die Identitätsunterscheidung direkt anhand der biometrischen Klangfarbe und der Frequenzmerkmale der Stimme.

## Wie funktioniert es? (Diarisierung Schritt für Schritt)
1. Spracherkennung (VAD - Voice Activity Detection): Musik, Hintergrundgeräusche und Atempausen in der Aufnahme werden herausgefiltert, sodass nur die Abschnitte übrig bleiben, die menschliche Sprache enthalten.

## Wo und in welchen Bereichen wird es eingesetzt?
Intelligente Meeting-Assistenten: KI-Zusammenfassungstools (Otter.ai, Meetily), die bei Zoom-, Google Meet- oder Teams-Meetings extrahieren, wer welche Entscheidung getroffen oder welche Aufgabe übernommen hat.Callcenter: Trennung der Gespräche zwischen Kunde und Mitarbeiter zur Durchführung von Stimmungsanalysen und Qualitätskontrollen.Podcast- und Interview-Transkription: Erstellung automatischer professioneller Untertitel und Sprecheridentifizierung bei Audio- und Videoinhalten mit mehreren Teilnehmern.Recht und Forensik: Dokumentation von Sprecherwechseln bei Gerichtsprotokollen und Sicherheitsbefragungen.

## Häufig verwechselt mit
Transcription (Speech-to-Text / STT) und Speaker Diarization werden häufig verwechselt. Eine klassische Speech-to-Text-Engine wandelt lediglich das Gesagte in Text um, kann jedoch nicht unterscheiden, wer spricht. Diarization hingegen identifiziert, „wer spricht“. Während beispielsweise OpenAI Whisper eine reine Transkription durchführt, lassen sich in Kombination mit Tools wie pyannote.audio oder WhisperX sowohl der Text als auch die Sprecheridentitäten vollständig erfassen.

## Häufige Fragen
**Definition von Diarisierung (Was bedeutet Diarisierung)?**
Es handelt sich um einen KI-Prozess, der bei Audioaufnahmen mit mehreren Teilnehmern die Schallwellen analysiert, um zu unterscheiden, wer wann gesprochen hat, und die Sprecherwechsel mit Zeitstempeln zu versehen.

**Kann das System die echten Namen der Sprecher selbst finden?**
Nein, wenn keine Stimmprobe vorab hinterlegt wurde, unterscheidet das System die Sprecher als Sprecher 1, Sprecher 2 usw.; die Namen müssen vom Benutzer oder durch ein integriertes Kalendersystem zugeordnet werden.

**Kann das Whisper-Modell alleine eine Diarisierung durchführen?**
Nein, die offiziellen Whisper-Modelle führen nur Transkriptionen durch; für die Sprecherunterscheidung werden sie zusammen mit speziellen Diarisierungsmodellen wie pyannote.audio verwendet.

**Was ist die größte Herausforderung für Diarisierungssysteme?**
Die korrekte Unterscheidung in Situationen, in denen mehrere Personen gleichzeitig sprechen (überlappende Sprache), sich die Worte vermischen oder in Umgebungen mit starkem Nachhall.


## Verwandte Begriffe
- [Transcription](/de/dictionary/transcription/)
- [Speech-to-Text](/de/dictionary/speech-to-text/)
- [NLP](/de/dictionary/nlp/)

## Verwandte Werkzeuge
- [Meetily](/de/discover/meetily/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/speaker-diarization/
