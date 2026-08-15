# Gestion centrale des services Grok

Développée pour les plateformes Grok Build, Grok Web et Grok Console, cette passerelle (passerelle API) regroupe la gestion multi-comptes dans un centre unique. Écrit en langage Go, l'outil offre une interface gérable en standardisant l'accès des utilisateurs aux différents services Grok.

- ★ 7 239
- Go
- GitHub Trending · 2026-07-15

## Ce que ça vous apporte
- Grok Build combine les comptes Web et console dans un seul panneau
- Fournit une interface API standard compatible avec OpenAI et Anthropic
- Fournit une gestion avancée des comptes, un routage de modèles et une gestion des erreurs

## Installation
**Installation rapide avec Docker**

```
git clone https://github.com/chenyme/grok2api.git
cd grok2api
cp config.example.yaml config.yaml
```

**Démarrer le service**

```
docker compose pull
docker compose up -d
```


## Exécution
**gestion des services**

```
docker compose logs -f grok2api
docker compose restart grok2api
docker compose down
```


## Si vous ne codez pas
J'ai terminé l'installation de Grok2API et me suis connecté au panneau d'administration. Maintenant, comment puis-je définir mes comptes Grok Build, Web ou Console sur le système, comment puis-je effectuer des correspondances de modèles et quelles étapes puis-je suivre pour générer la clé API pour une utilisation externe ? Veuillez expliquer ce processus étape par étape.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/grok2api/
