# Tunneling TCP pour le trafic réseau

Développé en langage Go, OpenFlux est un outil de tunneling TCP conçu pour la recherche sur la pile réseau (network stack). Grâce à la prise en charge de protocoles de transport enfichables (pluggable transports), il offre des possibilités flexibles d'analyse et de gestion du trafic réseau.

- ★ 2 184
- Go
- GitHub Trending · 2026-09-12

## Mises à jour

- **16 octobre 2026:** Étoiles 2,120 → 2,184, dernière version v0.13.0 (16 octobre 2026).
- **14 octobre 2026:** Étoiles 2,107 → 2,120, dernière version v0.7.3 (14 octobre 2026).
- **13 octobre 2026:** Étoiles 2,092 → 2,107, dernière version v0.7.2 (13 octobre 2026).
- **13 octobre 2026:** Étoiles 2,088 → 2,092, dernière version v0.7.0 (13 octobre 2026).

## Ce que ça vous apporte

- Gestion réseau flexible avec des protocoles de transport enfichables
- Routage du trafic réseau local avec prise en charge du proxy SOCKS5
- Transmission de données via Yandex Docs et WebRTC

## Installation

**Compilation du client de bureau et du nœud de sortie**

```
go mod tidy
go build -o universal-bypass-tool .
```

**Compilation du client Android**

```
export ANDROID_NDK_HOME=<your Android NDK path>
./build_android.sh
```

## Exécution

**Lancement du client de bureau**

```
./universal-bypass-tool --client --url "YOUR_YANDEX_DOC_URL" --socks5 :1080 --debug
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite créer un tunnel TCP en utilisant l'outil OpenFlux. Expliquez étape par étape les étapes de compilation nécessaires pour exécuter le client sur mon ordinateur de bureau, puis comment configurer les paramètres du proxy SOCKS5 sur le navigateur. De plus, précisez avec des détails techniques pourquoi il est nécessaire de bloquer les paquets RST avec iptables lors de la configuration d'un nœud de sortie (exit node) sur un serveur Linux, et quel est l'impact de cette opération sur la sécurité du réseau.

## Termes liés du glossaire

- [Pluggable Transports](https://trescout.com/fr/dictionary/pluggable-transports/)
- [Network Stack](https://trescout.com/fr/dictionary/network-stack/)
- [Proxy](https://trescout.com/fr/dictionary/proxy/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux utilisateurs qui effectuent des recherches sur la pile réseau et souhaitent tunneler le trafic TCP via différents protocoles de transport.
- **Licence:** GPL-3.0

## Liens

- [Dépôt GitHub →](https://github.com/p1neappleXpress/OpenFlux)
- [Lire en turc →](https://trescout.com/discover/openflux/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-12 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openflux/
