# Implantação de aplicativo em seu próprio servidor

OpenShip oferece uma plataforma de distribuição de aplicativos que os usuários podem hospedar em seus próprios servidores. Essa ferramenta, desenvolvida em linguagem TypeScript, facilita processos de auto-hospedagem como alternativa aos serviços de infraestrutura baseados em nuvem.

- ★ 11.135
- TypeScript
- GitHub Trending · 2026-07-21

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
Quero publicar um projeto usando Openship. Enquanto estiver no diretório do projeto, é suficiente conectar o diretório ao projeto com o comando openship init e então executar o comando openship deploy? Você pode explicar passo a passo como o banco de dados e a configuração SSL são gerenciados automaticamente neste processo?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openship/
