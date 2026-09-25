# Qu'est-ce que le Thread Safety ?

> Anglais : Thread Safety · Étymologie : vieil anglais thraed (fil) + latin salvus (intègre, sauf)

**Catégorie:** Dev  
**Dernière mise à jour:** 2026-09-22

Le thread safety (sécurité des threads) est une propriété logicielle garantissant qu'un code ou une structure de données préserve son intégrité lorsqu'il est exécuté simultanément par plusieurs fils d'exécution concurrents.

## Définition et étymologie
Ce concept associe le thread (fil d'exécution de calcul) à l'idée d'intégrité de la mémoire. En calcul concurrent, la sécurité ne concerne pas les pirates informatiques, mais la cohérence des variables partagées : si deux threads modifient la même valeur en mémoire sans synchronisation, les données deviennent incohérentes.

## Usage quotidien et contexte pratique
Exemples d'application en production :
- **Systèmes bancaires :** Empêcher que deux débits simultanés ne génèrent un solde négatif anormal.- **Billetterie en ligne :** Garantir qu'un même siège de spectacle ne puisse pas être réservé deux fois à la même milliseconde.- **Serveurs Web :** Traiter des milliers de requêtes parallèles lisant une mémoire cache partagée.

## Profondeur technique et architecture
Mécanismes techniques pour assurer le thread safety :
- **Verrous et Mutex :** Autoriser un seul fil d'exécution à pénétrer dans la section critique à un instant T.- **Opérations atomiques :** Instructions processeur directes (CAS) modifiant une variable de façon indivisible.- **Immuabilité :** Objets en lecture seule consultables par tous les threads sans risque de conflit.- **Modèle de propriété de Rust :** Le compilateur interdit les accès concurrents non synchronisés dès la compilation.

## Souvent confondu avec
On le confond parfois avec la sécurité informatique défensive. Le thread safety n'a aucun lien avec les antivirus ; il s'agit d'une garantie de logique algorithmique empêchant la corruption accidentelle de données internes.

## Perspectives interdisciplinaires
Analogies dans la vie courante :
- **Circulation routière :** Un pont à voie unique régulé par des feux alternés.- **Cuisine partagée :** Deux cuisiniers qui s'attendent pour utiliser tour à tour l'unique couteau de découpe.- **Guichet :** Une file d'attente disciplinée où chaque client avance quand le guichet se libère.

## Par analogie
C'est comme installer un verrou sur la porte de toilettes communes : tant qu'une personne est à l'intérieur, les autres attendent leur tour pour éviter toute surprise.

## Questions fréquentes

**Que se passe-t-il si un programme n'est pas thread-safe ?**  
Des conditions de concurrence (race conditions) surviennent, entraînant des données erronées ou des plantages imprévisibles.

**Les verrous résolvent-ils tous les problèmes de concurrence ?**  
Pas toujours ; mal ordonnés, ils peuvent provoquer des interblocages (deadlocks) où les threads restent bloqués à l'infini.

**Comment Rust résout-il cette difficulté ?**  
Grâce à son système de possession (ownership), Rust empêche la compilation de codes comportant des risques de concurrence de données.

**Les données immuables sont-elles toujours sûres pour les threads ?**  
Oui, car si une valeur ne peut jamais changer, plusieurs fils peuvent la lire en même temps sans créer de corruption.

## Termes liés
- [Concurrency](/fr/dictionary/concurrency/)
- [System Programming Language](/fr/dictionary/system-programming-language/)
- [Mutex](/fr/dictionary/mutex/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/thread-safety/
