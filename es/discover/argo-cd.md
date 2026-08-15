# Automatizar las implementaciones de Kubernetes

Argo CD es una herramienta que gestiona procesos declarativos de implementación continua para entornos Kubernetes. Proporciona actualizaciones automáticas de la infraestructura sincronizando los estados de las aplicaciones con los repositorios de Git.

- ★ 23.853
- Go
- GitHub Trending · 2026-07-09

## Qué aporta
- Sincronización automática de aplicaciones con repositorios Git
- Procesos de distribución declarativos y rastreables.
- Gestión optimizada del ciclo de vida en entornos Kubernetes

## Instalación
**Crear espacio de nombres**

```
kubectl create namespace argocd
```

**Aplicar manifiesto oficial**

```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```


## Ejecución
**Interfaz de acceso**

```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```


## Cómo empezar
- Fuente oficial →

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/argo-cd/
