# Agents vocaux natifs open source

La bibliothèque parole-parole développée par Hugging Face permet de créer des agents vocaux locaux à l'aide de modèles open source. Cet outil basé sur Python permet aux développeurs de créer des systèmes d'interaction vocale en temps réel qui s'exécutent sur l'appareil.

- ★ 13 072
- Python
- GitHub Trending · 2026-07-29

## Mises à jour

- **7 septembre 2026:** Étoiles 12,310 → 13,072, dernière version v1.0.0 (6 septembre 2026).
- **12 août 2026:** Étoiles 11,283 → 12,310, dernière version v0.2.12 (5 août 2026).
- **6 août 2026:** Étoiles 10,774 → 11,283, dernière version v0.2.12 (5 août 2026).
- **4 août 2026:** Étoiles 10,402 → 10,774, dernière version v0.2.11 (3 août 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite configurer mon propre agent vocal local à l'aide de cet outil. Quelles sont les étapes de base que je dois suivre pour créer un pipeline audio à faible latence à l'aide des composants VAD, STT, LLM et TTS ? Avec quelle commande puis-je mettre le serveur en marche et me connecter à un client compatible OpenAI Realtime ?

## Termes liés du glossaire

- [Voice Agents](https://trescout.com/fr/dictionary/voice-agents/)
- [Speech-to-Speech](https://trescout.com/fr/dictionary/speech-to-speech/)
- [STT](https://trescout.com/fr/dictionary/stt/)
- [LLM](https://trescout.com/fr/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent développer des systèmes d'interaction vocale natifs et personnalisables sur leur propre matériel.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/huggingface/speech-to-speech)
- [Lire en turc →](https://trescout.com/discover/speech-to-speech/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-29 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/speech-to-speech/
