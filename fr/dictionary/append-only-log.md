# Qu'est-ce que Append-only log ?

*Données et infra · Dernière mise à jour : 20 septembre 2026*

Un journal en ajout seul (append-only log) est une architecture de structure de données immuable où les données ne sont jamais modifiées ou supprimées sur place, et où chaque nouvelle transaction est ajoutée à la fin du fichier dans un ordre chronologique.

## Étymologie et paradigme d'immuabilité

Le concept de journal en ajout seul a été développé comme une alternative radicale au paradigme de « mise à jour sur place » (update-in-place) des bases de données traditionnelles. Dans les bases de données classiques, lorsqu'un solde ou un profil est mis à jour, l'ancienne donnée sur le disque est supprimée et remplacée par la nouvelle valeur. Cette approche crée de sérieux problèmes de fiabilité en raison des écritures interrompues lors d'un crash système, des goulots d'étranglement liés aux verrous et des accès disque aléatoires (random I/O).

Dans l'architecture de journal en ajout seul, le passé est sacré et ne peut être falsifié. Au lieu de modifier directement le solde d'un compte bancaire, chaque mouvement de dépôt et de retrait est ajouté comme un nouvel enregistrement à la fin du journal. L'état actuel du système est le résultat naturel de l'exécution chronologique (fold/reduce) de tous ces événements ajoutés depuis le début. Ce principe constitue l'épine dorsale des systèmes distribués modernes, des moteurs de stockage haute performance et des réseaux blockchain.

***Analogie :** Imaginez le grand livre officiel tenu par un comptable. Lorsqu'il commet une erreur sur une ligne, il ne peut pas revenir aux pages précédentes pour effacer le chiffre avec du correcteur. Au lieu de cela, il ajoute une nouvelle ligne d'écriture inversée sur la dernière ligne vide du registre pour corriger l'erreur. Le registre ne fait que croître vers l'avant, le passé n'est jamais modifié ; le mouvement de l'argent peut être audité de manière rétrospective. L'append-only log est exactement ce registre numérique ; il enregistre les données non pas comme une photographie instantanée, mais comme un historique vivant.*

## Profondeur technique et architecture du système

Au niveau technique, l'architecture de journal en ajout seul repose sur trois piliers fondamentaux en termes d'optimisation matérielle et de cohérence des données :

Accès séquentiel au disque (Sequential I/O) et WAL : Les disques magnétiques (HDD) et même les disques SSD/NVMe modernes fonctionnent avec un rendement bien supérieur lorsqu'ils écrivent sur des blocs consécutifs plutôt que sur des adresses aléatoires. C'est pourquoi les bases de données comme PostgreSQL, MySQL et SQLite utilisent le Write-Ahead Logging (WAL). Lorsqu'une transaction arrive, une ligne de journal en mode ajout seul (append-only) est d'abord écrite séquentiellement sur le disque, puis synchronisée via fsync. Ainsi, même en cas de coupure de courant soudaine du serveur, la base de données peut être restaurée dans un état parfaitement cohérent en quelques secondes lors du redémarrage, en relisant le journal depuis le début.
- LSM-Tree et fusion de données (Compaction) : Les moteurs NoSQL à forte intensité d'écriture tels que RocksDB, Apache Cassandra et Bigtable utilisent l'architecture Log-Structured Merge-Tree (LSM-Tree). Toutes les données entrantes sont d'abord ajoutées à une structure triée en mémoire (MemTable) et à un journal synchrone en mode écriture seule (append-only). Lorsque la MemTable est pleine, elle est vidée sur le disque sous forme de fichiers SSTable immuables. Les données anciennes ou invalides qui s'accumulent au fil du temps sont nettoyées par des opérations de fusion (compaction) s'exécutant en arrière-plan.
Event Sourcing et flux distribué (Kafka) : Dans les architectures de microservices, les plateformes de messagerie distribuée telles qu'Apache Kafka et Redpanda fonctionnent comme d'immenses journaux distribués en append-only. Au lieu que les états des applications soient stockés dans une base de données, les événements générés sont inscrits dans des journaux immuables. Différents services consomment ce journal à leur propre rythme pour construire leurs états locaux.
Immuabilité cryptographique et blockchain : les technologies de registre distribué (DLT), telles que Bitcoin et Ethereum, sont des journaux distribués en ajout seul (append-only) où chaque bloc contient l'empreinte cryptographique (hash) du bloc précédent. Aucun nœud du réseau ne peut modifier les blocs passés ; seuls de nouveaux blocs conformes aux règles de consensus peuvent être ajoutés à la fin du registre.

