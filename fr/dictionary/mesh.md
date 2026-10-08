# Qu'est-ce que Mesh ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Le maillage (mesh en anglais) est une architecture réseau dans laquelle des appareils ou des services se connectent et transfèrent des données entre eux sans dépendre d'un serveur central.

## Définition et origine du mot

Mesh signifie filet ou maille en anglais. Tout comme les nœuds d'un filet de pêche sont reliés entre eux, chaque nœud d'un réseau mesh est connecté à ses voisins. Dans les réseaux sans fil, le Wi-Fi mesh, et dans les architectures de microservices, le service mesh (par ex. Istio, Linkerd) sont deux utilisations courantes de ce concept.

***Analogie :** C'est comme si tous les musiciens jouaient en harmonie en s'écoutant les uns les autres, sans chef d'orchestre.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Wi-Fi mesh à la maison :** Alors qu'un modem unique est insuffisant dans une pièce, 2 à 3 unités mesh placées dans la maison assurent une couverture ininterrompue sous un seul nom de réseau. Votre connexion ne se coupe pas lorsque vous passez d'une pièce à l'autre.
**Maison intelligente :** La lampe, le thermostat et les capteurs sont connectés entre eux ; si l'un d'eux s'éteint, le signal continue son chemin via l'appareil voisin.
**Réseaux d'urgence :** Dans les zones où l'infrastructure a été endommagée, les téléphones se connectent entre eux pour acheminer les messages.

## Profondeur technique et architecture

Il existe trois mécanismes qui maintiennent la structure maillée (mesh) en vie :

**Découverte des nœuds (Discovery) :** Chaque nœud trouve les nœuds qui l'entourent et tient à jour sa liste de connexions.
**Routage :** Les données sont transmises de nœud en nœud, de la source à la destination. Certains protocoles diffusent le message à tout le monde, tandis que d'autres calculent le chemin le plus court.
**Auto-réparation :** Si un nœud est hors service, le trafic est automatiquement redirigé vers un autre chemin. Il n'y a pas de point de défaillance unique.

Cette résilience a un prix : chaque saut (hop) ajoute de la latence et, comme les nœuds transportent le trafic les uns des autres, la bande passante totale est partagée. C'est pourquoi le réseau maillé est privilégié là où la couverture et la résilience comptent plus que la vitesse.

Dans les microservices, le service mesh fonctionne un peu différemment : un petit proxy appelé sidecar est placé à côté des services. Le trafic transite par ces proxys, ce qui permet d'appliquer des politiques d'observabilité, de sécurité et de nouvelles tentatives sans avoir à écrire de code spécifique pour chaque service.

## Utilisation dans différentes disciplines

**Urbanisme :** Rues en plan quadrillé. Si une avenue est fermée, le trafic circule par les rues voisines.
**Textile :** Tissage du tissu. Même si un seul fil se rompt, il préserve l'intégrité de la structure.
**Biologie :** Réseaux neuronaux. Le signal peut contourner la zone endommagée.

## Foire aux questions

**À quoi sert le Wi-Fi Mesh ?**

Il fournit un signal puissant avec un nom de réseau unique dans chaque pièce de la maison. Sa différence par rapport aux répéteurs de portée est qu'il s'efforce de ne pas couper la connexion lors des passages d'une pièce à l'autre.

**Un service mesh et un réseau mesh sont-ils la même chose ?**

Non. Un réseau mesh est la manière dont les appareils sont connectés. Un service mesh, quant à lui, est une couche logicielle qui gère le trafic entre les microservices. Tous deux s'inspirent de l'idée d'une connexion décentralisée.

**Le mesh est-il toujours meilleur ?**

Non. Dans une petite maison ou un environnement avec peu d'appareils, un seul modem puissant peut être plus simple et plus rapide. Le système Mesh est utile en cas de problème de couverture ou pour les structures à plusieurs nœuds.

**Est-ce difficile à installer ?**

Les kits Mesh grand public s'installent généralement en quelques minutes via une application mobile. En revanche, une installation de type entreprise ou service mesh nécessite de la planification.

## Termes liés

- [Service Mesh](https://trescout.com/fr/dictionary/service-mesh/)
- [Network Stack](https://trescout.com/fr/dictionary/network-stack/)
- [Distributed](https://trescout.com/fr/dictionary/distributed/)

## Outils liés

- [Bitchat](https://trescout.com/fr/discover/bitchat/)
- [Meshery](https://trescout.com/fr/discover/meshery/)
- [Meshoptimizer](https://trescout.com/fr/discover/meshoptimizer/)
- [Modly](https://trescout.com/fr/discover/modly/)
- [Tailcat](https://trescout.com/fr/discover/tailcat/)
- [Bitchat Android](https://trescout.com/fr/discover/bitchat-android/)
- [Spirula Studio](https://trescout.com/fr/discover/spirula-studio/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/mesh/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/mesh/
