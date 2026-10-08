# Qu'est-ce que QA ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

> Quality Assurance

L'AQ (Assurance Qualité) est une discipline systématique de gestion de la qualité qui vise à prévenir les erreurs avant qu'elles ne surviennent à chaque étape du cycle de vie du développement logiciel, à établir des normes d'ingénierie et à garantir la fiabilité du produit final.

## Origines conceptuelles : Du cycle Deming et des lignes de production au logiciel

Le concept d'assurance qualité est né dans la production industrielle au milieu du XXe siècle, bien avant les logiciels. La gestion de la qualité totale (TQM) et le cycle PDCA (Plan-Do-Check-Act / Plan-Do-Check-Act), fondés par W. Edwards Deming et Walter Shewhart, soutiennent que la qualité ne peut pas être contrôlée ultérieurement, mais doit être intégrée au produit lui-même. Le principe Jidoka (arrêt immédiat de la chaîne lorsqu'un produit défectueux est fabriqué) dans le système de production Toyota est l'ancêtre de la philosophie moderne d'intégration continue (CI) et d'assurance qualité.

Dans le monde du logiciel, la célèbre recherche « Software Engineering Economics » de Barry Boehm a prouvé que si le coût de correction d'un bug remarqué au stade de la conception est de 1 unité, le coût de sa correction après sa mise en ligne (production) peut être multiplié par 100. L'assurance qualité existe pour éviter ce coût énorme et cette perte de réputation.

***Analogie :** Le débogage signifie intervenir sur la table d’opération, et tester les logiciels signifie effectuer des analyses en laboratoire. L'AQ est un protocole de santé publique et de médecine préventive : il vise à éliminer dès le début le risque de tomber malade en fixant des directives en matière d'alimentation saine, des calendriers de vaccination et des règles d'hygiène.*

## Distinction critique : AQ vs QC vs Tests

Bien que ces trois concepts soient souvent utilisés de manière interchangeable, il existe des limites méthodologiques claires entre eux :

**Essai:** Il s’agit du déroulement de scénarios (orientés produit et réactifs) pour trouver des erreurs concrètes (bugs) dans une version spécifique du logiciel.

**Contrôle Qualité (QC - Contrôle Qualité) :** C'est la porte d'audit (elle est orientée produit et réactive) qui vérifie si le produit est conforme aux spécifications techniques et aux critères d'acceptation déterminés avant sa sortie.

**Assurance qualité (AQ) :** Il s'agit de la discipline générale (elle est orientée processus et proactive) qui conçoit les méthodologies de développement, l'infrastructure de test, les normes architecturales et les processus CI/CD afin qu'aucun bug ne se produise.

## Paradigme moderne d'assurance qualité : Maj-Gauche et Maj-Droite

Dans le modèle traditionnel en cascade, les développeurs écrivaient du code, puis le « jetaient par-dessus le mur » au service QA pour le tester. Dans le monde Agile et DevOps moderne, cette approche a été remplacée par deux directions complémentaires :

**1. Maj-Gauche :** Il place le contrôle qualité au premier plan du développement. Pendant que le développeur écrit du code, il applique l'analyse statique (ESLint, SonarQube), la vérification de type (TypeScript), les tests unitaires (Jest, pytest) et le TDD (Test-Driven Development). L'ingénieur QA n'est pas la personne qui exécute les tests ici, mais un architecte de plate-forme qui construit l'infrastructure et les frameworks de test.

**2. Maj-Droite :** Maintenir la qualité après la mise en ligne du code. L'expérience utilisateur réelle est contrôlée grâce à la surveillance synthétique, aux distributions Canary, au suivi des erreurs (Sentry), à l'ingénierie du chaos et à l'analyse du trafic en direct.

## Testez la pyramide et les couches d'automatisation

Une architecture d'assurance qualité solide est basée sur le principe de la pyramide de tests de Mike Cohn :

**Tests unitaires :** Il constitue la base ; Il teste les fonctions indépendantes de manière isolée, fonctionne en quelques millisecondes et présente le coût le plus bas.

**Tests d'intégration et de contrat :** Valide les accords d'API de base de données, de cache et inter-microservices (par exemple Pact).

**Tests de bout en bout (Tests E2E) :** Simule les étapes d'un utilisateur réel dans le navigateur avec des outils comme Cypress ou Playwright ; Sa portée est plus large mais son entretien est plus coûteux.

**Tests non fonctionnels :** Comprend des tests de charge et de stress (k6, Locust), des analyses de vulnérabilité (SAST/DAST) et des contrôles d'accessibilité (WCAG/a11y).

## L'assurance qualité à l'ère de l'IA et du LLM

Avec la diffusion de systèmes probabilistes (non déterministes) tels que les grands modèles de langage (LLM), la discipline de l'AQ est entrée dans une nouvelle phase :

**Évaluations LLM (Evals):** Vérifications automatisées (DeepEval, Ragas) qui évaluent les hallucinations, l'exactitude, la toxicité et la pertinence des réponses du modèle.

**Tests de régression sémantique :** Des benchmarks qui mesurent si une modification apportée aux modèles d’invite dégrade la qualité des réponses précédentes.

**Production de tests prise en charge par l’intelligence artificielle :** Détection automatique des scénarios de tests et des différences de régression de l'interface visuelle avec les modèles d'intelligence artificielle.

## Questions fréquentes

**Que signifie l’assurance qualité et que signifie-t-elle ?**

C'est une abréviation de l'expression Assurance Qualité ; Cela signifie assurance qualité en turc. C'est la discipline d'ingénierie qui garantit le fonctionnement sans erreur des processus logiciels du début à la fin.

**Quelle est la différence entre l'AQ et le QC (Contrôle qualité) et les tests ?**

Les tests et le contrôle qualité sont des étapes réactives qui se concentrent sur la recherche de bogues dans le code existant. L'assurance qualité, quant à elle, est le processus proactif qui conçoit des processus de développement, des normes et des outils pour garantir qu'aucune erreur ne se produise en premier lieu.

**Que signifient les approches de test Shift-Left et Shift-Right ?**

Amener les processus de test Shift-Left au tout début du développement (au moment de l'écriture du code) ; Shift-Right fait référence à la surveillance instantanée de la santé du système et du comportement des utilisateurs dans l'environnement réel.

**Comment effectuer l'assurance qualité dans les applications basées sur l'IA et le LLM ?**

En plus des tests traditionnels, des cadres d'évaluation spéciaux (evals) sont utilisés pour mesurer les taux d'hallucinations, la similarité sémantique, la régression rapide et les mesures de précision RAG.

## Termes liés

- [Unit Testing](https://trescout.com/fr/dictionary/unit-testing/)
- [End-to-End Testing](https://trescout.com/fr/dictionary/end-to-end-testing/)
- [Testing Framework](https://trescout.com/fr/dictionary/testing-framework/)
- [Production Pipeline](https://trescout.com/fr/dictionary/production-pipeline/)
- [Benchmarks](https://trescout.com/fr/dictionary/benchmark/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)

## Outils liés

- [Gstack](https://trescout.com/fr/discover/gstack/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/qa/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/qa/
