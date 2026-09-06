# Qu'est-ce que Hooks ?

Ce sont des points de connexion qui vous permettent d'intervenir à des moments précis du processus d'exécution d'un logiciel pour effectuer des opérations personnalisées.

## Définition
Lorsqu'un logiciel s'exécute, ce sont des portes spéciales laissées par les développeurs pour leur permettre d'injecter leur propre code dans le flux principal. De cette façon, sans modifier le programme principal, vous pouvez faire en sorte que vos propres commandes s'exécutent lorsqu'un événement spécifique se produit. Par exemple, vous pouvez utiliser un hook pour demander une sauvegarde automatique lorsqu'un fichier est enregistré.

## Comment ça marche
Les développeurs de logiciels placent des marqueurs dans le code principal du type 'exécute cette fonction quand tu arrives ici'. Vous personnalisez ensuite le processus en connectant votre propre code à ces marqueurs. Grâce à cette méthode, même si le logiciel principal est mis à jour, les fonctionnalités que vous avez ajoutées continuent de fonctionner.

## Où est-ce utilisé
Vous les rencontrerez fréquemment en arrière-plan des sites web, dans les frameworks de développement d'applications et dans les systèmes de plugins.

## Souvent confondu avec
Ils peuvent être confondus avec les plugins ; alors que les hooks sont davantage des points de connexion au niveau du code, les plugins offrent des fonctionnalités plus étendues.

## Questions fréquentes
**Pourquoi ne pas modifier directement le code principal ?**
Modifier le code principal entraîne la suppression de toutes vos modifications lors de la mise à jour du logiciel ; les hooks, quant à eux, ne sont pas affectés par les mises à jour.


## Termes liés
- [Plugin](/fr/dictionary/plugin/)
- [Framework](/fr/dictionary/framework/)
- [API](/fr/dictionary/api/)

## Outils liés
- [Everything Claude Code](/fr/discover/everything-claude-code/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/hooks/
