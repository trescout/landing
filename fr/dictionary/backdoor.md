# Qu'est-ce que Backdoor ?

*Développement · Dernière mise à jour : 22 octobre 2026*

Il s'agit d'une méthode ou d'un logiciel qui permet un accès à distance secret à un système en contournant les mécanismes d'authentification standard.

## Définition

Une backdoor (porte dérobée) est une entrée secrète qui peut être laissée intentionnellement par les développeurs de logiciels à des fins de débogage ou installée ultérieurement dans le système par des attaquants. Grâce à cette méthode, les contrôles traditionnels de nom d'utilisateur, de mot de passe ou de cryptage sont désactivés. Des acteurs malveillants qui s'immiscent discrètement dans le système peuvent effectuer des opérations avec des privilèges administratifs pendant une longue période en utilisant la porte dérobée.

***Analogie :** C'est comparable au creusement d'un tunnel secret derrière le mur, que personne ne connaît, alors que des gardes montent la garde à l'entrée principale d'un château.*

## Comment ça marche

Les portes dérobées sont établies par un contrôle logique caché dans le code source ou par un port réseau secret laissé ouvert dans le système. Parfois, elles sont introduites dans la chaîne d'approvers par le biais de mises à jour, ou déclenchées par un petit outil de ligne de commande introduit à l'aide d'un exploit. Lorsqu'un attaquant envoie un signal ou une clé spéciale de l'extérieur, la porte dérobée lance directement une session d'accès à distance.

## Où est-ce utilisé

Elles sont fréquemment observées dans les attaques contre la chaîne d'approvisionnement, les cas d'espionnage d'entreprise et les opérations de menaces persistantes avancées (APT). Elles sont également détectées dans les firmwares ou les codes malveillants introduits dans des paquets open source.

## Souvent confondu avec

Elle peut être confondue avec un cheval de Troie (Trojan). Le cheval de Troie est l'enveloppe trompeuse utilisée pour propager le logiciel malveillant, tandis que la backdoor est la fonction qui assure un accès permanent et secret au système.

## Questions et réponses

**Pourquoi les développeurs mettent-ils une porte dérobée dans un système ?**

Dans certains cas, elle est laissée intentionnellement pour faciliter la maintenance ou pour un accès d'urgence, mais cette situation expose le système à un risque de sécurité majeur.

**Comment détecter une backdoor ?**

Elle peut être détectée grâce à la surveillance du trafic réseau anormal, au contrôle de l'intégrité des fichiers et à des analyses de code statique approfondies.

## Termes liés

- [Exploit](https://trescout.com/fr/dictionary/exploit/)
- [Remote Code Execution](https://trescout.com/fr/dictionary/remote-code-execution/)
- [Penetration Testing](https://trescout.com/fr/dictionary/penetration-testing/)
- [Vulnerability Scanning](https://trescout.com/fr/dictionary/vulnerability-scanning/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/backdoor/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/backdoor/
