# Qu'est-ce que TUI ?

> Text User Interface

Une TUI (Text User Interface / Interface utilisateur textuelle) est une interface utilisateur axée sur le clavier, fonctionnant sur les écrans de terminaux à l'aide de texte et de blocs de caractères, sans nécessiter de carte graphique.

## Cadre conceptuel, étymologie et évolution du terminal
Le terme TUI est l'abréviation de l'anglais Text User Interface (ou parfois Terminal User Interface). Dans l'histoire des interfaces informatiques, c'est un paradigme visuel hybride qui fait le pont entre la CLI (Interface en Ligne de Commande) et la GUI (Interface Graphique Utilisateur) :

## Architecture technique : mode brut (raw mode), séquences d'échappement ANSI et double tampon
Le fonctionnement en arrière-plan d'une application TUI repose sur trois mécanismes fondamentaux au niveau du système d'exploitation :

## La Renaissance moderne des TUI et les outils de développement
Ces dernières années, en réaction à la consommation excessive de mémoire des technologies web (applications lourdes basées sur Electron), on a assisté à une véritable renaissance des TUI dans l'écosystème des développeurs :

## Souvent confondu avec

## Questions fréquentes
**Que signifie TUI et quel est son acronyme ?**
TUI est l'abréviation de Text User Interface (Interface Utilisateur Texte) ou Terminal User Interface. Il désigne des interfaces visuelles et interactives qui fonctionnent sur la grille de caractères du terminal sans gestionnaire de fenêtres graphique.

**Quelles sont les principales différences entre CLI, GUI et TUI ?**
L'interface CLI fonctionne avec des commandes textuelles sur une seule ligne ; l'interface GUI se gère avec des pixels, des fenêtres et la souris ; tandis que l'interface TUI est un format hybride fonctionnant à l'aide de menus, de panneaux et de boîtes axés sur le clavier au sein du terminal.

**Comment les interfaces utilisateur de terminal (TUI) dessinent-elles l'écran ?**
Grâce aux séquences d'échappement ANSI (Escape Sequences) et aux codes de contrôle du terminal, le curseur est déplacé vers la ligne et la colonne souhaitées de l'écran, les codes de couleur sont attribués et les caractères de boîte Unicode sont tracés.

**Quelles sont les bibliothèques les plus populaires pour développer des TUI modernes ?**
Dans l'écosystème Rust, ratatui, en Go, bubbletea et lipgloss, et du côté de Python, les bibliothèques Textual et rich constituent la norme de l'industrie.


## Termes liés
- [CLI](/fr/dictionary/cli/)
- [Terminal](/fr/dictionary/terminal/)
- [Terminal Control](/fr/dictionary/terminal-control/)
- [Runtime](/fr/dictionary/runtime/)
- [Assembly](/fr/dictionary/assembly/)
- [Tech Stack](/fr/dictionary/tech-stack/)

## Outils liés
- [PI](/fr/discover/pi/)
- [Witr](/fr/discover/witr/)
- [Hister](/fr/discover/hister/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/tui/
