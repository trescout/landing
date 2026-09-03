# Treinamento personalizado apoiado por inteligência artificial

DeepTutor é um sistema de aulas particulares baseado em aprendizagem ao longo da vida que oferece processos educacionais personalizados usando dados de alunos. O projeto visa otimizar a experiência de aprendizagem com métodos de tutoria individualizados apoiados por inteligência artificial.

- ★ 38.520
- Python
- GitHub Trending · 2026-07-16

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
