# Communication d'équipe sécurisée et personnalisable

Rocket.Chat propose un système d'exploitation de communications sécurisé conçu pour les opérations critiques. La plateforme, développée avec le langage TypeScript, vise à centraliser les processus de messagerie et de collaboration internes.

- ★ 45 941
- TypeScript
- GitHub Trending · 2026-06-18

## Mise à jour
- 7 août 2026 : Star 45 919 → 45 941, dernière version 8.7.0 (7 août 2026).
- 2 août 2026 : Star 45 649 → 45 919, dernière version 8.6.1 (10 juillet 2026).

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
Pour commencer à installer Rocket.Chat, vous pouvez consulter le guide de déploiement sur la page de documentation officielle. Vous pouvez choisir l'une des méthodes Docker, Podman ou Kubernetes pour héberger sur votre propre serveur, ou envisager l'option Launchpad pour un démarrage plus rapide. Pour toutes les exigences techniques et les étapes d'installation détaillées, visitez le site de documentation officiel de Rocket.Chat.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/rocket-chat/
