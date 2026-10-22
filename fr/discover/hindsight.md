# Couche de mémoire intelligente pour les agents d'intelligence artificielle

Hindsight propose une couche mémoire d’apprentissage pour les agents d’intelligence artificielle. Cette bibliothèque open source améliore les processus décisionnels des agents en déduisant des interactions passées, permettant ainsi aux systèmes de produire des résultats plus cohérents au fil du temps.

- ★ 52 557
- GitHub Trending · 2026-09-25

## Mises à jour

- **22 octobre 2026:** Étoiles 51,834 → 52,557, dernière version v1.1.0 (21 octobre 2026).
- **20 octobre 2026:** Étoiles 49,114 → 51,834, dernière version v1.0.0 (13 octobre 2026).
- **13 octobre 2026:** Étoiles 47,195 → 49,114, dernière version v1.0.0 (13 octobre 2026).
- **8 octobre 2026:** Étoiles 46,537 → 47,195, dernière version v0.10.3 (8 octobre 2026).

## Ce que ça vous apporte

- Il fournit une architecture de mémoire qui apprend des interactions passées et produit des résultats plus cohérents au fil du temps.
- Il améliore les processus décisionnels des agents en allant au-delà du rappel direct des informations.
- Il contient des bibliothèques clientes pour différents langages tels que Python, Node.js et Go.

## Installation

**Démarrer un serveur avec Docker**

```
export OPENAI_API_KEY=sk-xxx

docker run -it --pull always --name hindsight --restart unless-stopped -p 8888:8888 -p 9999:9999 \
  -e HINDSIGHT_API_LLM_API_KEY=$OPENAI_API_KEY \
  -v hindsight-data:/home/hindsight/.pg0 \
  ghcr.io/vectorize-io/hindsight:latest
```

## Exécution

**Configurer un client avec Python**

```
pip install hindsight-client -U                                  # Python
npm install @vectorize-io/hindsight-client                        # Node.js / TypeScript
go get github.com/vectorize-io/hindsight/hindsight-clients/go     # Go
curl -fsSL https://hindsight.vectorize.io/get-cli | bash          # CLI
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je veux que mon agent IA apprenne des interactions passées, non seulement se souvienne de l’historique des conversations, mais prenne des décisions plus cohérentes au fil du temps. Aidez-moi à configurer la configuration du serveur et les connexions clients nécessaires pour intégrer cette couche mémoire dans mon projet.

Dépôt : https://github.com/vectorize-io/hindsight. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Memory Layer](https://trescout.com/fr/dictionary/memory-layer/)
- [Memory](https://trescout.com/fr/dictionary/memory/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Les développeurs qui souhaitent que leurs agents IA apprennent au fil du temps et prennent des décisions plus cohérentes.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/vectorize-io/hindsight)
- [Lire en turc →](https://trescout.com/discover/hindsight/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-25 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/hindsight/
