# Agents vocaux natifs open source

La bibliothèque parole-parole développée par Hugging Face permet de créer des agents vocaux locaux à l'aide de modèles open source. Cet outil basé sur Python permet aux développeurs de créer des systèmes d'interaction vocale en temps réel qui s'exécutent sur l'appareil.

- ★ 11 283
- Python
- GitHub Trending · 2026-07-29

## Mise à jour
- 6 août 2026 : Star 10 774 → 11 283, dernière version v0.2.12 (5 août 2026).
- 4 août 2026 : Star 10 402 → 10 774, dernière version v0.2.11 (3 août 2026).
- 2 août 2026 : Étoile 7 443 → 10 402, dernière version v0.2.10 (11 juin 2026).

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
