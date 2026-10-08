# Analyse utilisateur OSINT sur plus de 465 plateformes

User-Scanner, basé sur Python, effectue une recherche de renseignement en sources ouvertes (OSINT) sur plus de 465 réseaux sociaux, forums et dépôts de code à partir d'un seul nom d'utilisateur ou d'une adresse e-mail.

- ★ 5 007
- Python
- GitHub Trending · 2026-08-31

## Mises à jour

- **27 septembre 2026:** Étoiles 3,910 → 5,007, dernière version v1.5.2 (17 septembre 2026).

## Ce que ça vous apporte

- Couverture étendue des plateformes : vérification de la présence de comptes sur GitHub, Reddit, Twitter, Steam, Telegram et plus de 465 autres sites en une seule fois.
- Scan asynchrone haute vitesse : interrogation parallèle de centaines de cibles en quelques secondes grâce à une architecture basée sur asyncio et aiohttp.
- Filtrage des faux positifs : mécanisme de détection intelligent qui vérifie les codes d'état HTTP ainsi que les messages d'erreur dans le corps de la réponse.
- Exportation de rapports JSON et CSV : enregistrement des résultats d'analyse dans des formats structurés destinés à être utilisés dans des rapports de criminalistique numérique et de sécurité.
- Confidentialité et exécution locale : possibilité d'exécuter entièrement sur la machine locale sans envoyer aucune requête à des serveurs tiers.

## Installation

**Clonage du référentiel et installation des dépendances**

```
git clone https://github.com/kaifcodec/user-scanner.git
cd user-scanner
pip install -r requirements.txt
```

## Exécution

**Scan du nom d'utilisateur et de l'e-mail cibles**

```
python3 user_scanner.py -u hedef_kullanici
# veya e-posta ile:
python3 user_scanner.py -e hedef@ornek.com
```

## Architecture technique et principe de fonctionnement

- Modèles de base de données (manifestes de site JSON) : configuration modulaire contenant les modèles d'URL, les codes d'erreur et les regex de profil de plus de 465 plateformes.
- Pool de connexions simultanées : Utilisation optimale de la bande passante réseau par la mise en cache des résolutions DNS et des sockets TCP.
- En-têtes HTTP personnalisés et rotation d'User-Agent : simulation d'en-têtes de navigateur réalistes pour éviter les blocages WAF et les limitations de débit (rate limit).

## Scénarios de recherche OSINT et analyse de données

- Violation de données personnelles et suivi : cartographiez les réseaux sociaux sur lesquels les profils ayant fuité sont actifs grâce à la corrélation de noms d'utilisateur.
- Audits de sécurité d'entreprise : Déterminez si les employés de l'entreprise ouvrent des comptes sur des plateformes externes avec leurs adresses e-mail professionnelles.
- Défense contre l'ingénierie sociale : identifiez précocement les comptes d'usurpation non autorisés face aux attaques de hameçonnage ciblé (spear phishing).

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Pourriez-vous expliquer étape par étape comment je peux effectuer une analyse sur plus de 465 plateformes via un seul nom d'utilisateur en utilisant l'outil User-Scanner lors d'un audit de sécurité, exporter les résultats obtenus au format JSON et lister les profils suspects ?

## Questions fréquemment posées

- Est-il légal d'utiliser User-Scanner ? Oui. User-Scanner interroge uniquement l'existence de comptes sur des pages web publiques accessibles à tous ; il n'accède à aucun système non autorisé et ne pirate aucun mot de passe.
- Est-ce qu'il y a un support pour Tor ou proxy ? Oui. Vous pouvez masquer votre adresse IP et contourner les limitations de vitesse en acheminant les requêtes via des chaînes de proxy SOCKS5 ou HTTP.
- Combien de temps faut-il pour obtenir les résultats ? Grâce à son architecture asynchrone, l'analyse de plus de 465 plateformes prend généralement entre 20 et 45 secondes, selon votre connexion internet.
- Comment fonctionne la recherche par e-mail ? En mode e-mail, les signaux de vérification publics présents sur les points de terminaison de réinitialisation de mot de passe ou d'enregistrement de compte des services pris en charge sont examinés.

## Termes liés du glossaire

- [OSINT](https://trescout.com/fr/dictionary/osint/)
- [Proxy](https://trescout.com/fr/dictionary/proxy/)
- [Open Source](https://trescout.com/fr/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Chercheurs en cybersécurité, analystes OSINT, experts en informatique légale et hackers éthiques.
- **Licence:** GPL-3.0 (Açık kaynak copyleft lisansı)
- **Toit:** Scanner OSINT asynchrone en Python
- **Plateformes:** Linux, macOS, Windows

## Liens

- [Dépôt GitHub →](https://github.com/kaifcodec/user-scanner)
- [Lire en turc →](https://trescout.com/discover/user-scanner/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-31 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/user-scanner/
