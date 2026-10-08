# Tools : Outillage développeur, Function Calling et MCP


**Catégorie:** Dev  

**Dernière mise à jour:** 2026-09-19


Les outils (tools) désignent deux domaines vitaux en informatique : les utilitaires qui décuplent la productivité des développeurs, et les interfaces permettant aux modèles d'IA d'interagir avec le monde extérieur.


## Étymologie et métaphore de l'outil en informatique
Le mot anglais *tool* dérive du vieil anglais *tol* (instrument de travail). De même que la fabrication d'outils a transformé l'histoire humaine, la philosophie Unix a forgé l'informatique moderne : concevoir des programmes modulaires accomplissant une tâche unique et composables via des flux textuels.

## 1. Outils pour développeurs (DevTools)
L'ingénierie logicielle repose sur des strates d'outils spécialisés :
- **Compilateurs et moteurs de build :** GCC, Clang, rustc et Vite traduisent le code source en instructions machines optimisées.
- **Débogueurs et profileurs :** GDB, LLDB et les DevTools des navigateurs inspectent l'état de la mémoire et les trames réseau en direct.
- **Analyse statique et linters :** ESLint, Ruff ou SonarQube garantissent la qualité du code avant même son exécution.

## 2. Le tournant de l'IA : Tool Use et Function Calling
Sans outils, les grands modèles de langage (LLM) restent de simples générateurs statistiques de texte. L'utilisation d'outils comble quatre lacunes majeures :
1. **Informations en temps réel :** Interrogation d'API météo ou financières pour dépasser la date limite d'entraînement.
2. **Rigueur mathématique :** Délégation des calculs à des interpréteurs Python fiables.
3. **Capacité d'action :** Envoi de messages, modification de bases de données ou déclenchement de webhooks.
4. **Exploration système :** Navigation dans des arborescences de fichiers et des dépôts Git.

## 3. Model Context Protocol (MCP) : le standard universel
Pour éviter la multiplication de formats propriétaires incompatibles, Anthropic a conçu le **Model Context Protocol (MCP)**. À l'image de LSP pour les éditeurs de code, MCP offre un protocole JSON-RPC standardisé unifiant la communication entre clients IA et serveurs d'outils distants.

## 4. Outils à double usage en cybersécurité
En sécurité informatique, les outils présentent une nature intrinsèquement ambivalente :
- **Tests d'intrusion et audit :** Nmap, Wireshark et Burp Suite permettent aux experts défensifs de corriger les failles avant toute exploitation malveillante.
- **Fuzzing automatisé :** Des injecteurs comme AFL++ soumettent les protocoles à des flux de données aléatoires pour déceler les failles de mémoire zero-day.

## Par analogie
Un modèle de langage sans outils est comme un génie enfermé dans une pièce sans fenêtres ; lui fournir des outils revient à lui donner des mains, une calculatrice et un téléphone pour interagir avec le monde.

## Questions fréquentes

**Que signifie le concept d'outil (tool) en IA ?**  
C'est une fonction ou une API externe qu'un modèle de langage peut appeler automatiquement par des arguments JSON structurés pour exécuter une action réelle.

**Qu'est-ce que le protocole MCP d'Anthropic ?**  
C'est un standard ouvert facilitant l'interconnexion sécurisée entre assistants IA et sources de données ou logiciels tiers.

**Comment le modèle sélectionne-t-il le bon outil ?**  
Il analyse les descriptions textuelles et les schémas de paramètres de chaque outil disponible, puis génère un appel JSON conforme.

## Termes liés
- [MCP](/fr/dictionary/mcp/)
- [AI Agent](/fr/dictionary/ai-agent/)
- [Plugin](/fr/dictionary/plugin/)
- [SDK](/fr/dictionary/sdk/)

## Outils liés
- [ECC](/fr/discover/ecc/)
- [System Prompts and Models of AI Tools](/fr/discover/system-prompts-and-models-of-ai-tools/)
- [Claude Plugins Official](/fr/discover/claude-plugins-official/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/tools/
