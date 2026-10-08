# Analyser de longs enregistrements audio avec l'intelligence artificielle

Publié par Microsoft, VibeVoice a été développé comme un framework d'IA vocale open source. Grâce à sa structure basée sur Python, le système permet aux utilisateurs de former leurs propres modèles sonores et de les intégrer dans leurs applications.

- ★ 54 502
- GitHub Trending · 2026-06-07

**Note TreScout :** Le référentiel a changé après sa publication : la partie qui convertit le son en texte reste, la partie qui convertit le texte en son a été supprimée. Sa particularité est qu'il peut traiter de longs enregistrements en même temps. C'est un projet en évolution rapide, jetez un œil à l'état actuel de l'entrepôt avant de l'ajouter à votre entreprise.

## Mises à jour

- **27 septembre 2026:** Étoiles 51,860 → 54,502.
- **2 août 2026:** Étoiles 48,569 → 51,860.

## Ce que ça vous apporte

- Convertit jusqu'à 60 minutes d'enregistrement audio en texte à la fois.
- Il fournit l’identifiant du locuteur, l’horodatage et les détails du contenu de manière structurée.
- Fournit une prise en charge des mots clés définis par l'utilisateur pour les termes et noms personnalisés.

## Installation

**Installer depuis GitHub**

```
git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice
pip install -e .
```

## Exécution

**Démo Gradio**

```
python demo/vibevoice_asr_gradio_demo.py --model_path microsoft/VibeVoice-ASR --share
```

**Transcription du fichier**

```
python demo/vibevoice_asr_inference_from_file.py --model_path microsoft/VibeVoice-ASR --audio_files [ses-dosyasi]
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite analyser l'enregistrement audio de 60 minutes que j'ai à l'aide du modèle VibeVoice. J'ai besoin de récupérer qui sont les locuteurs, quand ils ont parlé et le contenu qu'ils ont dit sous forme de fichier texte structuré. Je souhaite également ajouter des mots-clés personnalisés afin que le modèle reconnaisse plus précisément les termes techniques. Comment puis-je structurer ce processus ?

## Termes liés du glossaire

- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux utilisateurs qui souhaitent convertir rapidement et de manière structurée des enregistrements audio à long terme, des résumés de réunions ou du contenu de podcast en texte.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/microsoft/VibeVoice)
- [Lire en turc →](https://trescout.com/discover/vibevoice/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-07 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/vibevoice/
