# Qu'est-ce que Prefix Cache Stability ?

C’est une technique qui permet à l’intelligence artificielle de répondre aux mêmes questions de manière beaucoup plus rapide et cohérente en gardant dans sa mémoire les informations qu’elle a préalablement traitées.

## Définition
Au lieu de repartir de zéro à chaque fois, les modèles d’intelligence artificielle mettent en cache les informations importantes (préfixe) au début de la conversation. De cette manière, le modèle n’a pas besoin de lire le contexte à plusieurs reprises et le temps de réponse est réduit.

## Comment ça marche
Le système verrouille les informations que le modèle utilise le plus fréquemment ou fournit initialement en mémoire et les utilise directement dans d'autres requêtes.

## Où est-ce utilisé
Il est utilisé dans les applications d’intelligence artificielle et les chatbots à fort trafic.

## Souvent confondu avec
Il peut être confondu avec le cache KV ; Le cache KV est la mémoire du modèle au moment de l'exécution, et c'est une stratégie qui garantit que la mémoire reste stable.

## Questions fréquentes
**Cette méthode augmente-t-elle la précision ?**
Oui, car le modèle part d’une base fixe plutôt que d’interpréter différemment à chaque fois les mêmes informations.


## Termes liés
- [KV Cache](/fr/dictionary/kv-cache/)
- [Inference Engine](/fr/dictionary/inference-engine/)
- [Context Window](/fr/dictionary/context-window/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/prefix-cache-stability/
