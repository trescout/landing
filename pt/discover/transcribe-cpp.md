# Conversão rápida de fala em sistemas locais

Transcribe.cpp é uma biblioteca de inferência de fala para texto desenvolvida em C++ que oferece suporte a mais de 16 famílias de modelos. Usando a infraestrutura ggml, esta ferramenta permite que diferentes modelos de processamento de áudio sejam executados com eficiência em sistemas locais.

- ★ 1.673
- C++
- GitHub Trending · 2026-07-21

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
Quero converter um arquivo de áudio local em texto usando a ferramenta Transcribe.cpp. Como posso processar meu arquivo de áudio no formato WAV mono de 16 kHz usando a ferramenta transcribe-cli compilada em meu sistema e o arquivo de modelo no formato GGUF que baixei? Explique a estrutura de comando necessária para este processo e os caminhos de arquivo aos quais devo prestar atenção.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/transcribe-cpp/
