# Tunneling TCP pour le trafic réseau

Développé en langage Go, OpenFlux est un outil de tunneling TCP conçu pour la recherche sur la pile réseau (network stack). Grâce à la prise en charge de protocoles de transport enfichables (pluggable transports), il offre des possibilités flexibles d'analyse et de gestion du trafic réseau.

- ★ 1 241
- Go
- GitHub Trending · 2026-09-12

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
Je souhaite créer un tunnel TCP en utilisant l'outil OpenFlux. Expliquez étape par étape les étapes de compilation nécessaires pour exécuter le client sur mon ordinateur de bureau, puis comment configurer les paramètres du proxy SOCKS5 sur le navigateur. De plus, précisez avec des détails techniques pourquoi il est nécessaire de bloquer les paquets RST avec iptables lors de la configuration d'un nœud de sortie (exit node) sur un serveur Linux, et quel est l'impact de cette opération sur la sécurité du réseau.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openflux/
