# Outil de surveillance de l'état des serveurs et des services

Uptime Kuma est un outil de surveillance auto-hébergé doté d'une interface visuelle. Permettant de suivre l'état de fonctionnement des sites Web et des services, cette application basée sur JavaScript offre une expérience conviviale.

- ★ 93 936
- JavaScript
- GitHub Trending · 2026-11-14

## Mises à jour

- **14 novembre 2026:** Étoiles 93,934 → 93,936, dernière version 2.5.11 (12 novembre 2026).

## Ce que ça vous apporte

- Suivez en temps réel les sites Web et les services
- Bénéficiez d'un support multilingue et de notifications
- Créez des pages de statut visuelles

## Installation

**Installation avec Docker Compose**

```
mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
```

**Installation avec la commande Docker**

```
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

## Exécution

**Exécuter avec Docker**

```
docker compose up -d
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite installer l'outil de surveillance Uptime Kuma. Pour utiliser Docker Compose, je dois exécuter cette commande : mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d. Pouvez-vous m'aider à compléter ces étapes ?

Dépôt : https://github.com/louislam/uptime-kuma. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Idéal pour toute personne souhaitant suivre le bon fonctionnement de sites Web et de serveurs sur sa propre infrastructure.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/louislam/uptime-kuma)
- [Lire en turc →](https://trescout.com/discover/uptime-kuma/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-14 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/uptime-kuma/
