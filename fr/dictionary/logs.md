# Qu'est-ce que Logs ?

Un log est une ligne d'événements système horodatée.

## Définition et origine du mot
"Log" signifie journal de bord : le capitaine note ce qui se passe dans un carnet. Le logiciel écrit également ligne par ligne ce qu'il fait en arrière-plan. En cas d'erreur, le carnet est ouvert et l'heure est vérifiée. C'est la première source de santé du système.

## Comment connaître et utiliser dans la vie quotidienne ?
Présentateur: Débogage.Application : Rapport de plantage.Sécurité : Trace d'événement.

## Profondeur technique et architecture
Les règles d'une bonne journalisation :

## Choses fréquemment mélangées
Souvent confondu avec le trace. Le log est l'enregistrement d'un événement, le trace est le cheminement de l'événement. L'un est une photo, l'autre est un film.

## Utilisation dans différentes disciplines
Boîte noire : Données de vol.Journal : Notes par ordre chronologique.Ticket de caisse : Journal des transactions.

## Foire aux questions
**Pourquoi les logs sont-ils nécessaires ?**
La cause de la panne se trouve dans l'enregistrement. Un système sans logs vole à l'aveugle.

**Où sont-ils écrits ?**
Dans un fichier ou un système centralisé. En production, une collecte centralisée est recommandée.

**Combien de temps sont-ils conservés ?**
Cela dépend de la politique. Le débogage nécessite des semaines, l'audit nécessite des années.

**Les données personnelles sont-elles enregistrées ?**
Non. Les mots de passe et les identifiants ne sont pas enregistrés, ils sont masqués.


## Termes liés
- [Observability](/fr/dictionary/observability/)
- [QA](/fr/dictionary/qa/)
- [Traces](/fr/dictionary/traces/)

## Outils liés
- [Grafana](/fr/discover/grafana/)
- [Modly](/fr/discover/modly/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/logs/
