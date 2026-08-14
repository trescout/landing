# Treinamento personalizado apoiado por inteligência artificial

DeepTutor é um sistema de aulas particulares baseado em aprendizagem ao longo da vida que oferece processos educacionais personalizados usando dados de alunos. O projeto visa otimizar a experiência de aprendizagem com métodos de tutoria individualizados apoiados por inteligência artificial.

- ★ 33.415
- Python
- GitHub Trending · 2026-07-16

## Atualizar
- 10 de agosto de 2026: Star 32.944 → 33.415, versão mais recente v1.5.11 (9 de agosto de 2026).
- 7 de agosto de 2026: Star 32.640 → 32.944, versão mais recente v1.5.10 (7 de agosto de 2026).
- 6 de agosto de 2026: Star 31.925 → 32.640, versão mais recente v1.5.9 (4 de agosto de 2026).
- 2 de agosto de 2026: Star 26.461 → 31.925, versão mais recente v1.5.8 (2 de agosto de 2026).

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
Como posso personalizar meu processo de aprendizagem usando o sistema DeepTutor? Explique as etapas básicas que preciso seguir para criar meus próprios parceiros de IA e otimizar minha experiência de aprendizagem ao longo da vida integrando meus materiais de treinamento personalizados neste sistema.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/deeptutor/
