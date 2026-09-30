# Cliente de banco de dados leve

Desenvolvido com a linguagem Rust, o dbx oferece um cliente de banco de dados leve de 25 MB que suporta mais de 100 tipos de bancos de dados. A aplicação desktop inclui recursos como suporte a interface de linha de comando (CLI) e Docker, além de um assistente de inteligência artificial integrado e o Protocolo de Conexão de Modelo (MCP).

- ★ 22.868
- Rust
- GitHub Trending · 2026-09-29

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

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/dbx/
