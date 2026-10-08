# Couche de mémoire intelligente pour les agents d'intelligence artificielle

Hindsight propose une couche mémoire d’apprentissage pour les agents d’intelligence artificielle. Cette bibliothèque open source améliore les processus décisionnels des agents en déduisant des interactions passées, permettant ainsi aux systèmes de produire des résultats plus cohérents au fil du temps.

- ★ 46 537
- GitHub Trending · 2026-09-25

## Mises à jour

- **7 octobre 2026:** Étoiles 44,051 → 46,537, dernière version v0.10.2 (29 septembre 2026).
- **1 octobre 2026:** Étoiles 41,939 → 44,051, dernière version v0.10.2 (29 septembre 2026).
- **29 septembre 2026:** Étoiles 39,425 → 41,939, dernière version v0.10.2 (29 septembre 2026).
- **28 septembre 2026:** Étoiles 35,563 → 39,425, dernière version v0.10.1 (21 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je veux que mon agent IA apprenne des interactions passées, non seulement se souvienne de l’historique des conversations, mais prenne des décisions plus cohérentes au fil du temps. Aidez-moi à configurer la configuration du serveur et les connexions clients nécessaires pour intégrer cette couche mémoire dans mon projet.

## Termes liés du glossaire

- [Memory Layer](https://trescout.com/fr/dictionary/memory-layer/)
- [Memory](https://trescout.com/fr/dictionary/memory/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Les développeurs qui souhaitent que leurs agents IA apprennent au fil du temps et prennent des décisions plus cohérentes.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/vectorize-io/hindsight)
- [Lire en turc →](https://trescout.com/discover/hindsight/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-25 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/hindsight/
