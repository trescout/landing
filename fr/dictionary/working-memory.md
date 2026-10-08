# Qu'est-ce que la Working Memory en IA ?

> Anglais : Working Memory · Étymologie : vieil anglais weorc (travail) + latin memoria (mémoire)

La working memory (mémoire de travail) en intelligence artificielle désigne l'ensemble des informations temporaires et actives conservées dans la fenêtre de contexte d'un modèle pour mener à bien un raisonnement ou une tâche en cours.

## Définition et étymologie
Elle représente l'établi temporaire du modèle : une fois la tâche achevée ou la session réinitialisée, ce brouillon de travail s'efface. La fenêtre de contexte sert de contenant physique, tandis que les données et jetons qui y sont injectés constituent la mémoire active du calcul.

## Usage quotidien et contexte pratique
Fonctions principales de la mémoire de travail :

## Profondeur technique et architecture
Gestion du budget de jetons (tokens) :

## Souvent confondu avec
On la confond souvent avec la mémoire à long terme. La mémoire à long terme est une base de données persistante (comme un profil utilisateur). La mémoire de travail est la mémoire vive temporaire qui disparaît dès la fermeture de la session.

## Perspectives interdisciplinaires
Analogies dans d'autres domaines :

## Questions fréquentes
**Que se passe-t-il lorsque la mémoire de travail d'une IA est saturée ?**
Elle doit supprimer les échanges les plus anciens, synthétiser l'historique ou risquer d'oublier le début de la consigne.

**Quelle est la différence entre mémoire de travail et poids du modèle ?**
Les poids représentent les connaissances permanentes apprises lors de l'entraînement ; la mémoire de travail est le texte passager injecté dans l'invite.

**Peut-on agrandir la mémoire de travail indéfiniment ?**
Non, car les coûts de calcul augmentent rapidement et le modèle risque de perdre de sa précision au milieu de contextes trop longs.

**À quoi sert le cache KV ?**
Il évite de recalculer l'attention des jetons précédents à chaque nouveau mot produit, divisant le temps de réponse par dix.


## Termes liés
- [Memory](/fr/dictionary/memory/)
- [Context Window](/fr/dictionary/context-window/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/working-memory/
