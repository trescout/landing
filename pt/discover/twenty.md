# CRM moderno e de código aberto

Twenty é uma alternativa de código aberto ao Salesforce que permite que equipes técnicas construam um CRM moderno que pode ser personalizado de acordo com seus processos de negócios. Você pode hospedar este sistema, que se concentra em fluxos de trabalho suportados por inteligência artificial, em seu próprio servidor.

- ★ 55.953
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## O que você ganha
- Uma alternativa gratuita e de código aberto ao Salesforce.
- Controle total sobre seus dados com a opção de auto-hospedagem.
- Fluxos de trabalho modernos alimentados por IA.
- Blocos de construção flexíveis que podem ser adaptados às necessidades do seu negócio.

## Instalação
**Baixar modelo de ambiente**

```
curl -o .env https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/.env.example
```

**Baixar arquivo Compose**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/docker-compose.yml
```

**Gerar chave de criptografia**

```
openssl rand -base64 32
```

**Iniciar serviços**

```
docker compose up -d
```


## Execução
**Acessar interface local**

```
http://localhost:3000
```


## Como instalar?
Geralmente é instalado em seu próprio servidor com Docker; as etapas de instalação estão na documentação. Requer algum conhecimento técnico para gerenciar.

## Como instalar, como usar?
Quero instalar um CRM de código aberto chamado Twenty; crie um novo aplicativo no terminal com o comando 'npx create-twenty-app my-app' e publique-o em meu espaço de trabalho com 'npx twenty app:publish --private'. Diga-me também como executá-lo com Docker Compose para auto-hospedagem.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/twenty/
