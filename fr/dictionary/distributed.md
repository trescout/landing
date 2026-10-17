# Qu'est-ce que Distributed ?

*Développement · Dernière mise à jour : 19 septembre 2026*

Dans le monde de l'informatique, le partage du matériel, des données et des processus de calcul est distribué entre de nombreux serveurs indépendants (nœuds) connectés les uns aux autres via le réseau, au lieu d'une seule machine centrale, et ce système sert l'utilisateur final comme s'il s'agissait d'un seul ordinateur entier.

## Étymologie et nature des systèmes distribués

Le mot "Distributed" se traduit en turc par "dağıtık" (distribué). L'un des pionniers de l'informatique, Leslie Lamport, a défini les systèmes distribués avec cette célèbre citation entrée dans l'histoire : "Un système distribué est un système dans lequel la panne d'un ordinateur dont vous ignorez même l'existence peut rendre votre propre ordinateur inutilisable."

Dans les architectures centralisées (monolithiques), toutes les opérations se déroulent sur une seule mémoire principale et un seul processeur. Dans les systèmes distribués, des centaines de nœuds physiquement répartis dans des centres de données sur différents continents du monde servent un objectif commun en communiquant via des câbles réseau peu fiables.

## 8 erreurs de l'informatique distribuée

Dans les années 1990, les ingénieurs de Sun Microsystems, L. Peter Deutsch et James Gosling, ont répertorié les « 8 erreurs mortelles » commises par les développeurs de logiciels développant des systèmes distribués. Toutes les lignes de défense des architectures cloud et microservices modernes sont construites selon ces idées fausses :

Le réseau est fiable : en réalité, des paquets se perdent, des lignes de fibre optique se coupent, des routeurs se bloquent.
2. La latence est nulle : la vitesse de la lumière et le délai de commutation réseau entre deux machines sont toujours présents.
3. La bande passante est infinie : à mesure que le volume de données augmente, les tuyaux du réseau se bouchent.
4. Le réseau est sécurisé : toutes les communications distribuées passent par des lignes ouvertes et nécessitent une protection cryptographique.
5. La topologie ne change pas : les serveurs démarrent et s'arrêtent en permanence, les adresses IP changent.
6. Il n'y a qu'un seul administrateur système : de multiples équipes et fournisseurs de cloud sont impliqués.
7. Le coût de transfert est nul : les coûts de sérialisation et de packaging CPU ne sont pas négligeables.
8. Le réseau est homogène : Linux, Windows, ARM, x86 et différents protocoles coexistent au sein du système.

## Théorème CAP et modèle PACELC

Le théorème CAP, formulé par Eric Brewer, définit les limites fondamentales de la gestion des données distribuées. En cas de partition réseau (Network Partition - P), le système doit choisir l'une des deux options suivantes :

- CP (Cohérence + Tolérance au partitionnement) : Le système choisit la cohérence. Les nœuds dont les données ne sont pas à jour refusent de répondre ; la disponibilité est sacrifiée (par exemple, les transactions financières et bancaires).
- AP (Disponibilité + Tolérance au partitionnement) : Le système privilégie la disponibilité. Les nœuds continuent de répondre, mais certains utilisateurs peuvent voir des données obsolètes datant de quelques secondes (par exemple, les fils d'actualité des réseaux sociaux).

Dans les systèmes modernes, le modèle PACELC de Daniel Abadi est utilisé : en cas de partition réseau (P), privilégie-t-on la disponibilité (A) ou la cohérence (C) ? Et lorsque le système fonctionne normalement (E), vise-t-on une faible latence (L) ou une cohérence immédiate (C) ?

## Protocoles de consensus : Raft et Paxos

Des algorithmes de consensus ont été développés pour que des serveurs indépendants, qui ne se font pas confiance et peuvent planter à tout moment, puissent se mettre d'accord sur une seule vérité :

Paxos : Algorithme de consensus développé par Leslie Lamport, mathématiquement prouvé mais extrêmement complexe à mettre en œuvre en pratique.
Raft : protocole de consensus conçu par Diego Ongaro et John Ousterhout pour résoudre la complexité de Paxos, pensé pour être intuitif et compréhensible par l'esprit humain. Il repose sur des machines à états gérant l'élection du leader (Leader Election), la réplication de journaux (Log Replication) et la sécurité (Safety) (il est au cœur de systèmes majeurs tels qu'etcd, Kubernetes et Consul).
Tolérance aux fautes byzantines (BFT) : fondement des protocoles de blockchain qui assurent le consensus même dans des environnements où certains nœuds diffusent délibérément des informations erronées ou malveillantes.

## Problème de temps et solutions dans les systèmes distribués

Dans un ordinateur centralisé, l’horloge matérielle représente un seul fait. Dans les systèmes distribués, les horloges des serveurs présentent une dérive d'horloge physique et NTP (Network Time Protocol) est insuffisant pour une précision à la milliseconde :

Horloges logiques de Lamport (Lamport Timestamps) : définissent l'ordre de survenance des événements plutôt que le temps physique.
- Horloges vectorielles : détecte les conflits de données en déterminant quelles données sont la cause ou l'effet des autres.
Google TrueTime : combinaison d'horloges atomiques et d'antennes GPS utilisée dans la base de données distribuée Google Spanner. En réduisant la marge d'incertitude à quelques millisecondes, elle permet des transactions ACID à l'échelle mondiale.

## Gestion distribuée des données et des transactions : modèle Saga

Dans les systèmes monolithiques, les transactions de base de données (ACID) sont remplacées dans les microservices par l'approche du modèle Saga (Saga Pattern). Au lieu de verrouiller les étapes distribuées de longue durée avec des protocoles de validation en deux phases (2PC - Two Phase Commit), on utilise des architectures pilotées par les événements où chaque service effectue sa propre transaction locale et où des transactions compensatoires (Compensating Transactions) sont déclenchées en cas d'erreur.

## Foire aux questions

**Que signifie Distribué (sens turc) ?**

Dans la terminologie informatique, cela signifie « distribué ». Il s'agit du partage de la puissance de calcul, de l'espace mémoire ou de la base de données entre de nombreuses machines indépendantes communiquant sur un réseau, plutôt que sur un seul serveur.

**Que signifie le théorème CAP en pratique ?**

Cela signifie que lorsqu'il y a une interruption ou un retard (split) dans la connexion réseau, le système doit soit garantir les données les plus à jour et conserver certaines demandes (cohérence), soit répondre immédiatement à chaque demande au prix de fournir des données obsolètes (disponibilité).

**Pourquoi l'algorithme de consensus Raft est-il utilisé dans les systèmes distribués ?**

Même si quelques serveurs du réseau tombent en panne, la majorité restante est utilisée pour garantir que les nœuds (Quorum) élisent un nouveau leader parmi eux et que les journaux de base de données sont synchronisés sans perte sur l'ensemble du cluster.

**Pourquoi le modèle Saga est-il préféré à l'engagement en deux phases (2PC) ?**

2PC (Two-Phase Commit) verrouille les ressources de base de données sur les nœuds distribués et verrouille l'ensemble du système lorsqu'une machine ne répond plus. Le modèle Saga, quant à lui, maintient la haute disponibilité du système en utilisant des événements asynchrones et des étapes de compensation.

## Termes liés

- [Cloud Computing](https://trescout.com/fr/dictionary/cloud-computing/)
- [Network Stack](https://trescout.com/fr/dictionary/network-stack/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)

## Outils liés

- [Elasticsearch](https://trescout.com/fr/discover/elasticsearch/)
- [Cassandra](https://trescout.com/fr/discover/cassandra/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/distributed/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/distributed/
