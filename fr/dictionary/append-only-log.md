# Append-Only Log Immutabilité, Write-Ahead Log et stockage séquentiel


**Catégorie:** Data & Infra  

**Dernière mise à jour:** 2026-09-20


Un append-only log (journal à ajout seul) est une structure de données où les nouveaux enregistrements s'écrivent exclusivement à la suite à la fin du fichier, les données existantes demeurant rigoureusement immuables.


## Étymologie et paradigme de l'immutabilité
Ce principe s'inspire directement des livres comptables traditionnels : un comptable ne gomme jamais une ligne erronée, il inscrit une nouvelle écriture compensatoire. En informatique, ce paradigme transforme les opérations aléatoires coûteuses en écritures séquentielles ultra-rapides.

## Profondeur technique et architecture système
Cette architecture est au cœur des moteurs de données modernes :
- **Write-Ahead Logging (WAL) :** Les bases comme PostgreSQL et SQLite écrivent chaque transaction dans un journal séquentiel avant de toucher aux index B-Tree, assurant la durabilité ACID.- **Arbres LSM (Log-Structured Merge) :** Des moteurs comme RocksDB et Cassandra dirigent les écritures vers un journal séquentiel immuable compacté périodiquement.- **Streaming d'événements distribué :** Apache Kafka organise ses flux de messages sous forme de journaux partitionnés accessibles en temps réel.

## Dimension sociologique : mémoire numérique et traçabilité
À l'ère de la falsification numérique, les journaux immuables garantissent une transparence totale. Dans Git, les registres de transparence de certificats ou la blockchain, chaque modification génère une preuve cryptographique inviolable.

## Erreurs fréquentes et écueils de conception
L'emploi de ces journaux exige une vigilance opérationnelle :
- **Saturation du stockage :** Sans politique de rétention ou de compactage régulier, le journal finit par remplir le disque dur du serveur.- **Amplification de lecture :** Reconstituer l'état présent nécessite de rejouer tout l'historique en l'absence d'instantanés (snapshots) périodiques.

## Par analogie
Un append-only log est comme graver des faits dans la pierre : vous ne pouvez pas effacer le passé ; pour rectifier une ligne, vous devez obligatoirement en tailler une nouvelle qui décrit le correctif.

## Questions fréquentes

**Que signifie le concept d'append-only log ?**  
C'est un modèle de stockage où les données sont ajoutées uniquement à la fin du fichier, interdisant toute modification rétroactive.

**Pourquoi les écritures séquentielles sont-elles plus performantes ?**  
Parce qu'elles évitent les déplacements aléatoires des têtes de lecture sur disque, exploitant la vitesse maximale des supports physiques.

**Comment évite-t-on la saturation de l'espace disque ?**  
Grâce au compactage de données, à la purge par segments et à la création d'instantanés d'états consolidés.

## Termes liés
- [Distributed](/fr/dictionary/distributed/)
- [Serialization](/fr/dictionary/serialization/)
- [Local](/fr/dictionary/local/)
- [Self-hosted](/fr/dictionary/self-hosted/)
- [Runtime](/fr/dictionary/runtime/)
- [Memory Management](/fr/dictionary/memory-management/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/append-only-log/
