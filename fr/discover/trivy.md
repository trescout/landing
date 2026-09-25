# Scanner de sécurité pour conteneurs et cloud

Trivy est un scanner de sécurité complet et ultra rapide qui identifie les vulnérabilités (CVE), les erreurs de configuration et les clés secrètes dans les conteneurs, clusters Kubernetes et dépôts de code. Grâce à son support natif des SBOM, il automatise la conformité DevSecOps.

- ★ 35.511
- Go
- GitHub Trending · 2026-06-04

## Ce que ça vous apporte
- Analyse multi-cibles complète: Inspectez les images de conteneurs (Docker, OCI), les systèmes de fichiers, dépôts Git distants et clusters Kubernetes avec un seul outil.
- Zéro infrastructure requise: Ne nécessite aucun serveur de base de données externe ni démon persistant ; fonctionne comme un binaire autonome léger.
- Détection des secrets et données sensibles: Identifie les clés API, mots de passe et certificats privés accidentellement commités dans le code ou les images.
- Contrôle de l'infrastructure as Code (IaC): Valide les fichiers Terraform, Dockerfile, Kubernetes YAML et CloudFormation avant la mise en production.
- SBOM et conformité des licences: Génère des inventaires logiciels aux formats CycloneDX et SPDX pour satisfaire aux exigences légales de la supply chain.

## Installation

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Utilisation de base

**Scanner une image de conteneur**

```
trivy image nom-image:tag
```

**Scanner le code source et les secrets**

```
trivy fs --scanners vuln,secret,misconfig .
```

**Générer un SBOM au format CycloneDX**

```
trivy image --format cyclonedx --output sbom.json nom-image:tag
```

## Architecture technique et fonctionnement interne

Développé par Aqua Security et la communauté open-source, Trivy offre des mécanismes de sécurité robustes pour DevSecOps :
- Base de données locale Trivy DB: Télécharge automatiquement un cache léger agrégeant les alertes de NVD, GitHub Advisory, Red Hat, Debian et Ubuntu pour des scans hors ligne rapides.
- Analyse statique des couches: Décompose les couches OCI sans exécuter le conteneur ni solliciter le démon Docker, évitant tout risque d'exécution de code malveillant.
- Moteur IaC basé sur Rego: Évalue les modèles d'infrastructure via des règles Open Policy Agent (OPA) pour bloquer les configurations à privilèges root.
- Cartographie complète des dépendances: Analyse les fichiers de verrouillage (package-lock.json, poetry.lock, Cargo.lock) pour repérer les failles transitives.

## Intégration DevSecOps et pipelines CI/CD

Trivy s'intègre comme un portail de qualité (quality gate) pour bloquer la promotion de code non sécurisé vers la production :

**Interrompre la compilation sur les vulnérabilités critiques**

```
trivy image --exit-code 1 --severity CRITICAL,HIGH nom-image:tag
```
- Retour rapide en amont (Shift-left): Les développeurs détectent les failles des bibliothèques open-source directement sur leur machine locale.
- Rapports SARIF automatisés: Exportez vers GitHub Code Scanning ou GitLab Security pour un suivi centralisé des vulnérabilités.
- Surveillance de cluster (Trivy Operator): Scrute en continu les charges de travail Kubernetes pour signaler les failles zero-day.

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je souhaite configurer un workflow GitHub Actions qui analyse mon image Docker et mon code source avec Trivy à chaque push et pull request. Peux-tu me préparer un fichier .github/workflows/trivy.yml qui échoue (exit-code 1) uniquement sur les alertes CRITICAL et HIGH, publie les résultats en SARIF dans l'onglet Security de GitHub et génère un artefact SBOM CycloneDX ?

- **Pour qui:** Ingénieurs DevOps, experts en cybersécurité et développeurs souhaitant automatiser les contrôles de vulnérabilités et la conformité SBOM.
- **Licence:** Apache-2.0 (Licence open-source permissive)
- **Développeur:** Aqua Security et communauté open-source
- **Formats de sortie:** Table, JSON, SARIF, CycloneDX, SPDX, Template

## Foire aux questions
- Trivy peut-il analyser une image sans démon Docker ? Oui. Trivy peut télécharger et inspecter des images directement depuis des registres distants (Docker Hub, GitHub Container Registry) ou lire des archives tar locales.
- Fonctionne-t-il dans des réseaux isolés (air-gapped) ? Oui. La base de données de vulnérabilités peut être pré-téléchargée et importée pour des analyses entièrement hors ligne.
- Qu'est-ce qu'un SBOM et pourquoi Trivy ? Le Software Bill of Materials détaille tous les composants et licences d'une application. Trivy génère des SBOM standardisés pour le code et les conteneurs.
- Quelle est la rapidité d'un scan Trivy ? Comme les analyses s'appuient sur une base de données locale pré-indexée sans appels réseau lors du scan, l'analyse ne prend que quelques secondes.

## Liens
- [GitHub →](https://github.com/aquasecurity/trivy)
- [Read in Turkish →](https://trescout.com/discover/trivy/)

## Termes liés du glossaire
Container CI-CD Vulnerability Scanning Cloud Native

---
Source: TreScout Discover · https://trescout.com/fr/discover/trivy/
