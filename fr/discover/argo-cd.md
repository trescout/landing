# Automatisez les déploiements Kubernetes

Argo CD est un outil qui gère les processus de déploiement continu déclaratif pour les environnements Kubernetes. Il fournit des mises à jour automatiques sur l'infrastructure en synchronisant les états des applications avec les référentiels Git.

- ★ 24 439
- Go
- GitHub Trending · 2026-07-09

## Mises à jour

- **21 octobre 2026:** Étoiles 24,377 → 24,439, dernière version v3.5.6 (20 octobre 2026).
- **12 octobre 2026:** Étoiles 24,345 → 24,377, dernière version v3.5.5 (12 octobre 2026).
- **7 octobre 2026:** Étoiles 24,154 → 24,345, dernière version v3.5.4 (6 octobre 2026).
- **14 septembre 2026:** Étoiles 24,005 → 24,154, dernière version v3.5.3 (14 septembre 2026).

## Ce que ça vous apporte

- Synchronisation automatique des applications avec les référentiels Git
- Processus de distribution déclaratifs et traçables
- Gestion rationalisée du cycle de vie dans les environnements Kubernetes

## Installation

**Créer un espace de noms**

```
kubectl create namespace argocd
```

**Appliquer le manifeste officiel**

```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Exécution

**Interface d'accès**

```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

## Pour commencer

Pour commencer à utiliser Argo CD, vous pouvez visiter la page de documentation officielle et suivre les étapes d'installation. Vous pouvez consulter la démo en direct pour comprendre le fonctionnement du projet et parcourir le site de documentation du CD Argo pour accéder à des guides complets.

- [Source officielle →](https://argo-cd.readthedocs.io)

## Termes liés du glossaire

- [Declarative Continuous Deployment](https://trescout.com/fr/dictionary/declarative-continuous-deployment/)
- [Continuous Deployment](https://trescout.com/fr/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux équipes logicielles et DevOps qui souhaitent automatiser les processus de déploiement et de cycle de vie de leurs applications exécutées sur Kubernetes.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/argoproj/argo-cd)
- [Lire en turc →](https://trescout.com/discover/argo-cd/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-09 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/argo-cd/
