# Kit autônomo de IA para antigravidade

Ag-kit é uma biblioteca de desenvolvimento que fornece as ferramentas e estruturas necessárias para criar agentes autônomos de inteligência artificial (agentes de IA) em projetos baseados em TypeScript. Ele permite que os desenvolvedores projetem rapidamente sistemas de agentes que possam gerenciar fluxos de trabalho complexos.

- ★ 8.159
- TypeScript
- GitHub Trending · 2026-07-28

## O que você ganha
- 20 funções diferentes de especialistas em IA
- Controle seguro de execução de comandos
- Memória persistente e gerenciamento de fluxo de trabalho

## Instalação
**Instalação no projeto**

```
npx @vudovn/ag-kit init
```

**Instalação global**

```
npm install -g @vudovn/ag-kit
ag-kit init
```


## Execução
**Verificação do espaço de trabalho**

```
npm run check:agents
npm run check:antigravity
npm run test:antigravity
```

**Testando o gancho de segurança**

```
printf '%s' '{"tool_args":{"CommandLine":"rm -rf /"}}' \
  | node .agents/hooks/validate-tool-call.mjs
```


## Se você não programa
Neste projeto, configurei um espaço de trabalho Antigravidade e ativei as ferramentas do AG Kit. Quero gerenciar minhas tarefas usando regras, funções de agentes especialistas e fluxos de trabalho definidos na pasta .agents/ no diretório do projeto. Certifique-se de que o gancho de segurança esteja ativo e planeje fluxos de trabalho complexos com os comandos /coordenar ou /orquestrar.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ag-kit/
