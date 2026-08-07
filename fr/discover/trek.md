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
Vous êtes assistant de voyage. À l'aide des outils MCP (Model Context Protocol) sur TREK, créez pour moi un plan de voyage de 3 jours à Paris, ajustez mon budget en fonction des limites de dépenses quotidiennes et créez une liste de colisage pour ce que je dois emporter avec moi.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/trek/
