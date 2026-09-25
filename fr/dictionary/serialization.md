# Qu'est-ce que la Sérialisation (Serialization) ?

> Anglais : Serialization · Étymologie : latin series (série, succession) + facere (faire)

**Catégorie:** Dev  
**Dernière mise à jour:** 2026-09-19

La sérialisation (serialization) est le processus de conversion de structures de données dynamiques, d'objets et de graphes de pointeurs en mémoire vive (RAM) en un flux d'octets linéaire ou un format textuel diffusable sur le réseau ou stockable sur disque.

## Définition et modèle mémoire : pourquoi sérialiser ?
Dans les systèmes d'exploitation modernes, chaque processus dispose d'un espace d'adressage virtuel isolé. Les objets créés dans le tas (heap) se lient par des pointeurs mémoire valables uniquement dans ce contexte d'exécution. La sérialisation aplatit ces graphes complexes pour produire une représentation portable et indépendante de l'environnement d'origine.

## Formats de sérialisation : textuel contre binaire
Le choix d'un format répond à des arbitrages précis :
- **Formats textuels (JSON, YAML, XML) :** Lisibles par l'œil humain et universellement supportés sur le Web, ils entraînent cependant une surconsommation CPU et de bande passante liée au traitement des chaînes.- **Formats binaires (Protocol Buffers, MessagePack, Avro) :** Représentations compactes, typage fort et encodage compact des entiers, offrant un débit élevé et une empreinte réseau minimale.- **Évolution des schémas :** Des solutions comme Protobuf assurent une compatibilité descendante et ascendante lors des mises à jour applicatives.

## Architecture de désérialisation Zero-Copy
La désérialisation classique recopie les octets reçus pour instancier de nouveaux objets en mémoire. Les bibliothèques modernes à haute performance (Cap'n Proto, FlatBuffers) utilisent la **désérialisation Zero-Copy** :
- **Accès direct en mémoire :** Les données sont organisées avec des décalages relatifs (offsets) précalculés.- **Absence de copie :** Le programme lit directement les données depuis le tampon réseau ou le fichier mappé en mémoire (mmap) sans allocation supplémentaire.

## Sécurité : Insecure Deserialization (CWE-502)
Lorsque les moteurs de sérialisation n'encodent pas seulement des données pures mais également des classes ou des fonctions exécutables (comme pickle en Python ou la sérialisation native Java), des failles critiques surviennent :
- **Exécution de code à distance (RCE) :** Un attaquant peut injecter des chaînes de gadgets exécutées automatiquement lors de la reconstruction d'objets.- **Recommandations :** Restreindre les échanges non fiables à des formats de données stricts (JSON, Protobuf) et contrôler l'intégrité via HMAC ou TLS.

## Par analogie
C'est comme démonter un meuble en pièces détachées pour le ranger dans un carton plat lors d'un déménagement, puis suivre la notice pour le réassembler à l'arrivée.

## Questions fréquentes

**Quelle est la différence fondamentale entre sérialisation et désérialisation ?**  
La sérialisation aplatit une structure mémoire en un flux d'octets. La désérialisation reconstitue l'objet structuré à partir de ce flux.

**Pourquoi ne faut-il jamais utiliser pickle avec des données non fiables ?**  
Pickle permet d'exécuter du code Python arbitraire dès l'étape de désérialisation, ce qui expose à des attaques RCE immédiates.

**Comment FlatBuffers parvient-il au Zero-Copy ?**  
En agençant les données binaires avec des décalages précalculés évitant toute instanciation d'objets intermédiaires.

**Quand privilégier JSON par rapport à Protobuf ?**  
Quand la lisibilité humaine, la simplicité de débogage et l'interopérabilité directe dans le navigateur priment sur la compression maximale.

## Termes liés
- [API](/fr/dictionary/api/)
- [Data Pipeline](/fr/dictionary/data-pipeline/)
- [Buffer](/fr/dictionary/buffer/)

## Outils liés
- [YAML Cpp](/fr/discover/yaml-cpp/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/serialization/
