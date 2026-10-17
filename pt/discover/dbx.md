# Cliente de banco de dados leve

Desenvolvido com a linguagem Rust, o dbx oferece um cliente de banco de dados leve de 25 MB que suporta mais de 100 tipos de bancos de dados. A aplicação desktop inclui recursos como suporte a interface de linha de comando (CLI) e Docker, além de um assistente de inteligência artificial integrado e o Protocolo de Conexão de Modelo (MCP).

- ★ 27.027
- Rust
- GitHub Trending · 2026-09-29

## Atualizações

- **17 de outubro de 2026:** Estrelas 26,967 → 27,027, versão mais recente v0.6.46 (16 de outubro de 2026).
- **16 de outubro de 2026:** Estrelas 26,784 → 26,967, versão mais recente v0.6.45 (15 de outubro de 2026).
- **15 de outubro de 2026:** Estrelas 26,630 → 26,784, versão mais recente v0.6.44 (14 de outubro de 2026).
- **14 de outubro de 2026:** Estrelas 25,978 → 26,630, versão mais recente v0.6.43 (14 de outubro de 2026).

## O que você ganha

- Suporta mais de cem tipos de banco de dados.
- Funciona com desktop, Docker e linha de comando.
- Inclui assistente de inteligência artificial e Protocolo de Conexão de Modelo.

## Instalação

**Instalação do Aplicativo de Desktop**

```
brew install --cask dbx
```

**Instalação da ferramenta de linha de comando**

```
npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json
```

## Execução

**Executando com Docker**

```
# The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Siga os passos necessários para instalar e executar o aplicativo dbx. Utilize o comando brew install --cask dbx para o aplicativo de desktop e npm install -g @dbx-app/cli para a ferramenta de linha de comando.
# ou via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json
Se desejar executar com Docker, utilize o comando:
# O padrão mantém a chave no volume persistente /app/data.
docker run -d --pull=always --name dbx -p 4224:4224 \
-v dbx-data:/app/data \
t8y2/dbx:latest

## Termos relacionados do glossário

- [Database Client](https://trescout.com/pt/dictionary/database-client/)
- [Local](https://trescout.com/pt/dictionary/local/)
- [Database](https://trescout.com/pt/dictionary/database/)
- [MCP](https://trescout.com/pt/dictionary/mcp/)
- [Agent](https://trescout.com/pt/dictionary/agent/)
- [CLI](https://trescout.com/pt/dictionary/cli/)

- **Para quem é:** Destina-se a desenvolvedores que desejam gerenciar diferentes tipos de banco de dados com uma interface leve e suporte de inteligência artificial.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/t8y2/dbx)
- [Ler em turco →](https://trescout.com/discover/dbx/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-29: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/dbx/
