# Composição editável com IA na produção musical

YuE é um sistema de geração de música equipado com capacidades como planejamento simbólico e geração de covers zero-shot. Este modelo de IA, que automatiza processos de edição musical, permite gerenciar composições complexas com fluxos de trabalho agentivos.

- ★ 10.749
- Python
- GitHub Trending · 2026-09-13

## Atualizações

- **3 de outubro de 2026:** Estrelas 9,749 → 10,749, versão mais recente yue2-v0.1.6 (9 de setembro de 2026).
- **19 de setembro de 2026:** Estrelas 8,744 → 9,749, versão mais recente yue2-v0.1.6 (9 de setembro de 2026).
- **15 de setembro de 2026:** Estrelas 7,463 → 8,744, versão mais recente yue2-v0.1.6 (9 de setembro de 2026).
- **13 de setembro de 2026:** Estrelas 7,459 → 7,463, versão mais recente yue2-v0.1.6 (9 de setembro de 2026).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero criar uma música usando o YuE2. Por favor, prepare um plano editável de melodia e acordes com base na letra e no estilo musical que desejo. Em seguida, use este plano para produzir uma gravação completa da música, incluindo vocais e acompanhamento instrumental. Se eu tiver um arquivo de notação, permita-me usá-lo para realizar edições.

## Termos relacionados do glossário

- [Zero-shot](https://trescout.com/pt/dictionary/zero-shot/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Adequado para músicos e criadores de conteúdo que desejam planejar suas composições musicais com a ajuda de inteligência artificial, fazer alterações em partituras e produzir músicas originais.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/multimodal-art-projection/YuE)
- [Ler em turco →](https://trescout.com/discover/yue/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-13: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/yue/
