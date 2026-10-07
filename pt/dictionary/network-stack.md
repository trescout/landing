# O que é Network Stack?

Pilha de rede é o conjunto de camadas de driver de hardware, kernel e protocolo de espaço do usuário que permitem que um sistema operacional ou hardware transmita, roteie e receba pacotes de dados pela rede.

## Arquitetura da Camada 1: OSI Camada 7 vs TCP/IP Camada 4
Na comunicação em rede, o modelo OSI de 7 camadas definido pela ISO é usado na teoria, e na prática o modelo TCP/IP, que forma a espinha dorsal da Internet:

## 2. Encapsulamento de pacotes e fluxo de decodificação
Quando um cliente envia uma solicitação ao servidor web, cada camada adiciona seu próprio cabeçalho à medida que os dados descem na pilha:

## 3. Ciclo de vida da pilha de rede no kernel Linux

## 4. Kernel Bypass e rede de próxima geração: eBPF/XDP e DPDK

## Perguntas frequentes
**O que significa pilha de rede, qual é o seu equivalente turco?**
É chamado de "pilha de rede" ou "pilha de protocolo" em turco. É uma hierarquia de regras sobrepostas de hardware e software que permitem que um computador se comunique através de uma rede.

**Onde está a principal diferença entre TCP e UDP na pilha de rede?**
Está localizado na camada de transmissão (Camada de Transporte/L4). O TCP garante que os pacotes cheguem completamente e em ordem com um mecanismo de confirmação (ACK); O UDP, por outro lado, envia pacotes na velocidade mais alta sem esperar confirmação.

**O que é MTU (Unidade Máxima de Transmissão)?**
É o maior tamanho de pacote que uma interface de rede pode transportar em um único quadro sem fragmentação. O valor MTU para Ethernet padrão é 1.500 bytes.

**Por que a arquitetura Kernel Bypass é usada?**
Eliminação dos custos de interrupção e cópia de memória do kernel Linux em volumes de dados extremamente altos, como 100 Gbps; É usado com DPDK e eBPF/XDP para processar pacotes diretamente no nível de hardware com latência zero.


## Termos relacionados
- [VPN](/pt/dictionary/vpn/)
- [Runtime](/pt/dictionary/runtime/)
- [Memory Management](/pt/dictionary/memory-management/)
- [Packet Fragmentation](/pt/dictionary/packet-fragmentation/)
- [API](/pt/dictionary/api/)

## Ferramentas relacionadas
- [OpenFlux](/pt/discover/openflux/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/network-stack/
