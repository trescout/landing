# Gérez les abonnements IA à partir d’un seul centre

Sub2API est un service intermédiaire open source qui fournit un accès unique et un partage des coûts aux abonnements Claude, OpenAI, Gemini et Grok.

- ★ 43 391
- Go
- GitHub Trending · 2026-08-23

## Mises à jour

- **7 octobre 2026:** Étoiles 43,206 → 43,391, dernière version v0.2.14 (7 octobre 2026).
- **2 octobre 2026:** Étoiles 43,199 → 43,206, dernière version v0.2.13 (2 octobre 2026).
- **2 octobre 2026:** Étoiles 43,119 → 43,199, dernière version v0.2.12 (2 octobre 2026).
- **30 septembre 2026:** Étoiles 43,041 → 43,119, dernière version v0.2.11 (30 septembre 2026).

## Ce que ça vous apporte

- Combine différents abonnements IA dans une seule interface
- Vous aide à répartir efficacement les coûts d’abonnement
- Offre la possibilité de travailler en intégration avec les outils existants

## Installation

**installation automatique**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

**Installation avec Docker**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
```

## Exécution

**Démarrer le service**

```
docker compose up -d
```

**Afficher le mot de passe administrateur**

```
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Comment puis-je configurer différents services d'IA tels que Claude, OpenAI, Gemini et Grok via une seule passerelle API à l'aide de la plateforme Sub2API ? Expliquez les étapes de base que je dois suivre pour allouer efficacement mes quotas d'abonnement et les intégrer à mes outils logiciels existants. Résumez également les problèmes juridiques et techniques auxquels je dois prêter attention afin de respecter les conditions de service de fournisseurs tels qu'Anthropic lors de l'utilisation de cette plateforme.

## Termes liés du glossaire

- [API](https://trescout.com/fr/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Pour les développeurs qui souhaitent gérer plusieurs abonnements IA sur une seule plateforme et optimiser leurs coûts.
- **Licence:** LGPL-3.0

## Liens

- [Dépôt GitHub →](https://github.com/Wei-Shaw/sub2api)
- [Lire en turc →](https://trescout.com/discover/sub2api/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-23 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/sub2api/
