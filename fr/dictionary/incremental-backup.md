# Qu'est-ce que Incremental Backup ?

Il s'agit d'une méthode de sauvegarde qui permet d'économiser du temps et de l'espace en enregistrant uniquement les fichiers modifiés depuis la dernière sauvegarde.

## Définition
La sauvegarde incrémentielle détecte uniquement les modifications récentes et les ajoute, plutôt que de copier toutes les données à chaque fois. Cette méthode réduit considérablement le temps de sauvegarde et vous permet d'utiliser efficacement l'espace de stockage. C’est une stratégie indispensable pour les grands ensembles de données.

## Comment ça marche
Le système vérifie la date de dernière modification des fichiers. Il ajoute uniquement les parties modifiées ou nouvellement ajoutées au fichier de sauvegarde.

## Où est-ce utilisé
Il est utilisé dans les bases de données d'entreprise, les serveurs de fichiers volumineux et les systèmes de sauvegarde professionnels.

## Souvent confondu avec
Il ne faut pas la confondre avec une sauvegarde complète ; une sauvegarde complète copie tout à chaque fois.

## Questions fréquentes
**Est-ce difficile lors de la restauration ?**
Oui, c'est un peu plus compliqué qu'une sauvegarde complète car toutes les parties doivent être combinées.

**À quelle fréquence faut-il le faire ?**
Cela peut être effectué quotidiennement ou toutes les heures, en fonction de votre taux d'échange de données.


## Termes liés
- [Backup Program](/fr/dictionary/backup-program/)
- [Data Pipeline](/fr/dictionary/data-pipeline/)

## Outils liés
- [Restic](/fr/discover/restic/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/incremental-backup/
