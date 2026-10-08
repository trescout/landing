# Support de QUIC et HTTP/3 avec Rust

Développé par Cloudflare, quiche propose une implémentation du protocole de transport QUIC et de la norme réseau HTTP/3 écrite en langage Rust. Visant à accélérer le trafic Internet, cette bibliothèque fournit une infrastructure de bas niveau pour les développeurs souhaitant optimiser les performances réseau.

- ★ 12 638
- GitHub Trending · 2026-09-20

## Mises à jour

- **27 septembre 2026:** Étoiles 12,452 → 12,638, dernière version 0.30.0 (17 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite utiliser cette bibliothèque écrite en langage de programmation Rust pour traiter des paquets QUIC et gérer les états de connexion réseau. Quelles étapes dois-je suivre pour exécuter le client et le serveur après avoir cloné le projet ?

## Termes liés du glossaire

- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Développeurs souhaitant optimiser les performances réseau et assurer la prise en charge de HTTP/3.
- **Licence:** BSD-2-Clause

## Liens

- [Dépôt GitHub →](https://github.com/cloudflare/quiche)
- [Lire en turc →](https://trescout.com/discover/quiche/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-20 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/quiche/
