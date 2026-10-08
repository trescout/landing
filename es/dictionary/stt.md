# ¿Qué es STT?

*Glosario · AI · Última actualización: 19 de septiembre de 2026*

> Speech-to-Text

STT (Speech-to-Text) es una tecnología de procesamiento de señales e inteligencia artificial que analiza el habla humana en ondas sonoras analógicas o digitales y las convierte en texto escrito con alta precisión.

## Origen conceptual, etimología y desarrollo histórico

STT consta de las iniciales de la expresión inglesa Speech-to-Text. En turco, se utiliza como "voz a texto", "reconocimiento de voz" o "transcripción de voz".

La historia de la investigación del reconocimiento de voz es uno de los problemas más desafiantes de la informática:

- 1952 (Sistema Audrey): El primer sistema desarrollado en los Laboratorios Bell sólo podía reconocer los números del 0 al 9 pronunciados por un solo hablante.
- Décadas de 1970 - Década de 1990 (Modelos estadísticos y HMM): Las ondas sonoras comenzaron a analizarse dividiéndolas en fonemas (las unidades de sonido más pequeñas) con Modelos Ocultos de Markov (HMM) y modelos de lenguaje de n-gramas. Sin embargo, la tasa de precisión fue bastante baja en entornos ruidosos y con diferentes acentos.
- Década de 2010 (aprendizaje profundo y modelos híbridos): las redes neuronales profundas (DNN, CNN, RNN) se combinaron con HMM, dando lugar a asistentes de voz (Siri, Google Assistant) en los teléfonos inteligentes.
- Década de 2020 (revolución de los transformadores de extremo a extremo): han aparecido en escena arquitecturas de extremo a extremo (OpenAI Whisper, Google Chirp, Conformer) que convierten ondas de sonido sin procesar directamente en espectrograma y luego en texto. Estos modelos, entrenados con cientos de miles de horas de datos multilingües, pueden transcribir con precisión susurros, acentos fuertes y entornos ruidosos.

***Analogía:** STT es la persona que se sienta a tu lado mientras hablas en una sala de conferencias, registrando cada palabra, pausa y entonación con precisión con una máquina de escribir taquigráfica ultrarrápida; Además, es como un perfecto mecanógrafo jefe que reconoce instantáneamente el idioma que usted habla y aplica automáticamente las reglas ortográficas.*

## Modelado acústico y estudio de arquitectura.

Un motor STT moderno pasa por las siguientes capas al convertir ondas de sonido analógicas en texto digital:

1. Preprocesamiento de audio y transformación de espectrograma: la señal de audio sin procesar (en formato PCM) se analiza con transformada de Fourier de corto tiempo (STFT · Transformada de Fourier de corto tiempo). Se convierte en espectrogramas Log-Mel adecuados para la percepción de frecuencia del oído humano. Este proceso convierte el sonido en un mapa de frecuencia visual.
2. Codificador acústico: el espectrograma se envía a la red neuronal profunda basada en Transformer. Al filtrar el ruido en las ondas sonoras, el modelo extrae a qué fonema o representación acústica corresponde cada segmento de sonido de 20 a 30 milisegundos (en el espacio latente).
3. Codificador de lenguaje y predicción de contexto (decodificador autorregresivo): las señales del modelo acústico se combinan con el modelo de lenguaje entrenado. En lenguas ricas en pronunciación como el turco, los homófonos (homófonos; por ejemplo, el número "cien" y el verbo "cien") se detectan correctamente según el contexto de la frase.
4. Puntuación y formato: se agregan mayúsculas, comas, puntos, signos de interrogación al texto sin formato y las expresiones numéricas ("quince" → "15") se convierten al formato de texto.

**Medición del rendimiento (WER · Tasa de error de palabras):** La precisión de un modelo STT se mide mediante la métrica de tasa de error de palabras (WER). Su fórmula es WER = (S+D+I)/N (S: sustitución, D: eliminación, I: inserción, N: total de palabras). En los modelos modernos, la tasa WER en inglés ha disminuido al 3-5%, y en idiomas aglutinantes como el turco, ha disminuido al 7-10%.

## Áreas de uso y ecosistema de código abierto

- Asistentes para reuniones y toma de notas: transcripción y resumen en tiempo real de conversaciones de Zoom, Google Meet o Teams (Otter.ai, Fireflies).
- Subtítulos y traducción: Generación automática de subtítulos para contenido de video y podcast en formato de marca de tiempo .srt y .vtt.
- Salud y Derecho: Médicos dictando notas de exámenes clínicos o escuchando actas sin utilizar las manos.
- Líder de código abierto (Whisper & Whisper.cpp): el modelo Whisper de código abierto de OpenAI y la biblioteca susurro.cpp de Georgi Gerganov, totalmente optimizadas en C/C++, ofrecen la capacidad de ejecutar STT con total privacidad en hardware nativo (Mac serie M, Raspberry Pi, GPU de consumo) sin depender del servidor.

## Preguntas frecuentes

**¿Qué significa STT y qué significa?**

STT es una abreviatura de "Speech-to-Text". Es una tecnología de inteligencia artificial que analiza señales de sonido, decodifica palabras y las convierte a formato de texto.

**¿Cuál es la diferencia entre STT y reconocimiento de voz?**

El reconocimiento de voz (Speaker Identification) se centra en detectar quién es el hablante (identidad biométrica). STT, por otro lado, transcribe el contenido de las palabras habladas independientemente de la identidad del hablante.

**¿Los modelos STT entienden correctamente los sonidos turcos?**

Los modelos de última generación basados ​​en Whisper y Conformer se entrenan en grandes conjuntos de datos de voz turcos; Puede realizar transcripciones y puntuaciones con gran precisión en turco fonéticamente rico.

**¿Es posible ejecutar STT local?**

Sí; Gracias a motores optimizados como susurro.cpp o más rápido-whisper, puedes ejecutar tus datos de voz sin conexión y con total privacidad en tu propia computadora, sin enviarlos a ningún servidor en la nube.

## Términos relacionados

- [Speech-to-Text](https://trescout.com/es/dictionary/speech-to-text/)
- [Speech-to-Speech](https://trescout.com/es/dictionary/speech-to-speech/)
- [Voice Cloning](https://trescout.com/es/dictionary/voice-cloning/)
- [Whisper](https://trescout.com/es/dictionary/whisper/)
- [Tokenizer](https://trescout.com/es/dictionary/tokenizer/)
- [Apple Silicon](https://trescout.com/es/dictionary/apple-silicon/)

## Herramientas relacionadas

- [Agents](https://trescout.com/es/discover/agents/)
- [Speech to Speech](https://trescout.com/es/discover/speech-to-speech/)
- [Transcribe.cpp](https://trescout.com/es/discover/transcribe-cpp/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/stt/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/stt/
