# Gerencie árvores de trabalho do Git

Worktrunk é uma interface de linha de comando (CLI) escrita em Rust que simplifica o gerenciamento de árvores de trabalho (worktree) do Git. Desenvolvida especialmente para suportar fluxos de trabalho paralelos de agentes de inteligência artificial, esta ferramenta acelera o trabalho em múltiplas tarefas simultaneamente.

- ★ 7.379
- Rust
- GitHub Trending · 2026-09-13

## O que você ganha
- Cria facilmente espaços de trabalho para executar múltiplas tarefas simultaneamente
- Acelera fluxos de trabalho locais com ganchos automáticos
- Suporta a execução paralela de agentes de inteligência artificial

## Instalação
**Instalação com Homebrew**

```
brew install worktrunk && wt config shell install
```

**Instalação via Cargo**

```
cargo install worktrunk && wt config shell install
```


## Execução
**Alternar entre árvores de trabalho**

```
wt switch feat
```

**Criar e inicializar uma nova árvore de trabalho**

```
wt switch -c -x claude feat
```


## Se você não programa
Quero usar o Worktrunk para criar uma nova árvore de trabalho no meu projeto Git existente e iniciar uma tarefa paralela nesta área. Como devo usar os comandos wt para gerenciar árvores de trabalho tão facilmente quanto branches e como posso aproveitar os hooks para automatizar meu fluxo de trabalho?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/worktrunk/
