# Faça backup de seus dados com segurança criptografando-os

Desenvolvido com a linguagem Go, o Restic oferece um programa de backup de código aberto que faz backup de dados de forma rápida e eficiente, criptografando-os. Esta ferramenta, que suporta diferentes sistemas de armazenamento, economiza espaço de armazenamento com o método de backup incremental.

- ★ 35.302
- GitHub Trending · 2026-06-12

**Nota da TreScout:** Ele armazena seus backups criptografando-os e não ocupa espaço porque não grava o mesmo arquivo duas vezes. Não possui interface clicável, é executado a partir da linha de comando e você define a tarefa de limpar backups antigos, caso contrário o armazenamento aumentará com o tempo. Tente restaurar um arquivo no mesmo dia em que você o instalou: caso contrário, você não saberá se o backup realmente funcionou.

## Atualizações

- **2 de agosto de 2026:** Estrelas 34,273 → 35,302, versão mais recente v0.19.1 (5 de julho de 2026).

## O que você ganha

- Fornece alta segurança criptografando dados
- Economiza espaço de armazenamento com backup incremental
- Compatível com diferentes sistemas de armazenamento local e em nuvem

## Instalação

**macOS · Homebrew**

```
brew install restic
```

**Windows · winget**

```
winget install restic.restic
```

## Execução

**Criar repositório de backup**

```
restic init --repo /path/to/repo
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero fazer backup dos meus dados com segurança usando Restic. Como posso exportar uma pasta local ou diretório específico para um armazenamento de backup criptografado? Você pode explicar passo a passo como criar o repositório de backup e iniciar o processo de backup inicial para que meus dados sejam criptografados?

## Termos relacionados do glossário

- [Backup Program](https://trescout.com/pt/dictionary/backup-program/)
- [Incremental Backup](https://trescout.com/pt/dictionary/incremental-backup/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para todos os usuários que desejam fazer backup de seus dados de forma rápida e eficiente, criptografando-os.
- **Licença:** BSD-2-Clause

## Links

- [Repositório no GitHub →](https://github.com/restic/restic)
- [Ler em turco →](https://trescout.com/discover/restic/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-12: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/restic/
