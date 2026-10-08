# Qu'est-ce que Emulator ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

Un émulateur est une couche système qui imite par logiciel l'architecture matérielle physique d'un ordinateur, d'un appareil mobile ou d'une console de jeux, vous permettant ainsi d'exécuter sur votre propre appareil des logiciels appartenant à des plates-formes étrangères.

## Cadre conceptuel, étymologie et différence avec le simulateur

Le terme émulateur vient du verbe latin « aemulari » (imiter, rivaliser, chercher à égaler). En turc, il est techniquement appelé « öykünücü » (imitateur) ou « donanım taklitçisi » (imitateur de matériel).

Dans le monde de l'informatique, pour éviter toute confusion conceptuelle, il est nécessaire de distinguer trois termes :

- Simulateur : Il modélise uniquement le comportement externe, les lois physiques ou les appels d'API d'un système ; il n'imite pas le matériel sous-jacent. Par exemple, l'iOS Simulator d'Apple Xcode exécute directement le code iOS de manière native sur le processeur x86 ou Apple Silicon de votre ordinateur, sans imiter les puces matérielles.
- Émulateur : Il reproduit à l'identique le processeur (CPU), la puce graphique (GPU), les bus mémoire et les registres matériels du système cible au niveau des instructions. Il traduit ligne par ligne en son propre langage le code machine binaire compilé pour une architecture étrangère.
- Virtualiseur (Virtualizer) : Exécute des systèmes ayant la même architecture de processeur que la machine hôte sous forme de partitions isolées directement sur le matériel (KVM, VMware ESXi). Comme il n'effectue pas de traduction de commandes, il est beaucoup plus rapide que les émulateurs.

***Analogie :** Cela revient à lire un manuel technique écrit dans une langue étrangère. Le simulateur est un guide qui résume le contenu du livre ; l'émulateur interpréteur est un élève qui prend un dictionnaire et traduit laborieusement chaque phrase mot à mot ; quant à l'émulateur JIT, c'est un traducteur simultané qui traduit professionnellement les chapitres du livre dans sa propre langue dès le départ, prend des notes, et lit ensuite couramment ce texte directement lors des lectures suivantes.*

## Architecture informatique et cycle du noyau : Fetch-Decode-Execute (Recherche-Décodage-Exécution)

Au cœur d'un émulateur se trouve un UC (CPU) virtuel modélisé par logiciel. Ce processeur virtuel exécute trois étapes à chaque cycle d'horloge :

1. Recherche (Fetch) : Lit l'instruction machine suivante à l'adresse de mémoire virtuelle pointée par le compteur de programme virtuel (Program Counter · PC).
2. Décodage (Decode) : Analyse le code d'opération (opcode) et les paramètres de l'instruction (par exemple MOV RAX, 0x1 ou ADD R1, R2).
3. Exécuter (Execute) : Met à jour les registres virtuels (registers) et les indicateurs (flags) en simulant la logique du matériel cible sur l'ordinateur hôte.

Méthodes de traduction d'instructions :

- Interpréteur (Interpreter) : Chaque instruction machine est lue individuellement au sein d'une boucle switch-case et le code C/Rust correspondant est appelé. Facile à développer et précis au cycle d'horloge, il sollicite toutefois lourdement le processeur (il est lent).
- Recompilation dynamique (JIT · Just-In-Time Recompiler) : c'est le secret des performances élevées des émulateurs modernes (Dolphin, RPCS3, QEMU). Les blocs de code machine étrangers sont analysés à la volée, convertis en une seule fois en code machine natif du processeur hôte (CPU hôte) et stockés dans la mémoire cache. Ainsi, lorsque la même boucle s'exécute à nouveau, le coût de traduction devient nul.
- Précision au cycle près (Cycle Accuracy) : Sur certaines consoles rétro (Game Boy, SNES), les développeurs de jeux ont synchronisé la puce sonore et la ligne de balayage raster avec l'horloge matérielle au niveau de la nanoseconde. Pour émuler ces appareils sans erreur, les cycles d'horloge CPU consommés par chaque instruction doivent être calculés sans délai.

## Domaines d'utilisation pour les développeurs, la sécurité et les entreprises

