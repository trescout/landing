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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero instalar o projeto LongCat-Video no meu sistema. Por favor, guie-me passo a passo para baixar o código-fonte com os comandos 'git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video' e 'cd LongCat-Video', e depois executar os comandos de download com 'pip install "huggingface_hub[cli]"' para acessar os arquivos necessários através da biblioteca de modelos Hugging Face.

## Termos relacionados do glossário

- [Clone](https://trescout.com/pt/dictionary/clone/)
- [Framework](https://trescout.com/pt/dictionary/framework/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É destinado a desenvolvedores e criadores de conteúdo que desejam produzir vídeos de alta qualidade e longa duração a partir de entradas de texto, imagem ou áudio com a ajuda de inteligência artificial.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/meituan-longcat/LongCat-Video)
- [Ler em turco →](https://trescout.com/discover/longcat-video/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-10-04: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/longcat-video/
