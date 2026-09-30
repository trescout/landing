# Journalisation rapide pour les projets C++

spdlog est une bibliothèque de journalisation ultra-rapide développée pour le langage de programmation C++, qui peut être utilisée uniquement en en-tête ou en tant que bibliothèque compilée. Il offre une gestion de sortie haute performance et sans décalage dans les projets logiciels utilisant les normes C++ modernes.

- ★ 29 437
- C++
- GitHub Trending · 2026-08-05

## Ce que ça vous apporte
- Performances de journalisation de plusieurs millions de lignes par seconde : crée une latence de l'ordre de la microseconde dans le thread principal de l'application avec une approche d'allocation de mémoire nulle et des optimisations du temps de compilation.
- File d'attente en anneau asynchrone et sans verrouillage : isole complètement les goulots d'étranglement d'E/S de fichiers ou de réseau du pipeline appelant en déchargeant les écritures de journaux vers le pool d'arrière-plan.
- Riche variété de cibles : sortie de console colorée, rotation des fichiers par taille, archives avec dates quotidiennes, écriture simultanée sur les cibles syslog et Android logcat.
- Puissance de formatage fmt intégrée : fournit un formatage de texte de style Python sûr, rapide et flexible à l'aide de la bibliothèque {fmt}, qui constitue la base de la norme de formatage C++20.
- Flexibilité d'utilisation en en-tête uniquement ou compilée : vous pouvez l'inclure dans votre projet en copiant un seul répertoire ou le lier en tant que bibliothèque statique pour réduire les temps de compilation.

## Installation
**macOS (Homebrew)**

```
brew install spdlog
```


## Comment démarrer et utilisation de base
Démarrer avec la bibliothèque spdlog est extrêmement simple. Une fois que vous avez inclus le fichier d'en-tête dans votre projet, vous pouvez appeler directement les fonctions de journalisation globale ou créer des objets de journalisation personnalisés :

## Architecture technique et principe de fonctionnement
- Distinction Logger et Sink : L'objet Logger filtre le journal entrant (trace, débogage, info, warn, err, critique). Les messages acceptés sont transférés vers un ou plusieurs objets Sink. Par exemple, un seul enregistreur peut écrire dans le fichier au format JSON tout en imprimant simultanément la couleur sur la console.
- Thread-safe (_mt vs _st) : spdlog fournit toutes les classes de récepteur sous deux formes : versions à verrouillage mutex multi-thread (_mt) et sans verrouillage (_st) spécifiques à un seul thread. En mode monothread, le coût du mutex est totalement nul.
- File d'attente en anneau asynchrone (Ring Buffer) : le bloc de mémoire alloué avec spdlog::init_thread_pool est consommé par le thread exécuté en arrière-plan. L'application principale laisse le journal dans la file d'attente et continue immédiatement son chemin.
- Rinçage intelligent du tampon (Flush) : les données sont conservées dans le tampon du système d'exploitation pour des raisons de performances ; Cependant, le mécanisme spdlog::flush_on(spdlog::level::err) peut être déclenché pour empêcher la perte de données dans les moments d'erreur critiques.

## Si vous ne codez pas
Je souhaite configurer la bibliothèque spdlog avec une architecture asynchrone à l'aide de CMake dans un projet C++ moderne. Pouvez-vous préparer le fichier CMakeLists.txt avec un exemple de fonction d'initialisation C++ qui fait pivoter le fichier lorsque la taille du journal atteint 10 Mo, donne également une sortie couleur à la console et le vide sur le disque immédiatement en cas d'erreur ?

## Questions fréquemment posées
- Spdlog doit-il être utilisé uniquement en en-tête ou compilé ? Dans les projets de petite et moyenne taille, l'utilisation de l'en-tête uniquement en ajoutant uniquement le répertoire include est très pratique. Cependant, dans les grands projets C++ composés de centaines de fichiers sources, il est recommandé de compiler et de lier la bibliothèque avec l'indicateur SPDLOG_COMPILED pour optimiser le temps de compilation.
- La journalisation affecte-t-elle la vitesse d’exécution de l’application principale ? Fonctionnant au niveau de la microseconde même en mode synchrone, spdlog réduit la charge d'E/S sur le thread principal à presque zéro lors de l'utilisation d'une architecture d'enregistrement asynchrone. Le message est copié dans la file d'attente et l'écriture sur le disque s'effectue en arrière-plan.
- Comment fonctionne le mécanisme de rotation des fichiers ? Lorsque la taille de fichier maximale spécifiée (par exemple 10 Mo) est atteinte, le fichier actif est archivé (application.1.txt, application.2.txt) et un nouveau fichier est ouvert à partir de zéro. Lorsque le nombre maximum de fichiers spécifié est dépassé, le fichier journal le plus ancien est automatiquement effacé.
- Y aura-t-il un conflit avec la bibliothèque fmt externe ? Non, spdlog utilise par défaut la version packagée en interne de fmt. Si vous le souhaitez, vous pouvez directement intégrer la bibliothèque fmt indépendante existante dans votre système avec spdlog en définissant la macro SPDLOG_FMT_EXTERNAL.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/spdlog/
