# Qu'est-ce que Network Stack ?

La pile réseau (Network Stack) est l'ensemble des pilotes matériels, du noyau (kernel) et des couches de protocole de l'espace utilisateur qui permettent à un système d'exploitation ou à un matériel de transmettre, router et recevoir des paquets de données sur un réseau.

## 1. Architecture en couches : 7 couches OSI vs 4 couches TCP/IP
Dans la communication réseau, le modèle OSI à 7 couches défini théoriquement par l'ISO est utilisé, tandis qu'en pratique, c'est le modèle TCP/IP qui constitue l'épine dorsale d'Internet :

## 2. Flux d'encapsulation et de décapsulation des paquets
Lorsqu'un client envoie une requête à un serveur web, les données descendent la pile et chaque couche ajoute son propre en-tête :

## 3. Cycle de vie de la pile réseau dans le noyau Linux (Kernel)

## 4. Kernel Bypass et réseau de nouvelle génération : eBPF / XDP et DPDK

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
- [VPN](/fr/dictionary/vpn/)
- [Runtime](/fr/dictionary/runtime/)
- [Memory Management](/fr/dictionary/memory-management/)
- [Packet Fragmentation](/fr/dictionary/packet-fragmentation/)
- [API](/fr/dictionary/api/)

## Outils liés
- [OpenFlux](/fr/discover/openflux/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/network-stack/
