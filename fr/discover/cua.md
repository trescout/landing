# Contrôle informatique pour les agents d'intelligence artificielle

CUA fournit une infrastructure open source pour les agents d'intelligence artificielle informatiques. Il rassemble un bac à sable, un kit de développement logiciel (SDK) et des outils de référence sous un même toit dans le but de former et d'évaluer les agents capables de contrôler les systèmes d'exploitation de bureau.

- ★ 21 225
- HTML
- GitHub Trending · 2026-06-16

## Mise à jour
- 12 août 2026 : Star 21 066 → 21 225, dernière version lume-v0.5.3 (11 août 2026).
- 10 août 2026 : Star 20 990 → 21 066, dernière version cli-v0.1.14 (10 août 2026).
- 7 août 2026 : Star 20 962 → 20 990, dernière version Fleet-v0.1.7 (7 août 2026).
- 6 août 2026 : Star 20 909 → 20 962, dernière version sandbox-v0.1.27 (5 août 2026).

## Ce que ça vous apporte
- Contrôler les applications de bureau en arrière-plan
- Bacs à sable isolés pour différents systèmes d'exploitation
- Outils d'analyse comparative pour mesurer les performances des agents

## Installation
**Installation du pilote (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Installation du SDK bac à sable**

```
pip install cua
```


## Exécution
**Démarrage de la machine virtuelle macOS**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```


## Si vous ne codez pas
Je souhaite développer un agent d'utilisation informatique utilisant l'infrastructure CUA. Aidez-moi à configurer la structure Python de base qui permettra à mon agent d'interagir avec les applications de bureau en arrière-plan, d'effectuer des clics de souris et d'envoyer des saisies au clavier. Créez un exemple d'esquisse de code qui exécute des commandes et prend des captures d'écran dans un environnement Linux à l'aide du SDK CUA Sandbox.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/cua/
