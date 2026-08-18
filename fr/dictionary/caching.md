# Qu'est-ce que Caching ?

Les données fréquemment utilisées sont temporairement stockées en mémoire pour un accès rapide.

## Définition
La mise en cache est une méthode d'accélération utilisée pour empêcher un système de calculer à plusieurs reprises les mêmes données ou de les extraire d'une source distante. Les données sont copiées dans une zone rapidement accessible (cache) et servies à partir de là en cas de besoin. Cela réduit considérablement le temps de réponse global du système.

## Comment ça marche
Lorsque le système demande des données, il examine d'abord le cache ; Si les données sont là, il les récupère immédiatement, sinon il les extrait de la source principale et en laisse une copie dans le cache.

## Où est-ce utilisé
Il est largement utilisé pour améliorer les performances des navigateurs Web, des applications et des centres de données à grande échelle.

## Souvent confondu avec
Il peut être confondu avec une base de données, mais le cache est temporaire et rapide, tandis que la base de données est permanente et plus volumineuse.

## Questions fréquentes
**Que se passe-t-il si le cache est plein ?**
Les données anciennes ou rarement utilisées sont supprimées et remplacées par de nouvelles données.


## Termes liés
- [KV Cache](/fr/dictionary/kv-cache/)
- [Prefix Cache](/fr/dictionary/prefix-cache/)
- [Database](/fr/dictionary/database/)

## Outils liés
- [Guava](/fr/discover/guava/)
- [Omlx](/fr/discover/omlx/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/caching/
