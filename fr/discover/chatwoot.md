# Plateforme de support client open source

Chatwoot est une plateforme open source qui offre un chat en direct, une assistance par e-mail et une gestion de bureau omnicanal. Développé comme alternative aux logiciels commerciaux tels qu'Intercom et Zendesk, cet outil vous permet de gérer les interactions clients à partir d'un centre unique.

- ★ 36 253
- GitHub Trending · 2026-06-12

## Ce que ça vous apporte
- Il regroupe tous les canaux clients dans une seule boîte de réception.
- Répond automatiquement aux questions de routine avec un assistant basé sur l'intelligence artificielle.
- Il vous donne un contrôle total sur vos données clients en les hébergeant sur votre propre serveur.

## Installation
**Télécharger le fichier d'environnement**

```
wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example
```

**Télécharger le fichier Docker Compose**

```
wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml
```

**Préparer la base de données**

```
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
```


## Exécution
**Démarrer les services**

```
docker compose up -d
```


## Si vous ne codez pas
Répondez aux questions en vous faisant passer pour un représentant du support client. En tant qu'assistant Captain AI sur Chatwoot, résolvez automatiquement les questions fréquemment posées et dirigez les problèmes complexes vers les coéquipiers concernés. Améliorez l’expérience du support client en fournissant toujours des informations courtoises, rapides et précises.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/chatwoot/
