# Distributed Systems: Falácias, teorema CAP, consenso e padrão Saga

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

Um sistema distribuído é uma infraestrutura computacional composta por múltiplos nós independentes conectados por rede que cooperam entre si para operar como uma única aplicação coerente.

## Etimologia e a Natureza dos Sistemas Distribuídos

O termo origina-se do latim *distribuere* (repartir, ratear). Como definiu Leslie Lamport : *«Um sistema distribuído é aquele no qual a falha de um computador que você nem sabia que existia pode tornar o seu próprio computador inutilizável.»* Em troca dessa complexidade, alcança-se tolerância geográfica a desastres e escalabilidade sem limites.

## As 8 Falácias da Computação Distribuída (Deutsch)

Formuladas na Sun Microsystems, ignorar essas oito suposições ingênuas compromete qualquer arquitetura moderna :

1. A rede é confiável.
2. A latência é zero.
3. A largura de banda é infinita.
4. A rede é segura.
5. A topologia nunca muda.
6. Existe apenas um administrador.
7. O custo de transporte é zero.
8. A rede é homogênea.

## O Teorema CAP e o Modelo PACELC

O **Teorema CAP** de Eric Brewer estabelece que bancos distribuídos só podem preservar duas de três garantias sob partição de rede :

- **Consistência (C):** Cada leitura retorna a gravação mais recente ou um erro de recusa.
- **Disponibilidade (A):** Cada nó saudável responde a requisições sem travar, mesmo sem dados atualizados.
- **Tolerância a Partições (P):** Manter a operação diante de falhas físicas no tráfego de rede. Como falhas de rede são inevitáveis, deve-se optar entre CP (HBase) ou AP (Cassandra).

O modelo **PACELC** complementa : *Se houver Partição (P), escolha entre Disponibilidade (A) e Consistência (C); Senão (Else), escolha entre Latência (L) e Consistência (C).*

## Protocolos de Consenso: Raft e Paxos

Para que nós distribuídos alcancem acordo unânime sobre o estado da aplicação em redes com perdas de pacotes :

- **Paxos:** O modelo formal pioneiro de Leslie Lamport, célebre pela sua elevada complexidade de codificação.
- **Raft:** Desenvolvido especificamente para ser compreensível por seres humanos, estruturado em eleição de líder e replicação de logs (adotado no etcd e Consul).

## O Problema do Tempo e Relógios Lógicos

Sem um relógio atômico central acessível instantaneamente por todos os servidores, ordenar ações no tempo físico gera distorções :

- **Relógios Lógicos de Lamport e Vetoriais:** Contadores abstratos que mapeiam a causalidade lógica das mensagens sem depender de segundos reais.
- **Google TrueTime:** Conjunto de receptores GPS e relógios atômicos instalados nos data centers para limitar a incerteza de sincronização a milissegundos.

## Gestão de Dados Distribuídos: O Padrão Saga

O método clássico de Two-Phase Commit (2PC) bloqueia tabelas e não escala em microsserviços. Adota-se o **Padrão Saga** :

- Cadeia sequencial de transações locais orquestradas por uma máquina de estados ou coreografadas por eventos assíncronos.
- Caso ocorra erro em qualquer etapa intermediária, o sistema executa ações compensatórias reversas para restaurar o estado contábil sem travar recursos.

*Um sistema centralizado é como um cozinheiro solitário que prepara pratos em um quiosque ; um sistema distribuído é como uma rede internacional de restaurantes onde centenas de filiais precisam entregar o mesmo padrão culinário lidando com quedas de sinal e atrasos de frete.*

## Perguntas frequentes

**O que caracteriza um sistema distribuído?**

A coordenação de múltiplos servidores independentes via rede que processam dados cooperativamente como uma entidade única.

**Por que o Teorema CAP impede ter 100% de consistência e disponibilidade simultâneas?**

Porque se o link de rede entre dois servidores romper, você precisa escolher entre pausar o serviço ou permitir que os dois recebam dados divergentes.

**Qual o diferencial do protocolo Raft?**

Ele resolve o problema de consenso distribuído com uma lógica estruturada de fácil compreensão e manutenção em comparação ao Paxos.

**Como o padrão Saga resolve operações em microsserviços?**

Executando passos locais sucessivos com rotinas de compensação para desfazer etapas anteriores caso surja algum erro.

## Termos relacionados

- [Cloud Computing](https://trescout.com/pt/dictionary/cloud-computing/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)

## Ferramentas relacionadas

- [Elasticsearch](https://trescout.com/pt/discover/elasticsearch/)
- [Cassandra](https://trescout.com/pt/discover/cassandra/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/distributed/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/distributed/
