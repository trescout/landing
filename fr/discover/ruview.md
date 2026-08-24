# Détection sans fil avec les signaux WiFi

RuView est une plateforme de détection qui utilise les informations d’état du canal WiFi (CSI) pour étudier les changements d’un environnement. Elle peut fonctionner avec du matériel ESP32 ou une carte réseau de recherche, et des données simulées sont disponibles pour une évaluation sans matériel.

- ★ 91 322
- GitHub Trending · 2026-05-30

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
- Préparez votre environnement avec la méthode Docker ou la méthode source des guides officiels.
- Sans matériel, commencez par examiner le parcours d’évaluation avec données simulées.
- Lancez la vérification déterministe par signal de référence décrite dans le guide de compilation avec `./verify`.
- Choisissez le parcours RSSI seul ou CSI complet selon votre matériel.

## Démarrage prudent

## Premier prompt
Comment évaluer un scénario simple de détection de mouvement avec des données WiFi CSI simulées ?

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


## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Dépôt GitHub officiel de RuView →
- Guide utilisateur de RuView →
- Guide de compilation de RuView →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ruview/
