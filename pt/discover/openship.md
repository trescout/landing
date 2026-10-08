# Implantação de aplicativo em seu próprio servidor

OpenShip oferece uma plataforma de distribuição de aplicativos que os usuários podem hospedar em seus próprios servidores. Essa ferramenta, desenvolvida em linguagem TypeScript, facilita processos de auto-hospedagem como alternativa aos serviços de infraestrutura baseados em nuvem.

- ★ 14.584
- TypeScript
- GitHub Trending · 2026-07-21

## Atualizações

- **7 de outubro de 2026:** Estrelas 14,558 → 14,584, versão mais recente v0.8.2 (6 de outubro de 2026).
- **6 de outubro de 2026:** Estrelas 13,545 → 14,558, versão mais recente v0.8.0 (27 de setembro de 2026).
- **29 de setembro de 2026:** Estrelas 12,541 → 13,545, versão mais recente v0.8.0 (27 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 12,135 → 12,541, versão mais recente v0.8.0 (27 de setembro de 2026).

## O que você ganha

- Processos automatizados de CI/CD
- Transição rápida do código para o contêiner
- Gerenciamento de banco de dados e SSL

## Instalação

**Instalação rápida via CLI**

```
npm i -g openship     # or: curl -fsSL https://get.openship.io | sh
openship up           # installs Openship as a background service (starts on boot, auto-restarts)
```

**Instalação com Docker**

```
git clone https://github.com/oblien/openship.git && cd openship
cp .env.example .env
docker compose up -d
```

## Execução

**Iniciar a implantação do projeto**

```
cd your-project
openship init         # link this directory to a project
openship deploy
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero publicar um projeto usando Openship. Enquanto estiver no diretório do projeto, é suficiente conectar o diretório ao projeto com o comando openship init e então executar o comando openship deploy? Você pode explicar passo a passo como o banco de dados e a configuração SSL são gerenciados automaticamente neste processo?

## Termos relacionados do glossário

- [Deployment Platform](https://trescout.com/pt/dictionary/deployment-platform/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)
- [Self-hosted](https://trescout.com/pt/dictionary/self-hosted/)
- [CI/CD](https://trescout.com/pt/dictionary/ci-cd/)
- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a desenvolvedores de software que desejam hospedar aplicativos em seus próprios servidores e implantá-los rapidamente, sem lidar com arquivos de configuração complexos.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/oblien/openship)
- [Ler em turco →](https://trescout.com/discover/openship/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-21: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openship/
