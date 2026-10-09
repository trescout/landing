# Qu'est-ce que MCP ?

*Glossaire · AI · Dernière mise à jour : 22 septembre 2026*

> Model Context Protocol

MCP (Model Context Protocol) est un protocole ouvert qui permet aux applications d'intelligence artificielle de se connecter de manière standard à des données et des outils externes.

## Définition et origine du mot

Au lieu d'écrire des connexions distinctes pour chaque application, une seule norme est utilisée. Le protocole est un standard ouvert développé pour augmenter l’interopérabilité de l’écosystème de l’IA. L’analogie avec la prise est pertinente : tout comme chaque appareil fonctionne avec la même prise, différentes sources de données se connectent à l’IA de la même manière.

***Analogie :** C'est comme une norme de prise ; Il permet de connecter facilement différentes sources de données à l’intelligence artificielle, tout comme chaque appareil fonctionne avec la même prise.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Assistants :** L'application d'intelligence artificielle lit votre calendrier et vos fichiers.
**Développement:** Lier l'éditeur de code au référentiel et à la documentation.
**Rapports :** Extraction récapitulative de la base de données en direct.

## Profondeur technique et architecture

L'architecture se compose de trois parties :

**Shoo :** Application d'IA (par exemple, assistant de bureau ou éditeur).
**Client:** Gestionnaire de connexions au sein de l'hôte.
**Serveur:** Petit programme qui présente des données ou un outil (système de fichiers, base de données, GitHub).

Les serveurs offrent trois fonctionnalités :

**Outil:** Fonction que le modèle peut appeler (recherche de fichiers, exécution de requêtes).
**Ressource:** Données (document, schéma) que le modèle peut lire.
**Rapide:** Modèle de tâche prêt.

Un paramètre client typique est le suivant :

```
{
  "mcpServers": {
    "dosya": {
      "command": "npx",
      "args": ["-y", "ornek-mcp-dosya"]
    }
  }
}
```

Règle de sécurité : Le serveur accède uniquement aux dossiers et processus autorisés. Chaque demande du modèle doit pouvoir passer l’approbation de l’utilisateur.

## Choses fréquemment mélangées

Peut être mélangé avec l'API. L'API est une porte unique, tandis que MCP est l'ensemble de règles qui garantit que les données passant par cette porte sont prononcées dans un langage standard. L'API est spécifique au serveur, MCP est commun à tous les serveurs.

## Utilisation dans différentes disciplines

**Électrique:** La norme de prise à laquelle chaque appareil est conforme.
**Chemin de fer:** Crochet standard pour relier les wagons.
**Langue:** Langage protocolaire commun utilisé en diplomatie.

## Foire aux questions

**Pourquoi le MCP est-il nécessaire ?**

Au lieu d'écrire un lien distinct pour chaque application, la méthode standard est suivie. Cela simplifie la sécurité et la maintenance.

**MCP est-il open source ?**

Oui. Il s'agit d'un standard ouvert, différentes applications peuvent écrire leurs propres clients et serveurs.

**Pourquoi utiliser MCP au lieu de l'API ?**

L'API est spécifique au serveur, chacune est apprise séparément. MCP propose un langage commun, le modèle se connecte au nouveau serveur prêt.

**Est-ce sécuritaire?**

Sa conception est basée sur les autorisations, mais vous devez garder la portée d'accès du serveur étroite et exiger une approbation pour les écritures.

## Termes liés

- [API](https://trescout.com/fr/dictionary/api/)
- [Data Pipeline](https://trescout.com/fr/dictionary/data-pipeline/)
- [AI Agent](https://trescout.com/fr/dictionary/ai-agent/)

## Outils liés

- [Langflow](https://trescout.com/fr/discover/langflow/)
- [Servers](https://trescout.com/fr/discover/servers/)
- [OpenCut](https://trescout.com/fr/discover/opencut/)
- [AI Engineering from Scratch](https://trescout.com/fr/discover/ai-engineering-from-scratch/)
- [Goose](https://trescout.com/fr/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/fr/discover/chrome-devtools-mcp/)
- [Codebase Memory MCP](https://trescout.com/fr/discover/codebase-memory-mcp/)
- [REA](https://trescout.com/fr/discover/rea/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/mcp/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/mcp/
