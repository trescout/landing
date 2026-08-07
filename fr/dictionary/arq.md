# Qu'est-ce que ARQ ?

> Automatic Repeat Request

Il s'agit d'un mécanisme de contrôle des erreurs qui garantit que les informations sont automatiquement renvoyées lorsqu'une erreur se produit lors de la transmission des données.

## Définition
Lors de l'envoi de données sur Internet, des paquets peuvent parfois être perdus ou corrompus. ARQ vérifie si le destinataire a reçu les données et s'il détecte une erreur, il indique à l'expéditeur "Je n'ai pas reçu ceci, envoyez à nouveau". De cette façon, on garantit que les données sont reçues complètement et sans erreurs.

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
- [API](/fr/dictionary/api/)
- [DNS Tunneling](/fr/dictionary/dns-tunneling/)
- [Computer Science](/fr/dictionary/computer-science/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/arq/
