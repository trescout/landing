# Qu'est-ce que Protocol Buffers ?

> Protobuf

Il s'agit d'une méthode qui permet à différents logiciels de regrouper et de transporter des données très rapidement et dans de petites tailles tout en communiquant entre eux.

## Définition
Les logiciels utilisent généralement des fichiers texte pour s'envoyer des données, mais ces fichiers peuvent parfois être très volumineux. Les tampons de protocole convertissent les données au format binaire, ce qui leur permet de prendre beaucoup moins de place et d'être transmises beaucoup plus rapidement. Il a été développé par Google et est désormais considéré comme la norme en matière de communication inter-systèmes.

## Comment ça marche
Vous définissez d'abord la structure des données dans un fichier modèle. Ensuite, votre logiciel regroupe les données à l'aide de ce modèle et les envoie à l'autre partie. Le côté récepteur restaure les données en utilisant le même modèle.

## Où est-ce utilisé
Il est utilisé dans les architectures de microservices, la communication d'applications mobiles avec des serveurs et des systèmes nécessitant des performances élevées.

## Souvent confondu avec
Il peut être confondu avec les formats de données textuels tels que JSON ou XML, mais il est beaucoup plus rapide et plus petit.

## Questions fréquentes
**Les gens savent-ils lire ?**
Non, les données ne peuvent pas être lues directement par les humains car elles sont au format binaire, elles sont conçues pour que seuls les ordinateurs puissent les comprendre.


## Termes liés
- [API](/fr/dictionary/api/)
- [Networking Stack](/fr/dictionary/networking-stack/)
- [Serialization](/fr/dictionary/serialization/)

## Outils liés
- [Protobuf](/fr/discover/protobuf/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/protocol-buffers/
