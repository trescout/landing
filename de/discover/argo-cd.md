# Automatisieren Sie Kubernetes-Bereitstellungen

Argo CD ist ein Tool, das deklarative kontinuierliche Bereitstellungsprozesse für Kubernetes-Umgebungen verwaltet. Es bietet automatische Aktualisierungen der Infrastruktur durch die Synchronisierung des Anwendungsstatus mit Git-Repositorys.

- ★ 23.927
- Go
- GitHub Trending · 2026-07-09

## Was es bringt
- Automatische Anwendungssynchronisierung mit Git-Repositorys
- Deklarative und nachverfolgbare Vertriebsprozesse
- Optimiertes Lebenszyklusmanagement in Kubernetes-Umgebungen

## Installation
**Namensraum erstellen**

```
kubectl create namespace argocd
```

**Wenden Sie das offizielle Manifest an**

```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```


## Ausführung
**Zugriffsschnittstelle**

```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```


## So fangen Sie an
- Offizielle Quelle →

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/argo-cd/
