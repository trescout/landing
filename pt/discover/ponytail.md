# Conjunto de Regras para Agentes de Codificação com IA

Conjunto de regras e sistema de plugins com licença MIT para agentes de codificação por IA. Destina-se a preservar verificação, tratamento de erros, segurança e acessibilidade enquanto os agentes escrevem código necessário.

- ★ 156.385
- JavaScript
- GitHub Trending · 2026-08-25

## Atualizações

- **6 de outubro de 2026:** Estrelas 155,501 → 156,385, versão mais recente v4.13.0 (5 de outubro de 2026).
- **5 de outubro de 2026:** Estrelas 152,240 → 155,501, versão mais recente v4.12.0 (5 de outubro de 2026).
- **3 de outubro de 2026:** Estrelas 146,524 → 152,240, versão mais recente v4.10.3 (3 de outubro de 2026).
- **27 de setembro de 2026:** Estrelas 138,874 → 146,524, versão mais recente v4.10.0 (14 de setembro de 2026).

## Instalação

**Adicionar o marketplace do Claude Code**

```
/plugin marketplace add DietrichGebert/ponytail
```

**Instalar o plugin do Claude Code**

```
/plugin install ponytail@ponytail
```

## Execução

**Selecionar nível do Ponytail**

```
/ponytail full
```

**Iniciar revisão de diff**

```
/ponytail-review
```

## O que esta ferramenta faz?

A escada de regras é aplicada depois que o código afetado pela mudança é lido. Um benchmark agentic corrigido reportou, em um repositório real FastAPI + React com 12 tarefas usando Haiku 4.5, médias como 54% menos linhas de código, 22% menos tokens, 20% menor custo e 27% menor duração em relação à linha de base no-skill; esses resultados são limitados às condições de teste especificadas.

## Para quem é?

Quem quer adicionar regras de verificação, segurança e acessibilidade a fluxos de codificação em Claude Code, Codex, Gemini CLI e outros hosts de agentes suportados.

## O que não esperar

Generalizar resultados específicos de benchmark para todos os projetos ou aplicar mudanças críticas de produção sem revisão humana.

## Destaques

- Regras orientadas a tarefas que visam reduzir código desnecessário
- Abordagem de revisão que preserva verificação, tratamento de erros, segurança e acessibilidade
- Plugins ou adaptadores de instrução para Claude Code, Codex, Gemini CLI e outros hosts

## Primeiro fluxo de uso

1. Instale a integração Ponytail para o host de agente que você usa
2. Verifique que a instalação está ativa dentro do host
3. Selecione o nível apropriado do Ponytail
4. Execute o fluxo de revisão ou auditoria sobre as alterações

## Início seguro

As porcentagens são médias do benchmark agentic corrigido em 12 tarefas de um repositório FastAPI + React com Haiku 4.5 e n=4. Uma camada adversarial separada relatou 100% de segurança. As faixas únicas históricas de 80% a 94% não representam uma média geral.

## Primeiro prompt

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Escreva apenas o código necessário para a tarefa, então revise as alterações quanto à verificação, tratamento de erros, segurança e acessibilidade.

## Termos relacionados do glossário

- [Benchmark](https://trescout.com/pt/dictionary/benchmark/)
- [Agentic](https://trescout.com/pt/dictionary/agentic/)
- [Token](https://trescout.com/pt/dictionary/token/)
- [Agent](https://trescout.com/pt/dictionary/agent/)
- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

## Links

- [Repositório no GitHub →](https://github.com/DietrichGebert/ponytail)
- [README oficial →](https://github.com/DietrichGebert/ponytail)
- [Método do benchmark agêntico →](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md)
- [Ler em turco →](https://trescout.com/discover/ponytail/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-25: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ponytail/
