# Qu'est-ce que Auto-fallback ?

Lorsqu'une erreur se produit dans un système ou que la méthode principale échoue, le système passe automatiquement à une méthode plus sûre ou alternative.

## Définition
Le repli automatique garantit que le système n'abandonne pas. Par exemple, lorsque votre modèle d'IA le plus avancé ne répond pas, le système passe automatiquement à un modèle plus rapide mais plus simple pour terminer le processus. Il s'agit d'une mesure de sécurité essentielle pour garantir que l'expérience utilisateur se poursuit sans interruption.

## Comment ça marche
Une règle « si cela ne fonctionne pas, faites ceci » est intégrée au logiciel. Le système vérifie constamment l'état et active la méthode de sauvegarde chaque fois que la méthode principale renvoie un code d'erreur.

## Où est-ce utilisé
Il est utilisé dans les services d’intelligence artificielle, les connexions réseau et la gestion de serveurs.

## Souvent confondu avec
C'est similaire à la gestion des erreurs ; Cependant, le repli automatique fait directement référence à une solution alternative.

## Questions fréquentes
**Cette fonctionnalité entraîne-t-elle des lenteurs ?**
Parfois, le processus de transition peut entraîner un retard de quelques millisecondes, mais cela vaut mieux qu'un arrêt complet du système.

**Est-ce que ça marche toujours ?**
Si la méthode de sauvegarde est également défectueuse, le système continuera à échouer, les sauvegardes doivent donc également être fiables.


## Termes liés
- [Observability](/fr/dictionary/observability/)
- [Runtime](/fr/dictionary/runtime/)
- [AI Gateway](/fr/dictionary/ai-gateway/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/auto-fallback/
