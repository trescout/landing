# Automate Kubernetes Deployments

Argo CD is a tool that manages declarative continuous deployment processes for Kubernetes environments. It provides automatic updates on the infrastructure by synchronizing application states with Git repositories.

- ★ 23,853
- Go
- GitHub Trending · 2026-07-09

## Update
- August 6, 2026: Star 23,807 → 23,853, latest version v3.5.0 (August 4, 2026).
- August 2, 2026: Star 23,488 → 23,807, latest version v3.4.6 (July 31, 2026).

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
To start using Argo CD, you can visit the official documentation page and follow the installation steps. You can review the live demo to understand how the project works and browse the Argo CD documentation site to access comprehensive guides.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/argo-cd/
