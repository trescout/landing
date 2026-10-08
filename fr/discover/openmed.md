# L'intelligence artificielle open source dans le domaine de la santé

OpenMed est une plateforme qui rassemble des modèles d'intelligence artificielle open source et des ensembles de données utilisés dans le domaine de la santé. Développée pour des applications à vocation médicale, cette bibliothèque basée sur Python vise à standardiser les processus de traitement des données de santé.

- ★ 5 329
- Python
- GitHub Trending · 2026-06-10

## Mises à jour

- **16 septembre 2026:** Étoiles 5,217 → 5,329, dernière version v2.5.0 (15 septembre 2026).
- **5 septembre 2026:** Étoiles 5,076 → 5,217, dernière version v2.3.0 (4 septembre 2026).
- **21 août 2026:** Étoiles 5,015 → 5,076, dernière version v2.2.0 (21 août 2026).
- **15 août 2026:** Étoiles 4,793 → 5,015, dernière version v2.1.0 (12 août 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite analyser un texte médical à l'aide de la bibliothèque OpenMed. J'ai Python installé sur mon appareil. Tout d'abord, j'ai terminé l'installation avec la commande pip install "openmed[hf]". Maintenant, quelles fonctions dois-je appeler dans mon code Python pour analyser mes notes cliniques et y détecter des termes médicaux ou des données personnelles (PII) ? Veuillez me créer un exemple simple de bloc de code sur la sélection du modèle et l'impression des sorties.

## Termes liés du glossaire

- [Apple Silicon](https://trescout.com/fr/dictionary/apple-silicon/)
- [Open Source](https://trescout.com/fr/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux professionnels de la santé et aux développeurs de logiciels qui souhaitent effectuer des analyses axées sur la confidentialité sur leur propre matériel sans envoyer leurs données médicales aux services cloud.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/maziyarpanahi/openmed)
- [Lire en turc →](https://trescout.com/discover/openmed/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-10 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openmed/
