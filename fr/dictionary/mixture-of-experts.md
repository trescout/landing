# Qu'est-ce que Mixture of Experts ?

> MoE

C'est un système qui résout des tâches complexes en les répartissant entre des sous-sections spécialisées dans différents domaines.

## Définition
Dans cette structure, au lieu que l'ensemble du modèle réponde à chaque question, seules les sections (experts) concernées par cette question sont activées. Cela permet au modèle, malgré sa taille gigantesque, de ne faire fonctionner que la partie nécessaire. En conséquence, on obtient des réponses à la fois plus intelligentes et plus rapides.

## Comment ça marche
Lorsqu'une question est posée, un mécanisme de « routage » détermine dans quel domaine d'expertise elle s'inscrit. Seuls ces experts traitent la question et génèrent une réponse.

## Où est-ce utilisé
Il est utilisé dans la plupart des grands modèles d'intelligence artificielle modernes pour augmenter l'efficacité.

## Souvent confondu avec
Il peut être confondu avec le traitement de toutes les données par un seul modèle.

## Questions fréquentes
**Comment les experts sont-ils choisis ?**
Pendant l'entraînement, le modèle apprend quels experts sont les meilleurs dans quel domaine.

**Cette méthode ralentit-elle le modèle ?**
Au contraire, il est plus rapide car seules les parties concernées sont activées.


## Termes liés
- [LLM](/fr/dictionary/llm/)
- [AI Models](/fr/dictionary/ai-models/)
- [Inference](/fr/dictionary/inference/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/mixture-of-experts/
