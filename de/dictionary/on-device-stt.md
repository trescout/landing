# Was ist On-device STT?

> Lokale Spracherkennung auf dem Endgerät

**Kategorie:** AI  
**Letzte Aktualisierung:** 2026-09-22

On-device STT (Speech-to-Text auf dem Gerät) bezeichnet Spracherkennungstechnologien, die gesprochenes Audio direkt auf der Hardware des Nutzers in Text umwandeln, ohne Tondateien an externe Cloud-Server zu senden.

## Definition und Wortherkunft
Vor dem Hintergrund strenger Datenschutzanforderungen und gewünschter Null-Latenz führt On-Device STT neuronale Akustikmodelle direkt auf lokalen NPUs und Grafikchips aus. Sprachaufnahmen verlassen das Endgerät zu keinem Zeitpunkt.

## Alltägliche Anwendung und Praxis
- **Smartphones und Tablets:** Zuverlässige Spracheingabe im Flugmodus ohne Internetempfang.
- **Vertrauliche Diktate:** Lokale Protokollierung von Patientengesprächen, Anwaltsnotizen und Vorstandsmeetings.
- **Smart-Home-Steuerung:** Sprachbediente Haushaltsgeräte, die lokale Befehle ausführen, ohne das Wohnzimmer abzuhören.

## Technische Tiefe und Architektur
Architektur und Inferenz-Stack:- **Quantisierte Akustikmodelle:** Kompakte neuronale Netze (Whisper.cpp, Vosk) mit 4-Bit- und 8-Bit-Quantisierung für minimale Ressourcennutzung.
- **NPU-Hardwarebeschleunigung:** Nutzung integrierter KI-Kerne (Apple Neural Engine, Qualcomm NPU) zur Schonung des Akkus.
- **Voice Activity Detection (VAD):** Energiesparende Vorstufen (Silero VAD), die Sprechpausen und Stille vor der Inferenz ausfiltern.

## Häufig verwechselt mit
Wird häufig mit Cloud-Sprach-APIs verwechselt. Cloud-Dienste leiten Audiodaten über das Internet an Rechenzentren weiter; On-Device STT löst die Inferenz vollständig autonom auf dem lokalen Chip.

## Interdisziplinäre Perspektiven
- **Dolmetschen:** Ein persönlicher Dolmetscher vor Ort im Raum vs. eine telefonische Übersetzungszentrale.
- **Protokollführung:** Ein Stenograf live im Gerichtssaal vs. der postalische Versand von Tonbändern an ein Schreibbüro.
- **Fotografie:** Eigene Dunkelkammer im Keller vs. das Einsenden von Filmen an ein Fotolabor.

## Als Analogie
Es gleicht einem persönlichen Übersetzer, der direkt neben Ihnen im Raum sitzt: Er hört zu und tippt den Text sofort mit, ohne dass Fremde am Telefon mithören.

## Häufige Fragen

**Ist die Erkennungsgenauigkeit vergleichbar mit Cloud-Diensten?**  
Ja, moderne quantisierte Modelle wie Whisper-small erreichen auf Standard-Datensätzen nahezu identische Fehlerraten.

**Funktioniert die Transkription vollständig offline?**  
Ja, sobald die Modellgewichte lokal gespeichert sind, wird keine Internetverbindung mehr benötigt.

**Wie viel Speicherplatz belegt ein solches Sprachmodell?**  
Je nach Komprimierung und Parameteranzahl bewegen sich kompakte Modelle zwischen 40 MB und 350 MB.

**Welche Open-Source-Engines treiben diese Entwicklung an?**  
Whisper.cpp, Sherpa-ONNX, Vosk und WhisperX.

## Verwandte Begriffe
- [Speech-to-Text](/de/dictionary/speech-to-text/)
- [SLM](/de/dictionary/slm/)
- [Digitale Privatsphäre](/de/dictionary/digital-privacy/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/on-device-stt/
