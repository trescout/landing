# Transformez votre historique de localisation en vidéo animée

Google Timeline Visualizer visualise une année de vos voyages avec vos données d'historique de localisation Google.

- ★ 3 030
- Kotlin
- GitHub Trending · 2026-08-20

## Mises à jour

- **5 octobre 2026:** Étoiles 2,990 → 3,030, dernière version v3.1.0 (5 octobre 2026).
- **13 septembre 2026:** Étoiles 2,980 → 2,990, dernière version v3.0.18 (12 septembre 2026).
- **9 septembre 2026:** Étoiles 2,972 → 2,980, dernière version v3.0.17 (9 septembre 2026).
- **7 septembre 2026:** Étoiles 2,969 → 2,972, dernière version v3.0.16 (6 septembre 2026).

## Ce que ça vous apporte

- Convertit les données de l'historique Google Maps en vidéo MP4
- Anime les itinéraires de voyage sur la carte
- Protège la confidentialité en traitant les données personnelles sur l'appareil

## Installation

**Installez et exécutez les dépendances nécessaires**

```
python -m pip install -r requirements.txt
python visualizer.py --input Timeline.json --year 2025 --camera-movement steady \
  --long-trip-compression balanced --output my_trip_2025.mp4
```

**Configurer les outils de développement**

```
./gradlew test lint assembleGithubDebug assemblePlayDebug
python -m pip install -r requirements-dev.txt
python -m pytest
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite créer une vidéo montrant mes voyages en utilisant le fichier Timeline.json dont je dispose. Après avoir installé les dépendances nécessaires dans l'environnement Python, quelle commande dois-je utiliser pour convertir mes données 2025 en un fichier nommé « my_trip_2025.mp4 » avec un mouvement de caméra « stable » et des paramètres de compression « équilibrés » ?

## Termes liés du glossaire

- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient à tous ceux qui souhaitent visualiser l'historique de localisation sur Google Maps et enregistrer des souvenirs de voyage au format vidéo.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/mahlernim/google-timeline-visualizer)
- [Lire en turc →](https://trescout.com/discover/google-timeline-visualizer/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-20 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/google-timeline-visualizer/
