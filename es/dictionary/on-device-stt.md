# ¿Qué es el On-device STT?

> Reconocimiento de Voz en el Dispositivo

**Categoría:** AI  
**Última actualización:** 2026-09-22

El on-device STT (Speech-to-Text en el dispositivo) es la tecnología de reconocimiento acústico que transcribe la voz a texto de manera local en el procesador del usuario, sin enviar archivos de audio a servidores externos.

## Definición y etimología
Diseñado para satisfacer exigencias estrictas de privacidad y latencia imperceptible, el STT local ejecuta modelos neuronales en aceleradores de hardware (NPU/GPU). La voz capturada por el micrófono se procesa y descarta en la memoria volátil del equipo.

## Contexto cotidiano e uso práctico
- **Teléfonos y tabletas:** Dictado de mensajes y notas de voz en modo avión o zonas de escasa cobertura.
- **Ámbito Médico y Legal:** Transcripción confidencial de historias clínicas y declaraciones notariales.
- **Domótica Autónoma:** Control de electrodomésticos por voz sin enviar las conversaciones familiares a la nube.

## Profundidad técnica y arquitectura
Estructura de Ingeniería:- **Redes Neuronales Cuantizadas:** Modelos optimizados (Whisper.cpp, Sherpa-ONNX) comprimidos a 4 y 8 bits (INT4/INT8).
- **Aceleración por NPU:** Ejecución directa en módulos neuronales integrados para no agotar la batería del dispositivo.
- **Detección de Actividad de Voz (VAD):** Filtros inteligentes (Silero VAD) que aíslan la voz del ruido de fondo previo a la transcripción.

## Suele confundirse con
Suele confundirse con las API de voz en la nube. Las plataformas cloud procesan el audio en centros remotos; el STT local realiza todo el cálculo dentro del procesador del propio teléfono u ordenador.

## Perspectivas interdisciplinares
- **Traducción:** Contar con un traductor presencial en la habitación frente a llamar a una centralita remota por teléfono.
- **Registro:** Un taquígrafo tomando actas en sala frente a enviar grabaciones por mensajería postal.
- **Revelado:** Disponer de un cuarto oscuro fotográfico propio frente a mandar los carretes a un laboratorio ajeno.

## Por analogía
Es igual que tener a un intérprete profesional sentado a su lado en la misma estancia: escucha lo que dice y lo anota de inmediato sin cables ni intermediarios.

## Preguntas frecuentes

**¿Ofrece la misma precisión que los servicios en la nube?**  
Sí, versiones destiladas recientes como Whisper-small compiten de tú a tú en tasa de error de palabras (WER).

**¿Requiere conexión a Internet para transcribir?**  
No, el procesamiento se ejecuta íntegramente en local con el dispositivo desconectado.

**¿Cuánto espacio de disco ocupa un modelo típico?**  
Los modelos cuantizados para producción suelen ocupar entre 45 MB y 300 MB.

**¿Qué proyectos de código abierto permiten implementarlo?**  
Whisper.cpp, Vosk, Sherpa-ONNX y WhisperX.

## Términos relacionados
- [Speech-to-Text](/es/dictionary/speech-to-text/)
- [SLM](/es/dictionary/slm/)
- [Privacidad Digital](/es/dictionary/digital-privacy/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/on-device-stt/
