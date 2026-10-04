# Crie vídeos longos de forma consistente

Desenvolvido pela Meituan, o LongCat-Video é um framework de geração de vídeo usado para criar vídeos longos de forma consistente. Esta ferramenta permite produzir conteúdos de vídeo de maior duração e alta qualidade, mantendo a consistência da imagem.

- ★ 8.892
- Python
- GitHub Trending · 2026-10-04

## O que você ganha
- Você pode gerar novos conteúdos de longa duração a partir de texto, imagem ou vídeos existentes.
- Você pode obter resultados em vídeos de vários minutos sem desvio de cor ou perda de qualidade.
- Você pode criar animações de personagens sincronizadas com o áudio usando arquivos de som.

## Instalação
**Baixar o repositório de código para o computador**

```
git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video
cd LongCat-Video
```

**Baixar os pesos do modelo**

```
pip install "huggingface_hub[cli]"
huggingface-cli download meituan-longcat/LongCat-Video --local-dir ./weights/LongCat-Video
huggingface-cli download meituan-longcat/LongCat-Video-Avatar --local-dir ./weights/LongCat-Video-Avatar
huggingface-cli download meituan-longcat/LongCat-Video-Avatar-1.5 --local-dir ./weights/LongCat-Video-Avatar-1.5
```


## Se você não programa
Quero instalar o projeto LongCat-Video no meu sistema. Por favor, guie-me passo a passo para baixar o código-fonte com os comandos 'git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video' e 'cd LongCat-Video', e depois executar os comandos de download com 'pip install "huggingface_hub[cli]"' para acessar os arquivos necessários através da biblioteca de modelos Hugging Face.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/longcat-video/
