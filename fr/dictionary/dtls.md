# Qu'est-ce que DTLS ?

*Développement · Dernière mise à jour : 7 novembre 2026*

> Datagram Transport Layer Security

Il s'agit d'un protocole de communication sécurisé adapté aux situations nécessitant rapidité et continuité dans la transmission des données.

## Définition

Le protocole DTLS est une refonte du protocole TLS (qui fonctionne normalement sur TCP) pour les réseaux tels que l'UDP, qui assurent la continuité mais présentent un risque de perte de paquets. Il minimise la latence sans compromettre la sécurité lorsque le flux de données en temps réel est vital.

***Analogie :** C'est comme envoyer des documents précieux par coursier à moto rapide au lieu de la poste normale ; l'ordre des paquets peut parfois être inversé, mais on gagne en vitesse.*

## Comment ça marche

Il reprend les règles de chiffrement et de sécurité du principe de TLS, mais les assouplit pour faire face aux situations de perte de paquets ou de modification de leur ordre.

## Où est-ce utilisé

Il est utilisé dans les applications d'appels audio et vidéo, les jeux en ligne et les protocoles de diffusion en direct.

## Souvent confondu avec

Il est confondu avec le TLS standard ; la principale différence est que l'un est sécurisé mais lent, tandis que l'autre est adapté à la diffusion en flux instantané.

## Questions et réponses

**Pourquoi n'utilise-t-on pas le TLS standard ?**

Le TLS standard ne tolère pas la perte de paquets et provoque des ralentissements lors des diffusions en direct.

**Sur quel type de réseau fonctionne-t-il ?**

Il fonctionne généralement sur des protocoles réseau basés sur UDP.

## Termes liés

- [TLS](https://trescout.com/fr/dictionary/tls/)
- [Network Stack](https://trescout.com/fr/dictionary/network-stack/)
- [Streaming Applications](https://trescout.com/fr/dictionary/streaming-applications/)

## Outils liés

- [Openssl](https://trescout.com/fr/discover/openssl/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/dtls/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/dtls/
