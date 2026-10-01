# Qu'est-ce que ab (ApacheBench) ?

> ApacheBench

Un outil de test de performance simple permettant de mesurer combien d'utilisateurs un serveur Web peut gérer simultanément.

## Définition
Lorsque vous créez un site Web, vous vous demandez combien de visiteurs ce site peut supporter en même temps. ApacheBench, ou ab en abrégé, s'exécute à partir de la ligne de commande et envoie des centaines de requêtes factices à votre serveur simultanément. Ainsi, vous pouvez voir à l'avance quand votre serveur plantera ou ralentira.

## Comment ça marche
Vous ouvrez l'écran du terminal et tapez les commandes spécifiant l'adresse Web que vous souhaitez tester et le nombre de requêtes à envoyer. L'outil vous fournit un rapport numérique indiquant le nombre de transactions que vous pouvez effectuer par seconde.

## Où est-ce utilisé
Il est utilisé pour mesurer les performances du serveur, juste avant qu'une vague de trafic importante ne soit attendue, ou pour effectuer un test de vitesse après une optimisation du système.

## Questions fréquentes
**Imite-t-il un vrai utilisateur ?**
Pas exactement, il bombarde simplement la cible de requêtes les unes après les autre à très grande vitesse.

**Ne fonctionne-t-il que sur les serveurs Apache ?**
Non, bien qu'il s'appelle ApacheBench, il peut tester n'importe quelle adresse Web accessible sur Internet.


## Termes liés
- [Benchmark](/fr/dictionary/benchmark/)
- [Load Generator](/fr/dictionary/load-generator/)
- [CLI](/fr/dictionary/cli/)

## Outils liés
- [HEY](/fr/discover/hey/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/apache-bench-ab/
