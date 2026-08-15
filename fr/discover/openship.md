# Déploiement d'applications sur votre propre serveur

OpenShip propose une plateforme de distribution d'applications que les utilisateurs peuvent héberger sur leurs propres serveurs. Cet outil, développé avec le langage TypeScript, facilite les processus d'auto-hébergement comme alternative aux services d'infrastructure basés sur le cloud.

- ★ 10 565
- TypeScript
- GitHub Trending · 2026-07-21

## Ce que ça vous apporte
- Processus CI/CD automatisés
- Transition rapide du code au conteneur
- Gestion de base de données et SSL

## Installation
**Installation rapide via CLI**

```
npm i -g openship     # or: curl -fsSL https://get.openship.io | sh
openship up           # installs Openship as a background service (starts on boot, auto-restarts)
```

**Installation avec Docker**

```
git clone https://github.com/oblien/openship.git && cd openship
cp .env.example .env
docker compose up -d
```


## Exécution
**Démarrer le déploiement du projet**

```
cd your-project
openship init         # link this directory to a project
openship deploy
```


## Si vous ne codez pas
Je souhaite publier un projet en utilisant Openship. Dans le répertoire du projet, est-il suffisant de connecter le répertoire au projet avec la commande openship init, puis d'exécuter la commande openship déployer ? Pouvez-vous expliquer étape par étape comment la base de données et la configuration SSL sont automatiquement gérées dans ce processus ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openship/
