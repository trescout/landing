# Qu'est-ce que Serialization ?

La sérialisation est le processus qui consiste à transformer des objets, des structures de données et des graphes de pointeurs alloués dynamiquement dans la mémoire vive (RAM) d'un langage de programmation en un flux d'octets plat et linéaire ou en un format textuel pouvant être transmis sur un réseau ou stocké sur un disque.

## Qu'est-ce que la sérialisation et pourquoi est-elle indispensable ? Modèle de mémoire
Dans les systèmes d'exploitation modernes, chaque processus s'exécute dans son propre espace d'adressage virtuel isolé. À l'exécution, un objet contient des variables locales sur la pile (stack), des blocs de mémoire alloués dynamiquement sur le tas (heap), des pointeurs de fonctions (vtable) et des adresses de référence (0x7ffee4b2...).

## Formats de sérialisation : Basés sur du texte vs Binaires
Choisir le bon format de sérialisation en architecture logicielle nécessite de trouver un équilibre entre la lisibilité humaine, le coût d'analyse (parsing) du processeur, la bande passante réseau et la sécurité des types.

## Architecture de désérialisation Zero-Copy
Dans les bibliothèques de sérialisation classiques (analyseurs JSON ou Protobuf standard), le processus de désérialisation s'articule autour des étapes suivantes :

## Dimension de Sécurité : Désérialisation Non Sécurisée (CWE-502)
Des vulnérabilités catastrophiques surviennent lorsque la sérialisation tente de transporter non seulement des données pures, mais aussi des classes d'objets et des comportements d'exécution. Présente dans le Top 10 de l'OWASP, la désérialisation non sécurisée (Insecure Deserialization) permet à un attaquant d'exécuter du code arbitraire sur le système (Remote Code Execution - RCE).

## Questions fréquentes
**Quelle est la différence fondamentale entre la sérialisation et la désérialisation ?**
La sérialisation est le processus qui consiste à convertir des objets vivants en mémoire en un flux d'octets ou de texte stockable ou transmissible. La désérialisation, quant à elle, est le processus qui consiste à lire et analyser cette séquence d'octets pour la reconvertir en un objet fonctionnel dans la mémoire du système cible.

**Dans les projets web, quand faut-il utiliser Protobuf ou FlatBuffers à la place de JSON ?**
Pour les clients web ouverts à l'internet général et les API publiques, JSON est idéal en raison de sa compatibilité avec les navigateurs et de sa facilité de débogage. Cependant, pour les microservices internes, les backends d'applications mobiles ou les flux de données en temps réel, Protobuf ou FlatBuffers doivent être privilégiés afin de réduire la bande passante réseau et le coût de traitement du processeur lié à l'analyse.

**Comment fonctionne l'attaque par désérialisation non sécurisée (Insecure Deserialization) et comment l'empêcher ?**
L'attaquant injecte des fonctions malveillantes ou des structures de classes à exécuter lors de la désérialisation dans les données sérialisées. Lorsque le serveur analyse ces données, des commandes système peuvent être déclenchées. Pour l'empêcher, les formats transportant une logique de classe doivent être abandonnés et seuls des formats schématiques transportant des données brutes (Protobuf, JSON Schema) doivent être utilisés.

**Que signifie la désérialisation sans copie (zero-copy deserialization) ?**
C'est une technique qui consiste à lire les données directement via des décalages de pointeurs dans la mémoire tampon (buffer), au lieu d'allouer de nouveaux espaces mémoire et de copier le flux d'octets entrant. En éliminant l'allocation mémoire, cela soulage le processeur et le ramasse-miettes (garbage collector).

**Qu'est-ce que l'évolution de schéma (Schema Evolution) et comment garantit-on la rétrocompatibilité et la compatibilité ascendante ?**
À mesure que le logiciel est mis à jour, les modèles de données changent. Des systèmes tels que Protobuf et Avro garantissent, en attribuant des identifiants numériques uniques aux champs, que les anciens clients ignorent les nouveaux champs (rétrocompatibilité) et que les nouveaux clients peuvent lire les anciennes données avec des valeurs par défaut (compatibilité ascendante).


## Termes liés
- [API](/fr/dictionary/api/)
- [Data Pipeline](/fr/dictionary/data-pipeline/)
- [Memory Management](/fr/dictionary/memory-management/)
- [Network Stack](/fr/dictionary/network-stack/)

## Outils liés
- [YAML Cpp](/fr/discover/yaml-cpp/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/serialization/
