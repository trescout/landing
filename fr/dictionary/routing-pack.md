# Qu'est-ce que Routing Pack ?

Un paquet de routage (Routing Pack) est un paquet de données utilisé par les périphériques réseau pour transférer des informations de routage entre eux.

## Définition et origine du mot
« Routing » signifie routage et « pack » signifie paquet. Dans les réseaux informatiques, les données sont transportées sous forme de petits fragments. Les routeurs décident du chemin que ces fragments doivent emprunter en consultant leur table de routage. Un « routing pack » est un paquet contenant les informations qui permettent de maintenir ces tables à jour. Par exemple, dans le protocole OSPF, les annonces d'état de lien, et dans le protocole BGP, les mises à jour d'accessibilité, sont diffusées via ce type de paquets.

## Comment connaître et utiliser dans la vie quotidienne ?
Infrastructure Internet : Les routeurs des fournisseurs de services s'envoient mutuellement des informations sur les chemins.Réseaux d'entreprise : Détermination de la ligne par laquelle le trafic entre les succursales doit transiter.Réseau domestique : La connaissance par votre modem du chemin vers Internet (généralement obtenue automatiquement).

## Profondeur technique et architecture
Les informations de routage se composent des éléments suivants :

## Utilisation dans différentes disciplines
Fret : Le plan d'itinéraire qui détermine par quels centres de transfert l'envoi passera.Trafic aérien : La notification préalable du couloir aérien que l'avion suivra.Courrier : Le tri de la lettre vers le centre de distribution en fonction du code postal figurant sur celle-ci.

## Foire aux questions
**« Routing Pack » est-il un terme standard ?**
Ce n'est pas un nom de standard en soi. C'est une expression générale décrivant des paquets contenant des informations de routage. Les standards sont des noms de protocoles tels qu'OSPF ou BGP.

**Que se passe-t-il si le paquet est perdu ?**
L'expéditeur renvoie le paquet s'il ne reçoit pas de réponse. Comme les informations de routage sont actualisées à intervalles réguliers, la table se rétablit rapidement.

**Puis-je voir le routage sur mon réseau domestique ?**
Ce n'est généralement pas nécessaire, le modem le gère automatiquement. Si vous êtes curieux, vous pouvez voir le chemin suivi par votre paquet avec la commande traceroute.

**Les informations de routage sont-elles sécurisées ?**
Dans les réseaux d'entreprise, les protocoles sont protégés par l'authentification et le filtrage. Sinon, de fausses informations de chemin pourraient détourner le trafic vers une mauvaise direction.


## Termes liés
- [Network Stack](/fr/dictionary/network-stack/)
- [API Gateway](/fr/dictionary/api-gateway/)
- [Proxy](/fr/dictionary/proxy/)

## Outils liés
- [Reverse Skill](/fr/discover/reverse-skill/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/routing-pack/
