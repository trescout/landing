# Gerenciamento central para serviços Grok

Desenvolvido para as plataformas Grok Build, Grok Web e Grok Console, este gateway (API gateway) reúne o gerenciamento de múltiplas contas em um único centro. Escrita na linguagem Go, a ferramenta oferece uma interface gerenciável padronizando o acesso dos usuários aos diversos serviços Grok.

- ★ 7.669
- Go
- GitHub Trending · 2026-07-15

## Atualizações

- **16 de setembro de 2026:** Estrelas 7,543 → 7,669, versão mais recente v3.1.6 (16 de setembro de 2026).
- **27 de agosto de 2026:** Estrelas 7,459 → 7,543, versão mais recente v3.1.5 (25 de agosto de 2026).
- **19 de agosto de 2026:** Estrelas 7,447 → 7,459, versão mais recente v3.1.4 (19 de agosto de 2026).
- **18 de agosto de 2026:** Estrelas 7,239 → 7,447, versão mais recente v3.1.3 (17 de agosto de 2026).

## O que você ganha

- Grok Build combina contas da Web e de console em um painel
- Fornece interface API padrão compatível com OpenAI e Anthropic
- Fornece gerenciamento avançado de contas, roteamento de modelo e tratamento de erros

## Instalação

**Instalação rápida com Docker**

```
git clone https://github.com/chenyme/grok2api.git
cd grok2api
cp config.example.yaml config.yaml
```

**Inicie o serviço**

```
docker compose pull
docker compose up -d
```

## Execução

**gerenciamento de serviços**

```
docker compose logs -f grok2api
docker compose restart grok2api
docker compose down
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Concluí a instalação do Grok2API e fiz login no painel de administração. Agora, como posso definir minhas contas Grok Build, Web ou Console para o sistema, como faço correspondências de modelo e quais etapas posso seguir para gerar a chave API para uso externo? Por favor, explique este processo passo a passo.

## Termos relacionados do glossário

- [API Gateway](https://trescout.com/pt/dictionary/api-gateway/)
- [Gateway](https://trescout.com/pt/dictionary/gateway/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É para desenvolvedores que desejam gerenciar várias contas Grok e usar esses serviços em seus aplicativos por meio de uma API padrão.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/chenyme/grok2api)
- [Ler em turco →](https://trescout.com/discover/grok2api/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-15: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/grok2api/
