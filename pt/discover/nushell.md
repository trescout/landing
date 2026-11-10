# Uma interface de linha de comando que oferece objetos estruturados

Desenvolvido na linguagem Rust, o nushell oferece uma nova interface de linha de comando (shell) que processa dados como objetos estruturados. Tendo alcançado o nível de produto mínimo viável (minimum-viable-product), este projeto pode apresentar instabilidade em alguns comandos, mas é preferido para o uso diário.

- ★ 41.079
- Rust
- GitHub Trending · 2026-11-07

## Atualizações

- **10 de novembro de 2026:** Estrelas 41,012 → 41,079, versão mais recente 0.117.0 (10 de novembro de 2026).
- **7 de novembro de 2026:** Estrelas 41,011 → 41,012, versão mais recente 0.116.1 (4 de outubro de 2026).

## O que você ganha

- Processa dados como objetos estruturados.
- Permite o fluxo de pipeline entre comandos.
- Carrega o conteúdo de arquivos como dados estruturados.

## Instalação

**Instalação**

```
# Linux and macOS
brew install nushell
# Windows
winget install nushell
```

## Execução

**Listando Pastas**

```
ls | where type == "dir" | table
# => ╭────┬──────────┬──────┬─────────┬───────────────╮
# => │ #  │   name   │ type │  size   │   modified    │
# => ├────┼──────────┼──────┼─────────┼───────────────┤
# => │  0 │ .cargo   │ dir  │     0 B │ 9 minutes ago │
# => │  1 │ assets   │ dir  │     0 B │ 2 weeks ago   │
# => │  2 │ crates   │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  3 │ docker   │ dir  │     0 B │ 2 weeks ago   │
# => │  4 │ docs     │ dir  │     0 B │ 2 weeks ago   │
# => │  5 │ images   │ dir  │     0 B │ 2 weeks ago   │
# => │  6 │ pkg_mgrs │ dir  │     0 B │ 2 weeks ago   │
# => │  7 │ samples  │ dir  │     0 B │ 2 weeks ago   │
# => │  8 │ src      │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  9 │ target   │ dir  │     0 B │ a day ago     │
# => │ 10 │ tests    │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │ 11 │ wix      │ dir  │     0 B │ 2 weeks ago   │
# => ╰────┴──────────┴──────┴─────────┴───────────────╯
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Gostaria de instalar e usar a nova interface de linha de comando chamada Nushell. Após concluir a instalação, ajude-me a executar o comando ls | where type == "dir" | table.

Repositório: https://github.com/nushell/nushell. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Shell](https://trescout.com/pt/dictionary/shell/)
- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para desenvolvedores que desejam gerenciar dados como objetos estruturados na linha de comando.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/nushell/nushell)
- [Ler em turco →](https://trescout.com/discover/nushell/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-11-07: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/nushell/
