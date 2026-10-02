# Qu'est-ce que Utilities ?

Les utilitaires (ou fonctions auxiliaires) sont des paquets de modules indépendants, pratiques et à usage unique qui assurent la maintenance et la gestion dans les systèmes d'exploitation, et qui effectuent des tâches routinières répétitives dans les projets logiciels.

## Origine conceptuelle et le terme "Utility" dans la vie quotidienne
Le mot anglais utility est dérivé de la racine latine utilis, signifiant « utile, commode », et du concept d'utilitas (utilité, adéquation à une fin). Dans l'anglais courant et le monde des affaires, ce terme apparaît dans plusieurs contextes différents :

## Au niveau des systèmes d'exploitation : la philosophie Unix et GNU Coreutils
En informatique, le concept moderne d'utilitaire repose sur la philosophie Unix, dont les bases ont été jetées aux laboratoires Bell. La règle fondamentale formulée par Doug McIlroy est la suivante : « Faites en sorte que chaque programme fasse une seule chose et qu'il la fasse bien. Concevez les programmes de manière à ce qu'ils puissent travailler ensemble. »

## Le dossier utils dans l'architecture logicielle et l'anti-pattern du « Tiroir à bazar »
Les développeurs de logiciels regroupent généralement les tâches telles que le formatage de dates, le nettoyage de chaînes de caractères, l'arrondi de devises ou le calcul de hashs cryptographiques dans des répertoires nommés utils/, helpers/ ou common/ au sein de leurs projets.

## Dans l'intelligence artificielle et le développement de jeux : Utility AI
Dans le domaine du développement de jeux et de l'intelligence artificielle, l'« Utility AI » est un modèle mathématique utilisé dans les mécanismes de prise de décision. Au lieu de machines à états finis (FSM) classiques ou d'arbres de comportement (Behavior Trees), un score d'utilité est attribué à chaque action possible en fonction des paramètres de l'état actuel, et le personnage choisit l'action qui offre l'utilité la plus élevée.

## Questions fréquentes
**Que signifie « Utilities » et quelle est sa traduction en turc ?**
« Utilities » signifie « outils utiles » en anglais. En informatique, il est traduit en turc par « yardımcı programlar » (programmes utilitaires), « yardımcı araçlar » (outils utilitaires) ou, au niveau du code, par « yardımcı fonksiyonlar » (fonctions utilitaires).

**Pourquoi le dossier « utils » dans les projets logiciels se transforme-t-il avec le temps en dette technique ?**
Lorsque les développeurs placent tout code n'appartenant pas à un module spécifique dans « utils », ce dossier se transforme en un tiroir à bazar incontrôlé de milliers de lignes, créant des dépendances circulaires et une complexité de code élevée.

**Quel est le lien entre la philosophie Unix et les outils utilitaires ?**
La philosophie Unix préconise que chaque outil utilitaire ne fasse qu'une seule chose parfaitement et qu'il soit enchaîné avec d'autres outils via des pipelines d'entrée/sortie pour résoudre des problèmes complexes.

**Les bibliothèques utilitaires comme Lodash sont-elles toujours nécessaires ?**
Les versions modernes de JavaScript (ES6+) ont perdu leur popularité d'antan car elles offrent nativement de nombreuses manipulations de base sur les tableaux et les objets ; cependant, elles sont toujours utilisées pour le clonage profond et les opérations fonctionnelles avancées.


## Termes liés
- [CLI](/fr/dictionary/cli/)
- [API](/fr/dictionary/api/)
- [Framework](/fr/dictionary/framework/)
- [Runtime](/fr/dictionary/runtime/)
- [Production Pipeline](/fr/dictionary/production-pipeline/)
- [Bundler](/fr/dictionary/bundler/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/utilities/
