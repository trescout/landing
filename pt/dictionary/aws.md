# O que é AWS?

> Amazon Web Services

**Categoria:** Dev  
**Última atualização:** 2026-09-22

AWS (Amazon Web Services) é a plataforma em nuvem da Amazon que oferece infraestrutura sob demanda de servidores, banco de dados, armazenamento e ferramentas de software pela internet.

## Definição e etimologia
Em vez de adquirir servidores físicos dispendiosos para manter em data centers locais, empresas alugam capacidade elástica dos centros de processamento da Amazon. A infraestrutura cresce em picos de demanda e diminui quando a atividade cai, operando no modelo de pagamento pelo que for consumido.

## Contexto cotidiano e uso prático
- **Aplicações Web:** Servidores que escalam dinamicamente durante campanhas promocionais.
- **Backup e Conformidade:** Armazenamento seguro de longo prazo para dados corporativos críticos.
- **Distribuição de Vídeo:** Pontos de presença globais que entregam streaming com latência mínima.
- **Startups:** Operações globais viabilizadas sem necessidade de investimento em hardware prévio.

## Profundidade técnica e arquitetura
Principais Serviços Estruturais :- **EC2:** Máquinas virtuais com capacidades customizadas de CPU e memória RAM.
- **S3:** Armazenamento de objetos com altíssima durabilidade e redundância de dados.
- **RDS:** Gerenciamento automatizado de bancos relacionais como PostgreSQL e MySQL.
- **Lambda:** Computação serverless executada estritamente quando há demanda de eventos.

Organiza-se em Regiões e Zonas de Disponibilidade (AZs). O Modelo de Responsabilidade Compartilhada determina que a AWS protege a infraestrutura física, cabendo ao cliente configurar a segurança de seus sistemas e dados.<div class="disc-cmd"><div class="disc-cmd-head"><span>Listar instâncias ativas via AWS CLI</span></div><pre><code>aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"</code></pre></div>

## Costuma ser confundido com
Costuma ser confundida com hospedagem de sites tradicional. Uma hospedagem comum apenas serve páginas simples; a AWS é um ecossistema com centenas de serviços integrados de inteligência artificial, mensageria e redes privadas.

## Perspectivas interdisciplinares
- **Rede de Energia:** Usar a tomada elétrica pública em vez de gerenciar um gerador a diesel próprio.
- **Self Storage:** Alugar compartimentos conforme a quantidade de caixas aumenta.
- **Transporte por App:** Pagar apenas pelo trajeto percorrido sem assumir custos de um veículo próprio.

## Por analogia
É como puxar energia da rede elétrica da cidade em vez de montar sua própria usina no quintal: você usa o quanto precisa e paga apenas pelo consumo apurado.

## Perguntas frequentes

**Quais as principais vantagens da AWS?**  
Escalabilidade elástica sem compra de hardware, implantação global rápida e redução de despesas de capital (CapEx para OpEx).

**Existe um plano gratuito para testes?**  
Sim. O AWS Free Tier concede acesso sem custo a limites definidos de instâncias EC2, buckets S3 e execuções no Lambda para novos clientes.

**Onde meus dados ficam fisicamente salvos?**  
Exatamente na Região geográfica que você selecionar ao criar o recurso, respeitando leis locais como a LGPD no Brasil.

**Como evitar surpresas na fatura mensal?**  
Criando alertas de orçamento no AWS Budgets, desativando recursos ociosos e definindo limites rígidos de cobrança.

## Termos relacionados
- [Computação em Nuvem](/pt/dictionary/cloud-computing/)
- [IaaS](/pt/dictionary/iaas/)
- [PaaS](/pt/dictionary/paas/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/aws/
