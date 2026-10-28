# Gateway de código aberto para WhatsApp

OpenWA oferece uma solução de gateway API gratuita e de código aberto para o protocolo de mensagens WhatsApp. Esta ferramenta, desenvolvida em linguagem TypeScript, permite aos usuários gerenciar integrações do WhatsApp em servidores próprios (auto-hospedados).

- ★ 16.328
- TypeScript
- GitHub Trending · 2026-06-17

## Atualizações

- **28 de outubro de 2026:** Estrelas 15,471 → 16,328, versão mais recente v0.26.0 (28 de outubro de 2026).
- **15 de outubro de 2026:** Estrelas 14,976 → 15,471, versão mais recente v0.25.0 (15 de outubro de 2026).
- **3 de outubro de 2026:** Estrelas 14,622 → 14,976, versão mais recente v0.24.0 (3 de outubro de 2026).
- **27 de setembro de 2026:** Estrelas 14,197 → 14,622, versão mais recente v0.23.7 (25 de setembro de 2026).

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

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero automatizar meus processos de mensagens via WhatsApp usando a ferramenta OpenWA. Acompanhe-me pelas etapas básicas de configuração necessárias para criar uma nova sessão, enviar mensagens e ouvir mensagens recebidas por meio de webhook usando endpoints da API REST. Diga-me no que preciso prestar atenção, especialmente em relação ao gerenciamento multisessão e à segurança da chave de API.

Repositório: https://github.com/rmyndharis/OpenWA. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Se uma chave de API for necessária, não me peça para digitá-la no chat. Mostre-me como adicioná-la ao arquivo .env e garanta que este arquivo não seja enviado ao Git.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [API Gateway](https://trescout.com/pt/dictionary/api-gateway/)
- [Gateway](https://trescout.com/pt/dictionary/gateway/)
- [Self-hosted](https://trescout.com/pt/dictionary/self-hosted/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a desenvolvedores que desejam desenvolver suas próprias integrações com o WhatsApp e pretendem ter controle total sobre a infraestrutura de mensagens.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/rmyndharis/OpenWA)
- [Ler em turco →](https://trescout.com/discover/openwa/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-17: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openwa/
