# Gérez ensemble vos projets de voyage

TREK est une application de planification de voyage auto-hébergée qui offre des fonctionnalités telles que la collaboration en temps réel, des cartes interactives et la gestion du budget. Grâce à la prise en charge des applications Web progressives (PWA) et à l'intégration de l'authentification unique (SSO), il permet aux utilisateurs d'organiser leurs processus de voyage de manière numérique.

- ★ 7 040
- GitHub Trending · 2026-06-26

## Ce que ça vous apporte

- Créez des itinéraires et des plans de voyage quotidiens par glisser-déposer
- Suivre les dépenses du groupe et les diviser par personne
- Gestion automatique des voyages et du budget avec intégration de l'intelligence artificielle

## Installation

**Installation rapide avec Docker**

```
ENCRYPTION_KEY=$(openssl rand -hex 32) docker run -d -p 3000:3000 \
  -e ENCRYPTION_KEY=$ENCRYPTION_KEY \
  -v ./data:/app/data -v ./uploads:/app/uploads mauriceboe/trek
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Vous êtes assistant de voyage. À l'aide des outils MCP (Model Context Protocol) sur TREK, créez pour moi un plan de voyage de 3 jours à Paris, ajustez mon budget en fonction des limites de dépenses quotidiennes et créez une liste de colisage pour ce que je dois emporter avec moi.

## Termes liés du glossaire

- [PWA](https://trescout.com/fr/dictionary/pwa/)
- [SSO](https://trescout.com/fr/dictionary/sso/)
- [Self-hosted](https://trescout.com/fr/dictionary/self-hosted/)
- [Model Context Protocol](https://trescout.com/fr/dictionary/model-context-protocol/)
- [Model Context Protocol](https://trescout.com/fr/dictionary/model-context-protocol-mcp/)
- [Context](https://trescout.com/fr/dictionary/context/)

- **Pour qui:** Il s'adresse aux voyageurs qui souhaitent organiser leurs voyages de manière numérique, suivre leurs dépenses et avoir un contrôle total sur leurs données.
- **Licence:** AGPL-3.0

## Liens

- [Dépôt GitHub →](https://github.com/mauriceboe/TREK)
- [Lire en turc →](https://trescout.com/discover/trek/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-26 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/trek/
