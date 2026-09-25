# Qu'est-ce que Git Push ?

> Anglais : Git Push · Étymologie : argot britannique git + latin pulsare (pousser, heurter)

**Catégorie:** Dev  
**Dernière mise à jour:** 2026-09-19

Git Push est la commande fondamentale de contrôle de version qui expédie les commits locaux, l'historique et les objets vers un serveur Git distant, synchronisant la branche distante avec le travail accompli en local.

## Par analogie
C'est comme rédiger des chapitres d'un livre sur son traitement de texte privé, puis expédier le manuscrit à la maison d'édition centrale pour que tous les coauteurs reçoivent la version mise à jour.

## 1. Définition et modèle de données en 4 couches de Git
Git est un système de gestion de versions distribué (DVCS) structuré en quatre zones d'état : le répertoire de travail, la zone d'index (staging), le dépôt local (.git) et le dépôt distant (GitHub, GitLab). Alors que <code>git commit</code> archive vos modifications sur votre propre disque dur, <code>git push</code> est l'action réseau qui transfère ces objets vers le serveur distant partagé par l'équipe.

## 2. Les commandes courantes (Aide-mémoire)
Syntaxes indispensables au quotidien :
- **Premier envoi de branche :** <code>git push -u origin feature-branche</code> (lie la branche locale à la branche distante).- **Envoi standard :** <code>git push</code> (met à jour la branche de suivi configurée).- **Envoi de tags :** <code>git push origin --tags</code> (publie les étiquettes de versions logicielles).- **Suppression distante :** <code>git push origin --delete ancienne-branche</code>.- **Écrasement sécurisé :** <code>git push --force-with-lease</code> (force la mise à jour seulement si aucun collègue n'a poussé de commit entre-temps).

## 3. Erreurs fréquentes et résolutions
Résoudre les rejets d'envoi classiques :
- **fatal: [rejected - non-fast-forward] :** La branche distante contient des commits absents de votre poste. Solution : exécuter <code>git pull --rebase origin main</code> puis relancer le push.- **fatal: The current branch has no upstream branch :** Utiliser le paramètre <code>-u</code> pour rattacher la branche locale à l'origin.- **Rejet de fichiers volumineux :** Git refuse les fichiers de plus de 100 Mo ; recourir à Git LFS pour les données binaires massives.

## Questions fréquentes

**Quelle est la différence entre 'git commit' et 'git push' ?**  
Git commit enregistre un instantané sur votre machine ; git push transmet cet historique sur le serveur distant partagé.

**Pourquoi privilégier '--force-with-lease' à '--force' ?**  
Parce que --force écrase brutalement le serveur même si un collègue a poussé du code ; --force-with-lease s'arrête si la branche a été modifiée par un tiers.

**À quoi servent les hooks pre-push ?**  
À exécuter des tests unitaires en local avant l'envoi pour bloquer le push si des anomalies sont détectées.

**Peut-on pousser vers plusieurs dépôts distants en même temps ?**  
Oui, en configurant plusieurs URLs sous le même alias de dépôt dans le fichier .git/config.

## Termes liés
- [CLI](/fr/dictionary/cli/)
- [Code Snippets](/fr/dictionary/code-snippets/)
- [Checkout](/fr/dictionary/checkout/)

## Outils liés
- [No Mistakes](/fr/discover/no-mistakes/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/git-push/
