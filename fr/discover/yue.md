# Composition éditable par intelligence artificielle dans la production musicale

YuE est un système de génération musicale doté de capacités telles que la planification symbolique et la génération de reprises en mode zéro-shot. Ce modèle d'IA, qui automatise les processus de composition musicale, vous permet de gérer des compositions complexes grâce à des flux de travail agentiques.

- ★ 10 749
- Python
- GitHub Trending · 2026-09-13

## Mises à jour

- **3 octobre 2026:** Étoiles 9,749 → 10,749, dernière version yue2-v0.1.6 (9 septembre 2026).
- **19 septembre 2026:** Étoiles 8,744 → 9,749, dernière version yue2-v0.1.6 (9 septembre 2026).
- **15 septembre 2026:** Étoiles 7,463 → 8,744, dernière version yue2-v0.1.6 (9 septembre 2026).
- **13 septembre 2026:** Étoiles 7,459 → 7,463, dernière version yue2-v0.1.6 (9 septembre 2026).

## Ce que ça vous apporte

- Génération de mélodies et de plans d'accords à partir de paroles et d'entrées de style
- Possibilité d'éditer les partitions musicales avant de les convertir en fichiers audio
- Réinterprétation et réarrangement de chansons existantes dans différents styles

## Installation

**Téléchargement et installation du projet**

```
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
python examples/generate.py --output outputs/first-song
```

## Exécution

**Création de chansons avec des partitions éditées**

```
python examples/generate.py --request examples/song.json \
  --abc-file edited.abc --cot full --output outputs/edited
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite créer une chanson en utilisant YuE2. Veuillez préparer un plan de mélodie et d'accords éditable basé sur les paroles et le style musical que je souhaite. Ensuite, utilisez ce plan pour produire un enregistrement complet de la chanson incluant les voix et l'accompagnement instrumental. Si je dispose d'un fichier de notation, permettez-moi de l'utiliser pour effectuer des modifications.

## Termes liés du glossaire

- [Zero-shot](https://trescout.com/fr/dictionary/zero-shot/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Convient aux musiciens et aux créateurs de contenu qui souhaitent planifier leurs compositions musicales à l'aide de l'intelligence artificielle, apporter des modifications aux partitions et produire des chansons originales.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/multimodal-art-projection/YuE)
- [Lire en turc →](https://trescout.com/discover/yue/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-13 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/yue/
