# Détection sans fil avec les signaux WiFi

RuView est une plateforme de détection qui utilise les informations d’état du canal WiFi (CSI) pour étudier les changements d’un environnement. Elle peut fonctionner avec du matériel ESP32 ou une carte réseau de recherche, et des données simulées sont disponibles pour une évaluation sans matériel.

- ★ 96 773
- GitHub Trending · 2026-05-30

## Mises à jour

- **7 octobre 2026:** Étoiles 96,651 → 96,773, dernière version v3067 (6 octobre 2026).
- **6 octobre 2026:** Étoiles 96,464 → 96,651, dernière version v3060 (5 octobre 2026).
- **5 octobre 2026:** Étoiles 95,926 → 96,464, dernière version v3037 (4 octobre 2026).
- **2 octobre 2026:** Étoiles 95,751 → 95,926, dernière version v2975 (2 octobre 2026).

## Installation

**Télécharger l’image Docker**

```
docker pull ruvnet/wifi-densepose:latest
```

**Cloner le code source**

```
git clone https://github.com/ruvnet/RuView.git
```

## Exécution

**Serveur de démonstration sans matériel**

```
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
```

**Vérification déterministe**

```
./verify
```

## Que fait cet outil ?

RuView est une plateforme sous licence MIT destinée aux expériences de détection avec les informations d’état du canal WiFi. Elle peut être installée avec Docker ou depuis les sources et évaluée avec des données simulées sans matériel. Les capacités dépendent du mode matériel : la détection RSSI seule sur ordinateur portable vise une présence et des mouvements grossiers, tandis que la détection avancée exige du matériel CSI complet.

## Pour qui ?

Les chercheurs et développeurs qui souhaitent expérimenter la présence, les mouvements ou les changements d’environnement à partir de signaux WiFi.

## À quoi ne faut-il pas s’attendre ?

Les usages de suivi médical ou les attentes de détection de pose avec un ordinateur portable standard en mode RSSI seul.

## Points forts

- Propose des chemins de détection CSI avec du matériel ESP32 et des cartes réseau de recherche.
- Peut être évaluée avec des données simulées sans matériel.
- Documente une vérification déterministe par signal de référence avec `./verify`.
- Sépare les capacités du mode RSSI seul sur ordinateur portable de celles du matériel CSI complet.

## Premiers pas

1. Préparez votre environnement avec la méthode Docker ou la méthode source des guides officiels.
2. Sans matériel, commencez par examiner le parcours d’évaluation avec données simulées.
3. Lancez la vérification déterministe par signal de référence décrite dans le guide de compilation avec `./verify`.
4. Choisissez le parcours RSSI seul ou CSI complet selon votre matériel.

## Démarrage prudent

Le mode RSSI seul sur ordinateur portable vise une détection grossière de présence et de mouvement et ne fournit pas de pose. La pose et certains benchmarks sont documentés comme expérimentaux, de première génération ou limités ; évaluez les résultats selon le mode matériel utilisé.

## Premier prompt

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Comment évaluer un scénario simple de détection de mouvement avec des données WiFi CSI simulées ?

## Termes liés du glossaire

- [WiFi](https://trescout.com/fr/dictionary/wifi/)
- [Benchmark](https://trescout.com/fr/dictionary/benchmark/)

## Liens

- [Dépôt GitHub →](https://github.com/ruvnet/RuView)
- [Dépôt GitHub officiel de RuView →](https://github.com/ruvnet/RuView)
- [Guide utilisateur de RuView →](https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md)
- [Guide de compilation de RuView →](https://github.com/ruvnet/RuView/blob/main/docs/build-guide.md)
- [Lire en turc →](https://trescout.com/discover/ruview/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-05-30 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ruview/
