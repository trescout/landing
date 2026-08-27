# Automatisez les déploiements Kubernetes

Argo CD est un outil qui gère les processus de déploiement continu déclaratif pour les environnements Kubernetes. Il fournit des mises à jour automatiques sur l'infrastructure en synchronisant les états des applications avec les référentiels Git.

- ★ 24 005
- Go
- GitHub Trending · 2026-07-09

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

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/argo-cd/
