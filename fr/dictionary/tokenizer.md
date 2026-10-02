# Qu'est-ce que Tokenizer ?

Le Tokenizer (tokeniseur ou segmentateur) est le composant fondamental de traitement de données qui convertit les textes en langage naturel en jetons numériques (token ID) que les grands modèles de langage (LLM) et les réseaux de neurones peuvent traiter mathématiquement.

## 1. Définition et problème fondamental : Pourquoi pas directement des mots ?
Les grands modèles de langage (GPT-4, Claude, Llama, etc.) ne lisent pas les textes lettre par lettre ou mot par mot comme les humains. Les réseaux de neurones ne peuvent traiter que des matrices, des tenseurs et des nombres. C'est pourquoi le texte doit d'abord être converti en nombres.

## 2. Algorithmes de tokenizer et leurs logiques mathématiques
Les principaux algorithmes de tokenisation au cœur des modèles de langage modernes sont les suivants :

## 3. La « Taxe de Tokenisation » en turc (The Tokenizer Tax)
Plus de 85 % des données d'entraînement des grands modèles de langage sont en anglais. Cette situation conduit à ce que le vocabulaire du tokenizer soit principalement rempli de racines et de mots anglais.

## 4. Sécurité et cas limites : Glitch Tokens
Les jetons spéciaux qui figurent dans le vocabulaire du tokenizer mais qui apparaissent rarement ou dans des contextes dénués de sens au sein du corpus de texte lors du pré-entraînement du modèle sont appelés "Glitch Tokens".

## Questions fréquentes
**Que signifie Tokenizer, quel est son équivalent en turc ?**
En turc, il est appelé « jetonlaştırıcı » ou « simgeleştirici ». C'est un logiciel qui divise les textes en langage naturel en les plus petits index numériques (tokens) que le modèle d'intelligence artificielle peut comprendre.

**À combien de mots ou de lettres correspond 1 token ?**
Dans les textes en anglais, 1 token équivaut en moyenne à 4 caractères ou 0,75 mot (100 mots correspondent à environ 130 tokens). Dans les langues agglutinantes comme le turc, un mot peut représenter en moyenne 2 à 3 tokens en raison de la fragmentation des suffixes.

**Comment fonctionne le BPE (Byte Pair Encoding) ?**
C'est un algorithme statistique qui construit un dictionnaire de sous-mots de taille fixe en commençant par les caractères les plus basiques et en combinant étape par étape les paires de caractères qui apparaissent le plus fréquemment côte à côte dans l'ensemble d'entraînement.

**Les modèles sans tokenizer (tokenizer-free) sont-ils possibles ?**
Oui ; les architectures de réseaux neuronaux de nouvelle génération développées récemment, telles que MambaByte et MegaByte, visent à éliminer l'inégalité linguistique en supprimant complètement la couche de tokenizer et en traitant directement les octets bruts (bytes).


## Termes liés
- [Token](/fr/dictionary/token/)
- [NLP](/fr/dictionary/nlp/)
- [Tokenizer-free](/fr/dictionary/tokenizer-free/)
- [Prompt Engineering](/fr/dictionary/prompt-engineering/)
- [Context](/fr/dictionary/context/)

## Outils liés
- [Minimind](/fr/discover/minimind/)
- [AI Engineering from Scratch](/fr/discover/ai-engineering-from-scratch/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/tokenizer/