Les émulateurs ne se contentent pas de porter des jeux de consoles rétro sur des écrans modernes ; ils constituent également des outils essentiels de l'ingénierie logicielle moderne :

- Développement d'applications mobiles : L'émulateur Android Studio utilise l'hyperviseur QEMU en arrière-plan pour permettre aux développeurs de tester leur code sur des centaines de configurations matérielles et d'écrans différentes sans avoir à acheter un téléphone réel.
- Transitions d'architecture croisée (traduction binaire) : Rosetta 2, proposé par Apple lors du passage des processeurs Intel à l'architecture ARM, est en réalité un moteur de traduction binaire AOT (Ahead-of-Time) et JIT sophistiqué. Il permet d'exécuter les applications x86_64 écrites pour Intel sur Apple Silicon à une vitesse quasi sans perte.
- Cybersécurité et analyse de logiciels malveillants (émulation en sandbox) : les analystes en sécurité exécutent un ransomware suspect sur un processeur virtuel émulé plutôt que de l'ouvrir directement sur un ordinateur physique. Les opérations d'écriture en mémoire et les appels système (syscalls) sont surveillés étape par étape.
- Modernisation des systèmes hérités (Legacy Modernization) : Dans les secteurs bancaire, de la défense et des infrastructures publiques, les systèmes IBM Mainframe ou DEC VAX datant des années 1980 continuent de fonctionner sans aucune interruption grâce à des émulateurs sur des serveurs Linux modernes.

## Dimension juridique et droits d'auteur

La légalité du développement d'émulateurs a été consacrée par des affaires jurisprudentielles dans le monde entier :

- Affaires Sony c. Connectix (2000) et Sony c. Bleem! : Les tribunaux ont statué que la rétro-ingénierie des principes de fonctionnement d'un matériel par la méthode de la salle blanche (clean-room reverse engineering) pour les transcrire sous forme logicielle est légale et relève de l'usage loyal (fair use).
- Limite de droits d'auteur : Le logiciel d'émulation en lui-même est légal. Cependant, copier sans autorisation ou télécharger sur Internet des fichiers BIOS propriétaires protégés par le droit d'auteur ou des ROM de jeux/logiciels sous copyright constitue une violation des droits d'auteur.

## Questions fréquentes

**Qu'est-ce qu'un émulateur et quel est son équivalent en turc ?**

Dérivé du mot anglais 'emulator', ce terme signifie émulateur en français. Il s'agit d'un système qui exécute des logiciels de plateformes étrangères en imitant les composants matériels d'un appareil par le biais de logiciels.

**Quelle est la différence fondamentale entre un émulateur et un simulateur ?**

Alors que le simulateur imite uniquement le comportement et la logique du système, l'émulateur copie à l'identique et par logiciel le processeur, le bus mémoire et les codes machine du matériel cible au niveau des instructions.

**Comment fonctionne le compilateur dynamique JIT (Just-In-Time) dans l'émulation ?**

Il convertit les blocs de code machine du processeur étranger en code machine natif du processeur de votre propre ordinateur au moment de l'exécution et les met en cache. Ainsi, lorsque le code est exécuté une seconde fois, il s'exécute à vitesse native.

**Est-il légal de développer et d'utiliser un émulateur ?**

Oui, les logiciels d'émulation écrits selon les principes de l'ingénierie inverse en salle propre sont tout à fait légaux. Cependant, distribuer sans autorisation les fichiers BIOS propriétaires de l'appareil ou des copies ROM protégées par des droits d'auteur constitue une violation du droit d'auteur.

## Termes liés

- [ROM](https://trescout.com/fr/dictionary/rom/)
- [Sandbox](https://trescout.com/fr/dictionary/sandbox/)
- [Virtual Machines](https://trescout.com/fr/dictionary/virtual-machines/)
- [Assembly](https://trescout.com/fr/dictionary/assembly/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Apple Silicon](https://trescout.com/fr/dictionary/apple-silicon/)

## Outils liés

- [Cool Retro Term](https://trescout.com/fr/discover/cool-retro-term/)
- [Sharpemu](https://trescout.com/fr/discover/sharpemu/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/emulator/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/emulator/
