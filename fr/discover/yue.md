# Composition éditable par intelligence artificielle dans la production musicale

YuE est un système de génération musicale doté de capacités telles que la planification symbolique et la génération de reprises en mode zéro-shot. Ce modèle d'IA, qui automatise les processus de composition musicale, vous permet de gérer des compositions complexes grâce à des flux de travail agentiques.

- ★ 9 749
- Python
- GitHub Trending · 2026-09-13

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
Je souhaite créer une chanson en utilisant YuE2. Veuillez préparer un plan de mélodie et d'accords éditable basé sur les paroles et le style musical que je souhaite. Ensuite, utilisez ce plan pour produire un enregistrement complet de la chanson incluant les voix et l'accompagnement instrumental. Si je dispose d'un fichier de notation, permettez-moi de l'utiliser pour effectuer des modifications.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/yue/
