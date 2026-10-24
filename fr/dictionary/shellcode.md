# Qu'est-ce que Shellcode ?

*Développement · Dernière mise à jour : 24 octobre 2026*

Il s'agit d'un code machine de petite taille qui permet d'obtenir un accès à la ligne de commande ou d'exécuter des commandes personnalisées sur une machine cible en exploitant des vulnérabilités dans les systèmes.

## Définition

Utilisé dans le monde de la cybersécurité et lors des tests d'intrusion, ce fragment de code spécial est injecté directement dans la mémoire du système. Il tire historiquement son nom de son objectif initial : ouvrir un shell de commande sur le système cible. Aujourd'hui, il est conçu non seulement pour ouvrir un shell, mais aussi pour exécuter tout type d'instruction personnalisée souhaitée sur le système.

***Analogie :** Vous pouvez le comparer à une petite carte d'accès qui se glisse secrètement par la porte verrouillée d'un bâtiment pour prendre le contrôle du panneau de commande de la salle de sécurité.*

## Comment ça marche

Les chercheurs en sécurité ou les attaquants identifient des vulnérabilités dans les logiciels, telles que les dépassements de tampon. Ensuite, ils placent le petit code machine qu'ils ont préparé dans la mémoire sous forme de séquence d'octets directement compréhensible par le processeur. Lorsque le processeur exécute ces commandes, un contrôle non autorisé est obtenu sur le système cible.

## Où est-ce utilisé

Vous le rencontrerez dans les analyses de sécurité, les tests d'intrusion et l'examen des logiciels malveillants.

## Souvent confondu avec

Il ne doit pas être confondu avec les scripts shell. Alors que les scripts shell sont des codes de haut niveau basés sur du texte, ce concept est un code binaire qui s'exécute directement au niveau du processeur.

## Questions et réponses

**Le shellcode est-il utilisé uniquement à des fins malveillantes ?**

Les experts en sécurité utilisent également ces codes pour tester la résistance défensive des systèmes et pour corriger les vulnérabilités.

**Pourquoi ces fragments de code sont-ils écrits avec une taille très réduite ?**

Ils sont conçus pour être aussi petits que possible afin de pouvoir s'infiltrer dans des espaces mémoire restreints et fonctionner sans être détectés par les filtres de sécurité.

## Termes liés

- [Exploit](https://trescout.com/fr/dictionary/exploit/)
- [Penetration Testing](https://trescout.com/fr/dictionary/penetration-testing/)
- [Vulnerability Scanning](https://trescout.com/fr/dictionary/vulnerability-scanning/)
- [Backdoor](https://trescout.com/fr/dictionary/backdoor/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/shellcode/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/shellcode/
