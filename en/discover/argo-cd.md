# Automate Kubernetes Deployments

Argo CD is a tool that manages declarative continuous deployment processes for Kubernetes environments. It provides automatic updates on the infrastructure by synchronizing application states with Git repositories.

- ★ 24,345
- Go
- GitHub Trending · 2026-07-09

## Updates

- **October 7, 2026:** Stars 24,154 → 24,345, latest release v3.5.4 (October 6, 2026).
- **September 14, 2026:** Stars 24,005 → 24,154, latest release v3.5.3 (September 14, 2026).
- **August 27, 2026:** Stars 23,927 → 24,005, latest release v3.5.2 (August 27, 2026).
- **August 15, 2026:** Stars 23,853 → 23,927, latest release v3.5.1 (August 12, 2026).

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

- [Declarative Continuous Deployment](https://trescout.com/en/dictionary/declarative-continuous-deployment/)
- [Continuous Deployment](https://trescout.com/en/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/en/dictionary/deployment/)

- **Who it is for:** It is suitable for software and DevOps teams that want to automate the deployment and lifecycle processes of their applications running on Kubernetes.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://argo-cd.readthedocs.io)
- [Read in Turkish →](https://trescout.com/discover/argo-cd/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-09: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/argo-cd/
