# Qu'est-ce que Speech-to-Speech ?

La technologie Speech-to-Speech (S2S / IA de voix à voix) est une technologie d'apprentissage profond de bout en bout qui analyse les ondes sonores directement de la source à la destination sans les convertir en une couche de texte intermédiaire, générant ainsi un nouveau signal vocal.

## De l'architecture en cascade traditionnelle à l'architecture de bout en bout
Les systèmes traditionnels de traduction vocale et de dialogue se composaient de trois étapes indépendantes appelées « cascade » :

## Infrastructure technique : Tokenisation audio et espace latent continu
Les étapes d'ingénierie fondamentales derrière les systèmes de parole à parole sont les suivantes :

## Domaines d'utilisation et perspectives d'avenir

## Questions fréquentes
**Que signifie Speech-to-Speech et comment fonctionne-t-il ?**
Le Speech-to-Speech (de la parole à la parole) est un modèle d'intelligence artificielle de bout en bout qui élimine la nécessité de convertir la parole en texte, en analysant directement l'onde sonore pour produire une sortie sous forme de voix.

**Quelle est la différence avec la cascade STT-TTS traditionnelle ?**
Les systèmes en cascade convertissent d'abord la voix en texte, puis le texte en voix ; cela entraîne une latence de plusieurs secondes et une perte d'émotion/d'accentuation. Le S2S, quant à lui, fonctionne avec une latence instantanée de 200 à 300 ms et préserve le caractère vocal du locuteur.

**Est-il possible d'interrompre le système S2S pendant qu'il parle ?**
Oui ; grâce au flux audio bidirectionnel complet (Full-Duplex), le modèle peut arrêter instantanément la génération vocale et passer en mode écoute lorsque l'utilisateur intervient.

**Quels sont les risques de sécurité liés à la traduction voix à voix ?**
La technologie de clonage vocal réaliste comporte des risques d'usurpation d'identité et de fraude. Pour cette raison, les systèmes S2S modernes intègrent des filigranes cryptographiques (audio watermarking) inaudibles à l'oreille humaine dans la voix synthétisée.


## Termes liés
- [STT](/fr/dictionary/stt/)
- [Speech-to-Text](/fr/dictionary/speech-to-text/)
- [Voice Cloning](/fr/dictionary/voice-cloning/)
- [Whisper](/fr/dictionary/whisper/)
- [Tokenizer](/fr/dictionary/tokenizer/)
- [Apple Silicon](/fr/dictionary/apple-silicon/)

## Outils liés
- [Speech to Speech](/fr/discover/speech-to-speech/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/speech-to-speech/
