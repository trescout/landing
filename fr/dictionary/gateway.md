# Qu'est-ce que Gateway ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Une passerelle (gateway en anglais) est un point de connexion qui gère le trafic entre différents réseaux.

## Définition et origine du mot

Gate signifie porte et way signifie chemin. Il s'agit d'une passerelle permettant à deux réseaux de communiquer entre eux : l'appareil reliant l'internet de votre domicile au monde extérieur en est l'exemple typique. Il examine les données entrantes et décide vers quel réseau elles doivent être dirigées.

***Analogie :** C'est comme la porte frontière d'un pays ; Il contrôle les arrivées et s'assure qu'elles se déroulent dans la bonne direction.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Modem domestique :** Connecte votre maison au réseau du fournisseur.
**Passerelle d'entreprise :** Point de contrôle du trafic de bureau.
**Cloud :** La porte d'entrée entre les réseaux virtuels.

## Profondeur technique et architecture

Les fonctions de la passerelle :

**Traduction d'adresses (NAT) :** Convertit les adresses internes en une seule adresse externe.
**Filtrage :** Bloque le trafic indésirable à la porte.
**Routage :** Achemine le paquet vers le bon réseau.

Les informations de route par défaut sont les suivantes :

```
default via 192.168.1.1 dev eth0
```

Cette ligne indique que toute destination non reconnue sera envoyée via le modem. La passerelle API, quant à elle, se situe à un niveau différent : elle gère les requêtes de service, et non le réseau.

## Choses fréquemment mélangées

Elle peut être confondue avec une passerelle API. La passerelle API gère les services logiciels, tandis que la passerelle réseau opère au niveau du réseau. L'une est une porte d'application, l'autre est une porte de routage.

## Utilisation dans différentes disciplines

**Poste frontière :** Contrôle et orientation des arrivants.
**Port :** Passage des navires en douane.
**Réception:** Orientation du visiteur vers le bon étage.

## Foire aux questions

**Peut-on accéder à Internet sans passerelle (gateway) ?**

Non. Le réseau local ne peut pas se connecter au monde extérieur, il reste isolé.

**Quelle est la différence avec une passerelle API (API gateway) ?**

La passerelle réseau transporte des paquets, la passerelle API gère des requêtes. L'une est au niveau réseau, l'autre au niveau application.

**Laquelle utilise-t-on à la maison ?**

La passerelle intégrée à votre modem suffit. Aucun réglage supplémentaire n'est nécessaire, l'adresse est distribuée automatiquement.

**Deux réseaux peuvent-ils être maintenus séparés ?**

Oui. Le passage est bloqué par des règles de pare-feu et les réseaux fonctionnent de manière isolée.

## Termes liés

- [API Gateway](https://trescout.com/fr/dictionary/api-gateway/)
- [Network Stack](https://trescout.com/fr/dictionary/network-stack/)
- [Proxy](https://trescout.com/fr/dictionary/proxy/)

## Outils liés

- [OmniRoute](https://trescout.com/fr/discover/omniroute/)
- [Fanqiang](https://trescout.com/fr/discover/fanqiang/)
- [Gitdiagram](https://trescout.com/fr/discover/gitdiagram/)
- [OpenWA](https://trescout.com/fr/discover/openwa/)
- [Grok2api](https://trescout.com/fr/discover/grok2api/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/gateway/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/gateway/
