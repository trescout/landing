# Qu'est-ce que TUI ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

> Text User Interface

Une TUI (Text User Interface / Interface utilisateur textuelle) est une interface utilisateur axée sur le clavier, fonctionnant sur les écrans de terminaux à l'aide de texte et de blocs de caractères, sans nécessiter de carte graphique.

## Cadre conceptuel, étymologie et évolution du terminal

Le terme TUI est l'abréviation de l'anglais Text User Interface (ou parfois Terminal User Interface). Dans l'histoire des interfaces informatiques, c'est un paradigme visuel hybride qui fait le pont entre la CLI (Interface en Ligne de Commande) et la GUI (Interface Graphique Utilisateur) :

- CLI (Command-Line Interface) : flux unidimensionnel dans lequel l'utilisateur saisit une commande d'une seule ligne et le système répond à cette commande par une sortie textuelle.
- GUI (Graphical User Interface) : Interface visuelle riche utilisant des pixels, des fenêtres, des curseurs de souris et des cartes accélératrices graphiques (GPU).
- TUI (Text User Interface) : interface en mode texte dotée de menus, qui utilise une grille de caractères bidimensionnelle composée de lignes et de colonnes sur l'écran du terminal au lieu de pixels, et qui intègre des fenêtres, des boutons, des barres d'état et des formulaires.

Les racines de la TUI remontent aux terminaux textuels physiques des années 1970 tels que le TeleType (TTY) et le DEC VT100. Sur ces terminaux, des séquences d'échappement ANSI (ANSI Escape Sequences, par exemple \033[2J pour effacer l'écran et \033[31m pour afficher le texte en rouge) ont été développées afin d'écrire du texte en couleur à des coordonnées spécifiques de l'écran et de déplacer le curseur.

***Analogie :** Au lieu de l'écran OLED tactile haute résolution d'un smartphone moderne (GUI), cela ressemble à des tableaux d'affichage mécaniques à volets (split-flap display) dans les aéroports ou à des tableaux d'affichage numériques. Chaque case ne peut contenir qu'une seule lettre ou un seul symbole, mais grâce à l'agencement organisé de ces symboles, un panneau de contrôle parfait et instantanément réactif émerge.*

## Architecture technique : mode brut (raw mode), séquences d'échappement ANSI et double tampon

Le fonctionnement en arrière-plan d'une application TUI repose sur trois mécanismes fondamentaux au niveau du système d'exploitation :

1. Mode brut du terminal (Raw Mode) : L'environnement de terminal standard fonctionne en mode "Cooked Mode" ; c'est-à-dire que le système d'exploitation met en attente et met en mémoire tampon les caractères jusqu'à ce que l'utilisateur appuie sur la touche Entrée. Lorsqu'une application TUI démarre, elle bascule le terminal en "Raw Mode" à l'aide de l'appel termios. Ainsi, chaque touche pressée par l'utilisateur (j, k, Ctrl+C, touches fléchées) est capturée instantanément sans attendre la touche Entrée.
2. Tampon d'écran alternatif (Alternate Screen Buffer) : grâce au tampon alternatif (tput smcup / rmcup), votre historique de terminal ne disparaît pas lorsque vous lancez htop ou vim, et vous pouvez retrouver votre ligne de commande d'origine à la fermeture du programme. L'interface TUI ouvre sa propre zone d'affichage virtuelle et revient à l'écran principal en quittant.
3. Double mise en mémoire tampon et rendu des différences (Diff Rendering) : pour éviter le scintillement (flickering) à l'écran, les moteurs TUI modernes conservent deux matrices de caractères en mémoire : l'écran actuel et l'écran suivant. Seules les cellules modifiées sont calculées et seules ces différences (diff) sont envoyées au terminal avec des codes ANSI, ce droit d'exécuter des animations fluides à 60 FPS.

## La Renaissance moderne des TUI et les outils de développement

Ces dernières années, en réaction à la consommation excessive de mémoire des technologies web (applications lourdes basées sur Electron), on a assisté à une véritable renaissance des TUI dans l'écosystème des développeurs :

- Faible consommation de ressources : Alors qu'une interface graphique consomme des centaines de mégaoctets de mémoire, une application TUI n'utilise que quelques mégaoctets de RAM.
- Zéro latence via SSH : lors de la gestion d'un serveur distant dans le cloud, le transfert d'interface graphique (VNC / RDP) nécessite une bande passante élevée ; en revanche, le TUI est ultra-rapide au sein d'un tunnel SSH, même sur des connexions mobiles à bas débit.
- État de flux au clavier (Flow State) : Travailler sans lever la main de la souris, grâce aux dispositions de touches de Vim (h, j, k, l), décuple la concentration et la productivité des ingénieurs.

Cadres et outils modernes incontournables :

- Monde de Rust : les bibliothèques ratatui (anciennement tui-rs) et crossterm sont devenues la norme de référence pour les projets TUI modernes grâce à leur sécurité mémoire et à leurs performances ultra-élevées.
- Le monde de Go : bubbletea (un framework réactif développé par l'équipe de Charm qui adapte le motif The Elm Architecture au terminal), lipgloss (un moteur de style) et bubbles.
- L'univers de Python : Textual et rich par Will McGugan.
- Outils TUI cultes : lazygit pour la gestion de Git, k9s pour les clusters Kubernetes, lazydocker pour Docker, btop et htop pour la surveillance système, et ncdu pour l'analyse de disque.

## Souvent confondu avec

- CLI vs TUI: la CLI est un modèle de questions-réponses sur une seule ligne (git status, ls -la). La TUI, quant à elle, est un panneau visuel bidimensionnel qui remplit la fenêtre du terminal avec des onglets, des listes et des raccourcis clavier (lazygit, k9s).
- Un TUI ne se résume pas à du texte brut : les terminaux modernes prennent en charge les Nerd Fonts (icônes), le support 24-bit TrueColor, les caractères de dessin de boîtes UTF-8 et même le rendu visuel réel directement dans le terminal grâce aux protocoles Kitty Graphics / Sixel.

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

- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Terminal](https://trescout.com/fr/dictionary/terminal/)
- [Terminal Control](https://trescout.com/fr/dictionary/terminal-control/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Assembly](https://trescout.com/fr/dictionary/assembly/)
- [Tech Stack](https://trescout.com/fr/dictionary/tech-stack/)

## Outils liés

- [PI](https://trescout.com/fr/discover/pi/)
- [Witr](https://trescout.com/fr/discover/witr/)
- [Hister](https://trescout.com/fr/discover/hister/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/tui/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/tui/