## Dimension sociologique : Mémoire numérique et piste d'audit

Le journal « append-only » dépasse le simple modèle logiciel pour représenter une philosophie de responsabilité numérique et de transparence. Dans le monde de l'entreprise et de l'administration publique, pouvoir répondre avec une certitude infalsifiable à la question « qui a modifié quoi et quand » est la soupape de sécurité la plus critique pour prévenir les crises de confiance.

Dans les systèmes traditionnels, la capacité d'un administrateur de base de données à effacer et réécrire l'historique avec une simple commande SQL fragilise la mémoire institutionnelle. Les systèmes « append-only », en garantissant que le passé ne peut être réécrit, tissent un bouclier d'immunité mathématique contre l'erreur humaine, les menaces internes et les abus de pouvoir.

## Erreurs et idées fausses courantes

Ne pas anticiper la consommation disque : si l'on oublie que les journaux ne font que croître et que l'on ne met pas en place des stratégies appropriées de rétention et de compactage des données, l'espace disque s'épuise rapidement.
Négliger les performances de lecture : scanner des millions de lignes de journaux du début à la fin (replay) pour calculer l'état final paralyse les temps de lecture ; des instantanés (snapshots) réguliers de l'état doivent être effectués.
Ignorer le droit à l'oubli du RGPD : lorsque les lois sur la protection des données personnelles exigent un droit à l'effacement, la suppression de données dans des journaux immuables complexifie l'architecture ; ce problème doit être résolu par la méthode du crypto-effacement (crypto-shredding), où les données sont rendues inintelligibles par la suppression de leur clé de chiffrement.

## Foire aux questions

**Pourquoi l'architecture de journal « append-only » est-elle plus rapide que le modèle de mise à jour sur place (update-in-place) ?**

Au lieu de rechercher des blocs aléatoires sur le disque, l'écriture séquentielle des données à la fin du fichier (append-only) minimise le mouvement de la tête de lecture et la latence d'E/S, permettant ainsi des vitesses d'écriture très élevées.

**Comment l'espace disque est-il géré si le journal en ajout seul (append-only log) croît indéfiniment ?**

Les systèmes prennent périodiquement des instantanés (snapshots) de l'état actuel et exécutent des processus de compactage ou de nettoyage de segments en arrière-plan pour supprimer ou archiver en toute sécurité les anciens journaux.

**Comment le journal en ajout seul est-il utilisé dans les systèmes distribués et Apache Kafka ?**

Les sujets (topics) Kafka sont des journaux en ajout seul partitionnés où les messages sont ajoutés dans l'ordre chronologique ; plusieurs consommateurs lisent le journal sans perte et à haute vitesse avec des valeurs d'offset indépendantes.

**Comment le droit à l'oubli du RGPD est-il appliqué dans les systèmes conservant des journaux en ajout seul ?**

Les données utilisateur dans le journal immuable sont chiffrées avec une clé spécifique ; lorsqu'un utilisateur demande sa suppression, seule la clé de chiffrement de cet utilisateur est détruite (crypto-shredding), rendant les données illisibles sans altérer le journal.

## Termes liés

- [Distributed](https://trescout.com/fr/dictionary/distributed/)
- [Serialization](https://trescout.com/fr/dictionary/serialization/)
- [Local](https://trescout.com/fr/dictionary/local/)
- [Self-hosted](https://trescout.com/fr/dictionary/self-hosted/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/append-only-log/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/append-only-log/
