# Gerencie árvores de trabalho do Git

Worktrunk é uma interface de linha de comando (CLI) escrita em Rust que simplifica o gerenciamento de árvores de trabalho (worktree) do Git. Desenvolvida especialmente para suportar fluxos de trabalho paralelos de agentes de inteligência artificial, esta ferramenta acelera o trabalho em múltiplas tarefas simultaneamente.

- ★ 9.348
- Rust
- GitHub Trending · 2026-09-13

## Atualizações

- **21 de outubro de 2026:** Estrelas 8,444 → 9,348, versão mais recente v0.81.0 (20 de outubro de 2026).
- **28 de setembro de 2026:** Estrelas 8,424 → 8,444, versão mais recente v0.80.0 (27 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 7,964 → 8,424, versão mais recente v0.79.0 (21 de setembro de 2026).
- **17 de setembro de 2026:** Estrelas 7,379 → 7,964, versão mais recente v0.78.0 (16 de setembro de 2026).

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

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero usar o Worktrunk para criar uma nova árvore de trabalho no meu projeto Git existente e iniciar uma tarefa paralela nesta área. Como devo usar os comandos wt para gerenciar árvores de trabalho tão facilmente quanto branches e como posso aproveitar os hooks para automatizar meu fluxo de trabalho?

Repositório: https://github.com/max-sixty/worktrunk. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Worktree](https://trescout.com/pt/dictionary/worktree/)
- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Projetado para desenvolvedores que trabalham em múltiplas tarefas de software ou agentes de inteligência artificial simultaneamente.

## Links

- [Repositório no GitHub →](https://github.com/max-sixty/worktrunk)
- [Ler em turco →](https://trescout.com/discover/worktrunk/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-13: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/worktrunk/
