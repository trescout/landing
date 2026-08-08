# Passerelle open source pour WhatsApp

OpenWA propose une solution de passerelle API gratuite et open source pour le protocole de messagerie WhatsApp. Cet outil, développé avec le langage TypeScript, permet aux utilisateurs de gérer les intégrations WhatsApp sur leurs propres serveurs (auto-hébergés).

- ★ 12 552
- TypeScript
- GitHub Trending · 2026-06-17

## Mise à jour
- 8 août 2026 : Star 12 544 → 12 552, dernière version v0.14.6 (8 août 2026).
- 8 août 2026 : Star 12 503 → 12 544, dernière version v0.14.5 (8 août 2026).
- 7 août 2026 : Star 12 466 → 12 503, dernière version v0.14.4 (7 août 2026).
- 6 août 2026 : Star 12 355 → 12 466, dernière version v0.14.2 (6 août 2026).

## Ce que ça vous apporte
- Contrôle total sur l'infrastructure de messagerie WhatsApp
- Gestion des sessions et des webhooks avec une interface moderne
- Installation rapide et facile avec le support Docker

## Installation
**Installation rapide avec Docker**

```
# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

**Environnement de développement local**

```
# Clone repository
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA

# Install dependencies (includes dashboard)
npm install

# Start API + Dashboard (config is auto-generated on first run)
npm run dev

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```


## Exécution
**Lancement dans un environnement de production**

```
# Basic production (SQLite, local storage)
docker compose up -d

# With PostgreSQL database
docker compose --profile postgres up -d

# Full stack (PostgreSQL, Redis, Dashboard, Traefik)
docker compose --profile full up -d
```


## Si vous ne codez pas
Je souhaite automatiser mes processus de messagerie via WhatsApp à l'aide de l'outil OpenWA. Expliquez-moi les étapes de configuration de base requises pour créer une nouvelle session, envoyer des messages et écouter les messages entrants via un webhook à l'aide des points de terminaison de l'API REST. Dites-moi à quoi je dois faire attention, notamment en ce qui concerne la gestion multi-session et la sécurité des clés API.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openwa/
