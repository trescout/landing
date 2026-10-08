# Navigateur furtif pour agents d'intelligence artificielle

Camofox est un navigateur furtif (stealth headless browser) qui permet aux agents d'intelligence artificielle de contourner les systèmes de détection de bots et les blocages de web scraping. Il fonctionne directement avec les outils d'automatisation de navigateur Puppeteer et Playwright, offrant une alternative à ces bibliothèques.

- ★ 11 460
- JavaScript
- GitHub Trending · 2026-09-08

## Mises à jour

- **7 octobre 2026:** Étoiles 11,433 → 11,460, dernière version camoufox-backup-404310733 (7 octobre 2026).
- **5 octobre 2026:** Étoiles 11,411 → 11,433, dernière version v1.18.1 (5 octobre 2026).
- **4 octobre 2026:** Étoiles 11,292 → 11,411, dernière version camoufox-backup-402708180 (4 octobre 2026).
- **1 octobre 2026:** Étoiles 11,228 → 11,292, dernière version v1.18.0 (30 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Tu es un gestionnaire de navigateur web. Accède aux sites web cibles en utilisant Camofox-browser. Utilise ce navigateur, dissimulé au niveau C++, pour éviter d'être détecté comme un bot. Lors de l'extraction de données à partir de pages web, privilégie les instantanés d'accessibilité (accessibility snapshots), plus légers que le HTML brut. Utilise des identifiants stables pour les éléments avec lesquels tu dois interagir et gère les sessions en les isolant par utilisateur.

## Termes liés du glossaire

- [Stealth Headless Browser](https://trescout.com/fr/dictionary/stealth-headless-browser/)
- [Headless Browser](https://trescout.com/fr/dictionary/headless-browser/)
- [Web Scraping](https://trescout.com/fr/dictionary/web-scraping/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux développeurs qui créent des agents d'intelligence artificielle devant extraire des données de sites web ou effectuer des opérations sur Internet.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/jo-inc/camofox-browser)
- [Lire en turc →](https://trescout.com/discover/camofox-browser/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-08 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/camofox-browser/
