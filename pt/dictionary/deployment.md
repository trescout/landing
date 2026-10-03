# O que é Deployment?

Deployment (implantação de software / lançamento em produção), é o processo pelo qual um componente de software, desenvolvido e testado em um ambiente local, é compilado e instalado em servidores de destino ou em uma infraestrutura de nuvem, tornando-se acessível aos usuários finais.

## Estrutura conceitual, etimologia e transformação histórica
Etimologicamente, o termo deployment baseia-se na terminologia militar; refere-se ao envio de tropas, munições ou equipamentos para posições estratégicas de combate, preparando-os para a operação ("to deploy"). Na engenharia de software, começou nas décadas de 1970 e 1980 com o carregamento de cartões perfurados ou fitas magnéticas em mainframes; evoluiu na década de 1990 para transferências de arquivos FTP/SSH executadas manualmente e, hoje, transformou-se em pipelines de nuvem totalmente declarativos e automatizados (GitOps).

## Estratégias de implantação com tempo de inatividade zero (Zero-Downtime)
Os principais padrões de implantação desenvolvidos para garantir que os usuários não sofram interrupções de serviço enquanto os aplicativos são atualizados são os seguintes:

## Pipeline CI/CD, GitOps e migrações de banco de dados
Uma arquitetura de implantação bem-sucedida é construída sobre três pilares fundamentais de engenharia:

## Gerenciamento de erros, observabilidade e arquitetura de Rollback
Existem duas boias de salvação fundamentais para erros no ambiente de produção que passam despercebidos até mesmo nos ambientes de teste mais avançados:

## Costuma ser confundido com

## Perguntas frequentes
**O que significa Deployment e qual é a tradução em português?**
É uma palavra de origem inglesa que significa 'implantação' ou 'colocação em produção'. É o processo de compilação de um pacote de software para torná-lo funcional em servidores de destino ou em ambiente de nuvem.

**Qual é a diferença entre Deployment e Release?**
O deployment é a instalação técnica e execução do código no servidor. Já o release é a disponibilização oficial do recurso para o usuário final por meio de Feature Flags ou etapas de marketing.

**Qual é a principal diferença entre o deployment Azul-Verde (Blue-Green) e o Canary?**
No deployment Azul-Verde, existem dois ambientes idênticos e o tráfego é transferido 100% para o novo ambiente de uma só vez através de um balanceador de carga. No deployment Canary, por sua vez, a nova versão é disponibilizada gradualmente, primeiro para uma pequena fatia de usuários de 1% a 5%, e a proporção é aumentada após a observação das métricas.

**Como as alterações de esquema de banco de dados são gerenciadas em um deployment sem interrupções (Zero-Downtime)?**
Elas são gerenciadas com o padrão Expand-Contract (Expandir e Contrair). Primeiro, novos campos retrocompatíveis são adicionados; após todos os servidores do sistema mudarem para o novo código e o fluxo de dados se estabilizar, os campos antigos são removidos.


## Termos relacionados
- [Runtime](/pt/dictionary/runtime/)
- [Compile-time](/pt/dictionary/compile-time/)
- [Cloud Computing](/pt/dictionary/cloud-computing/)
- [Production Pipeline](/pt/dictionary/production-pipeline/)
- [Tech Stack](/pt/dictionary/tech-stack/)
- [Git Push](/pt/dictionary/git-push/)

## Ferramentas relacionadas
- [Rocket.Chat](/pt/discover/rocket-chat/)
- [Chatwoot](/pt/discover/chatwoot/)
- [Argo Cd](/pt/discover/argo-cd/)
- [Openship](/pt/discover/openship/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/deployment/
