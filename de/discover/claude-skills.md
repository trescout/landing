# Bringen Sie Fachwissen in die KI-Coding-Agenten ein

Diese Bibliothek wurde für Claude Code und verschiedene Programmieragenten entwickelt und bietet mehr als 330 Kompetenzpakete und über 70 Spezialbefehle in verschiedenen Bereichen von der Technik bis zum Marketing. Dieses Python-basierte Toolset bietet anpassbare Skripte, um KI-basierte Arbeitsabläufe zu standardisieren und die Produktivität zu steigern.

- ★ 28.939
- Python
- GitHub Trending · 2026-07-05

## Aktualisierungen

- **29. Oktober 2026:** Sterne 28,795 → 28,939, neueste Version v2.14.3 (29. Oktober 2026).
- **27. Oktober 2026:** Sterne 28,584 → 28,795, neueste Version v2.14.2 (26. Oktober 2026).
- **23. Oktober 2026:** Sterne 28,525 → 28,584, neueste Version v2.14.1 (23. Oktober 2026).
- **22. Oktober 2026:** Sterne 28,485 → 28,525, neueste Version v2.14.0 (21. Oktober 2026).

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Aktivieren Sie die Kompetenzpakete in dieser Bibliothek für Claude Code oder den von Ihnen verwendeten Codierungsagenten. Standardisieren Sie meinen Arbeitsablauf und steigern Sie meine Produktivität mithilfe spezieller Skripte in Bereichen wie Technik, Marketing oder C-Level-Beratung. Integrieren Sie die spezifischen Funktionen, die ich benötige (z. B. Sicherheitsüberprüfung oder Produktentwicklung), in mein Projekt.

Repository: https://github.com/alirezarezvani/claude-skills. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [AI Skills](https://trescout.com/de/dictionary/ai-skills/)
- [CLI](https://trescout.com/de/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler und technische Teams, die durch künstliche Intelligenz unterstützte Codierungstools effizienter und kompetenter in ihren beruflichen Arbeitsabläufen einsetzen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/alirezarezvani/claude-skills)
- [Auf Türkisch lesen →](https://trescout.com/discover/claude-skills/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-05 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/claude-skills/
