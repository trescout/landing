# Qu'est-ce que ApacheBench (ab) ?

> Apache HTTP Server Benchmarking Tool

Il s'agit d'un outil de ligne de commande qui mesure les performances et les limites des serveurs Web dans un trafic de requêtes simultanées important.

## Définition
ApacheBench (ab) est un outil de mesure des performances léger et populaire utilisé pour tester le nombre de requêtes que les serveurs Web peuvent traiter sur une période de temps donnée. Il rapporte la réactivité du système en initiant des centaines de connexions simultanées avec une seule commande depuis la ligne de commande. Il aide les développeurs à vérifier les configurations du serveur et les optimisations du code.

## Comment ça marche
L'utilisateur détermine l'adresse cible à tester via le terminal, le nombre total de requêtes et le nombre de connexions (concurrence) à ouvrir simultanément. L'outil transmet rapidement les requêtes identifiées au serveur, collecte les temps de réponse et présente des mesures de base telles que les requêtes par seconde (RPS) sous forme de tableau.

## Où est-ce utilisé
Il est utilisé dans les tests de charge avant le lancement du site Web, dans les comparaisons de matériel serveur et dans la mesure du succès des optimisations du cache.

## Souvent confondu avec
Contrairement aux outils de test de charge avancés qui simulent des scénarios utilisateur complexes, il se concentre uniquement sur le chargement de charge séquentiel ou simultané sur une connexion HTTP spécifique.

## Questions fréquentes
**Le serveur Web Apache est-il requis pour utiliser ApacheBench ?**
Non. Il peut être exécuté de manière autonome pour tester Nginx, Node.js ou n’importe quel serveur HTTP.

**Quelle valeur est la plus prise en compte dans les résultats des tests ?**
Le nombre de requêtes terminées par seconde (Requêtes par seconde) et les délais de réponse en millisecondes sont les indicateurs les plus critiques.


## Termes liés
- [Benchmark](/fr/dictionary/benchmark/)
- [CLI](/fr/dictionary/cli/)
- [Concurrency](/fr/dictionary/concurrency/)
- [Deployment](/fr/dictionary/deployment/)

## Outils liés
- [HEY](/fr/discover/hey/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/apache-bench/
