# Gerencie seus planos de viagem juntos

TREK é um aplicativo de planejamento de viagens auto-hospedado que oferece recursos como colaboração em tempo real, mapas interativos e gerenciamento de orçamento. Com suporte progressivo a aplicativos da web (PWA) e integração de logon único (SSO), permite que os usuários organizem seus processos de viagem digitalmente.

- ★ 7.040
- GitHub Trending · 2026-06-26

## O que você ganha

- Crie rotas e planos de viagem diários arrastando e soltando
- Rastreando despesas do grupo e dividindo-as por pessoa
- Gestão automática de viagens e orçamento com integração de inteligência artificial

## Instalação

**Instalação rápida com Docker**

```
ENCRYPTION_KEY=$(openssl rand -hex 32) docker run -d -p 3000:3000 \
  -e ENCRYPTION_KEY=$ENCRYPTION_KEY \
  -v ./data:/app/data -v ./uploads:/app/uploads mauriceboe/trek
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Você é um assistente de viagem. Usando as ferramentas MCP (Model Context Protocol) do TREK, crie um plano de viagem de 3 dias para Paris para mim, ajuste meu orçamento com base nos limites de gastos diários e crie uma lista de bagagem para o que preciso levar comigo.

## Termos relacionados do glossário

- [PWA](https://trescout.com/pt/dictionary/pwa/)
- [SSO](https://trescout.com/pt/dictionary/sso/)
- [Self-hosted](https://trescout.com/pt/dictionary/self-hosted/)
- [Model Context Protocol](https://trescout.com/pt/dictionary/model-context-protocol/)
- [Model Context Protocol](https://trescout.com/pt/dictionary/model-context-protocol-mcp/)
- [Context](https://trescout.com/pt/dictionary/context/)

- **Para quem é:** É para viajantes que desejam organizar suas viagens digitalmente, acompanhar seus gastos e ter total controle sobre seus próprios dados.
- **Licença:** AGPL-3.0

## Links

- [Repositório no GitHub →](https://github.com/mauriceboe/TREK)
- [Ler em turco →](https://trescout.com/discover/trek/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-26: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/trek/
