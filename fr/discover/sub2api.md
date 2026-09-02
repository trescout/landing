# Gérez les abonnements IA à partir d’un seul centre

Sub2API est un service intermédiaire open source qui fournit un accès unique et un partage des coûts aux abonnements Claude, OpenAI, Gemini et Grok.

- ★ 40 163
- Go
- GitHub Trending · 2026-08-23

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
Comment puis-je configurer différents services d'IA tels que Claude, OpenAI, Gemini et Grok via une seule passerelle API à l'aide de la plateforme Sub2API ? Expliquez les étapes de base que je dois suivre pour allouer efficacement mes quotas d'abonnement et les intégrer à mes outils logiciels existants. Résumez également les problèmes juridiques et techniques auxquels je dois prêter attention afin de respecter les conditions de service de fournisseurs tels qu'Anthropic lors de l'utilisation de cette plateforme.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/sub2api/
