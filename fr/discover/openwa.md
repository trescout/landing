# Passerelle open source pour WhatsApp

OpenWA propose une solution de passerelle API gratuite et open source pour le protocole de messagerie WhatsApp. Cet outil, développé avec le langage TypeScript, permet aux utilisateurs de gérer les intégrations WhatsApp sur leurs propres serveurs (auto-hébergés).

- ★ 14 976
- TypeScript
- GitHub Trending · 2026-06-17

## Mises à jour

- **3 octobre 2026:** Étoiles 14,622 → 14,976, dernière version v0.24.0 (3 octobre 2026).
- **27 septembre 2026:** Étoiles 14,197 → 14,622, dernière version v0.23.7 (25 septembre 2026).
- **16 septembre 2026:** Étoiles 13,775 → 14,197, dernière version v0.23.5 (15 septembre 2026).
- **5 septembre 2026:** Étoiles 13,239 → 13,775, dernière version v0.23.4 (5 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite automatiser mes processus de messagerie via WhatsApp à l'aide de l'outil OpenWA. Expliquez-moi les étapes de configuration de base requises pour créer une nouvelle session, envoyer des messages et écouter les messages entrants via un webhook à l'aide des points de terminaison de l'API REST. Dites-moi à quoi je dois faire attention, notamment en ce qui concerne la gestion multi-session et la sécurité des clés API.

## Termes liés du glossaire

- [API Gateway](https://trescout.com/fr/dictionary/api-gateway/)
- [Gateway](https://trescout.com/fr/dictionary/gateway/)
- [Self-hosted](https://trescout.com/fr/dictionary/self-hosted/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent développer leurs propres intégrations WhatsApp et souhaitent avoir un contrôle total sur l'infrastructure de messagerie.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/rmyndharis/OpenWA)
- [Lire en turc →](https://trescout.com/discover/openwa/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-17 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openwa/
