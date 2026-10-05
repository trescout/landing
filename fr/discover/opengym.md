# Logiciel de suivi d'entraînement fonctionnant sur votre propre serveur

OpenGym est un outil de gestion de salle de sport open source permettant de planifier des routines d'entraînement et de suivre des exercices au poids de corps. Permettant aux utilisateurs d'héberger leurs données sur leur propre serveur, ce logiciel prend en charge l'importation de données à partir d'applications de fitness populaires (Strong, Hevy).

- ★ 3 424
- JavaScript
- GitHub Trending · 2026-10-05

## Ce que ça vous apporte
- Vous pouvez stocker vos données d'entraînement dans un espace sécurisé que vous contrôlez, plutôt que sur les serveurs d'entreprises tierces.
- Vous pouvez facilement importer vos données d'exercices passées depuis des applications de fitness populaires telles que Strong et Hevy.
- Même sans connexion Internet, vous pouvez planifier et suivre vos entraînements depuis votre téléphone ou votre ordinateur.

## Installation
**Avec la plateforme de gestion de conteneurs Docker, a**

```
git clone https://github.com/DuarteSantos8/openGym
cd openGym
cp .env.example .env
docker compose pull      # prebuilt images, amd64 + arm64 (skip this to build from source)
docker compose up -d
```


## Si vous ne codez pas
Je souhaite installer le logiciel de suivi d'entraînement openGym sur la plateforme de gestion de conteneurs Docker. Pourriez-vous m'expliquer étape par étape les instructions d'installation commençant par la commande 'git clone https://github.com/DuarteSantos8/openGym', comment configurer le fichier de variables d'environnement '.env', et comment accéder à l'application depuis un navigateur une fois l'installation terminée ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/opengym/
