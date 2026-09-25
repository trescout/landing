# Qu'est-ce que la QA (Assurance Qualité) ?

**Catégorie :** Développement
**Dernière mise à jour :** 2026-09-19

La QA (Quality Assurance - Assurance Qualité) est une discipline d'ingénierie logicielle systématique visant à prévenir l'apparition des anomalies à chaque étape du cycle de développement (SDLC), à bâtir des standards rigoureux et à garantir la fiabilité du produit fini.

## Origines conceptuelles : Du cycle de Deming à l'ingénierie logicielle
L'Assurance Qualité est née dans l'industrie manufacturière du milieu du XXe siècle bien avant l'avènement de l'informatique. Le Management de la Qualité Totale (TQM) et la roue de Deming (PDCA / Plan-Do-Check-Act) de W. Edwards Deming et Walter Shewhart affirmaient que la qualité ne peut être inspectée a posteriori, mais doit être intégrée dans le procédé de fabrication. Le principe Jidoka du système Toyota (arrêt immédiat de la chaîne lors d'une anomalie) est l'ancêtre direct de l'intégration continue (CI) moderne.Dans le logiciel, les travaux de Barry Boehm sur l'économie du génie logiciel ont prouvé que corriger une anomalie détectée dès la conception coûte 1 unité, contre jusqu'à 100 fois plus cher lorsqu'elle atteint la production. La QA est conçue pour neutraliser ce coût financier et ce risque réputationnel.

## Distinction fondamentale : QA vs QC vs Testing
Bien que ces trois termes soient souvent confondus, des frontières méthodologiques précises les séparent :Test (Testing) : Exécution de scénarios pour détecter des bugs concrets dans une version donnée (orienté produit et réactif).Contrôle Qualité (QC - Quality Control) : Porte de vérification validant la conformité du logiciel aux spécifications techniques avant livraison (orienté produit et réactif).Assurance Qualité (QA - Quality Assurance) : Discipline globale concevant les méthodologies, l'outillage de test, les standards d'architecture et les pipelines CI/CD pour empêcher l'apparition des bugs (orientée processus et proactive).

## Paradigmes modernes de la QA : Shift-Left et Shift-Right
Dans les anciens modèles en cascade, les développeurs écrivaient le code puis le 'jetaient par-dessus le mur' à l'équipe de test. Les approches agiles et DevOps ont substitué à cette friction deux démarches complémentaires :1. Shift-Left (Déplacement à gauche) : Avancer la validation au plus tôt dans le cycle. Dès la saisie du code, les ingénieurs appliquent analyse statique (SonarQube), typage strict, tests unitaires et TDD. L'ingénieur QA devient un architecte de plateforme concevant les frameworks d'automatisation.2. Shift-Right (Déplacement à droite) : Maintenir la qualité après déploiement en production. Tests synthétiques continus, déploiements canaris, télémétrie d'erreurs (Sentry) et chaos engineering valident la résilience en conditions réelles.

## Pyramide de tests et couches d'automatisation
Une architecture de QA robuste repose sur la pyramide de tests de Mike Cohn :Tests unitaires : Le socle fondamental ; rapides, isolés et peu coûteux en maintenance.Tests d'intégration et de contrat : Valident les échanges entre bases de données, caches et microservices (APIs REST, contrats Pact).Tests de bout en bout (E2E) : Pilotent des navigateurs avec Playwright ou Cypress pour simuler le parcours d'un utilisateur réel.Tests non-fonctionnels : Tests de charge (k6, Locust), audits de sécurité (SAST/DAST) et vérifications d'accessibilité (WCAG/a11y).

## Analogie
Le débogage s'apparente à une opération chirurgicale d'urgence et le test à une analyse en laboratoire. La QA est l'équivalent de la santé publique et de la médecine préventive : elle établit les règles d'hygiène et les protocoles sanitaires pour empêcher l'organisme de tomber malade.

## La QA à l'ère de l'intelligence artificielle et des LLM
Avec l'essor de systèmes non-déterministes comme les grands modèles de langage, la QA explore de nouveaux territoires :Évaluations de LLM (Evals) : Outils automatisés (DeepEval, Ragas) mesurant le taux d'hallucination, la fidélité factuelle et la pertinence sémantique.Tests de régression sémantique : Jeux d'étalonnage (benchmarks) s'assurant qu'une modification de prompt ne dégrade pas les réponses antérieures.Génération de tests par IA : Création autonome de scénarios aux limites et détection visuelle de régressions d'interface par vision par ordinateur.

## Questions fréquentes

### Que signifie l'acronyme QA en informatique ?
QA signifie Quality Assurance (Assurance Qualité). Il s'agit de la discipline d'ingénierie qui structure les processus et outils pour garantir la conformité et la fiabilité logicielle.

### En quoi la QA diffère-t-elle du test logiciel ?
Le test est une action réactive consistant à traquer les bugs dans un livrable existant. La QA est une démarche proactive qui conçoit les normes et environnements pour éviter que les bugs ne soient introduits.

### Que signifient les approches Shift-Left et Shift-Right ?
Shift-Left intègre la validation dès l'écriture du code (tests unitaires, linting), tandis que Shift-Right surveille en temps réel le comportement du système et des utilisateurs en production.

### Comment applique-t-on la QA sur des applications basées sur des LLM ?
En plus des tests classiques, on déploie des frameworks d'évaluation (evals) qui mesurent les taux d'hallucination, la dérive sémantique et la précision de la recherche RAG.

## Termes associés
- [Unit Testing](/fr/dictionary/unit-testing/)
- [End-to-End Testing](/fr/dictionary/end-to-end-testing/)
- [Testing Framework](/fr/dictionary/testing-framework/)
- [Production Pipeline](/fr/dictionary/production-pipeline/)
- [Benchmarks](/fr/dictionary/benchmark/)
- [Runtime](/fr/dictionary/runtime/)

## Outils associés
- [Gstack](/fr/discover/gstack/)

---
Source: TreScout Tech Dictionary · https://trescout.com/fr/dictionary/qa/
