# Analyser de longs enregistrements audio avec l'intelligence artificielle

Publié par Microsoft, VibeVoice a été développé comme un framework d'IA vocale open source. Grâce à sa structure basée sur Python, le système permet aux utilisateurs de former leurs propres modèles sonores et de les intégrer dans leurs applications.

- ★ 51 860
- GitHub Trending · 2026-06-07

## Mise à jour
- 2 août 2026 : Étoile 48 569 → 51 860.

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
Je souhaite analyser l'enregistrement audio de 60 minutes que j'ai à l'aide du modèle VibeVoice. J'ai besoin de récupérer qui sont les locuteurs, quand ils ont parlé et le contenu qu'ils ont dit sous forme de fichier texte structuré. Je souhaite également ajouter des mots-clés personnalisés afin que le modèle reconnaisse plus précisément les termes techniques. Comment puis-je structurer ce processus ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/vibevoice/
