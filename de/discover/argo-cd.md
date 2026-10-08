# Automatisieren Sie Kubernetes-Bereitstellungen

Argo CD ist ein Tool, das deklarative kontinuierliche Bereitstellungsprozesse für Kubernetes-Umgebungen verwaltet. Es bietet automatische Aktualisierungen der Infrastruktur durch die Synchronisierung des Anwendungsstatus mit Git-Repositorys.

- ★ 24.345
- Go
- GitHub Trending · 2026-07-09

## Aktualisierungen

- **7. Oktober 2026:** Sterne 24,154 → 24,345, neueste Version v3.5.4 (6. Oktober 2026).
- **14. September 2026:** Sterne 24,005 → 24,154, neueste Version v3.5.3 (14. September 2026).
- **27. August 2026:** Sterne 23,927 → 24,005, neueste Version v3.5.2 (27. August 2026).
- **15. August 2026:** Sterne 23,853 → 23,927, neueste Version v3.5.1 (12. August 2026).

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

- [Declarative Continuous Deployment](https://trescout.com/de/dictionary/declarative-continuous-deployment/)
- [Continuous Deployment](https://trescout.com/de/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)

- **Für wen es gedacht ist:** Es eignet sich für Software- und DevOps-Teams, die die Bereitstellungs- und Lebenszyklusprozesse ihrer auf Kubernetes ausgeführten Anwendungen automatisieren möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://argo-cd.readthedocs.io)
- [Auf Türkisch lesen →](https://trescout.com/discover/argo-cd/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-09 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/argo-cd/
