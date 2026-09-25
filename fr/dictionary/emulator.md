# Qu'est-ce qu'un Émulateur (Emulator) ?

> Anglais : Emulator · Étymologie : latin aemulari (rivaliser avec, imiter)

**Catégorie:** Dev  
**Dernière mise à jour:** 2026-09-19

Un émulateur (emulator) est un logiciel qui reproduit fidèlement le comportement matériel, le jeu d'instructions et les registres d'une machine étrangère, permettant d'exécuter ses programmes d'origine sur un autre ordinateur.

## Cadre conceptuel, étymologie et distinction avec le simulateur
Le terme vient du latin aemulari, signifiant imiter avec rivalité. Alors qu'un simulateur reproduit le comportement extérieur d'un système sans modéliser ses rouages internes (comme un simulateur de vol), l'émulateur recrée chaque circuit électronique virtuel : registres processeur, puces sonores et gestion de mémoire vive.

## Architecture informatique et cycle Fetch-Decode-Execute
Au cœur de l'émulateur tourne un processeur virtuel traduisant le code binaire invité :
- **Émulation par interpréteur :** Chaque instruction machine est lue, décodée et exécutée séquentiellement. Précise mais consommatrice de calcul.- **Recompilation dynamique (JIT) :** Les blocs d'instructions étrangers (ARM, MIPS) sont convertis à la volée en code machine natif (x86-64) et mis en cache pour une exécution ultra-rapide.- **Émulation au cycle près (Cycle-Accurate) :** Synchronisation temporelle à l'horloge près garantissant un respect parfait des cadences matérielles d'origine.

## Usages en développement, cybersécurité et entreprise
Domaines d'application essentiels des émulateurs :
- **Développement mobile :** Tester des applications Android ou iOS sur des postes de travail grâce à des émulateurs intégrés aux IDEs.- **Analyse de logiciels malveillants :** Exécuter des virus dans des environnements émulés isolés (comme QEMU) pour observer leur comportement sans risque.- **Préservation du patrimoine informatique :** Faire tourner des systèmes bancaires patrimoniaux sur des serveurs Cloud actuels.

## Aspects juridiques et propriété intellectuelle
La légalité du développement d'émulateurs a été confirmée par de grands arrêts judiciaires (notamment Sony v. Connectix) : la rétro-ingénierie en salle blanche du matériel est licite, à condition de ne pas distribuer de code propriétaire sous copyright (fichiers BIOS ou ROMs de jeux).

## Par analogie
Pour lire un manuel écrit en langue étrangère : le simulateur est un résumé expliquant le sujet général ; l'émulateur interpréteur traduit chaque mot un à un au dictionnaire ; le recompilateur JIT traduit des chapitres entiers dans votre langue à l'avance pour une lecture fluide.

## Questions fréquentes

**Quelle est la différence entre émulateur et machine virtuelle ?**  
La machine virtuelle exécute le code directement sur le même processeur physique ; l'émulateur traduit logiciellement un jeu d'instructions pour un processeur d'architecture totalement différente.

**Créer un émulateur est-il légal ?**  
Oui ; la rétro-ingénierie d'une architecture matérielle est autorisée dès lors qu'aucun BIOS protégé par le droit d'auteur n'est incorporé illégalement.

**Pourquoi émuler d'anciennes consoles demande-t-il parfois des processeurs puissants ?**  
Parce qu'une émulation au cycle près exige des milliers de cycles d'horloge de votre PC moderne pour reproduire fidèlement une seule fraction de seconde de l'horloge originale.

**Qu'est-ce que QEMU ?**  
Un émulateur et virtualiseur open source de référence capable de modéliser des architectures complètes (ARM, x86, RISC-V, MIPS).

## Termes liés
- [ROM](/fr/dictionary/rom/)
- [Virtual Machines](/fr/dictionary/virtual-machines/)
- [Apple Silicon](/fr/dictionary/apple-silicon/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/emulator/
