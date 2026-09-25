# Qu'est-ce que l'On-device STT ?

> Reconnaissance Vocale Embarquée sur l'Appareil

**Catégorie:** AI  
**Dernière mise à jour:** 2026-09-22

L'on-device STT (Speech-to-Text embarqué) désigne la technologie de reconnaissance vocale qui retranscrit la parole en texte directement sur l'appareil de l'utilisateur, sans transmettre d'enregistrement audio vers des serveurs distants.

## Définition et étymologie
Indispensable pour préserver la confidentialité et garantir un fonctionnement instantané, le STT embarqué exécute des modèles neuronaux acoustiques directement sur les puces du terminal (NPU, GPU). Les flux vocaux ne quittent jamais la machine hôte.

## Usage quotidien et contexte pratique
- **Smartphones et tablettes :** Dictée vocale instantanée fonctionnant en mode avion sans connexion.
- **Transcriptions sensibles :** Rédaction de comptes rendus médicaux et d'audiences juridiques confidentielles.
- **Appareils domotiques :** Ordres vocaux exécutés localement sans écoute clandestine externe.

## Profondeur technique et architecture
Architecture technique :- **Modèles acoustiques quantifiés :** Variantes allégées (Whisper.cpp, Vosk) optimisées en précision 4 ou 8 bits.
- **Accélération matérielle neuronale :** Utilisation des moteurs neuronaux dédiés (Apple Neural Engine, NPU Snapdragon) pour préserver la batterie.
- **Détection d'activité vocale (VAD) :** Filtrage initial (Silero VAD) activant le modèle uniquement lors des prises de parole réelles.

## Souvent confondu avec
Souvent confondu avec les API vocales cloud. Le cloud envoie la voix vers des centres de données distants ; le STT embarqué effectue l'intégralité de l'inférence sur le processeur local.

## Perspectives interdisciplinaires
- **Interprétariat :** Avoir un interprète personnel à ses côtés dans la pièce plutôt que faire appel à une centrale téléphonique à distance.
- **Sténographie :** Un greffier présent dans la salle d'audience vs l'envoi d'enregistrements audio à un prestataire externe.
- **Photographie :** Développer ses négatifs dans sa propre chambre noire vs expédier ses pellicules à l'autre bout du pays.

## Par analogie
C'est comme avoir un traducteur personnel assis à vos côtés : vous parlez et les mots sont retranscrits sur le champ, sans intermédiaire extérieur.

## Questions fréquentes

**Le STT embarqué est-il aussi précis que les services cloud ?**  
Oui, les modèles récents comme Whisper-small ou distil-whisper atteignent des scores de précision très proches des API cloud.

**Fonctionne-t-il sans connexion Internet ?**  
Oui, dès lors que les poids du modèle sont téléchargés sur l'appareil, aucune connexion n'est requise.

**Quel espace de stockage occupe un tel modèle ?**  
Selon le niveau de compression, la taille varie généralement entre 50 Mo et 400 Mo.

**Quels frameworks open source permettent de l'intégrer ?**  
Whisper.cpp, Sherpa-ONNX, Vosk et WhisperX.

## Termes liés
- [Speech-to-Text](/fr/dictionary/speech-to-text/)
- [SLM](/fr/dictionary/slm/)
- [Confidentialité Numérique](/fr/dictionary/digital-privacy/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/on-device-stt/
