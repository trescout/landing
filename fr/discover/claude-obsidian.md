# Système d'information local pour Claude Code

Crée une base Obsidian locale référencée à partir de documents sources et applique les modifications approuvées via des opérations réversibles.

- ★ 13 706
- Python
- GitHub Trending · 2026-08-25

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
- Clonez le dépôt et préparez un environnement Python 3.11 ou supérieur
- Générez un plan initial pour un vault distinct et examinez le fichier JSON du plan
- Vérifiez la valeur approved_plan_sha256 et approuvez l'opération complète
- Ouvrez le vault dans Obsidian et exécutez Claude Code avec le plugin local
- Démarrez le flux wiki et utilisez les étapes d'ajout de source, d'interrogation et d'enregistrement explicite

## Démarrage prudent

## Premier prompt
Démarrez un flux wiki Obsidian local en liant les sources aux registres de sources et d'affirmations.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Guide d’installation →
- README officiel →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/claude-obsidian/
