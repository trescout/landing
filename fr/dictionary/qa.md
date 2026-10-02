# Qu'est-ce que QA ?

> Quality Assurance

L'AQ (Assurance Qualité) est une discipline systématique de gestion de la qualité qui vise à prévenir les erreurs avant qu'elles ne surviennent à chaque étape du cycle de vie du développement logiciel, à établir des normes d'ingénierie et à garantir la fiabilité du produit final.

## Origines conceptuelles : Du cycle Deming et des lignes de production au logiciel
Le concept d'assurance qualité est né dans la production industrielle au milieu du XXe siècle, bien avant les logiciels. La gestion de la qualité totale (TQM) et le cycle PDCA (Plan-Do-Check-Act / Plan-Do-Check-Act), fondés par W. Edwards Deming et Walter Shewhart, soutiennent que la qualité ne peut pas être contrôlée ultérieurement, mais doit être intégrée au produit lui-même. Le principe Jidoka (arrêt immédiat de la chaîne lorsqu'un produit défectueux est fabriqué) dans le système de production Toyota est l'ancêtre de la philosophie moderne d'intégration continue (CI) et d'assurance qualité.

## Distinction critique : AQ vs QC vs Tests
Bien que ces trois concepts soient souvent utilisés de manière interchangeable, il existe des limites méthodologiques claires entre eux :

## Paradigme moderne d'assurance qualité : Maj-Gauche et Maj-Droite
Dans le modèle traditionnel en cascade, les développeurs écrivaient du code, puis le « jetaient par-dessus le mur » au service QA pour le tester. Dans le monde Agile et DevOps moderne, cette approche a été remplacée par deux directions complémentaires :

## Testez la pyramide et les couches d'automatisation
Une architecture d'assurance qualité solide est basée sur le principe de la pyramide de tests de Mike Cohn :

## L'assurance qualité à l'ère de l'IA et du LLM
Avec la diffusion de systèmes probabilistes (non déterministes) tels que les grands modèles de langage (LLM), la discipline de l'AQ est entrée dans une nouvelle phase :

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
- [Unit Testing](/fr/dictionary/unit-testing/)
- [End-to-End Testing](/fr/dictionary/end-to-end-testing/)
- [Testing Framework](/fr/dictionary/testing-framework/)
- [Production Pipeline](/fr/dictionary/production-pipeline/)
- [Benchmarks](/fr/dictionary/benchmark/)
- [Runtime](/fr/dictionary/runtime/)

## Outils liés
- [Gstack](/fr/discover/gstack/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/qa/
