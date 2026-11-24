# Outil d'intelligence artificielle qui rédige automatiquement des articles académiques

Développé par Google Research, PaperOrchestra est un cadre multi-agents qui transforme des idées brutes et des journaux d'expériences en brouillons LaTeX au format académique. Le logiciel prend en charge la rédaction d'articles de recherche en automatisant les processus de revue de littérature et de génération de visuels.

- ★ 6 261
- Python
- GitHub Trending · 2026-11-17

## Mises à jour

- **24 novembre 2026:** Étoiles 5,197 → 6,261.
- **20 novembre 2026:** Étoiles 4,162 → 5,197.
- **18 novembre 2026:** Étoiles 1,732 → 4,162.

## Ce que ça vous apporte

- Transforme des idées brutes en format académique
- Automatise la revue de littérature
- Génère les visuels et graphiques nécessaires

## Installation

**Configuration de l'environnement requis**

```
conda create -n paper_orchestra python=3.11
    conda activate paper_orchestra
    pip install -r requirements.txt
```

## Exécution

**Exécution avec le script**

```
./paper_writing_cli.sh
```

**Exécution via la ligne de commande**

```
python paper_writing_cli.py \
  --raw_materials_dir /path_to_your_raw_materials/ \
  --latex_template_dir /path_to_your_latex_template/ \
  --output_dir /path_to_your_output_folder/ \
  --use_plotting true
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite transformer mes idées de recherche et mes journaux d'expériences en brouillon d'article académique. Pour cela, installe d'abord les dépendances nécessaires en exécutant la commande conda create -n paper_orchestra python=3.11
conda activate paper_orchestra
pip install -r requirements.txt. Ensuite, utilise la commande ./paper_writing_cli.sh pour lancer le processus de rédaction de l'article.

Dépôt : https://github.com/google-research/paper-orchestra. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Multi-Agent Framework](https://trescout.com/fr/dictionary/multi-agent-framework/)
- [Multi-agent](https://trescout.com/fr/dictionary/multi-agent/)
- [Framework](https://trescout.com/fr/dictionary/framework/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il est destiné aux chercheurs qui souhaitent rédiger des ébauches académiques en automatisant le processus de rédaction d'articles de recherche.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/google-research/paper-orchestra)
- [Lire en turc →](https://trescout.com/discover/paper-orchestra/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-17 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/paper-orchestra/
