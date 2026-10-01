# Couche de mémoire intelligente pour les agents d'intelligence artificielle

Hindsight propose une couche mémoire d’apprentissage pour les agents d’intelligence artificielle. Cette bibliothèque open source améliore les processus décisionnels des agents en déduisant des interactions passées, permettant ainsi aux systèmes de produire des résultats plus cohérents au fil du temps.

- ★ 44 051
- GitHub Trending · 2026-09-25

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
Je veux que mon agent IA apprenne des interactions passées, non seulement se souvienne de l’historique des conversations, mais prenne des décisions plus cohérentes au fil du temps. Aidez-moi à configurer la configuration du serveur et les connexions clients nécessaires pour intégrer cette couche mémoire dans mon projet.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/hindsight/
