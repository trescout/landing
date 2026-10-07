# Qu'est-ce que Telemetry ?

La télémétrie est la collecte et la transmission automatiques d'informations sur l'état des logiciels et des appareils vers un centre de données.

## Définition et origine du mot
Le mot vient des racines grecques tele (loin) et metron (mesure). Les applications envoient aux développeurs des rapports sur le fonctionnement du logiciel : quelles fonctionnalités sont les plus utilisées, où l'application plante. Pour l'utilisateur, il s'agit généralement d'un flux de données qui s'exécute silencieusement en arrière-plan.

## Comment connaître et utiliser dans la vie quotidienne ?
Débogage : Collecte automatique des rapports de plantage.Décision produit : Simplification d'un bouton peu utilisé.Performance : Suivi du temps de chargement version par version.

## Profondeur technique et architecture
Les trois piliers de l'observabilité :

## Choses fréquemment mélangées
Cela peut être confondu avec le logging. Le log est une ligne d'événement unique. La métrique est un résumé numérique. Le trace est le parcours de la requête. La télémétrie est le nom du processus de collecte et de transmission de ces trois éléments.

## Utilisation dans différentes disciplines
Hôpital: Le moniteur patient transmettant le pouls à l'écran de l'infirmière.Aviation : Le stockage des données de vol dans la boîte noire.Énergie : Les compteurs signalent la consommation au centre.

## Foire aux questions
**Cela affecte-t-il ma vie privée ?**
Les données sont généralement collectées de manière anonyme et agrégée. Vous pouvez voir quelles données sont envoyées et les désactiver dans la section des paramètres de l'application.

**Quelle est la différence avec l'observabilité ?**
La télémétrie collecte et transmet les données. L'observabilité est la capacité de comprendre l'intérieur du système grâce aux données collectées. L'un est l'outil, l'autre est l'objectif.

**Est-il possible de le désactiver ?**
Dans la plupart des applications, oui, cela peut être désactivé dans les paramètres. Sur les appareils d'entreprise, cela peut rester activé par politique.

**Y a-t-il un coût ?**
Oui. Il y a des frais de transfert et de stockage des données. C'est pourquoi, en cas de trafic élevé, un échantillonnage est effectué : seule une partie des événements est envoyée, et non la totalité.


## Termes liés
- [Logs](/fr/dictionary/logs/)
- [Observability](/fr/dictionary/observability/)
- [Traces](/fr/dictionary/traces/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/telemetry/
