# Qu'est-ce que Runtime ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

Le runtime (temps d'exécution) désigne la période durant laquelle un programme est réellement exécuté sur le processeur et dans la mémoire de l'ordinateur après la phase de compilation, ainsi que l'infrastructure logicielle (Runtime Environment) qui rend cette exécution possible.

## 1. Les deux significations fondamentales du concept de runtime

En génie logiciel, le terme "Runtime" fait référence à deux concepts différents selon le contexte :

1. En tant que phase temporelle (Runtime / Temps d'exécution) : il s'agit de la période s'écoulant entre le moment où l'utilisateur final lance le programme et celui où il le ferme, succédant ainsi aux phases d'écriture du code (authoring) et de compilation (compile-time).
2. En tant qu'environnement d'exécution (Runtime Environment) : Il s'agit de l'ensemble des bibliothèques, gestionnaires de mémoire, ramasse-miettes et machines virtuelles nécessaires pour que le code écrit puisse s'exécuter directement sur le système d'exploitation et le matériel. Par exemple, Node.js, la JVM (Java Virtual Machine) ou le runtime Go sont des environnements d'exécution.

***Analogie :** Le temps de compilation (compile-time) correspond au moment où les plans architecturaux et les calculs statiques d'un bâtiment sont vérifiés par l'ingénieur sur une table ; s'il y a une erreur, elle est corrigée sur papier. Le temps d'exécution (runtime) est le moment où ce bâtiment est construit et où les gens s'y installent ; des événements imprévus tels qu'un tremblement de terre, une inondation ou une surcharge ne testent le bâtiment qu'à ce stade.*

## 2. Différence entre Compile-Time et Runtime

- Temps de compilation : Avant l'exécution du code, l'analyse syntaxique, les vérifications de type statiques et la conversion en code machine sont effectuées. Les erreurs de syntaxe et les incompatibilités de type sont détectées à cette étape.
- Runtime (Exécution) : L'allocation mémoire, les appels système et la gestion de la boucle d'événements sont effectués pendant que l'utilisateur exécute réellement le programme. Les erreurs de type NullPointerException, Segmentation Fault (SIGSEGV) et Stack Overflow surviennent à ce stade.

## 3. Runtimes gérés (Managed) vs non gérés (Unmanaged)

- Non géré (C, C++, Rust, Zig) : se compile directement en code machine natif ; aucune machine virtuelle lourde ni ramasse-miettes ne s'exécute en arrière-plan, seule une bibliothèque standard C (libc) légère est nécessaire. Offre une vitesse maximale et une latence nulle.
- Gérés (Java, C#, Go, JavaScript, Python) : S'exécutent au sein d'une machine virtuelle (JVM, CLR) ou d'un environnement d'exécution protégé. Ils intègrent des compilateurs JIT, des ramasse-miettes automatiques et un planificateur interne qui gère, comme dans le cas de Go, les goroutines.

## 4. La guerre des runtimes JavaScript modernes : Node.js vs Deno vs Bun

- Node.js (2009) : la norme industrielle qui combine le moteur V8 de Google avec la boucle d'événements d'E/S asynchrones libuv basée sur C++.
- Deno (2018) : plateforme moderne combinant le moteur V8 avec l'infrastructure Rust et Tokio, dotée d'un support TypeScript intégré et d'un bac à sable de permissions sécurisé.
- Bun (2023) : utilisant le moteur JavaScriptCore d'Apple WebKit et entièrement réécrit en langage Zig, il s'agit d'un environnement d'exécution de nouvelle génération offrant des entrées/sorties fichier/réseau bien plus rapides que celles de Node.js.

## Questions fréquentes

**Que signifie « runtime » et quel est son équivalent en français ?**

En français, on l'appelle « temps d'exécution » ou « environnement d'exécution ». Il désigne l'intervalle de temps pendant lequel un programme passe de l'état de code source à une exécution réelle sur le matériel informatique, ainsi que la couche logicielle qui prend en charge cette exécution.

**Qu'est-ce qu'une erreur d'exécution (Runtime Error) ?**

Il s'agit d'une erreur qui survient après avoir passé avec succès l'étape de compilation, mais qui provoque le plantage soudain de l'application pendant son exécution en raison d'une situation inattendue (division par zéro, accès à un objet vide, mémoire vive insuffisante).

**Node.js est-il un langage de programmation ou un environnement d'exécution (runtime) ?**

Node.js n'est pas un langage ; c'est un environnement d'exécution JavaScript open source qui permet au code JavaScript de s'exécuter sur des serveurs et des ordinateurs sans avoir besoin d'un navigateur.

**Comment la compilation JIT (Just-In-Time) fonctionne-t-elle au moment de l'exécution ?**

Le compilateur JIT détecte instantanément les blocs de code fréquemment utilisés ("hot paths") pendant l'exécution du programme et convertit ces blocs en code machine natif à la volée, augmentant ainsi considérablement les performances de l'application.

## Termes liés

- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)
- [Assembly](https://trescout.com/fr/dictionary/assembly/)
- [Compilation](https://trescout.com/fr/dictionary/compilation/)
- [Bundler](https://trescout.com/fr/dictionary/bundler/)
- [Tech Stack](https://trescout.com/fr/dictionary/tech-stack/)

## Outils liés

- [Andrej Karpathy Skills](https://trescout.com/fr/discover/andrej-karpathy-skills/)
- [Node](https://trescout.com/fr/discover/node/)
- [Deno](https://trescout.com/fr/discover/deno/)
- [BUN](https://trescout.com/fr/discover/bun/)
- [Svelte](https://trescout.com/fr/discover/svelte/)
- [Wand-Enhancer](https://trescout.com/fr/discover/wand-enhancer/)
- [Univer](https://trescout.com/fr/discover/univer/)
- [Onnxruntime](https://trescout.com/fr/discover/onnxruntime/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/runtime/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/runtime/
