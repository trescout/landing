# Qu'est-ce que Tokenizer ?

*Glossaire · AI · Dernière mise à jour : 19 septembre 2026*

Le Tokenizer (tokeniseur ou segmentateur) est le composant fondamental de traitement de données qui convertit les textes en langage naturel en jetons numériques (token ID) que les grands modèles de langage (LLM) et les réseaux de neurones peuvent traiter mathématiquement.

## 1. Définition et problème fondamental : Pourquoi pas directement des mots ?

Les grands modèles de langage (GPT-4, Claude, Llama, etc.) ne lisent pas les textes lettre par lettre ou mot par mot comme les humains. Les réseaux de neurones ne peuvent traiter que des matrices, des tenseurs et des nombres. C'est pourquoi le texte doit d'abord être converti en nombres.

Historiquement, trois approches différentes ont été essayées dans le traitement du langage naturel (NLP) :

1. Traitement par caractères : Le texte est divisé en lettres individuelles (k, i, t, a, p). La taille du vocabulaire est très réduite (quelques centaines de caractères), mais les phrases deviennent très longues. Comme la complexité de calcul du mécanisme d'attention (Self-Attention) dans l'architecture Transformer augmente avec le carré de la longueur de la séquence (O(N²)), la mémoire du modèle sature rapidement.
2. Traitement basé sur les mots : chaque mot est considéré comme une unité distincte. Cependant, dans ce cas, le nombre d'entrées dans le dictionnaire explose à plusieurs millions pour chaque suffixe flexionnel, faute de frappe ou nouveau mot ; chaque mot absent du dictionnaire est alors étiqueté comme « inconnu » (\<unk> - Out of Vocabulary) et le modèle perd tout son sens.
3. Solution de sous-mots (Subword) : C'est la norme moderne actuelle. Les mots fréquemment utilisés sont traités comme une seule unité ("livre"), tandis que les mots rares ou dérivés sont divisés en racines et suffixes significatifs ("livre" + "aire"). Ainsi, un nombre infini de mots peut être représenté avec une taille de vocabulaire fixe comprise entre 32 000 et 128 000 unités.

***Analogie :** Un tokenizer est une machine de tri qui, au lieu de diviser individuellement en lettres des centaines de milliers de livres différents entrant dans une bibliothèque, imprime des codes-barres spéciaux pour les syllabes et les racines de mots les plus fréquemment utilisées. Le modèle ne voit pas directement les lettres en lisant le texte, il enregistre dans sa mémoire les numéros de codes-barres qu'il lit pour chaque segment.*

## 2. Algorithmes de tokenizer et leurs logiques mathématiques

Les principaux algorithmes de tokenisation au cœur des modèles de langage modernes sont les suivants :

- Byte Pair Encoding (BPE) : Initialement un algorithme de compression de données, le BPE est aujourd'hui à la base des modèles de la série GPT et Llama. Il commence avec tous les caractères de base du texte et fusionne de manière itérative les paires de caractères les plus fréquentes dans le corpus pour les ajouter au dictionnaire.
- WordPiece : Popularisée par Google dans le modèle BERT, cette méthode est basée sur la probabilité plutôt que sur la fréquence. Lors de la fusion des paires, elle sélectionne les sous-unités de mots qui augmentent le plus le score de vraisemblance du modèle de langage sur les données d'entraînement.
- SentencePiece et Byte-Fallback : traite les espaces comme un sous-caractère spécial et considère le texte comme un flux d'octets bruts. Lorsqu'un caractère Unicode rare absent du dictionnaire est rencontré, il revient directement à l'octet UTF-8 (Byte-Fallback), réduisant ainsi l'erreur \<unk> à zéro.

## 3. La « Taxe de Tokenisation » en turc (The Tokenizer Tax)

Plus de 85 % des données d'entraînement des grands modèles de langage sont en anglais. Cette situation conduit à ce que le vocabulaire du tokenizer soit principalement rempli de racines et de mots anglais.

Dans les langues à morphologie riche et agglutinantes comme le turc, cette situation crée un coût important et une inégalité de contexte :

- La phrase « Artificial intelligence is transforming software engineering. » équivaut à environ 7 jetons.
- La phrase « Yapay zekâ yazılım mühendisliğini dönüştürüyor. » peut consommer entre 14 et 16 jetons en raison de la segmentation des suffixes.

C'est pourquoi les utilisateurs turcophones peuvent insérer moins de documents dans la même fenêtre de contexte et paient deux fois plus cher pour les services API. Avec Llama 3 et GPT-4o, le fait que la taille du dictionnaire dépasse 128k a considérablement amélioré l'efficacité des tokens en turc.

## 4. Sécurité et cas limites : Glitch Tokens

Les jetons spéciaux qui figurent dans le vocabulaire du tokenizer mais qui apparaissent rarement ou dans des contextes dénués de sens au sein du corpus de texte lors du pré-entraînement du modèle sont appelés "Glitch Tokens".

Par exemple, lorsque l'on interroge le modèle sur des jetons comme SolidGoldMagikarp, dérivés de noms d'utilisateur sur des forums Reddit ou de codes sur des sites de commerce électronique, l'intelligence artificielle commence à halluciner, peut aligner des insultes dénuées de sens ou se bloquer, car elle ne parvient pas à positionner correctement le vecteur de ce jeton dans l'espace d'embedding.

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

- [Token](https://trescout.com/fr/dictionary/token/)
- [NLP](https://trescout.com/fr/dictionary/nlp/)
- [Tokenizer-free](https://trescout.com/fr/dictionary/tokenizer-free/)
- [Prompt Engineering](https://trescout.com/fr/dictionary/prompt-engineering/)
- [Context](https://trescout.com/fr/dictionary/context/)

## Outils liés

- [AI Engineering from Scratch](https://trescout.com/fr/discover/ai-engineering-from-scratch/)
- [Minimind](https://trescout.com/fr/discover/minimind/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/tokenizer/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/tokenizer/
