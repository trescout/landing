# Journalisation rapide pour projets C++

spdlog est une bibliothèque de journalisation (logging) C++ ultra rapide, utilisable en en-têtes seuls (header-only) ou précompilée. Conçue selon les standards C++ modernes, elle assure des sorties sans latence et hautement performantes.

- ★ 29.437
- C++
- GitHub Trending · 2026-08-05

## Mises à jour
- 6 août 2026: Étoiles 29 402 → 29 437, dernière version v1.17.0 (4 janvier 2026).

## Ce que ça vous apporte
- Débit de millions de lignes par seconde: Conception sans allocation dynamique et optimisations à la compilation pour une latence minimale.
- Tampon circulaire asynchrone sans verrou: Délègue l'écriture à un pool de threads d'arrière-plan, protégeant le thread principal des blocages d'E/S.
- Multiples puits de sortie (sinks): Écriture simultanée vers la console en couleur, fichiers tournants par taille, archives quotidiennes et syslog.
- Moteur de formatage {fmt} intégré: Basé sur la bibliothèque {fmt} (standard C++20) pour un formatage typé, rapide et expressif.
- Flexibilité header-only ou compilée: Intégration directe par copie de répertoire ou liaison statique pour accélérer la compilation.

## Installation

**macOS (Homebrew)**

```
brew install spdlog
```

**Gestionnaire vcpkg**

```
vcpkg install spdlog
```

**Intégration CMake FetchContent**

```
include(FetchContent)
FetchContent_Declare(
  spdlog
  GIT_REPOSITORY https://github.com/gabime/spdlog.git
  GIT_TAG v1.17.0
)
FetchContent_MakeAvailable(spdlog)
target_link_libraries(mon_projet PRIVATE spdlog::spdlog)
```

Source: Formule Homebrew

## Pour commencer et utilisation de base

La prise en main de spdlog est immédiate. Après avoir inclus l'en-tête, utilisez directement les fonctions globales ou créez des loggers spécialisés :

**Exemple d'utilisation basique en C++**

```
#include "spdlog/spdlog.h"
#include "spdlog/sinks/rotating_file_sink.h"

int main() {
    // Journalisation console standard
    spdlog::info("spdlog demarre avec succes.");
    spdlog::warn("Attention: consommation memoire en hausse !");
    spdlog::error("Code d'erreur: {:d}, message: {}", 404, "Page introuvable");

    // Logger sur fichier tournant (max 5 Mo, 3 fichiers)
    auto file_logger = spdlog::rotating_logger_mt("file_logger", "logs/app.txt", 1024 * 1024 * 5, 3);
    file_logger->info("Ce message est thread-safe et archive automatiquement.");

    return 0;
}
```

## Architecture technique et fonctionnement interne

La rapidité remarquable de spdlog découle d'une architecture modulaire à surcoût nul :
- Séparation Logger et Sink: Le logger filtre par gravité (trace, debug, info, warn, err, critical) et transmet les entrées aux différents sinks.
- Sécurité des threads (_mt vs _st): Les classes sink existent en versions thread-safe (_mt) et en versions sans verrou pour thread unique (_st).
- File circulaire asynchrone (Ring Buffer): Le pool de threads dédié traite les messages en arrière-plan sans bloquer les calculs principaux.
- Vidage intelligent (Flush): Les données restent en cache mémoire et sont vidées automatiquement en cas d'erreur critique via spdlog::flush_on.

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je souhaite configurer spdlog dans un projet C++ moderne avec CMake en mode asynchrone. Peux-tu me fournir une fonction d'initialisation et un fichier CMakeLists.txt configurant une sortie console colorée, un fichier rotatif de 10 Mo et un vidage immédiat sur erreur ?

- **Pour qui:** Développeurs C++, créateurs de moteurs de jeu et systèmes embarqués exigeant une latence minimale.
- **Licence:** MIT (Licence open-source permissive)
- **Intégration:** En-têtes seuls ou bibliothèque précompilée
- **Standards:** C++11, C++14, C++17, C++20

## Foire aux questions
- Pourquoi utiliser spdlog plutôt que printf ou std::cout ? spdlog est infiniment plus rapide, thread-safe, gère les niveaux de sévérité et formate via {fmt} sans bloquer le thread principal.
- Peut-on formater des objets ou classes personnalisées ? Oui, en surchargeant operator<< ou en spécialisant fmt::formatter pour vos types de données.
- Est-ce adapté aux moteurs de jeu et au trading haute fréquence ? Oui, les sinks asynchrones garantissent un traitement en quelques nanosecondes sans impacter la boucle de rendu.
- Supporte-t-il la sortie JSON structurée ? Oui, vous pouvez formater les messages en JSON pour les exporter vers Grafana Loki, Datadog ou Elasticsearch.

## Liens
- [GitHub →](https://github.com/gabime/spdlog)
- [Read in Turkish →](https://trescout.com/discover/spdlog/)

## Termes liés du glossaire
Logging Logs Runtime Memory Management

---
Source: TreScout Discover · https://trescout.com/fr/discover/spdlog/
