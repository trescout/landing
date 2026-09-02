# Comunicação de equipe segura e personalizável

Rocket.Chat oferece um sistema operacional de comunicação seguro projetado para operações de missão crítica. A plataforma, desenvolvida com a linguagem TypeScript, tem como objetivo centralizar processos internos de mensagens e colaboração.

- ★ 46.064
- TypeScript
- GitHub Trending · 2026-06-18

## O que você ganha
- Segurança de dados com criptografia ponta a ponta
- Possibilidade de hospedagem em servidor próprio
- Ampla integração e suporte a aplicativos

## Instalação
**Clonar repositório oficial do compose**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git
```

**Criar arquivo de ambiente**

```
cd rocketchat-compose
cp .env.example .env
```

**Iniciar serviços MongoDB e Rocket.Chat**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml up -d
```


## Execução
**Acessar interface local**

```
http://localhost:3000
```


## Como começar
- Fonte oficial →

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/rocket-chat/
