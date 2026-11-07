# Qu'est-ce que Time Series Database ?

*Données et infra · Dernière mise à jour : 7 novembre 2026*

Base de données spéciale qui stocke les changements au fil du temps dans l'ordre chronologique.

## Définition

Une base de données de séries temporelles (Time Series Database) est un type de base de données à haute vitesse où les données sont enregistrées avec un horodatage et où les changements en quelques secondes sont analysés. Contrairement aux bases de données classiques, au lieu de mettre à jour les données, elle ajoute continuellement un nouvel enregistrement temporel en dessous. Elle est optimisée pour surveiller l'état instantané de millions de capteurs ou de serveurs.

***Analogie :** C'est comme si un athlète tenait un carnet avec un chronomètre, y écrivant sa fréquence cardiaque et sa vitesse seconde par seconde tout au long de l'entraînement.*

## Comment ça marche

Les systèmes envoient des rapports d'état à intervalles réguliers, et cette base de données écrit ces rapports sur son disque de manière chronologique. Lors des requêtes, elle vous permet de graphiquer très rapidement les tendances passées et les changements instantanés.

## Où est-ce utilisé

Elle est utilisée dans les outils de surveillance des performances des serveurs, les flux de données boursières et les systèmes de capteurs pour maisons intelligentes.

## Souvent confondu avec

Elle peut être confondue avec les bases de données relationnelles ; alors que les bases de données relationnelles mettent à jour les états instantanés, ces systèmes accumulent tout l'historique au fil du temps.

## Questions et réponses

**Pourquoi une base de données normale n'est-elle pas utilisée pour cela ?**

Les bases de données normales ralentissent sous des piles de données massives qui s'accumulent avec le temps, tandis que ces systèmes sont conçus pour traiter les données temporelles très rapidement.

**Les anciennes données sont-elles supprimées ?**

Généralement, après une certaine période, les anciennes données sont automatiquement résumées ou nettoyées du disque.

## Termes liés

- [Database](https://trescout.com/fr/dictionary/database/)
- [Monitoring Tool](https://trescout.com/fr/dictionary/monitoring-tool/)
- [Data Processing](https://trescout.com/fr/dictionary/data-processing/)

## Outils liés

- [Prometheus](https://trescout.com/fr/discover/prometheus/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/time-series-database/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/time-series-database/
