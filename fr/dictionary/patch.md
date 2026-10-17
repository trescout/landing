# Qu'est-ce que Patch ?

*Développement · Dernière mise à jour : 19 septembre 2026*

Un patch est une mise à jour de code et de fichier publiée pour corriger les erreurs d'un logiciel, combler les vulnérabilités de sécurité ou améliorer les fonctions existantes.

## 1. Patch dans le monde des logiciels et des jeux

Traditionnellement, lorsqu'une erreur se produit dans un programme, télécharger et installer l'intégralité du logiciel à partir de zéro est inefficace en termes de bande passante et de temps. Le correctif applique uniquement les octets ou fichiers modifiés au système cible.

- Correctifs de sécurité : déployés en urgence pour corriger les vulnérabilités de sécurité critiques (CVE) et les vulnérabilités Zero Day.
- Corrections de bugs : corrige les erreurs logiques qui perturbent la stabilité ou provoquent des plantages inattendus.
- Correctifs de jeu et équilibrage : il s'agit de mises à jour qui équilibrent les capacités des personnages, ajoutent du nouveau contenu et optimisent les performances dans les jeux multijoueurs en ligne. Il est généralement accompagné de « Notes de mise à jour » détaillées.
- Correctif : un correctif à portée limitée publié immédiatement pour éteindre l'incendie dans l'environnement de production sans attendre le cycle de test.

***Analogie :** Réparer une petite déchirure dans votre tenue, c'est comme coudre dessus un morceau de tissu approprié au lieu de jeter le vêtement en entier. Il remplace uniquement les pièces défectueuses sans réinstaller l'intégralité du logiciel.*

## 2. Correctif dans les outils de développement : correctif UNIX et Git

Dans le monde open source et les systèmes de contrôle de version, un correctif est un document en texte brut qui représente la différence entre deux fichiers ou commits.

### Commande et historique des correctifs UNIX

Historiquement basé sur la métaphore consistant à recouvrir les trous des cartes perforées avec du ruban adhésif ou à réparer des bandes de papier, « patch » a été standardisé avec la commande patch écrite par Larry Wall en 1985. Le patch produit avec la commande diff -u old.c new.c > fix.patch peut être appliqué directement au code source du côté opposé avec patch \< fix.patch.

### Utilisation du correctif dans l'environnement Git

Git propose des outils avancés pour diffuser des correctifs via des listes de diffusion ou des canaux hors ligne :

- git format-patch : convertit les commits spécifiques en fichiers .patch conviviaux pour le courrier électronique avec les informations sur l'auteur, le message de commit et le code différent.
- git apply : applique un fichier de correctif directement au répertoire de travail sans créer de validation.
- git am : lit les correctifs au format e-mail et crée automatiquement des commits avec l'auteur et la date d'origine (particulièrement standard dans le développement du noyau Linux).

## 3. HTTP PATCH dans l'architecture Web et les API REST

Les méthodes PUT et PATCH sont fréquemment comparées lors de la mise à jour des données dans les services RESTful :

- PUT (Full Remplacement) : Retransmet la totalité de la source. Les champs non spécifiés sont généralement réinitialisés par défaut ou supprimés. L'opération PUT est idempotente (envoyer la même requête encore et encore produit le même résultat).
- PATCH (Partial Update - RFC 5789) : envoie un corps contenant uniquement les champs dont la modification est demandée. Par exemple, pour mettre à jour uniquement l'adresse email d'un utilisateur, au lieu d'envoyer l'intégralité de l'objet profil, il suffit de transmettre uniquement le champ concerné.
- Patch JSON (RFC 6902) : il s'agit d'une structure qui définit des séquences atomiques d'opérations telles que l'ajout, la suppression, le remplacement, le déplacement, la copie et le test pour standardiser les modifications.

## Résumé comparatif : « Patch » dans différents contextes

| Contexte | Qu'est-ce que ça veut dire? | Objectif principal | Exemple typique |
|---|---|---|---|
| Logiciel et système d'exploitation | Package de mise à jour | Fermeture de vulnérabilité, stabilité | Correctif Windows Update KB, correctif Zero-day |
| Monde du jeu | Mise à jour du contenu et de l'équilibre | Equilibre du gameplay, performances, méta changement | Patch de saison (Patch 14.2), mise à jour d'équilibrage |
| Git et contrôle de version | Fichier de modifications basées sur les lignes | Partage de code, révision de code, contribution | git format-patch HEAD~1, linux-kernel.patch |
| API Web / HTTP | Méthode de mise à jour partielle | Économie de réseau, modification partielle de la ressource | PATCH /api/users/42 corps : {"status": "active"} |

## Questions fréquentes

**Que signifie Patch ? Quel est son équivalent turc ?**

Son équivalent turc est « patch » ou « bug patch ». Il fait référence à des extraits de code qui réparent ou mettent à jour une partie spécifique d'un système ou d'un logiciel sans modifier l'ensemble du système.

**Quelle est la différence entre un correctif et un correctif ?**

Les correctifs sont généralement publiés après des tests approfondis avec des versions planifiées (par exemple, des bulletins de sécurité mensuels). Un correctif, quant à lui, est un correctif d'intervention rapide et imprévu, préparé pour arrêter immédiatement un crash d'urgence ou une vulnérabilité de sécurité survenant dans l'environnement de production.

**Quelle est la principale différence entre HTTP PUT et HTTP PATCH ?**

PUT vise à remplacer complètement la ressource et donne le même résultat si la même requête est répétée (idempotente). PATCH, en revanche, ne met à jour que partiellement les zones spécifiées de la source (mise à jour partielle) et ne doit pas nécessairement être idempotent dans tous les scénarios.

**Pourquoi les fichiers de correctifs sont-ils toujours utilisés lorsqu'il existe une PR (Pull Request) dans l'environnement Git ?**

Des projets open source bien établis tels que le noyau Linux, le propre processus de développement de Git et Postgres maintiennent un flux de travail de mise à jour de correctifs basé sur le courrier électronique afin d'éviter de dépendre des plates-formes Web centrales (GitHub, etc.).

**Qu’est-ce que le Patch Tuesday ?**

C'est le nom donné au calendrier industriel dans lequel Microsoft distribue régulièrement des correctifs de sécurité en masse pour Windows et les produits d'entreprise le deuxième mardi de chaque mois.

## Termes liés

- [Vulnerability Scanning](https://trescout.com/fr/dictionary/vulnerability-scanning/)
- [Security Scanner](https://trescout.com/fr/dictionary/security-scanner/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)
- [Git Push](https://trescout.com/fr/dictionary/git-push/)

## Outils liés

- [PLFM RADAR](https://trescout.com/fr/discover/plfm-radar/)
- [PhotoGIMP](https://trescout.com/fr/discover/photogimp/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/patch/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/patch/
