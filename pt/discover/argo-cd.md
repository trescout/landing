# Automatize implantações do Kubernetes

Argo CD é uma ferramenta que gerencia processos declarativos de implantação contínua para ambientes Kubernetes. Ele fornece atualizações automáticas na infraestrutura, sincronizando os estados do aplicativo com os repositórios Git.

- ★ 23.853
- Go
- GitHub Trending · 2026-07-09

## Atualizar
- 6 de agosto de 2026: Star 23.807 → 23.853, versão mais recente v3.5.0 (4 de agosto de 2026).
- 2 de agosto de 2026: Star 23.488 → 23.807, versão mais recente v3.4.6 (31 de julho de 2026).

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
Para começar a usar o Argo CD, você pode visitar a página de documentação oficial e seguir os passos de instalação. Você pode revisar a demonstração ao vivo para entender como o projeto funciona e navegar no site de documentação do Argo CD para acessar guias completos.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/argo-cd/
