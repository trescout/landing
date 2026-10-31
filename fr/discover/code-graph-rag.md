# Interrogez votre référentiel de code avec l'intelligence artificielle

Code-graph-rag combine des graphiques de connaissances et une génération assistée par récupération (RAG) pour comprendre et interroger des structures complexes dans de grands référentiels de code. Il permet aux développeurs d'analyser et d'éditer des bases de code dans différents langages à l'aide de l'intelligence artificielle.

- ★ 5 303
- Python
- GitHub Trending · 2026-08-10

## Mises à jour

- **31 octobre 2026:** Étoiles 5,284 → 5,303, dernière version v0.4.5 (30 octobre 2026).
- **26 octobre 2026:** Étoiles 5,279 → 5,284, dernière version v0.3.13 (25 octobre 2026).
- **24 octobre 2026:** Étoiles 5,278 → 5,279, dernière version v0.3.2 (24 octobre 2026).
- **23 octobre 2026:** Étoiles 5,264 → 5,278, dernière version v0.2.19 (22 octobre 2026).

## Ce que ça vous apporte

- Découvrez les relations complexes en transformant la base de code en un graphe de connaissances
- Obtenez des réponses sur la structure du code en posant des questions en langage naturel
- Apportez des modifications précises au code avec des outils de recherche et d'édition structurés

## Installation

**Installation avec le gestionnaire de paquets**

```
uv tool install "code-graph-rag[treesitter-full,semantic]"
```

**Méthode d'installation alternative**

```
pipx install "code-graph-rag[treesitter-full,semantic]"
```

## Exécution

**Démarrage de la base de données**

```
cgr daemon up
```

**Analyser et interroger l'entrepôt**

```
cgr start --repo-path /path/to/repo --update-graph
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Analysez mon référentiel de code à l'aide de l'outil Code-Graph-RAG. Répondez à mes questions en utilisant les relations entre les fonctions, les classes et les modules dans votre base de code. Suggérer des modifications ou des optimisations que je devrais apporter au code en utilisant les capacités d'analyse structurelle fournies par l'outil.

Dépôt : https://github.com/vitali87/code-graph-rag. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Monorepo](https://trescout.com/fr/dictionary/monorepo/)
- [RAG](https://trescout.com/fr/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs de logiciels qui souhaitent comprendre et interroger les relations structurelles dans des référentiels de code vastes et complexes et apporter des modifications en toute sécurité à l'aide de l'intelligence artificielle.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/vitali87/code-graph-rag)
- [Lire en turc →](https://trescout.com/discover/code-graph-rag/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-10 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/code-graph-rag/
