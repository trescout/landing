# Système d'information local pour Claude Code

Crée une base Obsidian locale référencée à partir de documents sources et applique les modifications approuvées via des opérations réversibles.

- ★ 14 822
- Python
- GitHub Trending · 2026-08-25

## Mises à jour

- **11 septembre 2026:** Étoiles 14,727 → 14,822, dernière version v2.2.0 (10 septembre 2026).
- **8 septembre 2026:** Étoiles 13,706 → 14,727, dernière version v2.1.1 (25 août 2026).
- **27 août 2026:** Étoiles 12,404 → 13,706, dernière version v2.1.1 (25 août 2026).

## Installation

**Ajouter le marketplace Claude Code**

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
```

**Installer le plugin claude-obsidian**

```
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

**Générer le plan pour un vault distinct**

```
python3 scripts/claude-obsidian.py init <new-vault> --generated-at <ISO-UTC> --operation-id init-reviewed
```

## Exécution

**Vérifier l'installation du plugin**

```
claude plugin list
```

**Démarrer le flux wiki**

```
/claude-obsidian:wiki
```

## Que fait cet outil ?

Organise le contenu de recherche avec registres de sources et d'affirmations, pages liées et cartes de connaissances. Des agents parallèles produisent des ébauches, et un orchestrateur applique les modifications approuvées via une opération réversible.

## Pour qui ?

Ceux qui souhaitent créer une base de connaissances Obsidian locale et sourcée pour Claude Code.

## À quoi ne faut-il pas s’attendre ?

Ne remplace pas l'enregistrement automatique des transcriptions, la synchronisation cloud, une garantie d'exactitude ni les sauvegardes et le contrôle de version.

## Points forts

- Fonctionnement local par défaut et approche explicite de sortie réseau
- Pages liées et sourcées avec registres de sources et d'affirmations
- Application des modifications approuvées via des opérations réversibles

## Premiers pas

1. Clonez le dépôt et préparez un environnement Python 3.11 ou supérieur
2. Générez un plan initial pour un vault distinct et examinez le fichier JSON du plan
3. Vérifiez la valeur approved_plan_sha256 et approuvez l'opération complète
4. Ouvrez le vault dans Obsidian et exécutez Claude Code avec le plugin local
5. Démarrez le flux wiki et utilisez les étapes d'ajout de source, d'interrogation et d'enregistrement explicite

## Démarrage prudent

Ce système n'est pas une source d'exactitude garantie. Utilisez des sauvegardes et le contrôle de version pour vos données; vérifiez les sorties réseau et le plan appliqué.

## Premier prompt

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Démarrez un flux wiki Obsidian local en liant les sources aux registres de sources et d'affirmations.

## Termes liés du glossaire

- [Agent Skills](https://trescout.com/fr/dictionary/agent-skills/)
- [AI Skills](https://trescout.com/fr/dictionary/ai-skills/)
- [Agent](https://trescout.com/fr/dictionary/agent/)

## Liens

- [Dépôt GitHub →](https://github.com/AgriciDaniel/claude-obsidian)
- [Guide d’installation →](https://github.com/AgriciDaniel/claude-obsidian/blob/main/docs/install-guide.md)
- [README officiel →](https://github.com/AgriciDaniel/claude-obsidian)
- [Lire en turc →](https://trescout.com/discover/claude-obsidian/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-25 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/claude-obsidian/
