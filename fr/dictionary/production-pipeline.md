# Qu'est-ce que Production Pipeline ?

Un pipeline de production (chaîne de production) est une chaîne de processus d'ingénierie intégrés qui permet la compilation automatique, les tests, les analyses de sécurité, l'empaquetage et le déploiement sans interruption du code source écrit par les développeurs vers l'environnement de production.

## Origine conceptuelle, étymologie et philosophie de la chaîne de production
Le terme "pipeline" est emprunté aux oléoducs et aquaducs du transport de pétrole et d'eau, et "production" aux chaînes de montage (assembly line) des usines industrielles pour être appliqué au génie logiciel. Tout comme la révolution apportée par la chaîne de montage en série d'Henry Ford dans l'industrie automobile au début du XXe siècle, le pipeline de production est le standard de production industrielle moderne qui met fin aux processus de déploiement manuels, sujets à des erreurs et incertains dans l'industrie du logiciel.

## Les 5 stations critiques d'une chaîne de production
Un pipeline de production d'entreprise complet se compose des étapes suivantes :

## Distinctions sectorielles : Production Pipeline vs Data Pipeline vs VFX Pipeline
Le mot "Pipeline" prend des sens différents selon les disciplines techniques :

## Les métriques DORA et l'efficacité de l'ingénierie
La maturité du pipeline de production d'une organisation se mesure à l'aide des quatre métriques d'or définies par la recherche DORA (DevOps Research and Assessment) de Google :

## Questions fréquentes
**Que signifie un pipeline de production et quel est son objectif principal ?**
Cela signifie une chaîne de production logicielle. Son objectif est de s'assurer que le code source développé est testé et compilé automatiquement, sans erreur humaine, et livré en toute sécurité aux serveurs de production.

**Quelle est la différence entre un pipeline de production et CI/CD ?**
CI/CD (Intégration Continue / Déploiement Continu) est la méthodologie fondamentale et la colonne vertébrale du pipeline. Le pipeline de production est quant à lui le nom du système étendu qui englobe, en plus de la CI/CD, le provisionnement d'environnements, les analyses de sécurité (DevSecOps), les mécanismes d'approbation et les outils d'observabilité.

**Avec quels outils le pipeline de production est-il mis en place ?**
GitHub et GitLab pour le contrôle de version ; GitHub Actions, Jenkins et ArgoCD pour l'orchestration ; Docker pour la conteneurisation ; Kubernetes et Terraform pour l'infrastructure sont les outils les plus courants.

**Y a-t-il des interruptions du système lors du déploiement ?**
Dans un pipeline de production bien conçu, les méthodes de déploiement Blue-Green ou Canary sont utilisées ; ainsi, les utilisateurs sont basculés vers la nouvelle version sans ressentir d'interruption (zéro temps d'arrêt).


## Termes liés
- [Deployment](/fr/dictionary/deployment/)
- [Data Pipeline](/fr/dictionary/data-pipeline/)
- [Cloud Computing](/fr/dictionary/cloud-computing/)
- [Tech Stack](/fr/dictionary/tech-stack/)
- [Git Push](/fr/dictionary/git-push/)
- [Runtime](/fr/dictionary/runtime/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/production-pipeline/
