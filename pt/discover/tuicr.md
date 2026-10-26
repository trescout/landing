# Revendo código com Vim no terminal

Desenvolvido com a linguagem Rust, tuicr é uma ferramenta de revisão de código baseada na interface do usuário do terminal que oferece suporte a atalhos de teclado do Vim. Ele permite que os desenvolvedores gerenciem seu processo de revisão de código diretamente do terminal.

- ★ 3.463
- Rust
- GitHub Trending · 2026-07-31

## Atualizações

- **26 de outubro de 2026:** Estrelas 3,221 → 3,463, versão mais recente v0.28.0 (26 de outubro de 2026).
- **27 de setembro de 2026:** Estrelas 3,132 → 3,221, versão mais recente v0.27.0 (23 de setembro de 2026).
- **16 de setembro de 2026:** Estrelas 3,009 → 3,132, versão mais recente v0.26.0 (15 de setembro de 2026).
- **3 de setembro de 2026:** Estrelas 2,908 → 3,009, versão mais recente v0.25.0 (2 de setembro de 2026).

## O que você ganha

- Revisão rápida de código no terminal com atalhos do Vim
- Poste comentários diretamente no GitHub e GitLab
- Suporte de saída estruturada para ferramentas de IA

## Instalação

**Instalação padrão**

```
curl -fsSL tuicr.dev/install.sh | sh
# or
brew install agavra/tap/tuicr
```

**Gerenciadores de pacotes alternativos**

```
# Cargo
cargo install tuicr

# Mise
mise use github:agavra/tuicr

# Nix
nix run github:agavra/tuicr
```

## Execução

**Revise as mudanças locais**

```
tuicr -w
```

**Revise um PR específico**

```
tuicr pr 125
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Revise esta revisão de código e prepare uma lista estruturada de quaisquer bugs ou sugestões de melhoria que você encontrar, com cada comentário identificado pelo caminho do arquivo e número da linha. Ao fazer a revisão, forneça sugestões concretas que aumentarão a legibilidade e o desempenho do código, com base nos dados em formato markdown que copiei do tuicr.

Repositório: https://github.com/agavra/tuicr. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Code Review](https://trescout.com/pt/dictionary/code-review/)
- [User Interface](https://trescout.com/pt/dictionary/user-interface/)
- [Interface](https://trescout.com/pt/dictionary/interface/)
- [Markdown](https://trescout.com/pt/dictionary/markdown/)
- [Terminal](https://trescout.com/pt/dictionary/terminal/)
- [Rust](https://trescout.com/pt/dictionary/rust/)

- **Para quem é:** É para desenvolvedores que desejam gerenciar seus processos de revisão de código com atalhos do Vim sem sair do terminal.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/agavra/tuicr)
- [Ler em turco →](https://trescout.com/discover/tuicr/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-31: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/tuicr/
