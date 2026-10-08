# O que é Deployment?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

Deployment (implantação de software / lançamento em produção), é o processo pelo qual um componente de software, desenvolvido e testado em um ambiente local, é compilado e instalado em servidores de destino ou em uma infraestrutura de nuvem, tornando-se acessível aos usuários finais.

## Estrutura conceitual, etimologia e transformação histórica

Etimologicamente, o termo deployment baseia-se na terminologia militar; refere-se ao envio de tropas, munições ou equipamentos para posições estratégicas de combate, preparando-os para a operação ("to deploy"). Na engenharia de software, começou nas décadas de 1970 e 1980 com o carregamento de cartões perfurados ou fitas magnéticas em mainframes; evoluiu na década de 1990 para transferências de arquivos FTP/SSH executadas manualmente e, hoje, transformou-se em pipelines de nuvem totalmente declarativos e automatizados (GitOps).

Na engenharia de software moderna, o deployment deixou de ser uma operação única, dolorosa e de alto risco realizada à meia-noite. Graças aos mecanismos de Integração Contínua e Entrega Contínua (CI/CD), é um fluxo de trabalho padrão onde o código é transferido com segurança para o ambiente de produção centenas de vezes ao dia.

***Analogia:** Assemelha-se à operação de troca de trilhos de um trem de alta velocidade cheio de passageiros. No método tradicional, era necessário parar o trem na estação e soldar os trilhos (tempo de inatividade / downtime); o deployment moderno é como se o trem estivesse a 300 quilômetros por hora e o desvio automático mudasse para a nova linha em milissegundos, sem que os passageiros sintam sequer um solavanco.*

## Estratégias de implantação com tempo de inatividade zero (Zero-Downtime)

Os principais padrões de implantação desenvolvidos para garantir que os usuários não sofram interrupções de serviço enquanto os aplicativos são atualizados são os seguintes:

1. Implantação Azul-Verde (Blue-Green Deployment): Mantêm-se dois ambientes de servidor idênticos, sendo um que recebe o tráfego de produção (Azul) e outro que fica ocioso (Verde). O novo código é implantado no ambiente verde, realizam-se os testes de fumaça (smoke tests) e, quando tudo funciona perfeitamente, o balanceador de carga (Load Balancer) direciona o tráfego para o verde em milissegundos. Se surgir algum problema, o sistema reverte instantaneamente para o azul (rollback instantâneo).
2. Implantação Canária: O nome vem do século XIX, quando os mineiros de carvão levavam um canário na gaiola para detectar vazamentos de gás tóxico precocemente. A nova versão é disponibilizada inicialmente para apenas 1% a 5% do tráfego total de usuários. As taxas de erro (HTTP 5xx), o consumo de memória e os tempos de resposta são monitorados; se o sistema estiver estável, a porcentagem é aumentada gradualmente para 25%, 50% e 100%.
3. Atualização Contínua (Rolling Deployment): É a atualização de containers um a um (por exemplo, em lotes de 20%) em clusters Kubernetes ou frotas de servidores. Os pods antigos são encerrados em sequência e substituídos por pods da nova versão. Não exige custos adicionais com hardware de backup, mas requer o gerenciamento de um período de transição em que duas versões diferentes operam simultaneamente em produção.
4. Implantação Sombria (Shadow / Dark Deployment): O tráfego de usuários em tempo real é copiado (espelhamento de tráfego) e enviado também para a nova versão que roda em segundo plano. No entanto, as respostas geradas pela nova versão não são entregues ao usuário; apenas o desempenho do sistema sob carga real e a precisão do algoritmo são medidos.

## Pipeline CI/CD, GitOps e migrações de banco de dados

Uma arquitetura de implantação bem-sucedida é construída sobre três pilares fundamentais de engenharia:

- Automação de CI/CD e Métricas DORA: Quando um engenheiro faz um commit em um repositório Git, o código passa automaticamente por verificação de lint, testes unitários e de integração são executados, a imagem do contêiner Docker é compilada e implantada no ambiente de destino. De acordo com as métricas do DevOps Research and Assessment (DORA), equipes de alto desempenho reduzem a frequência de implantação (Deployment Frequency) para o nível de horas, enquanto minimizam o tempo de entrega de alterações (Lead Time) e a taxa de falha.
- Princípio do GitOps: É a declaração da infraestrutura e das versões de aplicativos diretamente por um repositório Git usando ferramentas como ArgoCD ou Flux. O repositório Git é a única fonte da verdade (Single Source of Truth); se o estado real nos servidores divergir do estado no Git, o sistema se sincroniza automaticamente.
- O Dilema do Esquema de Banco de Dados (Padrão Expand-Contract): O código pode ser atualizado com tempo de inatividade zero, mas a exclusão de uma coluna nas tabelas do banco de dados pode causar a falha da versão antiga. Por isso, os engenheiros aplicam o padrão "Expandir-Contrair" (Execução Paralela): primeiro, a nova coluna é adicionada e gravada em ambas as versões; após todos os servidores migrarem para a nova versão, a coluna antiga é excluída com segurança.

## Gerenciamento de erros, observabilidade e arquitetura de Rollback

Existem duas boias de salvação fundamentais para erros no ambiente de produção que passam despercebidos até mesmo nos ambientes de teste mais avançados:

- Rollback Automático: Assim que as ferramentas de APM (Datadog, Prometheus) detectam uma anomalia nos limites de erro (por exemplo, quando a taxa de erro excede 1%), elas revertem para a imagem Docker ou tag Git estável anterior sem a necessidade de intervenção humana.
- Feature Flags (Sinalizadores de Recursos): Separam os processos de implantação (deployment) e lançamento (release). Mesmo que o código esteja rodando no servidor, um novo recurso pode ser mantido oculto na interface do usuário; em um momento de risco, ele pode ser desativado instantaneamente com um único interruptor no painel.

## Costuma ser confundido com

- Development vs Deployment: Development (desenvolvimento) mutfakta şefin yemeği hazırlaması ve tatmasıdır; Deployment ise yemeğin masaya servis edilip müşterinin tüketimine sunulmasıdır.
- Deployment vs Release: O deployment é uma ação técnica; refere-se ao carregamento do código no servidor. Já o release é a disponibilização de um recurso para os usuários, a realização do anúncio de marketing e a ativação oficial por parte da unidade de negócios.

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

- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Compile-time](https://trescout.com/pt/dictionary/compile-time/)
- [Cloud Computing](https://trescout.com/pt/dictionary/cloud-computing/)
- [Production Pipeline](https://trescout.com/pt/dictionary/production-pipeline/)
- [Tech Stack](https://trescout.com/pt/dictionary/tech-stack/)
- [Git Push](https://trescout.com/pt/dictionary/git-push/)

## Ferramentas relacionadas

- [Rocket.Chat](https://trescout.com/pt/discover/rocket-chat/)
- [Chatwoot](https://trescout.com/pt/discover/chatwoot/)
- [Argo Cd](https://trescout.com/pt/discover/argo-cd/)
- [Openship](https://trescout.com/pt/discover/openship/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/deployment/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/deployment/
