# Automate Kubernetes Deployments

Argo CD is a tool that manages declarative continuous deployment processes for Kubernetes environments. It provides automatic updates on the infrastructure by synchronizing application states with Git repositories.

- ★ 24,005
- Go
- GitHub Trending · 2026-07-09

## What you get
- Automatic application synchronization with Git repositories
- Declarative and trackable distribution processes
- Streamlined lifecycle management in Kubernetes environments

## Installation
**Create namespace**

```
kubectl create namespace argocd
```

**Apply official manifesto**

```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```


## Running it
**Access interface**

```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```


## Getting started
- Official source →

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/argo-cd/
