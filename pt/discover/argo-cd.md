# Automatize implantações do Kubernetes

Argo CD é uma ferramenta que gerencia processos declarativos de implantação contínua para ambientes Kubernetes. Ele fornece atualizações automáticas na infraestrutura, sincronizando os estados do aplicativo com os repositórios Git.

- ★ 24.377
- Go
- GitHub Trending · 2026-07-09

## Atualizações

- **12 de outubro de 2026:** Estrelas 24,345 → 24,377, versão mais recente v3.5.5 (12 de outubro de 2026).
- **7 de outubro de 2026:** Estrelas 24,154 → 24,345, versão mais recente v3.5.4 (6 de outubro de 2026).
- **14 de setembro de 2026:** Estrelas 24,005 → 24,154, versão mais recente v3.5.3 (14 de setembro de 2026).
- **27 de agosto de 2026:** Estrelas 23,927 → 24,005, versão mais recente v3.5.2 (27 de agosto de 2026).

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

Para começar a usar o Argo CD, você pode visitar a página de documentação oficial e seguir os passos de instalação. Você pode revisar a demonstração ao vivo para entender como o projeto funciona e navegar no site de documentação do Argo CD para acessar guias completos.

- [Fonte oficial →](https://argo-cd.readthedocs.io)

## Termos relacionados do glossário

- [Declarative Continuous Deployment](https://trescout.com/pt/dictionary/declarative-continuous-deployment/)
- [Continuous Deployment](https://trescout.com/pt/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)

- **Para quem é:** É adequado para equipes de software e DevOps que desejam automatizar os processos de implantação e ciclo de vida de seus aplicativos em execução no Kubernetes.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/argoproj/argo-cd)
- [Ler em turco →](https://trescout.com/discover/argo-cd/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-09: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/argo-cd/
