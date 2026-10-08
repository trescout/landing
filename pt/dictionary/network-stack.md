# O que é Network Stack?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

Pilha de rede é o conjunto de camadas de driver de hardware, kernel e protocolo de espaço do usuário que permitem que um sistema operacional ou hardware transmita, roteie e receba pacotes de dados pela rede.

## Arquitetura da Camada 1: OSI Camada 7 vs TCP/IP Camada 4

Na comunicação em rede, o modelo OSI de 7 camadas definido pela ISO é usado na teoria, e na prática o modelo TCP/IP, que forma a espinha dorsal da Internet:

- Camada de aplicação (L7): HTTP/HTTPS, DNS, SSH, gRPC. É o nível em que os dados são apresentados ou produzidos ao usuário.
- Camada de Transporte (L4): TCP (transmissão confiável e sequencial), UDP (streaming orientado a taxas) e QUIC (HTTP/3 base). A unidade de dados do protocolo é chamada Segmento.
- Camada Internet/Rede (L3): IPv4, IPv6, ICMP, BGP. Ele permite que os pacotes sejam roteados ao redor do mundo. A unidade de dados do protocolo é chamada Pacote.
- Interface de Rede/Camada de Link (L2/L1): Ethernet (802.3), Wi-Fi (802.11), fibra óptica e linhas de cobre. The protocol data unit is defined as Frame.

***Analogia:** É semelhante a uma operação de carga internacional: você escreve a carta (Aplicativo), coloca a carta no envelope e anexa o recibo registrado (TCP), coloca o envelope em um pacote com endereço internacional (IP), o pacote é carregado em um contêiner (Ethernet Frame) e atravessa o oceano no navio cargueiro (Linha física).*

## 2. Encapsulamento de pacotes e fluxo de decodificação

Quando um cliente envia uma solicitação ao servidor web, cada camada adiciona seu próprio cabeçalho à medida que os dados descem na pilha:

```
[Kullanıcı Verisi: "GET / HTTP/1.1"]
                   ↓ (Taşıma Katmanı - TCP başlığı eklenir: Portlar, Sıra No)
[TCP Header | Payload]  --> TCP Segment (MSS ~1460 bayt)
                   ↓ (Ağ Katmanı - IP başlığı eklenir: Kaynak/Hedef IP)
[IP Header | TCP Header | Payload]  --> IP Paketi (MTU: 1500 bayt)
                   ↓ (Veri Bağı Katmanı - Ethernet başlığı ve FCS kuyruğu eklenir)
[Ethernet Header | IP Header | TCP Header | Payload | FCS Tail]  --> Ethernet Frame
```

Ao chegar ao servidor alvo, o processo é revertido (Descapsulação); Camada por camada, os cabeçalhos são removidos e os dados são entregues ao soquete.

## 3. Ciclo de vida da pilha de rede no kernel Linux

1. Hardware e Ring Buffer: A NIC captura o pacote e o copia via DMA para o RX Ring Buffer na RAM.
2. Hard IRQ e SoftIRQ (NAPI): NIC lança interrupção de hardware; O kernel pesquisa pacotes com ksoftirqd no modo NAPI para evitar bloqueio de CPU.
3. sk_buff (Socket Buffer): O kernel aloca a estrutura de dados sk_buff que carrega ponteiros para cada pacote.
4. Filtragem e roteamento: as regras do nftables são verificadas e se o pacote pertencer ao soquete local, ele é entregue à máquina de estado TCP.
5. Chamada de Sistema: O pacote é colocado no buffer de recebimento do soquete (recv-Q); A aplicação lê os dados com epoll_wait().

## 4. Kernel Bypass e rede de próxima geração: eBPF/XDP e DPDK

- eBPF e XDP (eXpress Data Path): O pacote é filtrado na camada do driver da placa de rede antes que o sk_buff seja alocado; É aqui que gigantes como a Cloudflare reduzem os ataques DDoS sem sobrecarregar o núcleo.
- DPDK (Data Plane Development Kit): Ignora completamente o kernel; A aplicação no espaço do usuário acessa diretamente a memória da placa de rede sem nenhuma cópia.
- QUIC/HTTP/3: Em vez do TCP central na camada de transporte, um protocolo criptografado baseado em UDP que é executado no espaço do usuário e supera o bloqueio Head-of-Line foi trocado.

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

- [VPN](https://trescout.com/pt/dictionary/vpn/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Memory Management](https://trescout.com/pt/dictionary/memory-management/)
- [Packet Fragmentation](https://trescout.com/pt/dictionary/packet-fragmentation/)
- [API](https://trescout.com/pt/dictionary/api/)

## Ferramentas relacionadas

- [OpenFlux](https://trescout.com/pt/discover/openflux/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/network-stack/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/network-stack/
