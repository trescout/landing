# Moteur de recherche d'emploi open source

Développé en Go, freehire est un moteur de recherche open source (dont le code source est accessible et modifiable par tous) conçu pour les chercheurs d'emploi. Il offre une plateforme permettant aux utilisateurs de parcourir et de trouver des offres d'emploi.

- ★ 2 661
- Go
- GitHub Trending · 2026-10-22

## Mises à jour

- **22 octobre 2026:** Étoiles 2,643 → 2,661, dernière version extension-v0.1.10 (21 octobre 2026).

## Ce que ça vous apporte

- Accédez sans intermédiaire et de manière actualisée aux offres d'emploi tech collectées directement depuis les pages carrières des entreprises.
- Consultez une liste propre et filtrable en éliminant les doublons d'annonces présentés sur différents sites d'emploi.
- Gérez votre processus de recherche d'emploi grâce à l'analyse de compatibilité de votre CV et à un tableau de bord de suivi des candidatures propulsé par l'IA.

## Installation

**Installation de l'ensemble du système dans un environnement conteneurisé et**

```
make up        # build + start the whole stack in Docker:
               # api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs
```

## Exécution

**avec un port différent si le port par défaut est occupé**

```
HIRE_HOST_PORT=8090 make up
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite exécuter l'application de recherche d'emploi open source Freehire sur mon propre système. Pour démarrer tous les services et vérifier l'état de l'API à l'aide du logiciel de gestion de conteneurs Docker et de l'outil d'automatisation Make, exécutez les commandes suivantes dans l'ordre : make up # build + start the whole stack in Docker:
# api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs

Dépôt : https://github.com/strelov1/freehire. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Localhost](https://trescout.com/fr/dictionary/localhost/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** C'est pour ceux qui souhaitent suivre sans intermédiaire les offres d'emploi en logiciel et technologie sur les pages carrières des entreprises, ou faire fonctionner leur propre moteur de recherche d'emploi indépendant.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/strelov1/freehire)
- [Lire en turc →](https://trescout.com/discover/freehire/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-10-22 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/freehire/
