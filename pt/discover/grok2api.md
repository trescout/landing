# Gerenciamento central para serviços Grok

Desenvolvido para as plataformas Grok Build, Grok Web e Grok Console, este gateway (API gateway) reúne o gerenciamento de múltiplas contas em um único centro. Escrita na linguagem Go, a ferramenta oferece uma interface gerenciável padronizando o acesso dos usuários aos diversos serviços Grok.

- ★ 7.239
- Go
- GitHub Trending · 2026-07-15

## Atualizar
- 10 de agosto de 2026: Star 7.022 → 7.239, versão mais recente v3.1.2 (10 de agosto de 2026).
- 6 de agosto de 2026: Star 6.945 → 7.022, versão mais recente v3.1.1 (5 de agosto de 2026).
- 2 de agosto de 2026: Estrela 5.927 → 6.945, versão mais recente v3.0.11 (29 de julho de 2026).

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
Concluí a instalação do Grok2API e fiz login no painel de administração. Agora, como posso definir minhas contas Grok Build, Web ou Console para o sistema, como faço correspondências de modelo e quais etapas posso seguir para gerar a chave API para uso externo? Por favor, explique este processo passo a passo.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/grok2api/
