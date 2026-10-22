# Qu'est-ce que Vector Database ?

*Données et infra · Dernière mise à jour : 20 septembre 2026*

Une base de données vectorielle (Vector Database) est une architecture de base de données spécialement conçue pour stocker, indexer et interroger des vecteurs numériques de haute dimension (embeddings) et leurs distances de similarité sémantique en quelques millisecondes.

## Étymologie et espace sémantique multidimensionnel

La base de données vectorielle (Vector Database) est le composant le plus critique de la couche de stockage des données de l'écosystème moderne de l'intelligence artificielle et de l'apprentissage profond. Les bases de données relationnelles traditionnelles (RDBMS) et les systèmes NoSQL sont optimisés pour interroger les données via des correspondances exactes (par exemple `WHERE id = 5` ou `name LIKE '%Ali%'`) et des hiérarchies strictes. Cependant, la grande majorité des données rencontrées à l'ère de l'intelligence artificielle (textes, photos, sons, vidéos) est de nature non structurée (unstructured).

Pour donner un sens à ces données non structurées, les modèles d'apprentissage profond les convertissent en séquences de vecteurs numériques composées de centaines ou de milliers de dimensions, appelées « embeddings ». Les bases de données vectorielles calculent les distances géométriques entre des millions, voire des milliards de points de données dans cet immense espace multidimensionnel. Cela permet de récupérer les données « les plus proches sémantiquement les unes des autres » (Nearest Neighbor Search) à des vitesses que les méthodes de recherche traditionnelles jugent impossibles.

***Analogie :** Une bibliothèque où des millions de livres sont classés uniquement par nom d'auteur par ordre alphabétique représente une base de données SQL classique. Si vous demandez : « Apporte-moi des romans de style Dostoïevski qui évoquent un sentiment de solitude et portent la mélancolie de l'automne », le catalogue classique se bloque, car ces mots ne figurent pas nécessairement sur les couvertures. Une base de données vectorielles revient quant à elle à positionner les livres dans une galaxie gigantesque. Les livres mélancoliques se regroupent dans un amas d'étoiles particulier, tandis que les aventures de science-fiction se trouvent dans un autre bras. Lorsque vous arrivez avec une émotion, le système trouve les étoiles voisines les plus proches dans la galaxie en quelques millisecondes.*

## Profondeur technique et architecture d'indexation

- Métriques de distance : La similarité entre deux embeddings est calculée à l'aide des formules de Similarité Cosinus (angle), de Distance Euclidienne (distance directe) ou de Produit Scalaire.
- Voisins les plus proches approximatifs (ANN) et HNSW : Au lieu d'une recherche par force brute parmi des millions de vecteurs, des résultats sont obtenus en millisecondes grâce aux graphiques de petits mondes hiérarchiques (HNSW) et aux index IVF.
- Recherche Hybride et Filtrage des Métadonnées : Non seulement les vecteurs, mais combinés avec des métadonnées structurées telles que la date, l'utilisateur et la catégorie, un pré-filtrage est appliqué.
- Quantification et recherche multimodale : La consommation de RAM est réduite de 75 % grâce à la quantification scalaire et par produit ; avec des modèles de type CLIP, les images et le texte peuvent être recherchés dans le même espace vectoriel.

## Dimension sociologique : la mémoire à long terme de l'intelligence artificielle

Les bases de données vectorielles constituent la mémoire numérique à long terme qui résout le problème de la "perte de mémoire" (amnésie) des modèles d'intelligence artificielle. Les grands modèles de langage sont à eux seuls des systèmes statiques et oublieux ; chaque fois qu'une session se ferme, ils perdent leurs expériences passées.

La base de données vectorielles confère à ces modèles une mémoire associative similaire à l'esprit humain. La correspondance décennale d'une entreprise, l'historique de milliers de patients d'un médecin ou l'ensemble des archives d'un chercheur sont stockés dans une base vectorielle et mis à la disposition de l'intelligence artificielle. Cette technologie transforme les silos de données en un réseau d'intelligence sémantique, modifiant de manière permanente le paradigme d'accès de l'humanité à l'information.

## Erreurs et idées fausses courantes

- Incompatibilité de modèles : Faire concourir des vecteurs produits par différents modèles d'embedding dans la même collection produit des résultats absurdes.
- Oublier le filtre de métadonnées : La similarité vectorielle pure peut omettre le contexte temporel ou catégoriel ; elle doit être complétée par des filtres.
- Ne pas anticiper le coût de la mémoire : Conserver des vecteurs de grande dimension en RAM sans compression entraîne une explosion des coûts ; une quantification doit être appliquée.

## Questions et réponses

**Les bases de données relationnelles classiques (PostgreSQL, etc.) peuvent-elles être utilisées comme bases de données vectorielles ?**

Oui ; grâce à des extensions open source comme pgvector, des bases de données relationnelles puissantes telles que PostgreSQL peuvent exécuter avec succès des recherches de similarité vectorielle en créant des index HNSW.

**Quelle est la différence entre une base de données vectorielle et une recherche en texte intégral (Full-Text) traditionnelle ?**

La recherche en texte intégral (Elasticsearch, etc.) se concentre sur la correspondance exacte des mots (lexicale), tandis que la base de données vectorielle trouve les synonymes, les relations conceptuelles et la similarité sémantique.

**Que signifie la dimension des embeddings (dimensions) ?**

Elle indique par combien de coordonnées numériques une donnée est représentée ; par exemple, un embedding à 1536 dimensions est la coordonnée ponctuelle de cette donnée dans un espace multidimensionnel à 1536 axes.

**Comment la quantification permet-elle de réaliser des économies dans les bases de données vectorielles ?**

En convertissant les nombres à virgule flottante 32 bits (float32) en entiers 8 bits ou 1 bit, elle réduit la consommation de mémoire (RAM) jusqu'à 75 % et multiplie la vitesse de recherche.

## Termes liés

- [Embedding](https://trescout.com/fr/dictionary/embedding/)
- [RAG](https://trescout.com/fr/dictionary/rag/)
- [LLM](https://trescout.com/fr/dictionary/llm/)
- [Context Window](https://trescout.com/fr/dictionary/context-window/)
- [Knowledge Graph](https://trescout.com/fr/dictionary/knowledge-graph/)
- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)

## Outils liés

- [Turbovec](https://trescout.com/fr/discover/turbovec/)
- [Zvec](https://trescout.com/fr/discover/zvec/)
- [ODS](https://trescout.com/fr/discover/ods/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/vector-database/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/vector-database/
