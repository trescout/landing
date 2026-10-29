# Gerencie assinaturas de IA em um único centro

Sub2API é um serviço intermediário de código aberto que fornece acesso de ponto único e compartilhamento de custos para assinaturas Claude, OpenAI, Gemini e Grok.

- ★ 45.041
- Go
- GitHub Trending · 2026-08-23

## Atualizações

- **29 de outubro de 2026:** Estrelas 44,674 → 45,041, versão mais recente v0.2.19 (28 de outubro de 2026).
- **23 de outubro de 2026:** Estrelas 44,184 → 44,674, versão mais recente v0.2.18 (23 de outubro de 2026).
- **16 de outubro de 2026:** Estrelas 43,885 → 44,184, versão mais recente v0.2.17 (16 de outubro de 2026).
- **13 de outubro de 2026:** Estrelas 43,558 → 43,885, versão mais recente v0.2.16 (13 de outubro de 2026).

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

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Como posso configurar diferentes serviços de IA como Claude, OpenAI, Gemini e Grok através de um único gateway de API usando a plataforma Sub2API? Explique as etapas básicas que preciso seguir para alocar com eficiência minhas cotas de assinatura e integrá-las às minhas ferramentas de software existentes. Além disso, resumir as questões jurídicas e técnicas às quais preciso prestar atenção para cumprir os termos de serviço de fornecedores como a Anthropic ao utilizar esta plataforma.

Repositório: https://github.com/Wei-Shaw/sub2api. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [API](https://trescout.com/pt/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Para desenvolvedores que desejam gerenciar múltiplas assinaturas de IA em uma única plataforma e otimizar seus custos.
- **Licença:** LGPL-3.0

## Links

- [Repositório no GitHub →](https://github.com/Wei-Shaw/sub2api)
- [Ler em turco →](https://trescout.com/discover/sub2api/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-23: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/sub2api/
