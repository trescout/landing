# Treinamento personalizado apoiado por inteligência artificial

DeepTutor é um sistema de aulas particulares baseado em aprendizagem ao longo da vida que oferece processos educacionais personalizados usando dados de alunos. O projeto visa otimizar a experiência de aprendizagem com métodos de tutoria individualizados apoiados por inteligência artificial.

- ★ 40.808
- Python
- GitHub Trending · 2026-07-16

## Atualizações

- **5 de outubro de 2026:** Estrelas 40,358 → 40,808, versão mais recente v1.6.13 (4 de outubro de 2026).
- **27 de setembro de 2026:** Estrelas 40,334 → 40,358, versão mais recente v1.6.12 (27 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 39,561 → 40,334, versão mais recente v1.6.11 (24 de setembro de 2026).
- **14 de setembro de 2026:** Estrelas 39,283 → 39,561, versão mais recente v1.6.8 (14 de setembro de 2026).

## O que você ganha

- Sistema de aulas particulares com foco na aprendizagem ao longo da vida
- Interação com agentes de inteligência artificial personalizados
- Base de conhecimento avançada e suporte RAG

## Instalação

**Instalação rápida**

```
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # prompts for ports + LLM provider + optional embedding
deeptutor start    # starts backend + frontend; keep the terminal open
```

**Executando com Docker**

```
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

## Execução

**Inicialização do sistema**

```
deeptutor start    # starts backend + frontend; keep the terminal open
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Como posso personalizar meu processo de aprendizagem usando o sistema DeepTutor? Explique as etapas básicas que preciso seguir para criar meus próprios parceiros de IA e otimizar minha experiência de aprendizagem ao longo da vida integrando meus materiais de treinamento personalizados neste sistema.

## Termos relacionados do glossário

- [Lifelong Learning](https://trescout.com/pt/dictionary/lifelong-learning/)
- [Personalized Tutoring](https://trescout.com/pt/dictionary/personalized-tutoring/)
- [Tutoring](https://trescout.com/pt/dictionary/tutoring/)
- [RAG](https://trescout.com/pt/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para estudantes e instrutores que desejam criar seu próprio assistente educacional particular e estabelecer um ambiente de aprendizagem personalizado.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/HKUDS/DeepTutor)
- [Ler em turco →](https://trescout.com/discover/deeptutor/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-16: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/deeptutor/
