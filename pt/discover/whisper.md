# Transcreva sons com inteligência artificial

Desenvolvido pela OpenAI, Whisper é um modelo de reconhecimento de fala treinado por um método de aprendizagem de supervisão fraca em larga escala. Oferece altas taxas de precisão na conversão e tradução de dados de áudio multilíngues em texto.

- ★ 106.452
- Python
- GitHub Trending · 2026-06-07

## O que você ganha
- Converta arquivos de áudio em texto com alta precisão.
- Traduzindo conversas de diferentes idiomas para o inglês.
- Identificação de idioma e detecção de atividade de fala em conteúdo de áudio.

## Instalação
**Dependências do sistema**

```
sudo apt update && sudo apt install ffmpeg
```

**Requisito adicional de instalação**

```
pip install setuptools-rust
```


## Execução
**Converter arquivo de áudio em texto**

```
whisper audio.flac audio.mp3 audio.wav --model turbo
```

**Transcrição em um idioma específico**

```
whisper japanese.wav --language Japanese
```


## Se você não programa
Quero converter meu arquivo de áudio em texto usando a ferramenta Whisper. Fiz as instalações necessárias no meu sistema. Qual é a estrutura básica de comandos que preciso digitar no terminal para traduzir o conteúdo do meu arquivo de áudio em texto e como devo usar o parâmetro de especificação de idioma para arquivos de áudio em diferentes idiomas?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/whisper/
