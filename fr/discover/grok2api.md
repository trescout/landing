# Gestion centrale des services Grok

Développée pour les plateformes Grok Build, Grok Web et Grok Console, cette passerelle (passerelle API) regroupe la gestion multi-comptes dans un centre unique. Écrit en langage Go, l'outil offre une interface gérable en standardisant l'accès des utilisateurs aux différents services Grok.

- ★ 7 669
- Go
- GitHub Trending · 2026-07-15

## Mises à jour

- **16 septembre 2026:** Étoiles 7,543 → 7,669, dernière version v3.1.6 (16 septembre 2026).
- **27 août 2026:** Étoiles 7,459 → 7,543, dernière version v3.1.5 (25 août 2026).
- **19 août 2026:** Étoiles 7,447 → 7,459, dernière version v3.1.4 (19 août 2026).
- **18 août 2026:** Étoiles 7,239 → 7,447, dernière version v3.1.3 (17 août 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

J'ai terminé l'installation de Grok2API et me suis connecté au panneau d'administration. Maintenant, comment puis-je définir mes comptes Grok Build, Web ou Console sur le système, comment puis-je effectuer des correspondances de modèles et quelles étapes puis-je suivre pour générer la clé API pour une utilisation externe ? Veuillez expliquer ce processus étape par étape.

## Termes liés du glossaire

- [API Gateway](https://trescout.com/fr/dictionary/api-gateway/)
- [Gateway](https://trescout.com/fr/dictionary/gateway/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent gérer plusieurs comptes Grok et utiliser ces services dans leurs applications via une API standard.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/chenyme/grok2api)
- [Lire en turc →](https://trescout.com/discover/grok2api/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-15 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/grok2api/
