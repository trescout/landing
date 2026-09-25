# Memory Management Stack, Heap, ramasse-miettes et mémoire OS


**Catégorie:** Dev  

**Dernière mise à jour:** 2026-09-19


La gestion de la mémoire (memory management) est l'ensemble des processus logiciels et matériels régissant l'allocation, l'usage et la libération de la mémoire vive (RAM) tout au long du cycle de vie d'un programme.


## 1. Anatomie de la mémoire : distinction entre Stack et Heap
Un programme organise sa mémoire vive allouée en deux zones aux caractéristiques distinctes :
- **Mémoire de pile (Stack) :** Structure séquentielle de type LIFO (dernier entré, premier sorti) gérée directement par le processeur. Elle conserve les cadres d'appels de fonctions et les variables locales primitives. L'allocation se résume à déplacer le registre de pointeur de pile (RSP), assurant une vitesse maximale et une libération automatique dès la fin de la fonction.- **Mémoire de tas (Heap) :** Vaste espace dynamique alloué à la demande pour des objets de taille variable dont la durée de vie dépasse la fonction courante. L'allocation (via malloc ou new) requiert de parcourir des tables de fragmentation, ce qui la rend plus lente que la pile.

## 2. Les trois paradigmes de gestion de la mémoire
Les langages de programmation appliquent trois philosophies distinctes :
- **Gestion manuelle (C, C++) :** Le développeur réserve les blocs avec <code>malloc()</code> et doit obligatoirement les libérer avec <code>free()</code>. Elle garantit un contrôle absolu mais expose aux fuites de mémoire (memory leaks) et aux failles d'exploitation (use-after-free).- **Ramasse-miettes automatique (Java, Go, JavaScript, Python) :** Un processus d'arrière-plan (Garbage Collector) inspecte les graphes d'objets pour recycler automatiquement ceux qui ne sont plus référencés, au prix de courtes pauses d'exécution.- **Système de possession et emprunt (Rust) :** Rust valide la sécurité mémoire à la compilation grâce à des règles strictes d'Ownership : chaque valeur a une variable propriétaire unique et est détruite automatiquement dès que son propriétaire sort du champ lexical.

## 3. Niveau système d'exploitation : mémoire virtuelle et OOM Killer
Sous les langages applicatifs, le noyau du système d'exploitation coordonne la RAM via le composant matériel MMU (Memory Management Unit) :
- **Mémoire virtuelle et pagination :** Chaque processus s'exécute dans un espace d'adressage virtuel découpé en pages de 4 Ko. La MMU mappe ces adresses virtuelles vers les trames réelles de la RAM.- **Fautes de page et fichier d'échange (Swap) :** Si une adresse mémoire a été déchargée sur le disque dur, une interruption (page fault) oblige le noyau à la rapatrier en RAM.- **OOM Killer (Out Of Memory) :** Lorsque la mémoire vive est saturée sans possibilité d'échange, le noyau Linux déclenche l'OOM Killer pour stopper brutalement les processus les plus gourmands afin d'éviter le blocage de la machine.

## Par analogie
La mémoire de pile est comme une pile d'assiettes où l'on pose et retire rapidement des éléments par le haut ; le tas est comme un vaste entrepôt où l'on dépose des cartons de toutes tailles en tenant un registre minutieux pour ne rien égarer.

## Questions fréquentes

**Quelle est la différence fondamentale entre la Stack et la Heap ?**  
La pile (Stack) est automatique, ultrarapide et liée à la portée d'une fonction ; le tas (Heap) est dynamique, volumineux et nécessite un suivi manuel ou un ramasse-miettes.

**Qu'est-ce qu'une fuite de mémoire (memory leak) ?**  
C'est l'omission de libérer des blocs mémoire alloués sur le tas, ce qui fait croître l'empreinte RAM de l'application jusqu'au plantage.

**Comment Rust assure-t-il la sécurité sans ramasse-miettes ?**  
Grâce aux règles d'Ownership et de durée de vie vérifiées lors de la compilation, le compilateur insère le code de libération de manière déterministe.

**Pourquoi le noyau Linux utilise-t-il l'OOM Killer ?**  
Pour empêcher un gel total du système d'exploitation lorsqu'il n'y a plus aucun octet de RAM disponible pour satisfaire les processus critiques.

## Termes liés
- [Runtime](/fr/dictionary/runtime/)
- [State Management](/fr/dictionary/state-management/)
- [Serialization](/fr/dictionary/serialization/)
- [Network Stack](/fr/dictionary/network-stack/)
- [Assembly](/fr/dictionary/assembly/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/memory-management/
