# Qu'est-ce que Worktree ?

C'est une structure qui vous permet de travailler simultanément sur différentes versions d'un projet sans modifier le dossier du projet original.

## Définition
Worktree vous permet d'ouvrir différentes branches du projet dans des dossiers distincts sans perturber votre espace de travail principal lors du développement logiciel. Par exemple, tout en développant une fonctionnalité dans le projet principal, vous pouvez simultanément corriger un ancien bug dans un autre dossier. Cela élimine la perte de temps et la confusion causées par le changement constant de branches.

## Comment ça marche
Vous ajoutez un nouveau worktree via des systèmes de contrôle de version comme Git. Le système lie une copie du projet à un répertoire différent pour vous, et vous continuez à y travailler sans toucher au répertoire principal.

## Où est-ce utilisé
Il est utilisé dans les projets logiciels complexes lorsque des corrections de bugs urgentes doivent être effectuées pendant le développement de fonctionnalités de longue durée.

## Souvent confondu avec
Ce n'est pas la même chose que de simplement copier des dossiers ; les worktrees sont liés au même dépôt Git et fonctionnent de manière synchronisée.

## Questions fréquentes
**Pourquoi ne pas simplement copier des dossiers séparément ?**
Copier gaspille de l'espace disque et rend la gestion de l'historique Git difficile ; le worktree est beaucoup plus efficace.

**Est-ce que cela fonctionne avec tous les projets Git ?**
Oui, cette fonctionnalité est prise en charge dans toutes les versions modernes de Git.


## Termes liés
- [Source Control](/fr/dictionary/source-control/)
- [Git Push](/fr/dictionary/git-push/)
- [Repository Checkout](/fr/dictionary/repository-checkout/)

## Outils liés
- [Worktrunk](/fr/discover/worktrunk/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/worktree/
