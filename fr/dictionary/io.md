# Qu'est-ce que I/O ?

> Input/Output

I/O (Input/Output, entrée/sortie) correspond aux échanges de données entre le système et le monde extérieur.

## Définition et origine du mot
Saisie au clavier, téléchargement de fichier, résultat affiché à l'écran : tout cela relève des E/S. Le système communique avec le monde extérieur par ce canal. C'est comme les sens et les mains de l'ordinateur.

## Comment connaître et utiliser dans la vie quotidienne ?
Clavier : Saisie de texte.Réseau : Téléchargement de fichier.Écran : Affichage des résultats.

## Profondeur technique et architecture
Concepts :

## Utilisation dans différentes disciplines
Humain : Entrée par les yeux et les oreilles, sortie par la parole.Restaurant : Prise de commande à l'entrée, service à la sortie.Usine : Entrée de matières premières, sortie de produits finis.

## Foire aux questions
**Pourquoi les E/S constituent-elles un goulot d'étranglement ?**
Le processeur est rapide, le disque et le réseau sont lents. Lorsque les données ne suivent pas, le système attend, c'est là que le goulot d'étranglement se produit.

**Qu'est-ce que le blocage ?**
C'est un appel qui attend qu'un résultat arrive. Il bloque l'interface et gaspille des ressources sur le serveur.

**Comment l'accélérer ?**
Grâce au cache, à la lecture par lots et aux appels asynchrones. On mesure d'abord, puis on corrige le maillon le plus faible.

**Quel est le rapport avec l'asynchrone ?**
C'est un système qui permet d'effectuer d'autres tâches pendant l'attente. Il permet de gérer de multiples tâches avec un seul thread.


## Termes liés
- [API](/fr/dictionary/api/)
- [Data Pipeline](/fr/dictionary/data-pipeline/)
- [Streaming Applications](/fr/dictionary/streaming-applications/)

## Outils liés
- [Asio](/fr/discover/asio/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/io/
