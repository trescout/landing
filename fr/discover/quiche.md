# Support de QUIC et HTTP/3 avec Rust

Développé par Cloudflare, quiche propose une implémentation du protocole de transport QUIC et de la norme réseau HTTP/3 écrite en langage Rust. Visant à accélérer le trafic Internet, cette bibliothèque fournit une infrastructure de bas niveau pour les développeurs souhaitant optimiser les performances réseau.

- ★ 12 638
- GitHub Trending · 2026-09-20

## Ce que ça vous apporte
- Implémenter le protocole de transport QUIC
- Travailler sur la norme réseau HTTP/3
- Traiter des paquets réseau de bas niveau

## Installation
**Cloner le projet**

```
git clone https://github.com/cloudflare/quiche
```


## Exécution
**Exécuter le client**

```
cargo run --bin quiche-client -- https://cloudflare-quic.com/
```

**Exécuter le serveur**

```
cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key
```


## Si vous ne codez pas
Je souhaite utiliser cette bibliothèque écrite en langage de programmation Rust pour traiter des paquets QUIC et gérer les états de connexion réseau. Quelles étapes dois-je suivre pour exécuter le client et le serveur après avoir cloné le projet ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/quiche/
