# Qu'est-ce que Vector Database ?

Il s’agit d’un type particulier de base de données dans laquelle l’intelligence artificielle stocke les données afin de pouvoir les retrouver rapidement en fonction de leur signification.

## Définition
Une base de données vectorielle est un système de stockage spécial qui stocke les données sous forme de vecteurs numériques représentant leur signification, plutôt que de lignes et de colonnes traditionnelles. Cette structure permet à l’intelligence artificielle de trouver les données les plus pertinentes parmi des millions de données en quelques millisecondes.

## Comment ça marche
Tout d’abord, les données sont converties en vecteurs numériques à l’aide de la méthode d’intégration. Lorsqu'une requête est effectuée, la base de données mesure la distance entre le vecteur de la requête et les vecteurs des données. Ceux dont la distance est la plus courte, c'est-à-dire ceux dont la signification est la plus proche, sont renvoyés comme résultats.

## Où est-ce utilisé
Il est utilisé dans les systèmes de recherche intelligents, les moteurs de recommandation et les systèmes RAG où l'intelligence artificielle crée une mémoire à long terme.

## Souvent confondu avec
Il est confondu avec les bases de données classiques telles que SQL, mais les bases de données classiques recherchent des correspondances exactes tandis que les bases de données vectorielles recherchent des similitudes.

## Questions fréquentes
**Est-ce plus lent que les bases de données classiques ?**
Non, c’est beaucoup plus rapide que les méthodes classiques pour les recherches de similarité dans de très grands ensembles de données.

**Quelles données peuvent être stockées ?**
Toutes les données dont la signification peut être convertie en vecteur, telles que du texte, une image, de l'audio ou de la vidéo, peuvent être stockées.


## Termes liés
- [Embedding](/fr/dictionary/embedding/)
- [RAG](/fr/dictionary/rag/)
- [Knowledge Graph](/fr/dictionary/knowledge-graph/)
- [Memory Engine](/fr/dictionary/memory-engine/)

## Outils liés
- [Zvec](/fr/discover/zvec/)
- [Turbovec](/fr/discover/turbovec/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/vector-database/
