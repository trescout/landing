# Produisez des sons naturels et doux

MOSS-TTS (MOSI.AI et OpenMOSS) ; Il s'agit d'une famille de modèles open source qui offre une reproduction vocale et sonore haute fidélité. Il propose des solutions pour des scénarios tels que la synthèse vocale de textes longs, la prise en charge de plusieurs locuteurs et la diffusion en continu en temps réel.

- ★ 3 939
- Python
- Apache-2.0
- GitHub Trending · 29 May 2026

## Que propose-t-il ?
- Il fournit une synthèse vocale et vocale haute fidélité.
- Il offre un support multi-enceintes.
- Prend en charge le streaming audio en temps réel.
- Il est basé sur la famille de modèles open source.

## Comment installer, comment utiliser ?
**Créer un environnement conda**

```
conda create -n moss-tts python=3.12 -y
conda activate moss-tts
```

**Cloner et installer le référentiel**

```
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime]"
```

**Exécuter la démo de Gradio**

```
python clis/moss_tts_app.py
```


## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/moss-tts/
