# ¿Qué es Speaker Diarization?

La diarización de hablantes (Speaker Diarization) es una tecnología de inteligencia artificial que analiza las ondas sonoras en una grabación de audio con múltiples participantes para responder a la pregunta "¿quién habló y cuándo?", etiquetando los segmentos de voz según la identidad de los hablantes.

## Definición y origen del concepto (Definición de Diarización)
La diarización, cuyo origen etimológico proviene del verbo francés diariser (llevar un diario), es el proceso en ingeniería de audio que consiste en dividir un flujo de sonido en segmentos temporales para asignar cada fragmento a una identidad de hablante específica (por ejemplo, Hablante 1, Hablante 2). Independientemente del contenido de la conversación, realiza la distinción de identidad directamente a través del timbre biométrico y las características de frecuencia de la voz.

## ¿Cómo funciona? (Diarización paso a paso)
1. Detección de Actividad de Voz (VAD - Voice Activity Detection): Se eliminan la música, el ruido de fondo y las pausas de respiración en la grabación, extrayendo solo las secciones que contienen voz humana.

## ¿Dónde y en qué áreas se utiliza?
Asistentes de reuniones inteligentes: Herramientas de resumen con inteligencia artificial (Otter.ai, Meetily) que identifican quién tomó qué decisión o tarea en reuniones de Zoom, Google Meet o Teams.Centros de llamadas: Análisis de sentimiento y control de calidad mediante la separación de las conversaciones entre el cliente y el agente.Transcripción de podcasts y entrevistas: Creación automática de subtítulos profesionales y diferenciación de hablantes en contenidos de audio y video con múltiples participantes.Derecho y ciencia forense digital: Documentación de los cambios de hablante en registros judiciales e interrogatorios de seguridad.

## Suele confundirse con
La transcripción (STT) suele confundirse con la diarización de locutores. Un motor de conversión de voz a texto clásico solo transcribe "qué se dijo", pero no puede distinguir quién lo dijo. La diarización, por su parte, identifica "quién lo dijo". Por ejemplo, mientras que OpenAI Whisper realiza una transcripción pura, al combinarlo con herramientas como pyannote.audio o WhisperX, se obtienen tanto el texto como las identidades de los locutores de forma completa.

## Preguntas frecuentes
**¿Definición de diarización (qué significa diarización)?**
Es un proceso de inteligencia artificial que analiza las ondas sonoras en grabaciones de audio con múltiples participantes para distinguir quién habló y cuándo, etiquetando los cambios de hablante con marcas de tiempo.

**¿Puede el sistema encontrar los nombres reales de los hablantes por sí mismo?**
No, si no se ha proporcionado una muestra de voz previamente, el sistema distingue a los hablantes como Hablante 1, Hablante 2, etc.; los nombres deben ser asignados por el usuario o mediante un sistema de calendario integrado.

**¿Puede el modelo Whisper realizar diarización por sí solo?**
No, los modelos oficiales de Whisper solo realizan transcripción; para la separación de hablantes, se utilizan junto con modelos de diarización especializados como pyannote.audio.

**¿Cuál es la situación más difícil para los sistemas de diarización?**
Realizar una distinción precisa cuando varias personas hablan al mismo tiempo (habla superpuesta), cuando las palabras se mezclan o en entornos con eco.


## Términos relacionados
- [Transcription](/es/dictionary/transcription/)
- [Speech-to-Text](/es/dictionary/speech-to-text/)
- [NLP](/es/dictionary/nlp/)

## Herramientas relacionadas
- [Meetily](/es/discover/meetily/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/speaker-diarization/
