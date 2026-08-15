# Agents vocaux natifs open source

La bibliothèque parole-parole développée par Hugging Face permet de créer des agents vocaux locaux à l'aide de modèles open source. Cet outil basé sur Python permet aux développeurs de créer des systèmes d'interaction vocale en temps réel qui s'exécutent sur l'appareil.

- ★ 12 310
- Python
- GitHub Trending · 2026-07-29

## Ce que ça vous apporte
- Ligne audio modulaire à faible latence
- Prise en charge de WebSocket compatible avec OpenAI Realtime
- Possibilité de travailler localement sur différents matériels

## Installation
**Configuration de base**

```
pip install speech-to-speech
```

**Installation à partir du code source**

```
git clone https://github.com/huggingface/speech-to-speech.git
cd speech-to-speech
uv sync
```


## Exécution
**Démarrage du serveur**

```
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech
```

**Connexion avec le client**

```
python scripts/listen_and_play_realtime.py --host 127.0.0.1 --port 8765
```


## Si vous ne codez pas
Je souhaite configurer mon propre agent vocal local à l'aide de cet outil. Quelles sont les étapes de base que je dois suivre pour créer un pipeline audio à faible latence à l'aide des composants VAD, STT, LLM et TTS ? Avec quelle commande puis-je mettre le serveur en marche et me connecter à un client compatible OpenAI Realtime ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/speech-to-speech/
