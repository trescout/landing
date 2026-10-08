# Agentes de voz nativos de código abierto

La biblioteca de voz a voz desarrollada por Hugging Face permite crear agentes de voz locales utilizando modelos de código abierto. Esta herramienta basada en Python permite a los desarrolladores crear sistemas de interacción de voz en tiempo real que se ejecutan en el dispositivo.

- ★ 13.072
- Python
- GitHub Trending · 2026-07-29

## Actualizaciones

- **7 de septiembre de 2026:** Estrellas 12,310 → 13,072, última versión v1.0.0 (6 de septiembre de 2026).
- **12 de agosto de 2026:** Estrellas 11,283 → 12,310, última versión v0.2.12 (5 de agosto de 2026).
- **6 de agosto de 2026:** Estrellas 10,774 → 11,283, última versión v0.2.12 (5 de agosto de 2026).
- **4 de agosto de 2026:** Estrellas 10,402 → 10,774, última versión v0.2.11 (3 de agosto de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero configurar mi propio agente de voz local usando esta herramienta. ¿Cuáles son los pasos básicos que debo seguir para crear una canalización de audio de baja latencia utilizando componentes VAD, STT, LLM y TTS? ¿Con qué comando puedo poner en marcha el servidor y conectarme con un cliente compatible con OpenAI Realtime?

## Términos relacionados del glosario

- [Voice Agents](https://trescout.com/es/dictionary/voice-agents/)
- [Speech-to-Speech](https://trescout.com/es/dictionary/speech-to-speech/)
- [STT](https://trescout.com/es/dictionary/stt/)
- [LLM](https://trescout.com/es/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores que desean desarrollar sistemas de interacción de voz nativos y personalizables en su propio hardware.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/huggingface/speech-to-speech)
- [Leer en turco →](https://trescout.com/discover/speech-to-speech/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-29: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/speech-to-speech/
