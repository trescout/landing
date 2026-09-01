# Conjunto de Regras para Agentes de Codificação com IA

Conjunto de regras e sistema de plugins com licença MIT para agentes de codificação por IA. Destina-se a preservar verificação, tratamento de erros, segurança e acessibilidade enquanto os agentes escrevem código necessário.

- ★ 119.108
- JavaScript
- GitHub Trending · 2026-08-25

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
- Instale a integração Ponytail para o host de agente que você usa
- Verifique que a instalação está ativa dentro do host
- Selecione o nível apropriado do Ponytail
- Execute o fluxo de revisão ou auditoria sobre as alterações

## Início seguro

## Primeiro prompt
Escreva apenas o código necessário para a tarefa, então revise as alterações quanto à verificação, tratamento de erros, segurança e acessibilidade.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- README oficial →
- Método do benchmark agêntico →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ponytail/
