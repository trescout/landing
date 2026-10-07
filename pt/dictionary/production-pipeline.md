# O que é Production Pipeline?

O pipeline de produção (production pipeline) é uma cadeia de processos de engenharia integrados que permite que o código-fonte escrito pelos desenvolvedores de software seja compilado, testado, submetido a varreduras de segurança, empacotado e implantado no ambiente de produção com zero tempo de inatividade.

## Origem conceitual, etimologia e a filosofia da linha de produção
A palavra "pipeline" foi emprestada da engenharia de software a partir dos oleodutos e gasodutos de transporte de petróleo e água; "production" foi emprestada das linhas de montagem (assembly line) das fábricas industriais. Assim como a revolução que Henry Ford criou na indústria automotiva com a linha de produção em série no início do século XX, o pipeline de produção é o padrão industrial moderno no setor de software que acaba com os processos de implantação manuais, propensos a erros e incertos.

## As 5 estações críticas de uma linha de produção
Um pipeline de produção corporativo completo consiste nas seguintes etapas:

## Distinções setoriais: Pipeline de Produção vs Pipeline de Dados vs Pipeline de VFX
A palavra "Pipeline" tem significados diferentes em disciplinas técnicas distintas:

## Métricas DORA e produtividade de engenharia
A maturidade do pipeline de produção de uma organização é medida pelas quatro métricas de ouro estabelecidas na pesquisa DORA (DevOps Research and Assessment) do Google:

## Perguntas frequentes
**O que significa pipeline de produção e qual é o seu objetivo principal?**
Significa pipeline de produção de software. Tem como objetivo garantir que o código-fonte desenvolvido seja testado e compilado automaticamente, livre de erros humanos, e entregue com segurança aos servidores de produção.

**Qual é a diferença entre pipeline de produção e CI/CD?**
CI/CD (Integração Contínua / Entrega Contínua) é a metodologia fundamental e a espinha dorsal do pipeline. Já o pipeline de produção é o nome do sistema abrangente que, além de CI/CD, engloba provisionamento de ambiente, verificações de segurança (DevSecOps), mecanismos de aprovação e ferramentas de observabilidade.

**Com quais ferramentas o pipeline de produção é construído?**
GitHub e GitLab para controle de versão; GitHub Actions, Jenkins e ArgoCD para orquestração; Docker para empacotamento; Kubernetes e Terraform para infraestrutura são as ferramentas mais comuns.

**Ocorre interrupção no sistema durante a implantação?**
Em um pipeline de produção bem projetado, são utilizados métodos de implantação Blue-Green ou Canary; dessa forma, os usuários são transferidos para a nova versão sem sentir interrupções (zero-downtime).


## Termos relacionados
- [Deployment](/pt/dictionary/deployment/)
- [Data Pipeline](/pt/dictionary/data-pipeline/)
- [Cloud Computing](/pt/dictionary/cloud-computing/)
- [Tech Stack](/pt/dictionary/tech-stack/)
- [Git Push](/pt/dictionary/git-push/)
- [Runtime](/pt/dictionary/runtime/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/production-pipeline/
