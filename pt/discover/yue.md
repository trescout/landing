# Composição editável com IA na produção musical

YuE é um sistema de geração de música equipado com capacidades como planejamento simbólico e geração de covers zero-shot. Este modelo de IA, que automatiza processos de edição musical, permite gerenciar composições complexas com fluxos de trabalho agentivos.

- ★ 9.749
- Python
- GitHub Trending · 2026-09-13

## O que você ganha
- Criação de melodia e plano de acordes com entrada de letra e estilo
- Capacidade de editar notas musicais antes de convertê-las em arquivos de áudio
- Reinterpretação e edição de músicas existentes em diferentes estilos

## Instalação
**Download e instalação do projeto**

```
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
python examples/generate.py --output outputs/first-song
```


## Execução
**Criação de música com notas editadas**

```
python examples/generate.py --request examples/song.json \
  --abc-file edited.abc --cot full --output outputs/edited
```


## Se você não programa
Quero criar uma música usando o YuE2. Por favor, prepare um plano editável de melodia e acordes com base na letra e no estilo musical que desejo. Em seguida, use este plano para produzir uma gravação completa da música, incluindo vocais e acompanhamento instrumental. Se eu tiver um arquivo de notação, permita-me usá-lo para realizar edições.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/yue/
