# Agentes de voz nativos de código abierto

La biblioteca de voz a voz desarrollada por Hugging Face permite crear agentes de voz locales utilizando modelos de código abierto. Esta herramienta basada en Python permite a los desarrolladores crear sistemas de interacción de voz en tiempo real que se ejecutan en el dispositivo.

- ★ 12.310
- Python
- GitHub Trending · 2026-07-29

## Actualizar
- 12 de agosto de 2026: Star 11,283 → 12,310, última versión v0.2.12 (5 de agosto de 2026).
- 6 de agosto de 2026: Star 10,774 → 11,283, última versión v0.2.12 (5 de agosto de 2026).
- 4 de agosto de 2026: Star 10,402 → 10,774, última versión v0.2.11 (3 de agosto de 2026).
- 2 de agosto de 2026: Star 7,443 → 10,402, última versión v0.2.10 (11 de junio de 2026).

## Qué aporta
- Línea de audio modular de baja latencia
- Compatibilidad con WebSocket compatible con OpenAI Realtime
- Oportunidad de trabajar localmente en hardware diferente.

## Instalación
**Configuración básica**

```
pip install speech-to-speech
```

**Instalación desde el código fuente**

```
git clone https://github.com/huggingface/speech-to-speech.git
cd speech-to-speech
uv sync
```


## Ejecución
**Iniciando el servidor**

```
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech
```

**Conectando con el cliente**

```
python scripts/listen_and_play_realtime.py --host 127.0.0.1 --port 8765
```


## Si no programa
Quiero configurar mi propio agente de voz local usando esta herramienta. ¿Cuáles son los pasos básicos que debo seguir para crear una canalización de audio de baja latencia utilizando componentes VAD, STT, LLM y TTS? ¿Con qué comando puedo poner en marcha el servidor y conectarme con un cliente compatible con OpenAI Realtime?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/speech-to-speech/
