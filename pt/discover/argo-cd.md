# Automatize implantações do Kubernetes

Argo CD é uma ferramenta que gerencia processos declarativos de implantação contínua para ambientes Kubernetes. Ele fornece atualizações automáticas na infraestrutura, sincronizando os estados do aplicativo com os repositórios Git.

- ★ 24.005
- Go
- GitHub Trending · 2026-07-09

## O que você ganha
- Sincronização automática de aplicativos com repositórios Git
- Processos de distribuição declarativos e rastreáveis
- Gerenciamento simplificado do ciclo de vida em ambientes Kubernetes

## Instalação
**Criar namespace**

```
kubectl create namespace argocd
```

**Aplicar manifesto oficial**

```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```


## Execução
**Interface de acesso**

```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```


## Como começar
- Fonte oficial →

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/argo-cd/
