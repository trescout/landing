# Agentes de voz nativos de código aberto

A biblioteca de conversão de fala desenvolvida pela Hugging Face permite a criação de agentes de voz locais usando modelos de código aberto. Esta ferramenta baseada em Python permite que os desenvolvedores criem sistemas de interação por voz em tempo real que rodam no dispositivo.

- ★ 12.310
- Python
- GitHub Trending · 2026-07-29

## O que você ganha
- Linha de áudio modular de baixa latência
- Suporte WebSocket compatível com OpenAI Realtime
- Oportunidade de trabalhar localmente em diferentes hardwares

## Instalação
**Configuração básica**

```
pip install speech-to-speech
```

**Instalação a partir do código-fonte**

```
git clone https://github.com/huggingface/speech-to-speech.git
cd speech-to-speech
uv sync
```


## Execução
**Iniciando o servidor**

```
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech
```

**Conectando-se com o cliente**

```
python scripts/listen_and_play_realtime.py --host 127.0.0.1 --port 8765
```


## Se você não programa
Quero configurar meu próprio agente de voz local usando esta ferramenta. Quais são as etapas básicas que preciso seguir para criar um pipeline de áudio de baixa latência usando componentes VAD, STT, LLM e TTS? Com qual comando posso levantar o servidor e conectar-me a um cliente compatível com OpenAI Realtime?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/speech-to-speech/
