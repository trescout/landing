# Navigateur furtif pour agents d'intelligence artificielle

Camofox est un navigateur furtif (stealth headless browser) qui permet aux agents d'intelligence artificielle de contourner les systèmes de détection de bots et les blocages de web scraping. Il fonctionne directement avec les outils d'automatisation de navigateur Puppeteer et Playwright, offrant une alternative à ces bibliothèques.

- ★ 10 915
- JavaScript
- GitHub Trending · 2026-09-08

## Ce que ça vous apporte
- Contourne les systèmes de détection de bots et les blocages de web scraping au niveau C++.
- Consomme 90 % de données en moins par rapport au HTML standard grâce aux instantanés d'accessibilité.
- Assure une gestion des cookies et du stockage basée sur l'utilisateur grâce à l'isolation des sessions.

## Installation
**Fonctionnement direct**

```
npx @askjo/camofox-browser
```

**Installation à partir du code source**

```
git clone https://github.com/jo-inc/camofox-browser
cd camofox-browser
npm install
npm start  # downloads Camoufox on first run (~300MB)
```


## Exécution
**Démarrage du serveur local**

```
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# -> http://localhost:9377
```


## Si vous ne codez pas
Tu es un gestionnaire de navigateur web. Accède aux sites web cibles en utilisant Camofox-browser. Utilise ce navigateur, dissimulé au niveau C++, pour éviter d'être détecté comme un bot. Lors de l'extraction de données à partir de pages web, privilégie les instantanés d'accessibilité (accessibility snapshots), plus légers que le HTML brut. Utilise des identifiants stables pour les éléments avec lesquels tu dois interagir et gère les sessions en les isolant par utilisateur.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/camofox-browser/
