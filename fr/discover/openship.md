# Déploiement d'applications sur votre propre serveur

OpenShip propose une plateforme de distribution d'applications que les utilisateurs peuvent héberger sur leurs propres serveurs. Cet outil, développé avec le langage TypeScript, facilite les processus d'auto-hébergement comme alternative aux services d'infrastructure basés sur le cloud.

- ★ 14 584
- TypeScript
- GitHub Trending · 2026-07-21

## Mises à jour

- **7 octobre 2026:** Étoiles 14,558 → 14,584, dernière version v0.8.2 (6 octobre 2026).
- **6 octobre 2026:** Étoiles 13,545 → 14,558, dernière version v0.8.0 (27 septembre 2026).
- **29 septembre 2026:** Étoiles 12,541 → 13,545, dernière version v0.8.0 (27 septembre 2026).
- **27 septembre 2026:** Étoiles 12,135 → 12,541, dernière version v0.8.0 (27 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite publier un projet en utilisant Openship. Dans le répertoire du projet, est-il suffisant de connecter le répertoire au projet avec la commande openship init, puis d'exécuter la commande openship déployer ? Pouvez-vous expliquer étape par étape comment la base de données et la configuration SSL sont automatiquement gérées dans ce processus ?

## Termes liés du glossaire

- [Deployment Platform](https://trescout.com/fr/dictionary/deployment-platform/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)
- [Self-hosted](https://trescout.com/fr/dictionary/self-hosted/)
- [CI/CD](https://trescout.com/fr/dictionary/ci-cd/)
- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs de logiciels qui souhaitent héberger des applications sur leurs propres serveurs et souhaitent les déployer rapidement sans avoir à gérer de fichiers de configuration complexes.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/oblien/openship)
- [Lire en turc →](https://trescout.com/discover/openship/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-21 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openship/
