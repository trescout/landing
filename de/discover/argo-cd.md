# Automatisieren Sie Kubernetes-Bereitstellungen

Argo CD ist ein Tool, das deklarative kontinuierliche Bereitstellungsprozesse für Kubernetes-Umgebungen verwaltet. Es bietet automatische Aktualisierungen der Infrastruktur durch die Synchronisierung des Anwendungsstatus mit Git-Repositorys.

- ★ 23.853
- Go
- GitHub Trending · 2026-07-09

## Aktualisieren
- 6. August 2026: Star 23.807 → 23.853, neueste Version v3.5.0 (4. August 2026).
- 2. August 2026: Star 23.488 → 23.807, neueste Version v3.4.6 (31. Juli 2026).

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
Um mit der Verwendung der Argo-CD zu beginnen, können Sie die offizielle Dokumentationsseite besuchen und den Installationsschritten folgen. Sie können sich die Live-Demo ansehen, um zu verstehen, wie das Projekt funktioniert, und auf der Argo-CD-Dokumentationsseite nach umfassenden Anleitungen suchen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/argo-cd/
