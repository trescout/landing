# Qu'est-ce que Append-only ?

*Glossaire · Data · Dernière mise à jour : 24 août 2026*

Il s'agit d'une méthode d'enregistrement dans laquelle les données peuvent uniquement être ajoutées, ne peuvent pas être modifiées ou supprimées.

## Définition

Lors de l'ajout d'informations à une base de données ou à un fichier, le principe consiste à ajouter chaque nouvelle information à la fin de la liste plutôt que de remplacer les anciennes données. Cette méthode est essentielle pour préserver l’historique et la sécurité des données. Puisqu’aucune donnée n’est supprimée, il est possible de retracer tous les mouvements dans le système.

***Analogie :** C'est comme écrire chaque transaction avec un stylo à bille, au lieu d'écrire avec un crayon dans un grand livre comptable ; Vous ne pouvez pas noircir les anciennes pages.*

## Comment ça marche

Le système n'accepte qu'une commande « ajouter » plutôt qu'une commande qui met à jour les données. De cette manière, l’historique des données est toujours préservé.

## Où est-ce utilisé

Il est utilisé dans les technologies blockchain, les systèmes de tenue de journaux et les bases de données vérifiables.

## Souvent confondu avec

Peut être confondu avec les bases de données traditionnelles ; les méthodes traditionnelles peuvent mettre à jour les données, cette méthode ne le permet jamais.

## Questions fréquentes

**Que se passe-t-il si je fais une erreur ?**

Au lieu de supprimer les données erronées, vous ajoutez un nouvel enregistrement qui corrige l'erreur.

**Pourquoi est-ce si sûr ?**

Puisque les données ne peuvent pas être modifiées, il est presque impossible de manipuler le passé.

## Termes liés

- [Database](https://trescout.com/fr/dictionary/database/)
- [Logs](https://trescout.com/fr/dictionary/logs/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/append-only/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/append-only/
