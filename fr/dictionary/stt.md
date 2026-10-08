# Qu'est-ce que STT ?

*Glossaire · AI · Dernière mise à jour : 19 septembre 2026*

> Speech-to-Text

STT (Speech-to-Text) est une technologie d'intelligence artificielle et de traitement du signal qui analyse la parole humaine sous forme d'ondes sonores analogiques ou numériques et la convertit en texte écrit avec une grande précision.

## Origine conceptuelle, étymologie et évolution historique

STT est constitué des initiales de l’expression anglaise Speech-to-Text. En turc, il est utilisé comme « Speech to Text », « Reconnaissance vocale » ou « Transcription vocale ».

L’histoire de la recherche sur la reconnaissance vocale constitue l’un des problèmes les plus complexes de l’informatique :

- 1952 (Système Audrey) : Le premier système développé aux Laboratoires Bell ne pouvait reconnaître que les chiffres de 0 à 9 prononcés par un seul locuteur.
- Années 1970-1990 (Modèles statistiques et HMM) : Les ondes sonores ont commencé à être analysées en les divisant en phonèmes (les plus petites unités sonores) avec des modèles de Markov cachés (HMM) et des modèles de langage n-gramme. Cependant, le taux de précision était assez faible dans des environnements bruyants et avec des accents différents.
- Années 2010 (Deep Learning & Hybrid Models) : Les réseaux de neurones profonds (DNN, CNN, RNN) sont associés au HMM, donnant naissance aux assistants vocaux (Siri, Google Assistant) sur smartphones.
- Années 2020 (End-to-End Transformer Revolution) : des architectures de bout en bout (OpenAI Whisper, Google Chirp, Conformer) qui convertissent l'onde sonore brute directement en spectrogramme puis en texte sont arrivées sur la scène. Formés sur des centaines de milliers d’heures de données multilingues, ces modèles peuvent retranscrire avec précision les chuchotements, les accents prononcés et les environnements bruyants.

***Analogie :** STT est la personne qui s'assoit à côté de vous pendant que vous parlez dans une salle de conférence, enregistrant avec précision chacun de vos mots, pauses et intonations avec une sténographie ultra-rapide ; De plus, il est comme un parfait dactylo en chef qui reconnaît instantanément la langue que vous parlez et applique automatiquement les règles d’orthographe.*

## Modélisation acoustique et architecture d'étude

Un moteur STT moderne passe par les couches suivantes lors de la conversion des ondes sonores analogiques en texte numérique :

1. Prétraitement audio et transformation du spectrogramme : Le signal audio brut (au format PCM) est analysé avec une transformée de Fourier à court terme (STFT · Transformée de Fourier à court terme). Il est converti en spectrogrammes Log-Mel adaptés à la perception fréquentielle de l'oreille humaine. Ce processus convertit le son en une carte de fréquence visuelle.
2. Encodeur acoustique : le spectrogramme est transmis au réseau neuronal profond basé sur un transformateur. En filtrant le bruit dans les ondes sonores, le modèle extrait à quel phonème ou représentation acoustique correspond chaque tranche sonore de 20 à 30 millisecondes (dans l'espace latent).
3. Encodeur de langage et prédiction de contexte (décodeur autorégressif) : les signaux du modèle acoustique sont combinés avec le modèle de langage entraîné. Dans les langues riches en prononciation comme le turc, les homophones (homophones ; par exemple, le nombre « cent » et le verbe « cent ») sont détectés correctement en fonction du contexte de la phrase.
4. Ponctuation et formatage : des majuscules, des virgules, des points, des points d'interrogation sont ajoutés au texte brut et les expressions numériques ("quinze" → "15") sont converties au format texte.

**Mesure des performances (WER · Taux d'erreur de mot) :** La précision d'un modèle STT est mesurée par la métrique Word Error Rate (WER). Sa formule est WER = (S + D + I) / N (S : substitution, D : suppression, I : insertion, N : total de mots). Dans les modèles modernes, le taux de WER en anglais est tombé à 3 à 5 % et dans les langues agglutinantes comme le turc, il a diminué à 7 à 10 %.

## Domaines d'utilisation et écosystème open source

- Assistants de réunion et de prise de notes : Transcription et synthèse en temps réel des conversations Zoom, Google Meet ou Teams (Otter.ai, Fireflies).
- Sous-titres et traduction : génération automatique de sous-titres pour le contenu vidéo et podcast au format horodatage .srt et .vtt.
- Santé et droit : Les médecins dictent des notes d’examen clinique ou des procès-verbaux d’audience sans utiliser leurs mains.
- Leader de l'Open Source (Whisper & Whisper.cpp) : le modèle open source Whisper d'OpenAI et la bibliothèque Whisper.cpp de Georgi Gerganov, entièrement optimisées en C/C++, offrent la possibilité d'exécuter STT en toute confidentialité sur du matériel natif (Mac série M, Raspberry Pi, GPU grand public) sans dépendre du serveur.

## Questions fréquentes

**Que signifie STT et que signifie-t-il ?**

STT est l'abréviation de « Speech-to-Text ». Il s'agit d'une technologie d'intelligence artificielle qui analyse les signaux sonores, décode les mots et les convertit au format texte.

**Quelle est la différence entre STT et la reconnaissance vocale ?**

La reconnaissance vocale (Speaker Identification) se concentre sur la détection de l'identité de l'orateur (identité biométrique). STT, quant à lui, retranscrit le contenu des paroles prononcées quelle que soit l’identité du locuteur.

**Les modèles STT comprennent-ils correctement les sons turcs ?**

Les modèles de pointe basés sur Whisper et Conformer sont formés sur de vastes ensembles de données vocales turques ; Il peut effectuer la transcription et la ponctuation avec une grande précision dans un turc phonétiquement riche.

**Est-il possible d'exécuter un STT local ?**

Oui; Grâce à des moteurs optimisés tels que Whisper.cpp ou Faster-Whisper, vous pouvez gérer vos données vocales hors ligne et en toute confidentialité sur votre propre ordinateur, sans les envoyer à un serveur cloud.

## Termes liés

- [Speech-to-Text](https://trescout.com/fr/dictionary/speech-to-text/)
- [Speech-to-Speech](https://trescout.com/fr/dictionary/speech-to-speech/)
- [Voice Cloning](https://trescout.com/fr/dictionary/voice-cloning/)
- [Whisper](https://trescout.com/fr/dictionary/whisper/)
- [Tokenizer](https://trescout.com/fr/dictionary/tokenizer/)
- [Apple Silicon](https://trescout.com/fr/dictionary/apple-silicon/)

## Outils liés

- [Agents](https://trescout.com/fr/discover/agents/)
- [Speech to Speech](https://trescout.com/fr/discover/speech-to-speech/)
- [Transcribe.cpp](https://trescout.com/fr/discover/transcribe-cpp/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/stt/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/stt/
