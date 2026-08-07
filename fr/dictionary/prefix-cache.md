# Qu'est-ce que Prefix Cache ?

Une méthode d’accélération qui évite à l’intelligence artificielle de répéter les mêmes opérations en gardant en mémoire les débuts de texte qu’elle a préalablement traités.

## Définition
Les modèles d’intelligence artificielle peuvent lire depuis le début à chaque fois lors du traitement de textes longs. Le cache de préfixe enregistre la partie de début inchangée de ce texte en mémoire. Ainsi, le modèle utilise les informations littérales au lieu de relire cette partie lors de sa prochaine requête.

## Comment ça marche
Le système met en cache les préfixes des textes traités par le modèle. Lorsqu'une requête similaire arrive, le système utilise immédiatement cette partie du cache et traite uniquement les parties nouvellement ajoutées.

## Où est-ce utilisé
Il est utilisé dans les services LLM, les conversations nécessitant un contexte long et les applications d'intelligence artificielle à fort trafic.

## Souvent confondu avec
Il peut être confondu avec le cache KV ; Alors que le cache KV contient l'état interne du modèle, le cache de préfixe contient les blocs de texte.

## Questions fréquentes
**Quelle vitesse fournit-il ?**
Cela réduit considérablement le temps de réponse, notamment lorsque vous travaillez sur des documents longs.

**Est-il toujours disponible ?**
Oui, mais comme cela prend de la place en mémoire, il faut le gérer en fonction de la capacité du système.


## Termes liés
- [KV Cache](/fr/dictionary/kv-cache/)
- [Context Window](/fr/dictionary/context-window/)
- [Inference](/fr/dictionary/inference/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/prefix-cache/
