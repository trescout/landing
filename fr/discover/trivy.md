# Scanner de sécurité des conteneurs et du cloud

Trivy est un outil d'analyse de sécurité complet qui détecte les vulnérabilités, les erreurs de configuration et les secrets dans les conteneurs, les clusters Kubernetes, les référentiels de code et les infrastructures cloud en quelques secondes. Il automatise les processus DevSecOps de bout en bout avec la prise en charge de la nomenclature logicielle (SBOM).

- ★ 35 511
- Go
- GitHub Trending · 2026-06-04

## Ce que ça vous apporte
- Analyse de cibles multicouche : inspecte les images de conteneurs (Docker, OCI), les systèmes de fichiers locaux, les dépôts Git distants, les disques de machines virtuelles et les clusters Kubernetes en direct avec un seul outil.
- Charge d'infrastructure supplémentaire nulle : il ne nécessite pas de serveur de base de données externe ni d'agents lourds fonctionnant en permanence ; il fournit des analyses en quelques secondes sous la forme d'un seul binaire exécutable.
- Détection de données sensibles et de clés secrètes : détecte grâce à son moteur heuristique les clés API, mots de passe et certificats privés accidentellement intégrés dans le code source ou les couches d'images.
- Audit d'infrastructure en tant code (IaC) : détecte les erreurs de configuration de sécurité dans les fichiers Terraform, Dockerfile, Kubernetes YAML et CloudFormation avant leur passage en production.
- Conformité des SBOM et des licences open source : génère des nomenclatures de logiciels (SBOM) conformes aux normes CycloneDX et SPDX, garantissant la sécurité de la chaîne d'approvisionnement logicielle en conformité avec les réglementations en vigueur.

## Installation
**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```


## Exécution
**Scanner l'image du conteneur**

```
trivy image imaj-adi:etiket
```


## Architecture technique et principe de fonctionnement
- Base de données Trivy et cache local : télécharge automatiquement un cache de base de données léger qui inclut les bulletins de sécurité de NVD, de la base de données des avis GitHub, de Red Hat, de Debian, d'Ubuntu et d'Alpine. Étant donné que les analyses sont effectuées via ce cache local, l'outil fonctionne à une vitesse fulgurante même dans des environnements soumis à des restrictions réseau.
- Analyse de couches statiques : analyse directement les couches OCI sans exécuter les images de conteneur ni nécessiter de démon Docker. Cette approche ne compromet pas la sécurité du système pendant le processus de numérisation.
- Moteur IaC et politiques Rego : il vérifie les modèles d'infrastructure à l'aide de règles compatibles avec Open Policy Agent (OPA). Les ports ouverts non sécurisés ou les services s'exécutant avec des privilèges root sont signalés instantanément.
- Standardisation des SBOM : analyse les fichiers de verrouillage du gestionnaire de paquets (package-lock.json, poetry.lock, Cargo.lock, etc.) pour générer une carte complète des dépendances de votre application.

## Intégration du DevSecOps et du pipeline CI/CD
- Rétroaction précoce : Avant d'envoyer leur code vers le dépôt distant, les développeurs exécutent Trivy dans leur environnement local pour identifier instantanément les vulnérabilités dans leurs bibliothèques open source.
- Rapports SARIF automatiques : Les sorties SARIF générées sont exportées vers les tableaux de bord de GitHub Code Scanning ou GitLab Security, permettant aux équipes d'effectuer un suivi centralisé des vulnérabilités.
- Audit de cluster en direct (Trivy Operator) : surveille en continu les charges de travail s'exécutant dans l'environnement Kubernetes et signale instantanément les vulnérabilités zero-day nouvellement découvertes.

## Si vous ne codez pas
Je souhaite configurer un workflow de sécurité sur GitHub Actions qui analyse mon image Docker et mes codes sources avec Trivy à chaque demande de code push et pull (PR). Pouvez-vous créer un fichier .github/workflows/trivy.yml complet qui arrête la construction uniquement sur les vulnérabilités CRITIQUES et ÉLEVÉES (code de sortie 1), télécharge les résultats sur le tableau de bord de sécurité GitHub au format SARIF et crée un fichier SBOM au format CycloneDX ?

## Questions fréquemment posées
- Est-ce que Trivy peut scanner des images de conteneurs sans démon Docker ? Oui. Trivy peut télécharger et scanner des images directement à partir de registres d'images distants (Docker Hub, GitHub Container Registry, AWS ECR, etc.) ou d'archives tar locales, sans avoir besoin du client ou du service d'arrière-plan (démon) Docker.
- Fonctionne-t-il dans des environnements isolés (air-gapped) ? Oui. La base de données Trivy (trivy-db) peut être téléchargée au préalable et transférée dans l'environnement réseau fermé. Trivy peut effectuer des analyses via le cache de sa base de données locale sans connexion Internet.
- Qu'est-ce qu'un SBOM et pourquoi Trivy est-il privilégié dans ce domaine ? Un SBOM (Software Bill of Materials) est une liste d'inventaire numérique qui documente toutes les bibliothèques open source, versions et licences contenues dans votre logiciel. Trivy est l'un des rares outils standard capables de générer des SBOM à la fois au niveau des images et au niveau du code source.
- Comment exclure les faux positifs ou les risques acceptés ? En ajoutant un fichier .trivyignore à la racine du projet, vous pouvez lister les codes CVE que vous souhaitez ignorer, ligne par ligne. Cela permet d'éviter des interruptions de build inutiles dans les pipelines CI/CD.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/trivy/
