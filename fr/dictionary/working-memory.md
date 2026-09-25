# Qu'est-ce que la Working Memory en IA ?

> Anglais : Working Memory · Étymologie : vieil anglais weorc (travail) + latin memoria (mémoire)

**Catégorie:** AI  
**Dernière mise à jour:** 2026-09-22

La working memory (mémoire de travail) en intelligence artificielle désigne l'ensemble des informations temporaires et actives conservées dans la fenêtre de contexte d'un modèle pour mener à bien un raisonnement ou une tâche en cours.

## Définition et étymologie
Elle représente l'établi temporaire du modèle : une fois la tâche achevée ou la session réinitialisée, ce brouillon de travail s'efface. La fenêtre de contexte sert de contenant physique, tandis que les données et jetons qui y sont injectés constituent la mémoire active du calcul.

## Usage quotidien et contexte pratique
Fonctions principales de la mémoire de travail :
- **Continuité du dialogue :** Retenir les questions et réponses précédentes au fil d'une conversation.- **Brouillon de raisonnement :** Conserver les étapes intermédiaires lors d'un prompt guidé pas à pas (Chain-of-Thought).- **Coordination d'outils :** Stocker temporairement les réponses d'API avant de rédiger la réponse finale.

## Profondeur technique et architecture
Gestion du budget de jetons (tokens) :
- **Capacité maximale :** Sur une fenêtre de 128 000 jetons, si l'historique en occupe 100 000, il ne reste que 28 000 jetons pour réfléchir et répondre.- **Cache KV (Key-Value) :** Les modèles de type Transformer conservent en mémoire GPU les représentations des jetons passés pour accélérer la génération.- **Stratégies d'éviction :** Lorsque la limite approche, le système résume les messages anciens pour libérer de l'espace.

## Souvent confondu avec
On la confond souvent avec la mémoire à long terme. La mémoire à long terme est une base de données persistante (comme un profil utilisateur). La mémoire de travail est la mémoire vive temporaire qui disparaît dès la fermeture de la session.

## Perspectives interdisciplinaires
Analogies dans d'autres domaines :
- **Mathématiques :** La feuille de brouillon où l'on pose ses calculs intermédiaires avant de la jeter.- **Menuiserie :** L'établi sur lequel on dépose ses outils pendant la fabrication, rangé en fin de journée.- **Informatique :** La mémoire vive (RAM) par rapport au disque dur de stockage permanent.

## Par analogie
C'est comme une feuille de brouillon sur laquelle on note des calculs intermédiaires pour résoudre un problème de géométrie : une fois le résultat trouvé, on jette le brouillon.

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
- [Attention Mechanism](/fr/dictionary/attention-mechanism/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/working-memory/
