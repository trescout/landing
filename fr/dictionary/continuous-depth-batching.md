# Qu'est-ce que Continuous Depth Batching ?

Il s’agit d’une méthode qui permet aux modèles d’intelligence artificielle de traiter un grand nombre de requêtes arrivant simultanément, de manière continue et rapide, sans attente.

## Définition
Les requêtes externes adressées aux modèles d’intelligence artificielle sont mises en file d’attente. Cette méthode empêche le système de rester inactif en gérant intelligemment la profondeur et le timing du traitement des requêtes entrantes au sein du modèle. Ainsi, les ressources matérielles sont utilisées de la manière la plus efficace possible et les temps de réponse sont raccourcis.

## Comment ça marche
Les fragments de texte entrants ou les charges de calcul sont regroupés dynamiquement en fonction de la capacité instantanée du modèle. Grâce à la gestion des files d'attente, chaque transaction de données est immédiatement remplacée par une nouvelle.

## Où est-ce utilisé
Il est utilisé pour augmenter les performances des infrastructures de serveurs et des services d'intelligence artificielle basés sur le cloud qui hébergent de grands modèles de langage.

## Souvent confondu avec
Contrairement aux méthodes classiques de traitement par lots, il n’attend pas la fin des requêtes, il alimente le flux instantanément.

## Questions fréquentes
**Est-ce que cela réduit les coûts du serveur ?**
Oui, il optimise les coûts en fournissant des services à davantage d'utilisateurs simultanément sur le même matériel.


## Termes liés
- [Continuous Batching](/fr/dictionary/continuous-batching/)
- [Inference Server](/fr/dictionary/inference-server/)
- [GPU](/fr/dictionary/gpu/)
- [LLM Inference](/fr/dictionary/llm-inference/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/continuous-depth-batching/
