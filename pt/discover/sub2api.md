# Gerencie assinaturas de IA em um único centro

Sub2API é um serviço intermediário de código aberto que fornece acesso de ponto único e compartilhamento de custos para assinaturas Claude, OpenAI, Gemini e Grok.

- ★ 40.573
- Go
- GitHub Trending · 2026-08-23

## O que você ganha
- Combina diferentes assinaturas de IA em uma interface
- Ajuda você a alocar custos de assinatura de forma eficiente
- Oferece a oportunidade de trabalhar integrado com ferramentas existentes

## Instalação
**instalação automática**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

**Instalação com Docker**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
```


## Execução
**Inicie o serviço**

```
docker compose up -d
```

**Ver senha do administrador**

```
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```


## Se você não programa
Como posso configurar diferentes serviços de IA como Claude, OpenAI, Gemini e Grok através de um único gateway de API usando a plataforma Sub2API? Explique as etapas básicas que preciso seguir para alocar com eficiência minhas cotas de assinatura e integrá-las às minhas ferramentas de software existentes. Além disso, resumir as questões jurídicas e técnicas às quais preciso prestar atenção para cumprir os termos de serviço de fornecedores como a Anthropic ao utilizar esta plataforma.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/sub2api/
