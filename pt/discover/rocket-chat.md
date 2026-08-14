# Comunicação de equipe segura e personalizável

Rocket.Chat oferece um sistema operacional de comunicação seguro projetado para operações de missão crítica. A plataforma, desenvolvida com a linguagem TypeScript, tem como objetivo centralizar processos internos de mensagens e colaboração.

- ★ 45.941
- TypeScript
- GitHub Trending · 2026-06-18

## Atualizar
- 7 de agosto de 2026: Star 45.919 → 45.941, última versão 8.7.0 (7 de agosto de 2026).
- 2 de agosto de 2026: Star 45.649 → 45.919, última versão 8.6.1 (10 de julho de 2026).

## O que você ganha
- Segurança de dados com criptografia ponta a ponta
- Possibilidade de hospedagem em servidor próprio
- Ampla integração e suporte a aplicativos

## Instalação
**Linux · Pacote Snap (editor do Rocket.Chat)**

```
sudo snap install rocketchat-server
```

**Repositório oficial de composição do Docker**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git && cd rocketchat-compose && cp .env.example .env
```


## Execução
**Lançar com Docker**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml -f docker.yml up -d
```


## Como começar
- Fonte oficial →
Para começar a instalar o Rocket.Chat, você pode revisar o Guia de implantação na página de documentação oficial. Você pode escolher um dos métodos Docker, Podman ou Kubernetes para hospedar em seu próprio servidor ou considerar a opção Launchpad para um início mais rápido. Para todos os requisitos técnicos e etapas detalhadas de instalação, visite o site de documentação oficial do Rocket.Chat.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/rocket-chat/
