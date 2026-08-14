# Gateway de código aberto para WhatsApp

OpenWA oferece uma solução de gateway API gratuita e de código aberto para o protocolo de mensagens WhatsApp. Esta ferramenta, desenvolvida em linguagem TypeScript, permite aos usuários gerenciar integrações do WhatsApp em servidores próprios (auto-hospedados).

- ★ 12.674
- TypeScript
- GitHub Trending · 2026-06-17

## Atualizar
- 12 de agosto de 2026: Star 12.605 → 12.674, versão mais recente v0.16.0 (11 de agosto de 2026).
- 10 de agosto de 2026: Star 12.552 → 12.605, última versão v0.15.0 (9 de agosto de 2026).
- 8 de agosto de 2026: Star 12.544 → 12.552, versão mais recente v0.14.6 (8 de agosto de 2026).
- 8 de agosto de 2026: Star 12.503 → 12.544, versão mais recente v0.14.5 (8 de agosto de 2026).

## O que você ganha
- Controle total sobre a infraestrutura de mensagens do WhatsApp
- Gerenciamento de sessão e webhook com interface moderna
- Instalação rápida e fácil com suporte Docker

## Instalação
**Instalação rápida com Docker**

```
# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

**Ambiente de desenvolvimento local**

```
# Clone repository
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA

# Install dependencies (includes dashboard)
npm install

# Start API + Dashboard (config is auto-generated on first run)
npm run dev

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```


## Execução
**Lançamento em um ambiente de produção**

```
# Basic production (SQLite, local storage)
docker compose up -d

# With PostgreSQL database
docker compose --profile postgres up -d

# Full stack (PostgreSQL, Redis, Dashboard, Traefik)
docker compose --profile full up -d
```


## Se você não programa
Quero automatizar meus processos de mensagens via WhatsApp usando a ferramenta OpenWA. Acompanhe-me pelas etapas básicas de configuração necessárias para criar uma nova sessão, enviar mensagens e ouvir mensagens recebidas por meio de webhook usando endpoints da API REST. Diga-me no que preciso prestar atenção, especialmente em relação ao gerenciamento multisessão e à segurança da chave de API.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openwa/
