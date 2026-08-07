# Qu'est-ce que Packet Fragmentation ?

Il s'agit du processus de division des données envoyées sur Internet en morceaux plus petits en fonction de la capacité de transport du réseau.

## Définition
Lors de l'envoi de données sur Internet, chaque réseau a une taille maximale qu'il peut transporter. Si les données que vous envoyez sont plus volumineuses que cette taille, le système les divise en petits morceaux, les livre à la destination et les réassemble là-bas.

## Comment ça marche
Au fur et à mesure que les données sont envoyées, les périphériques réseau vérifient la taille du paquet. Si la limite est dépassée, le paquet est fragmenté et chaque fragment reçoit un « numéro de séquence ». Le dispositif de réception examine ces numéros et assemble les pièces dans le bon ordre.

## Où est-ce utilisé
Cela se produit constamment en arrière-plan pendant les protocoles Internet et les processus réseau.

## Souvent confondu avec
Cela peut être confondu avec une perte de données, mais il s'agit d'un processus de partitionnement contrôlé.

## Questions fréquentes
**Que se passe-t-il si des pièces sont perdues ?**
L'appareil de réception se rend compte qu'il manque des pièces et demande à l'expéditeur de renvoyer cette pièce.


## Termes liés
- [Networking Stack](/fr/dictionary/networking-stack/)
- [DNS Tunneling](/fr/dictionary/dns-tunneling/)

## Outils liés
- [Zapret Discord Youtube](/fr/discover/zapret-discord-youtube/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/packet-fragmentation/
