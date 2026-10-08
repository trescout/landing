# Bringen Sie Fachwissen in die KI-Coding-Agenten ein

Diese Bibliothek wurde für Claude Code und verschiedene Programmieragenten entwickelt und bietet mehr als 330 Kompetenzpakete und über 70 Spezialbefehle in verschiedenen Bereichen von der Technik bis zum Marketing. Dieses Python-basierte Toolset bietet anpassbare Skripte, um KI-basierte Arbeitsabläufe zu standardisieren und die Produktivität zu steigern.

- ★ 27.840
- Python
- GitHub Trending · 2026-07-05

## Aktualisierungen

- **8. Oktober 2026:** Sterne 26,514 → 27,840, neueste Version v2.12.0 (25. August 2026).
- **27. September 2026:** Sterne 25,061 → 26,514, neueste Version v2.12.0 (25. August 2026).
- **27. August 2026:** Sterne 24,867 → 25,061, neueste Version v2.12.0 (25. August 2026).
- **24. August 2026:** Sterne 23,654 → 24,867, neueste Version v2.9.0 (28. Mai 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Aktivieren Sie die Kompetenzpakete in dieser Bibliothek für Claude Code oder den von Ihnen verwendeten Codierungsagenten. Standardisieren Sie meinen Arbeitsablauf und steigern Sie meine Produktivität mithilfe spezieller Skripte in Bereichen wie Technik, Marketing oder C-Level-Beratung. Integrieren Sie die spezifischen Funktionen, die ich benötige (z. B. Sicherheitsüberprüfung oder Produktentwicklung), in mein Projekt.

## Verwandte Begriffe aus dem Glossar

- [AI Skills](https://trescout.com/de/dictionary/ai-skills/)
- [CLI](https://trescout.com/de/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler und technische Teams, die durch künstliche Intelligenz unterstützte Codierungstools effizienter und kompetenter in ihren beruflichen Arbeitsabläufen einsetzen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/alirezarezvani/claude-skills)
- [Auf Türkisch lesen →](https://trescout.com/discover/claude-skills/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-05 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/claude-skills/
