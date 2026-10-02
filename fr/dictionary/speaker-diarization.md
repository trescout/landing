# Qu'est-ce que Speaker Diarization ?

La diarisation des haut-parleurs (séparation ou enregistrement des haut-parleurs) analyse les ondes sonores dans un enregistrement audio à plusieurs participants pour savoir « qui a parlé quand ? Il s'agit d'une technologie d'intelligence artificielle qui répond à la question et étiquette les segments de parole en fonction de l'identité des locuteurs.

## Définition et origine du concept (définition de la diarisation)
La diarisation, dont le mot vient du verbe français « tenir un journal » (diariser), est le processus d'ingénierie audio consistant à diviser le flux audio en segments dépendants du temps et à faire correspondre chaque segment avec une identité de locuteur spécifique (par exemple, Speaker 1, Speaker 2). Quel que soit le contenu du discours, il distingue directement l’identité grâce aux caractéristiques biométriques du timbre et de la fréquence de la voix.

## Comment ça marche ? (Diarisation étape par étape)
1. Détection d'activité vocale (VAD) : La musique, les bruits de fond et les interruptions de respiration dans l'enregistrement sont éliminés et seules les sections contenant des voix humaines sont extraites.

## Où et dans quels domaines est-il utilisé ?
Assistants de réunion intelligents : Outils de résumé par intelligence artificielle (Otter.ai, Meetily) qui identifient qui a pris quelle décision ou quelle tâche lors des réunions Zoom, Google Meet ou Teams.Centres d'appels : Analyse des sentiments et contrôle qualité en séparant les conversations entre le client et l'agent.Transcription de podcasts et d'entretiens : Création automatique de sous-titres professionnels et identification des locuteurs dans les contenus audio et vidéo multi-participants.Droit et informatique légale : Documentation des changements de locuteurs dans les dossiers judiciaires et les interrogatoires de sécurité.

## Souvent confondu avec
La transcription (conversion audio-texte / STT) est souvent confondue avec la diarisation du locuteur. Un moteur Speech-to-Text traditionnel transcrit uniquement « ce qui a été dit » mais ne peut pas distinguer qui l'a dit. La diarisation, en revanche, trouve « qui l'a dit ». Par exemple, alors qu'OpenAI Whisper effectue une transcription pure ; Lorsqu'il est combiné avec des outils tels que pyannote.audio ou WhisperX, le texte complet et les identifiants des locuteurs sont obtenus.

## Questions fréquentes
**Définition de la diarisation (que signifie la diarisation) ?**
Il s'agit d'un processus d'intelligence artificielle qui analyse les ondes sonores dans les enregistrements audio multi-participants pour distinguer qui a parlé et quand, et pour étiqueter les changements de locuteurs avec des horodatages.

**Le système peut-il trouver lui-même les vrais noms des locuteurs ?**
Non, si aucun échantillon vocal n'a été préalablement enregistré, le système distingue les locuteurs sous les noms de Locuteur 1, Locuteur 2 ; les noms doivent être associés par l'utilisateur ou par un système de calendrier intégré.

**Le modèle Whisper peut-il effectuer seul la diarisation ?**
Non, les modèles officiels Whisper ne font que transcrire ; Il est utilisé avec des modèles de diarisation spéciaux tels que pyannote.audio pour la séparation des haut-parleurs.

**Quelle est la situation la plus difficile pour les systèmes de diarisation ?**
Il s'agit d'effectuer la discrimination correcte dans des environnements où plusieurs personnes parlent en même temps (paroles superposées), où les mots sont confus ou où il y a un écho.


## Termes liés
- [Transcription](/fr/dictionary/transcription/)
- [Speech-to-Text](/fr/dictionary/speech-to-text/)
- [NLP](/fr/dictionary/nlp/)

## Outils liés
- [Meetily](/fr/discover/meetily/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/speaker-diarization/
