# ¿Qué es Speech-to-Speech?

Speech-to-Speech (S2S / IA de voz a voz) es una tecnología de aprendizaje profundo de extremo a extremo que analiza las ondas de sonido directamente desde la fuente hasta el destino, sin convertirlas en una capa de texto intermedia, y genera una nueva señal de audio.

## De la arquitectura en cascada tradicional a la arquitectura de extremo a extremo
Los sistemas tradicionales de traducción de voz y de diálogo constaban de tres etapas independientes llamadas "cascada":

## Infraestructura técnica: Tokenización de voz y espacio latente continuo
Los pasos fundamentales de ingeniería detrás de los sistemas de voz a voz son los siguientes:

## Casos de uso y visión de futuro

## Preguntas frecuentes
**¿Qué significa de voz a voz y cómo funciona?**
De voz a voz (Speech-to-Speech) es un modelo de inteligencia artificial de extremo a extremo que elimina la necesidad de convertir el habla en texto, analizando directamente la onda sonora y produciendo resultados nuevamente como voz.

**¿Cuál es la diferencia con la cascada STT-TTS tradicional?**
Los sistemas en cascada convierten primero la voz en texto y luego nuevamente en voz; esto provoca retrasos de varios segundos y pérdida de emoción/énfasis. Por otro lado, S2S funciona con un retraso instantáneo de 200-300 ms y preserva el carácter vocal del hablante.

**¿Se puede interrumpir al hablar en el sistema S2S (Interrupción)?**
Sí; gracias a la transmisión de audio full-duplex, el modelo puede detener instantáneamente la generación de voz y pasar al modo de escucha cuando el usuario interrumpe.

**¿Cuáles son los riesgos de seguridad en la traducción de voz a voz?**
La tecnología de clonación de voz realista conlleva el riesgo de usurpación de identidad y fraude. Por esta razón, en los sistemas S2S modernos, se integran marcas de agua criptográficas (audio watermarking) que el oído humano no puede percibir en la voz sintetizada.


## Términos relacionados
- [STT](/es/dictionary/stt/)
- [Speech-to-Text](/es/dictionary/speech-to-text/)
- [Voice Cloning](/es/dictionary/voice-cloning/)
- [Whisper](/es/dictionary/whisper/)
- [Tokenizer](/es/dictionary/tokenizer/)
- [Apple Silicon](/es/dictionary/apple-silicon/)

## Herramientas relacionadas
- [Speech to Speech](/es/discover/speech-to-speech/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/speech-to-speech/
