# Crie cenas tridimensionais a partir de streaming de dados

Lingbot-map é um modelo básico 3D feed-forward projetado para reconstruir cenas a partir de dados de streaming. O projeto otimiza processos de visualização através do processamento de dados ambientais complexos, graças à sua arquitetura desenvolvida em linguagem Python.

- ★ 17.060
- Python
- GitHub Trending · 2026-06-29

## Atualizações

- **16 de setembro de 2026:** Estrelas 16,054 → 17,060.
- **2 de agosto de 2026:** Estrelas 8,439 → 16,054.

## O que você ganha

- Reconstrução 3D estável de longas sequências de vídeo
- Suporte para inferência de streaming de baixa latência
- Arquitetura de inteligência artificial que pode processar dados ambientais complexos

## Instalação

**Preparação do ambiente e configuração básica**

```
conda create -n lingbot-map python=3.10 -y
conda activate lingbot-map
```

**Instalando as bibliotecas necessárias**

```
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```

## Execução

**Iniciando a cena de amostra**

```
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/courthouse --mask_sky
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero criar uma cena 3D a partir de streaming de dados usando o LingBot-Map. Concluí a instalação e meu arquivo de modelo está pronto. Como posso iniciar a interface de visualização no meu navegador local usando o comando necessário para executar a instância do Courthouse?

## Termos relacionados do glossário

- [Foundation Model](https://trescout.com/pt/dictionary/foundation-model/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para pesquisadores e desenvolvedores interessados ​​em visão computacional 3D e processamento de dados de streaming.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/Robbyant/lingbot-map)
- [Ler em turco →](https://trescout.com/discover/lingbot-map/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-29: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/lingbot-map/
