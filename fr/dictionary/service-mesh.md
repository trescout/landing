# Qu'est-ce que Service Mesh ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Le service mesh est la couche d'infrastructure invisible qui gère le trafic des microservices.

## Définition et origine du mot

Dans un système composé de centaines de composants, il est difficile pour ces derniers de se trouver et de communiquer en toute sécurité. Le service mesh gère la communication, régule le trafic et assure la sécurité. Il applique des politiques réseau sans toucher au code.

***Analogie :** C'est comme la tour de contrôle qui gère le trafic aérien dans un grand aéroport ; elle garantit que les services se déplacent en toute sécurité sans entrer en collision.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Cloud :** Grandes applications à microservices.
**Banque :** Trafic de services hautement sécurisé.
**E-commerce :** Ligne de commande sous la charge des campagnes.

## Profondeur technique et architecture

Parties:

**Sidecar :** Petit proxy à côté de chaque service, le trafic y transite.
**Plan de contrôle :** Le cerveau qui distribue les règles.
**Plan de données :** Les proxys qui font le travail.
**mTLS :** Authentification chiffrée inter-services.
**Résilience :** Nouvel essai et disjoncteur.

Règle de nouvel essai :

```
retries:
  attempts: 3
  perTryTimeout: 2s
```

Istio et Linkerd en sont des implémentations connues. Dans un petit système, le coût dépasse les avantages.

## Utilisation dans différentes disciplines

**Aéroport :** La tour qui évite les collisions d'avions.
**Trafic :** Le réseau de signalisation qui régule le flux.
**Courrier :** Le centre de distribution qui achemine l'envoi.

## Foire aux questions

**Est-ce nécessaire pour chaque projet ?**

Non. Dans un système à faible nombre de services, cela ajoute de la charge. Cela prend tout son sens lorsque la complexité augmente.

**Qu'est-ce que ça coûte ?**

Cela ajoute de la mémoire et de la latence par proxy. C'est le prix à payer pour obtenir de l'observabilité.

**Kubernetes est-il obligatoire ?**

Non, mais ils sont souvent utilisés ensemble. Il existe également des versions qui s'exécutent sur des machines virtuelles.

**Est-ce que cela remplace une passerelle API ?**

Non. La passerelle est la porte extérieure, le maillage (mesh) gère le trafic interne. Les deux fonctionnent ensemble.

## Termes liés

- [Cloud Native](https://trescout.com/fr/dictionary/cloud-native/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Proxy](https://trescout.com/fr/dictionary/proxy/)

## Outils liés

- [Meshery](https://trescout.com/fr/discover/meshery/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/service-mesh/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/service-mesh/
