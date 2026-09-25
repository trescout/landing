# Distributed Systems Mythes, théorème CAP, consensus et transactions Saga


**Catégorie:** Dev  

**Dernière mise à jour:** 2026-09-19


Un système distribué (ou système réparti) est une architecture informatique composée de multiples machines autonomes reliées par un réseau qui coordonnent leurs actions pour paraître unifiées aux utilisateurs.


## Étymologie et nature des systèmes distribués
Le mot *distribué* provient du latin *distribuere* (répartir, diviser). Comme le résumait Leslie Lamport : *« Un système distribué est un système où la panne d'un ordinateur dont vous ignoriez jusqu'à l'existence peut rendre votre propre machine inutilisable. »* Contrairement aux mainframes centraux, ils troquent la simplicité contre une scalabilité horizontale infinie.

## Les 8 mythes de l'informatique distribuée (Deutsch)
Définis chez Sun Microsystems, ces huit postulats erronés mènent à l'échec s'ils ne sont pas anticipés :
- Le réseau est fiable.
- La latence est nulle.
- La bande passante est infinie.
- Le réseau est sécurisé.
- La topologie ne change jamais.
- Il n'y a qu'un seul administrateur.
- Le coût de transport des données est nul.
- Le réseau est homogène.

## Le théorème CAP et le modèle PACELC
Le **théorème CAP** d'Eric Brewer démontre qu'en cas de partition réseau, un système de données distribué ne peut garantir simultanément que deux de ces trois propriétés :
- **Cohérence (C) :** Chaque lecture retourne la donnée la plus récente ou une erreur.- **Disponibilité (A) :** Chaque nœud opérationnel répond toujours sans garantie d'état à jour.- **Tolérance au partitionnement (P) :** Le système continue de fonctionner malgré les coupures réseau. Comme les coupures sont inévitables, il faut arbitrer entre CP (ZooKeeper) et AP (Cassandra).
Le modèle **PACELC** affine l'analyse : *en cas de Partition (P), choisir entre Disponibilité (A) et Cohérence (C) ; Sinon (Else), choisir entre Latence (L) et Cohérence (C).*

## Protocoles de consensus : Raft et Paxos
Pour s'accorder sur un état unique sur un réseau instable, les systèmes recourent à des algorithmes de consensus :
- **Paxos :** L'algorithme historique prouvé par Leslie Lamport, réputé pour sa grande complexité d'implémentation pratique.- **Raft :** Conçu pour être compréhensible par l'esprit humain, décomposant le consensus en élection de leader, réplication de logs et sécurité (utilisé dans etcd).

## Le problème du temps et les horloges logiques
En l'absence d'horloge physique absolue commune, déterminer l'ordre chronologique des événements entre serveurs distants est un défi physique majeur :
- **Horloges logiques de Lamport et horloges vectorielles :** Compteurs séquentiels établissant la causalité (« arrivé-avant ») sans dépendre de l'heure matérielle.- **Google TrueTime :** Infrastructure associant horloges atomiques et récepteurs GPS pour encadrer l'incertitude temporelle à quelques millisecondes (utilisée dans Spanner).

## Gestion des données distribuées : le pattern Saga
Le protocole de validation à deux phases (2PC) bloque les ressources et ne passe pas à l'échelle. Les microservices utilisent le **pattern Saga** :
- Une succession de transactions locales coordonnées par orchestration (machine d'état) ou chorégraphie (événements pub/sub).
- En cas d'échec d'une étape, le système déclenche des transactions de compensation rétroactives pour annuler proprement les opérations précédentes.

## Par analogie
Un système centralisé est comme un chef cuisinier travaillant seul dans son camion ; un système distribué est comme une chaîne mondiale de restaurants où des centaines de cuisines doivent coordonner leurs menus malgré les coupures téléphoniques et les retards de livraison.

## Questions fréquentes

**Qu'est-ce qu'un système distribué en informatique ?**  
C'est un ensemble de serveurs indépendants communiquant par réseau pour réaliser une tâche commune de manière transparente pour l'utilisateur.

**Pourquoi le théorème CAP impose-t-il un choix ?**  
Parce qu'en cas de coupure de liaison entre serveurs, on doit soit bloquer les écritures pour préserver la vérité, soit les accepter au risque d'avoir des données divergentes.

**Quelle est la différence entre Raft et Paxos ?**  
Tous deux résolvent le consensus distribué, mais Raft a été conçu pour être plus simple à comprendre et à maintenir en production.

**Comment le pattern Saga remplace-t-il les transactions globales ?**  
En découpant le flux en opérations locales indépendantes associées à des étapes de compensation rétroactives en cas d'erreur.

## Termes liés
- [Cloud Computing](/fr/dictionary/cloud-computing/)
- [Network Stack](/fr/dictionary/network-stack/)
- [Deployment](/fr/dictionary/deployment/)
- [Runtime](/fr/dictionary/runtime/)

## Outils liés
- [Elasticsearch](/fr/discover/elasticsearch/)
- [Cassandra](/fr/discover/cassandra/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/distributed/
