# Tests unitaires standard de l'industrie dans les projets C++

GoogleTest et GoogleMock sont des frameworks de test open source standard qui vous permettent d'exécuter des tests unitaires, des simulations et des tests paramétriques sur des projets C++ modernes.

- ★ 39 588
- C++
- GitHub Trending · 2026-08-27

## Mises à jour

- **27 septembre 2026:** Étoiles 38,987 → 39,588, dernière version v1.18.0 (10 août 2026).

## Ce que ça vous apporte

- Macros de vérification riches : diagnostic d'erreur clair avec les macros ASSERT_* (erreur critique, termine le test) et EXPECT_* (enregistre l'erreur, continue le flux de test).
- Infrastructure Mock avancée (GoogleMock) : possibilité de simuler facilement des interfaces et de définir des attentes d'appel avec MOCK_METHOD pour isoler les dépendances.
- Capacité de test paramétrique : possibilité de répéter automatiquement la même logique de test sur des dizaines d'entrées et d'ensembles de données différents avec un seul modèle.
- Sécurité multiplateforme et thread : vérification des scénarios de crash avec une architecture thread-safe et des tests de mort dans les environnements Linux, macOS et Windows.
- Intégration CI/CD et reporting : intégration transparente avec les pipelines GitHub Actions, Jenkins et GitLab CI avec les formats de sortie XML et JSON compatibles JUnit.

## Installation

**Ajout au projet avec CMake FetchContent**

```
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.tar.gz
)
FetchContent_MakeAvailable(googletest)
```

## Exécution

**Compilez le test et exécutez-le avec CTest**

```
cmake -B build -S .
cmake --build build
ctest --test-dir build --output-on-failure
```

## Architecture technique et principe de fonctionnement

- Gestion des appareils de test et du cycle de vie : les ressources mémoire sont gérées en toute sécurité avant et après chaque test grâce aux procédures de configuration et de démontage.
- Isolation des processus pour les tests de mort : il détecte le plantage inattendu du programme ou la génération d'assertions dans des processus enfants isolés avec le mécanisme fork.
- Modèles de test paramétrés par type : fournit une infrastructure de test paramétrée par type pour tester simultanément des classes basées sur des modèles (modèles C++) avec différents types de données.

## Cas de test et intégration de GoogleMock

- Abstraction des appels de base de données et de réseau : simulez les réponses et les latences d'API attendues sans établir de connexion réseau réelle à l'aide de MOCK_METHOD.
- Nombre d'appels et validation des paramètres : Vérifiez combien de fois une fonction est appelée, avec quels arguments et dans quel ordre avec la macro EXPECT_CALL.
- Examen des scénarios de lancement d'erreurs : assurez la durabilité en testant les blocs de code de lancement d'exceptions avec les macros EXPECT_THROW.

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite écrire des tests unitaires pour une classe d'analyseur de données à l'aide de GoogleTest et GoogleMock dans un projet C++ moderne. Pouvez-vous expliquer avec des exemples de code comment structurer mon fichier CMakeLists.txt, un exemple d'appareil de test TEST_F et comment créer un objet fictif avec MOCK_METHOD et valider les attentes d'appel ?

## Questions fréquemment posées

- Quelle est la manière la plus moderne d’inclure GoogleTest dans le projet ? Le mécanisme FetchContent est l’approche la plus recommandée dans les projets CMake modernes. Il télécharge le code source et le lie au processus de construction cible sans avoir besoin d'un gestionnaire de packages externe.
- Quelle est la principale différence entre EXPECT_* et ASSERT_* ? Lorsque les macros EXPECT_* échouent, elles enregistrent l'erreur mais permettent au reste de la fonction de s'exécuter. ASSERT_* quitte la fonction de test actuelle immédiatement en cas d'erreur.
- GoogleMock est-il une bibliothèque distincte ? GoogleMock était initialement un projet distinct, mais a longtemps été fusionné avec le référentiel GoogleTest sous un même toit ; Les deux sont installés et utilisés ensemble.
- Offre-t-il la sécurité des threads ? Oui. GoogleTest s'exécute de manière thread-safe sur les systèmes prenant en charge les pthreads et sous Windows ; Il synchronise avec précision les notifications simultanées de plusieurs threads.

## Termes liés du glossaire

- [Fork](https://trescout.com/fr/dictionary/fork/)
- [Parser](https://trescout.com/fr/dictionary/parser/)
- [CI/CD](https://trescout.com/fr/dictionary/ci-cd/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Open Source](https://trescout.com/fr/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Ingénieurs logiciels C++, développeurs de systèmes embarqués et architectes système.
- **Licence:** BSD 3-Clause (Esnek açık kaynak lisansı)
- **Toit:** Bibliothèque de tests et de simulations C++
- **Plateformes:** Linux, macOS, Windows, Android, iOS

## Liens

- [Dépôt GitHub →](https://github.com/google/googletest)
- [Lire en turc →](https://trescout.com/discover/googletest/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-27 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/googletest/
