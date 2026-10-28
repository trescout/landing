# Treinamento personalizado apoiado por inteligência artificial

DeepTutor é um sistema de aulas particulares baseado em aprendizagem ao longo da vida que oferece processos educacionais personalizados usando dados de alunos. O projeto visa otimizar a experiência de aprendizagem com métodos de tutoria individualizados apoiados por inteligência artificial.

- ★ 46.783
- Python
- GitHub Trending · 2026-07-16

## Atualizações

- **28 de outubro de 2026:** Estrelas 44,479 → 46,783, versão mais recente v1.6.15 (18 de outubro de 2026).
- **27 de outubro de 2026:** Estrelas 41,717 → 44,479, versão mais recente v1.6.15 (18 de outubro de 2026).
- **19 de outubro de 2026:** Estrelas 40,928 → 41,717, versão mais recente v1.6.15 (18 de outubro de 2026).
- **8 de outubro de 2026:** Estrelas 40,808 → 40,928, versão mais recente v1.6.14 (8 de outubro de 2026).

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

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Como posso personalizar meu processo de aprendizagem usando o sistema DeepTutor? Explique as etapas básicas que preciso seguir para criar meus próprios parceiros de IA e otimizar minha experiência de aprendizagem ao longo da vida integrando meus materiais de treinamento personalizados neste sistema.

Repositório: https://github.com/HKUDS/DeepTutor. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

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

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-16: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/deeptutor/
