# Qu'est-ce que Logging ?

La journalisation (ou logging) consiste à enregistrer les événements d'un programme de manière chronologique.

## Définition et origine du mot
Un journal (log) est un registre d'événements. Lorsqu'un programme rencontre une erreur silencieuse, il est possible de consulter ce registre pour comprendre ce qu'il a fait jusqu'à ce moment-là. C'est comme la boîte noire d'un avion : c'est le premier endroit que l'on examine après un incident.

## Comment connaître et utiliser dans la vie quotidienne ?
Présentateur: Débogage.Produit: Suivi d'utilisation.Sécurité : Journalisation des événements.

## Profondeur technique et architecture
Niveaux :

## Choses fréquemment mélangées
On pense qu'il s'agit d'observabilité. Pourtant, la journalisation en est la pierre angulaire : le journal est la matière première, la capacité d'observation est le produit.

## Utilisation dans différentes disciplines
Boîte noire : Enregistrement des données de vol.Journal : Notes par ordre chronologique.Enregistrement de la caméra : Archive des événements.

## Foire aux questions
**Est-ce bien de tout sauvegarder ?**
Non. Un excès ralentit le système et masque l'essentiel ; un enregistrement équilibré est maintenu.

**Qu'est-ce qu'un niveau ?**
C'est l'étiquette d'urgence de l'enregistrement. Il sert de filtre lors de la recherche.

**Où les enregistrements sont-ils écrits ?**
Dans un fichier, un système central ou un service cloud. En production, une collecte centralisée est recommandée.

**Combien de temps sont-ils conservés ?**
Cela dépend de la politique. Le débogage nécessite des semaines, l'audit nécessite des années.


## Termes liés
- [Observability](/fr/dictionary/observability/)
- [Traces](/fr/dictionary/traces/)
- [Logs](/fr/dictionary/logs/)

## Outils liés
- [OmniRoute](/fr/discover/omniroute/)
- [Spdlog](/fr/discover/spdlog/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/logging/
