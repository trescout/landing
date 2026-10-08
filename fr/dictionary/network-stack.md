# Qu'est-ce que Network Stack ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

La pile réseau (Network Stack) est l'ensemble des pilotes matériels, du noyau (kernel) et des couches de protocole de l'espace utilisateur qui permettent à un système d'exploitation ou à un matériel de transmettre, router et recevoir des paquets de données sur un réseau.

## 1. Architecture en couches : 7 couches OSI vs 4 couches TCP/IP

Dans la communication réseau, le modèle OSI à 7 couches défini théoriquement par l'ISO est utilisé, tandis qu'en pratique, c'est le modèle TCP/IP qui constitue l'épine dorsale d'Internet :

- Couche Application (L7) : HTTP/HTTPS, DNS, SSH, gRPC. Il s'agit du niveau où les données sont présentées à l'utilisateur ou générées par celui-ci.
- Couche Transport (L4) : TCP (transmission fiable et ordonnée), UDP (flux axé sur la vitesse) et QUIC (base de HTTP/3). L'unité de données de protocole est appelée Segment.
- Couche Internet / Réseau (L3) : IPv4, IPv6, ICMP, BGP. Assure le routage des paquets à l'échelle mondiale. L'unité de données de protocole est appelée paquet (Packet).
- Interface réseau / Couche de liaison (L2/L1) : Ethernet (802.3), Wi-Fi (802.11), fibre optique et lignes en cuivre. L'unité de données de protocole est définie comme une trame (Frame).

***Analogie :** C'est similaire à une opération de fret international : vous écrivez la lettre (Application), vous mettez la lettre dans une enveloppe et ajoutez un accusé de réception (TCP), vous placez l'enveloppe dans un colis avec une adresse internationale (IP), le colis est chargé dans un conteneur (trame Ethernet) et traverse l'océan par cargo (ligne physique).*

## 2. Flux d'encapsulation et de décapsulation des paquets

Lorsqu'un client envoie une requête à un serveur web, les données descendent la pile et chaque couche ajoute son propre en-tête :

```
[Kullanıcı Verisi: "GET / HTTP/1.1"]
                   ↓ (Taşıma Katmanı - TCP başlığı eklenir: Portlar, Sıra No)
[TCP Header | Payload]  --> TCP Segment (MSS ~1460 bayt)
                   ↓ (Ağ Katmanı - IP başlığı eklenir: Kaynak/Hedef IP)
[IP Header | TCP Header | Payload]  --> IP Paketi (MTU: 1500 bayt)
                   ↓ (Veri Bağı Katmanı - Ethernet başlığı ve FCS kuyruğu eklenir)
[Ethernet Header | IP Header | TCP Header | Payload | FCS Tail]  --> Ethernet Frame
```

Une fois arrivé sur le serveur cible, le processus s'inverse (décapsulation) ; les en-têtes sont retirés couche par couche et les données sont transmises au socket.

## 3. Cycle de vie de la pile réseau dans le noyau Linux (Kernel)

1. Matériel et Ring Buffer : La carte réseau (NIC) capture le paquet et le copie dans le RX Ring Buffer de la RAM via DMA.
2. Hard IRQ & SoftIRQ (NAPI) : La carte réseau (NIC) déclenche une interruption matérielle ; pour éviter le blocage du CPU, le noyau traite les paquets par lots (polling) via ksoftirqd en mode NAPI.
3. sk_buff (Socket Buffer) : Le noyau alloue la structure de données sk_buff, qui contient les pointeurs pour chaque paquet.
4. Filtrage et routage : les règles nftables sont analysées et, si le paquet appartient à une socket locale, il est transmis à la machine d'état TCP.
5. Appel système : Le paquet est placé dans le tampon de réception (recv-Q) du socket ; l'application lit les données via epoll_wait().

## 4. Kernel Bypass et réseau de nouvelle génération : eBPF / XDP et DPDK

- eBPF et XDP (eXpress Data Path) : le paquet est filtré au niveau de la couche pilote de la carte réseau avant même l'allocation du sk_buff ; des géants comme Cloudflare y bloquent les attaques DDoS sans aucune charge pour le noyau.
- DPDK (Data Plane Development Kit) : contourne entièrement le noyau ; l'application en espace utilisateur accède directement à la mémoire de la carte réseau avec zéro copie.
- QUIC / HTTP/3 : Le protocole de transport TCP au niveau du noyau a été remplacé par un protocole chiffré basé sur UDP, fonctionnant dans l'espace utilisateur et permettant de contourner le blocage en tête de ligne (Head-of-Line blocking).

## Questions fréquentes

**Que signifie « network stack » et quel est son équivalent en français ?**

En français, on l'appelle « pile réseau » ou « pile de protocoles ». Il s'agit d'une hiérarchie de règles matérielles et logicielles superposées qui permettent à un ordinateur de communiquer via un réseau.

**Où se situe la différence fondamentale entre TCP et UDP dans la pile réseau ?**

Elle se situe au niveau de la couche de transport (Transport Layer / L4). TCP garantit que les paquets arrivent complets et dans l'ordre grâce à un mécanisme d'accusé de réception (ACK) ; UDP, quant à lui, envoie les paquets à la vitesse maximale sans attendre de confirmation.

**Qu'est-ce que le MTU (Maximum Transmission Unit) ?**

Il s'agit de la taille maximale de paquet qu'une interface réseau peut transporter dans une seule trame sans fragmentation. Pour l'Ethernet standard, la valeur MTU est de 1500 octets.

**Pourquoi l'architecture Kernel Bypass est-elle utilisée ?**

Elle est utilisée pour éliminer les coûts d'interruption et de copie mémoire du noyau Linux lors de volumes de données extrêmement élevés tels que 100 Gbps, et pour traiter les paquets directement au niveau matériel avec une latence nulle via DPDK et eBPF/XDP.

## Termes liés

- [VPN](https://trescout.com/fr/dictionary/vpn/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)
- [Packet Fragmentation](https://trescout.com/fr/dictionary/packet-fragmentation/)
- [API](https://trescout.com/fr/dictionary/api/)

## Outils liés

- [OpenFlux](https://trescout.com/fr/discover/openflux/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/network-stack/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/network-stack/
