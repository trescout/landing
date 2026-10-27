# Logiciel de suivi d'entraînement fonctionnant sur votre propre serveur

OpenGym est un outil de gestion de salle de sport open source permettant de planifier des routines d'entraînement et de suivre des exercices au poids de corps. Permettant aux utilisateurs d'héberger leurs données sur leur propre serveur, ce logiciel prend en charge l'importation de données à partir d'applications de fitness populaires (Strong, Hevy).

- ★ 16 384
- JavaScript
- GitHub Trending · 2026-10-05

## Mises à jour

- **27 octobre 2026:** Étoiles 15,063 → 16,384, dernière version v1.4.3 (26 octobre 2026).
- **23 octobre 2026:** Étoiles 14,645 → 15,063, dernière version v1.4.2 (23 octobre 2026).
- **22 octobre 2026:** Étoiles 13,304 → 14,645, dernière version v1.4.1 (10 octobre 2026).
- **18 octobre 2026:** Étoiles 12,021 → 13,304, dernière version v1.4.1 (10 octobre 2026).

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

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite installer le logiciel de suivi d'entraînement openGym sur la plateforme de gestion de conteneurs Docker. Pourriez-vous m'expliquer étape par étape les instructions d'installation commençant par la commande 'git clone https://github.com/DuarteSantos8/openGym', comment configurer le fichier de variables d'environnement '.env', et comment accéder à l'application depuis un navigateur une fois l'installation terminée ?

Dépôt : https://github.com/DuarteSantos8/openGym. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Si une clé API est nécessaire, ne me demande pas de l'écrire dans la conversation. Montre-moi comment l'ajouter au fichier .env et assure-toi que ce fichier n'est pas envoyé sur Git.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Clone](https://trescout.com/fr/dictionary/clone/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux passionnés de sport qui accordent de l'importance à la confidentialité de leurs données d'entraînement et qui souhaitent suivre gratuitement leurs routines de salle de sport sur leur propre serveur.
- **Licence:** AGPL-3.0

## Liens

- [Dépôt GitHub →](https://github.com/DuarteSantos8/openGym)
- [Lire en turc →](https://trescout.com/discover/opengym/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-10-05 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/opengym/
