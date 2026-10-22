# Agentes de voz nativos de código aberto

A biblioteca de conversão de fala desenvolvida pela Hugging Face permite a criação de agentes de voz locais usando modelos de código aberto. Esta ferramenta baseada em Python permite que os desenvolvedores criem sistemas de interação por voz em tempo real que rodam no dispositivo.

- ★ 13.072
- Python
- GitHub Trending · 2026-07-29

## Atualizações

- **7 de setembro de 2026:** Estrelas 12,310 → 13,072, versão mais recente v1.0.0 (6 de setembro de 2026).
- **12 de agosto de 2026:** Estrelas 11,283 → 12,310, versão mais recente v0.2.12 (5 de agosto de 2026).
- **6 de agosto de 2026:** Estrelas 10,774 → 11,283, versão mais recente v0.2.12 (5 de agosto de 2026).
- **4 de agosto de 2026:** Estrelas 10,402 → 10,774, versão mais recente v0.2.11 (3 de agosto de 2026).

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

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero configurar meu próprio agente de voz local usando esta ferramenta. Quais são as etapas básicas que preciso seguir para criar um pipeline de áudio de baixa latência usando componentes VAD, STT, LLM e TTS? Com qual comando posso levantar o servidor e conectar-me a um cliente compatível com OpenAI Realtime?

Repositório: https://github.com/huggingface/speech-to-speech. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Voice Agents](https://trescout.com/pt/dictionary/voice-agents/)
- [Speech-to-Speech](https://trescout.com/pt/dictionary/speech-to-speech/)
- [STT](https://trescout.com/pt/dictionary/stt/)
- [LLM](https://trescout.com/pt/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a desenvolvedores que desejam desenvolver sistemas de interação de voz nativos e personalizáveis ​​em seu próprio hardware.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/huggingface/speech-to-speech)
- [Ler em turco →](https://trescout.com/discover/speech-to-speech/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-29: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/speech-to-speech/
