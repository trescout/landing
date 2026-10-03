# Assembly Définition, registres et architecture système

Le terme Assembly désigne deux réalités en informatique : d'une part le langage de programmation symbolique de plus bas niveau contrôlant directement le processeur (CPU), et d'autre part les unités de déploiement modulaires (.NET assembly).

## 1. Langage de programmation bas niveau (Assembly Language)
Le processeur ne traite que des signaux binaires (code machine / opcodes). Le langage d'assemblage remplace ces octets bruts par des abréviations mnémotechniques lisibles :

## 2. Registres processeur et architecture x86-64
Dans un processeur 64 bits x86-64, les registres essentiels se divisent en deux groupes :

## 3. CISC vs RISC : différences entre x86-64 et ARM64
L'architecture x86-64 repose sur le modèle CISC (jeu d'instructions complexe) permettant des instructions à longueur variable manipulant directement la mémoire. ARM64 (Apple Silicon, smartphones) adopte le modèle RISC (jeu d'instructions réduit) à longueur fixe de 32 bits et architecture Load-Store, offrant un rendement énergétique remarquable.

## 4. Appels système (Syscall) et exemple sous Linux x86-64

## 5. .NET Assembly et WebAssembly (WASM)

## Questions fréquentes
**Qu'est-ce que le langage Assembly et à quoi sert-il ?**
C'est le langage symbolique le plus proche du matériel, correspondant directement aux instructions du processeur, indispensable pour les pilotes et l'ingénierie inverse.

**Quelle est la différence entre un assembleur et un compilateur ?**
Le compilateur transforme un code de haut niveau structuré en instructions machines, tandis que l'assembleur traduit les mnémoniques un pour un en octets binaires sans restructuration logique.

**Où utilise-t-on encore l'assembleur aujourd'hui ?**
Dans les chargeurs d'amorçage (bootloaders), les systèmes embarqués critiques, l'analyse de malwares et l'optimisation de moteurs graphiques.


## Termes liés
- [Memory Management](/fr/dictionary/memory-management/)
- [Runtime](/fr/dictionary/runtime/)
- [Compilation](/fr/dictionary/compilation/)
- [Apple Silicon](/fr/dictionary/apple-silicon/)
- [Emulator](/fr/dictionary/emulator/)

## Outils liés
- [Apollo-11](/fr/discover/apollo-11/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/assembly/
