# Qu'est-ce que Caching ?

La mise en cache (caching) consiste à copier des données fréquemment utilisées vers une couche rapide.

## Définition et origine du mot
Le cache désigne une mémoire tampon. Au lieu de recalculer les mêmes données, le système les fournit à partir d'une copie. Le temps de réponse diminue et la charge est allégée. Il fonctionne à tous les niveaux, du navigateur au centre de données.

## Comment connaître et utiliser dans la vie quotidienne ?
Navigateur : Stockage de pages et d'images.Application : Copie hors ligne.Présentateur: Stockage des résultats de requête.

## Profondeur technique et architecture
Stratégies :

## Choses fréquemment mélangées
On pense à la base de données. La base de données est persistante et vaste, le cache est temporaire et rapide. L'un est un coffre-fort, l'autre est un portefeuille de poche.

## Utilisation dans différentes disciplines
Sac : Livre souvent utilisé à portée de main.Réfrigérateur : Nourriture quotidienne devant.Garde-manger : Stock global en arrière-plan.

## Foire aux questions
**Que se passe-t-il si le cache est plein ?**
L'ancien et le moins utilisé est supprimé, le nouveau est écrit. La politique gère cela.

**Quand est-ce nettoyé ?**
À l'expiration du délai, lorsque la capacité est dépassée ou manuellement. Les données critiques sont conservées à court terme.

**Y a-t-il un risque d'incohérence ?**
C'est possible. Lorsque la source change, la copie devient obsolète ; une discipline de version et de durée est nécessaire.

**Où est-ce conservé ?**
En mémoire, sur disque ou en périphérie CDN. Le choix dépend de l'équilibre entre vitesse et capacité.


## Termes liés
- [KV Cache](/fr/dictionary/kv-cache/)
- [Prefix Cache](/fr/dictionary/prefix-cache/)
- [Database](/fr/dictionary/database/)

## Outils liés
- [Free for Dev](/fr/discover/free-for-dev/)
- [OmniRoute](/fr/discover/omniroute/)
- [Guava](/fr/discover/guava/)
- [Omlx](/fr/discover/omlx/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/caching/
