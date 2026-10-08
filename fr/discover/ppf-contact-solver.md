# Gérer les contacts dans les simulations physiques

PPF Contact Solver, en tant que moteur physique de ZOZO, est conçu pour résoudre les contacts entre le tissu, le solide et la corde dans des simulations basées sur la physique. Il augmente la cohérence physique des simulations en calculant l'interaction de différentes géométries. Il peut également être exécuté à distance grâce au plug-in Blender.

- ★ 4 514
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

## Mises à jour

- **1 octobre 2026:** Étoiles 4,513 → 4,514, dernière version addon-2026-10-01-2043 (1 octobre 2026).
- **1 octobre 2026:** Étoiles 4,507 → 4,513, dernière version addon-2026-10-01-0946 (1 octobre 2026).
- **27 septembre 2026:** Étoiles 4,508 → 4,507, dernière version addon-2026-09-27-2158 (27 septembre 2026).
- **27 septembre 2026:** Étoiles 4,490 → 4,508, dernière version addon-2026-09-22-2204 (22 septembre 2026).

## Installation

**Démarrer le conteneur GPU**

```
docker run --rm -it --name ppf-contact-solver --gpus all -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e WEB_PORT=8080 ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```

## Qu'est-ce que ça fait ?

- Il effectue des simulations réalistes de tissus, d'objets solides et de cordes.
- Augmente la cohérence physique dans les simulations.
- Il peut être piloté à distance via Blender.
- Il s'agit d'une solution axée sur la recherche (le propre moteur physique de ZOZO).

## À qui ne convient-il pas ?

Ce n'est pas une application pour utilisateur final. Des connaissances en programmation et en simulation physique sont requises pour pouvoir les utiliser ; Il fait davantage appel au domaine du graphisme/recherche.

## Comment installer, comment utiliser ?

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Exécutez le solveur de contacts physiques ppf-contact-solver de ZOZO avec Docker (GPU NVIDIA requis) : exécutez la commande docker suivante, puis ouvrez http://localhost:8080 dans le navigateur et essayez les exemples JupyterLab prêts à l'emploi.

## Termes liés du glossaire

- [Container](https://trescout.com/fr/dictionary/container/)
- [Localhost](https://trescout.com/fr/dictionary/localhost/)
- [GPU](https://trescout.com/fr/dictionary/gpu/)
- [Open Source](https://trescout.com/fr/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Utilisateurs techniques, chercheurs qui effectuent des simulations graphiques/physiques
- **Difficulté:** Axé sur la technique avancée/la recherche
- **Quelles offres:** Solution de contact tissu/solide/corde
- **Ça marche:** Plugin Python + Blender
- **Frais:** Gratuit · open source (Apache-2.0)

**Licence:** Apache-2.0 · vous pouvez l'utiliser librement, le modifier, en faire un usage commercial (inclut également la protection par brevet).

## Liens

- [Dépôt GitHub →](https://github.com/st-tech/ppf-contact-solver)
- [Lire en turc →](https://trescout.com/discover/ppf-contact-solver/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-05-26 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ppf-contact-solver/
