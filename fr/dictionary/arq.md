# Qu'est-ce que ARQ ?

*Glossaire · Dev · Dernière mise à jour : 12 juin 2026*

> Automatic Repeat Request

Il s'agit d'un mécanisme de contrôle des erreurs qui garantit que les informations sont automatiquement renvoyées lorsqu'une erreur se produit lors de la transmission des données.

## Définition

Lors de l'envoi de données sur Internet, des paquets peuvent parfois être perdus ou corrompus. ARQ vérifie si le destinataire a reçu les données et s'il détecte une erreur, il indique à l'expéditeur "Je n'ai pas reçu ceci, envoyez à nouveau". De cette façon, on garantit que les données sont reçues complètement et sans erreurs.

***Analogie :** En parlant au téléphone, l'autre partie dit : « Je n'ai pas compris, pouvez-vous le répéter ? C'est comme dire et répéter cette phrase.*

## Comment ça marche

L'expéditeur envoie le paquet de données et attend un accusé de réception. Si la confirmation n'est pas reçue dans un certain délai, le colis est considéré comme endommagé ou perdu et est réexpédié.

## Où est-ce utilisé

Il est utilisé dans les protocoles de base et les protocoles réseau d'Internet, tels que le protocole TCP.

## Questions fréquentes

**Pourquoi est-ce si important ?**

Les connexions Internet ne sont pas toujours parfaites ; ARQ garantit la fiabilité des données.

**Est-ce que cela entraînera un retard ?**

Oui, renvoyer des colis défectueux peut ralentir un peu le processus.

## Termes liés

- [API](https://trescout.com/fr/dictionary/api/)
- [DNS Tunneling](https://trescout.com/fr/dictionary/dns-tunneling/)
- [Computer Science](https://trescout.com/fr/dictionary/computer-science/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/arq/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/arq/
