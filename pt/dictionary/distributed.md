# O que é Distributed?

*Desenvolvimento · Última atualização: 19 de setembro de 2026*

Distribuído, no mundo da computação, é o compartilhamento de hardware, dados e processos de cálculo entre muitos servidores independentes (nós) conectados entre si pela rede, em vez de uma única máquina central, e esse sistema atende ao usuário final como se fosse um único computador inteiro.

## Etimologia e a natureza dos sistemas distribuídos

A palavra "Distribuído" significa distribuído em turco. Leslie Lamport, uma das pioneiras da ciência da computação, definiu sistemas distribuídos com o seguinte aforismo que entrou para a história: “Um sistema distribuído é um sistema no qual a falha de um computador que você nem sabe que existe pode inutilizar seu próprio computador”.

Nas arquiteturas centralizadas (monolíticas), todas as operações ocorrem em uma única memória principal e processador. Em sistemas distribuídos, centenas de nós espalhados fisicamente por data centers em diferentes continentes do mundo atendem a um propósito comum, comunicando-se por meio de cabos de rede não confiáveis.

## 8 falácias da computação distribuída

Na década de 1990, os engenheiros da Sun Microsystems, L. Peter Deutsch e James Gosling, listaram os "8 erros mortais" cometidos por desenvolvedores de software que desenvolvem sistemas distribuídos. Todas as linhas de defesa das arquiteturas modernas de nuvem e microsserviços são construídas de acordo com estes equívocos:

1. A rede é confiável: na realidade, os pacotes são perdidos, as linhas de fibra quebram, os roteadores travam.
2. A latência é zero: a velocidade da luz e a latência de comutação de rede entre duas máquinas estão sempre presentes.
3. A largura de banda é infinita: À medida que o volume de dados aumenta, os canais da rede ficam obstruídos.
4. A rede é segura: toda comunicação distribuída passa por linhas abertas e requer proteção criptográfica.
5. A topologia não muda: os servidores são constantemente ligados e desligados, os endereços IP mudam.
6. Existe apenas um administrador de sistema: múltiplas equipes e provedores de nuvem estão envolvidos.
7. O custo de transporte é zero: Os custos de serialização e empacotamento da CPU não podem ser ignorados.
8. A rede é homogênea: Linux, Windows, ARM, x86 e diferentes protocolos trabalham juntos no sistema.

## Teorema CAP e modelo PACELC

O Teorema CAP, proposto por Eric Brewer, traça os limites fundamentais do gerenciamento distribuído de dados. Quando ocorre uma partição de rede (P), o sistema deve escolher uma de duas opções:

- CP (Consistência + Tolerância de Partição): O sistema seleciona consistência. Os nós cujos dados estão desatualizados recusam-se a responder; a acessibilidade é sacrificada (transações financeiras e bancárias, por exemplo).
- AP (Disponibilidade + Tolerância de Partição): O sistema seleciona a disponibilidade. Os nós continuam respondendo, mas alguns usuários podem ver dados desatualizados de alguns segundos atrás (por exemplo, feeds de mídia social).

Nos sistemas modernos, utiliza-se o Modelo PACELC de Daniel Abadi: Quando a rede está dividida (P) Disponibilidade ou Consistência; Quando o sistema estiver operando normalmente, Else (E) Latency (baixa latência) ou Consistency (consistência instantânea) será direcionado?

## Protocolos de consenso: Raft e Paxos

Algoritmos de consenso foram desenvolvidos para que servidores independentes, que não confiam uns nos outros e podem travar a qualquer momento, possam concordar com uma única verdade:

- Paxos: Algoritmo de consenso desenvolvido por Leslie Lamport, comprovado matematicamente, mas extremamente complexo de implementar na prática.
- Raft: Um protocolo de consenso humano-inteligente desenvolvido por Diego Ongaro e John Ousterhout para resolver a complexidade de Paxos. Leader Election é baseado em máquinas de estado de segurança e replicação de log (funciona no coração de sistemas gigantes como Etcd, Kubernetes, Consul).
- Tolerância a Falhas Bizantinas (BFT): É a base dos protocolos blockchain que garantem consenso mesmo em ambientes onde alguns nós espalham deliberadamente informações errôneas ou maliciosas.

## Problema de tempo e soluções em sistemas distribuídos

Num computador central, o relógio do hardware representa um fato único. Em sistemas distribuídos, os relógios dos servidores mostram desvios do relógio físico e o NTP (Network Time Protocol) é insuficiente para precisão de milissegundos:

- Lamport Logical Times (Lamport Timestamps): Define a "ordem dos eventos" em vez do tempo físico.
- Relógios vetoriais: detecta conflitos de dados determinando quais dados são causa ou efeito um do outro.
- Google TrueTime: Combinação de relógios atômicos e antenas GPS utilizadas no banco de dados distribuído do Google Spanner. Permite transações ACID em escala global, reduzindo a margem de incerteza para alguns milissegundos.

## Gerenciamento distribuído de dados e transações: Padrão Saga

As transações de banco de dados (transações ACID) em sistemas monolíticos são substituídas pela abordagem Saga Pattern em microsserviços. Em vez de etapas distribuídas de longa duração serem bloqueadas com bloqueios de duas fases (2PC - Two Phase Commit); São utilizadas arquiteturas orientadas a eventos onde cada serviço executa sua ação local e, em caso de erro, são acionadas transações de compensação retroativas.

## Perguntas Frequentes

**O que significa Distribuído (significado turco)?**

Na terminologia de TI, significa “distribuído”. É o compartilhamento de poder de computação, espaço de memória ou banco de dados entre muitas máquinas independentes que se comunicam em uma rede, em vez de um único servidor.

**O que o Teorema CAP significa na prática?**

Isso significa que quando há uma interrupção ou atraso (divisão) na conexão de rede, o sistema deve garantir os dados mais atualizados e reter algumas solicitações (Consistência), ou responder a todas as solicitações imediatamente, às custas de fornecer dados obsoletos (Disponibilidade).

**Por que o algoritmo de consenso Raft é usado em sistemas distribuídos?**

Mesmo que alguns servidores da rede caiam, a maioria restante é usada para garantir que os nós (Quorum) elejam um novo líder entre eles e os logs do banco de dados sejam sincronizados sem perdas em todo o cluster.

**Por que o padrão Saga é preferido ao compromisso de duas fases (2PC)?**

2PC (Two-Phase Commit) bloqueia recursos de banco de dados em nós distribuídos e bloqueia todo o sistema quando uma máquina deixa de responder. O padrão Saga, por outro lado, mantém a alta disponibilidade do sistema utilizando eventos assíncronos e etapas de compensação.

## Termos relacionados

- [Cloud Computing](https://trescout.com/pt/dictionary/cloud-computing/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)

## Ferramentas relacionadas

- [Elasticsearch](https://trescout.com/pt/discover/elasticsearch/)
- [Cassandra](https://trescout.com/pt/discover/cassandra/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/distributed/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/distributed/
