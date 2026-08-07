# Automatisez les déploiements Kubernetes

Argo CD est un outil qui gère les processus de déploiement continu déclaratif pour les environnements Kubernetes. Il fournit des mises à jour automatiques sur l'infrastructure en synchronisant les états des applications avec les référentiels Git.

- ★ 23 853
- Go
- GitHub Trending · 2026-07-09

## Mise à jour
- 6 août 2026 : Star 23 807 → 23 853, dernière version v3.5.0 (4 août 2026).
- 2 août 2026 : Star 23 488 → 23 807, dernière version v3.4.6 (31 juillet 2026).

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
- Source officielle →
Pour commencer à utiliser Argo CD, vous pouvez visiter la page de documentation officielle et suivre les étapes d'installation. Vous pouvez consulter la démo en direct pour comprendre le fonctionnement du projet et parcourir le site de documentation du CD Argo pour accéder à des guides complets.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/argo-cd/
