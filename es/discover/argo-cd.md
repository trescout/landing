# Automatizar las implementaciones de Kubernetes

Argo CD es una herramienta que gestiona procesos declarativos de implementación continua para entornos Kubernetes. Proporciona actualizaciones automáticas de la infraestructura sincronizando los estados de las aplicaciones con los repositorios de Git.

- ★ 24.345
- Go
- GitHub Trending · 2026-07-09

## Actualizaciones

- **7 de octubre de 2026:** Estrellas 24,154 → 24,345, última versión v3.5.4 (6 de octubre de 2026).
- **14 de septiembre de 2026:** Estrellas 24,005 → 24,154, última versión v3.5.3 (14 de septiembre de 2026).
- **27 de agosto de 2026:** Estrellas 23,927 → 24,005, última versión v3.5.2 (27 de agosto de 2026).
- **15 de agosto de 2026:** Estrellas 23,853 → 23,927, última versión v3.5.1 (12 de agosto de 2026).

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

- [Declarative Continuous Deployment](https://trescout.com/es/dictionary/declarative-continuous-deployment/)
- [Continuous Deployment](https://trescout.com/es/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)

- **Para quién es:** Es adecuado para equipos de software y DevOps que desean automatizar los procesos de implementación y ciclo de vida de sus aplicaciones que se ejecutan en Kubernetes.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://argo-cd.readthedocs.io)
- [Leer en turco →](https://trescout.com/discover/argo-cd/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-09: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/argo-cd/
