# Communication d'équipe sécurisée et personnalisable

Rocket.Chat propose un système d'exploitation de communications sécurisé conçu pour les opérations critiques. La plateforme, développée avec le langage TypeScript, vise à centraliser les processus de messagerie et de collaboration internes.

- ★ 46 005
- TypeScript
- GitHub Trending · 2026-06-18

## Ce que ça vous apporte
- Sécurité des données avec cryptage de bout en bout
- Possibilité d'hébergement sur votre propre serveur
- Large intégration et prise en charge des applications

## Installation
**Linux · Package Snap (éditeur de Rocket.Chat)**

```
sudo snap install rocketchat-server
```

**Dépôt de composition officiel Docker**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git && cd rocketchat-compose && cp .env.example .env
```


## Exécution
**Lancer avec Docker**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml -f docker.yml up -d
```


## Pour commencer
- Source officielle →

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/rocket-chat/
