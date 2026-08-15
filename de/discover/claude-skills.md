# Bringen Sie Fachwissen in die KI-Coding-Agenten ein

Diese Bibliothek wurde für Claude Code und verschiedene Programmieragenten entwickelt und bietet mehr als 330 Kompetenzpakete und über 70 Spezialbefehle in verschiedenen Bereichen von der Technik bis zum Marketing. Dieses Python-basierte Toolset bietet anpassbare Skripte, um KI-basierte Arbeitsabläufe zu standardisieren und die Produktivität zu steigern.

- ★ 23.654
- Python
- GitHub Trending · 2026-07-05

## Was es bringt
- Mehr als 350 vorgefertigte Skill-Pakete
- Breites Fachwissen vom Engineering bis zum Marketing
- Kompatibel mit 13 verschiedenen Codierungstools

## Installation
**Gemini-CLI-Installation**

```
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

**OpenClaw-Installation**

```
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```


## Ausführung
**Konvertieren Sie Funktionen für den Cursor**

```
# 1. Convert all skills to all tools (takes ~15 seconds)
./scripts/convert.sh --tool all

# 2. Install into your project (with confirmation)
./scripts/install.sh --tool cursor --target /path/to/project

# Or use --force to skip confirmation:
./scripts/install.sh --tool aider --target . --force

# 3. Verify
find .cursor/rules -name "*.mdc" | wc -l  # Should show 346
```


## Wenn Sie nicht programmieren
Aktivieren Sie die Kompetenzpakete in dieser Bibliothek für Claude Code oder den von Ihnen verwendeten Codierungsagenten. Standardisieren Sie meinen Arbeitsablauf und steigern Sie meine Produktivität mithilfe spezieller Skripte in Bereichen wie Technik, Marketing oder C-Level-Beratung. Integrieren Sie die spezifischen Funktionen, die ich benötige (z. B. Sicherheitsüberprüfung oder Produktentwicklung), in mein Projekt.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/claude-skills/
