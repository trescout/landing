# L'intelligence artificielle open source dans le domaine de la santé

OpenMed est une plateforme qui rassemble des modèles d'intelligence artificielle open source et des ensembles de données utilisés dans le domaine de la santé. Développée pour des applications à vocation médicale, cette bibliothèque basée sur Python vise à standardiser les processus de traitement des données de santé.

- ★ 4 793
- Python
- GitHub Trending · 2026-06-10

## Ce que ça vous apporte
- Extrait des informations médicales structurées à partir de textes cliniques.
- Anonymise les données de santé personnelles sur l’appareil.
- Il exécute plus de 1 000 modèles d’IA médicale hors ligne.

## Installation
**Configuration de base**

```
pip install "openmed[hf]"
```

**Prise en charge du silicium Apple (MLX)**

```
pip install "openmed[mlx]"
```


## Exécution
**Analyse simple avec Python**

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```


## Si vous ne codez pas
Je souhaite analyser un texte médical à l'aide de la bibliothèque OpenMed. J'ai Python installé sur mon appareil. Tout d'abord, j'ai terminé l'installation avec la commande pip install "openmed[hf]". Maintenant, quelles fonctions dois-je appeler dans mon code Python pour analyser mes notes cliniques et y détecter des termes médicaux ou des données personnelles (PII) ? Veuillez me créer un exemple simple de bloc de code sur la sélection du modèle et l'impression des sorties.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openmed/
