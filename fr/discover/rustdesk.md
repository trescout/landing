# Contrôle de bureau à distance open source

Développée avec Rust, RustDesk est une application de bureau à distance open source que vous pouvez héberger sur votre propre serveur. Offrant un accès et un contrôle à distance, ce logiciel crée une solution alternative aux services payants tels que TeamViewer.

- ★ 124 982
- Rust
- GitHub Trending · 2026-08-15

## Mises à jour

- **2 octobre 2026:** Étoiles 120,872 → 124,982, dernière version 1.5.0 (30 septembre 2026).
- **15 août 2026:** Étoiles 120,685 → 120,872, dernière version 1.4.9 (6 juillet 2026).

## Ce que ça vous apporte

- Possibilité d'hébergement sur votre propre serveur
- Contrôle total sur les données
- Solution prête à l'emploi qui ne nécessite aucune configuration supplémentaire

## Installation

**Installation de VCPKG**

```
git clone https://github.com/microsoft/vcpkg
cd vcpkg
git checkout 2023.04.15
cd ..
vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=$HOME/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite établir une connexion bureau à distance à l'aide de RustDesk. Comment puis-je configurer mon propre serveur pour assurer la sécurité de mes données et quels sont les paramètres de sécurité de base auxquels je dois prêter attention lors de la connexion ?

Dépôt : https://github.com/rustdesk/rustdesk. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux utilisateurs qui souhaitent répondre à leurs besoins d'accès et de contrôle à distance en conservant leurs données sur leurs propres serveurs plutôt que sur des services tiers.
- **Licence:** AGPL-3.0

## Liens

- [Dépôt GitHub →](https://github.com/rustdesk/rustdesk)
- [Lire en turc →](https://trescout.com/discover/rustdesk/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-15 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/rustdesk/
