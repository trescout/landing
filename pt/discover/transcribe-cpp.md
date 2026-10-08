# Conversão rápida de fala em sistemas locais

Transcribe.cpp é uma biblioteca de inferência de fala para texto desenvolvida em C++ que oferece suporte a mais de 16 famílias de modelos. Usando a infraestrutura ggml, esta ferramenta permite que diferentes modelos de processamento de áudio sejam executados com eficiência em sistemas locais.

- ★ 1.982
- C++
- GitHub Trending · 2026-07-21

## Atualizações

- **4 de outubro de 2026:** Estrelas 1,981 → 1,982, versão mais recente v0.3.1 (4 de outubro de 2026).
- **3 de outubro de 2026:** Estrelas 1,963 → 1,981, versão mais recente v0.3.0 (3 de outubro de 2026).
- **27 de setembro de 2026:** Estrelas 1,865 → 1,963, versão mais recente v0.2.4 (25 de setembro de 2026).
- **31 de agosto de 2026:** Estrelas 1,825 → 1,865, versão mais recente v0.2.3 (30 de agosto de 2026).

## O que você ganha

- Suporte para 16 famílias de modelos diferentes
- Alto desempenho em GPU e CPU
- Inferência eficiente com formato GGUF

## Instalação

**Instalação Linux compatível com Vulkan**

```
# Ubuntu/Debian
sudo apt install build-essential cmake libvulkan-dev glslc libopenblas-dev

cmake -B build -DTRANSCRIBE_VULKAN=ON
cmake --build build
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero converter um arquivo de áudio local em texto usando a ferramenta Transcribe.cpp. Como posso processar meu arquivo de áudio no formato WAV mono de 16 kHz usando a ferramenta transcribe-cli compilada em meu sistema e o arquivo de modelo no formato GGUF que baixei? Explique a estrutura de comando necessária para este processo e os caminhos de arquivo aos quais devo prestar atenção.

## Termos relacionados do glossário

- [Speech-to-Text](https://trescout.com/pt/dictionary/speech-to-text/)
- [STT](https://trescout.com/pt/dictionary/stt/)
- [GGUF](https://trescout.com/pt/dictionary/gguf/)
- [Inference](https://trescout.com/pt/dictionary/inference/)
- [CPU](https://trescout.com/pt/dictionary/cpu/)
- [GPU](https://trescout.com/pt/dictionary/gpu/)

- **Para quem é:** É para desenvolvedores que desejam executar sistemas de reconhecimento de fala rápidos e com foco na privacidade em seu próprio hardware.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/handy-computer/transcribe.cpp)
- [Ler em turco →](https://trescout.com/discover/transcribe-cpp/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-21: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/transcribe-cpp/
