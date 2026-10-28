# Bereite Designregeln für Kodierungsassistenten vor

elayadesign/ai-design-skills bietet eine Sammlung von Designfähigkeiten, die aus einer Markdown-Regeldatei bestehen, welche von KI-Kodierungswerkzeugen (Claude Code, Cursor, Codex, Windsurf) gelesen werden kann. Dieses Projekt stellt eine richtungsweisende Ressource für KI-gestützte Werkzeuge dar, um Designprozesse zu standardisieren.

- ★ 9.826
- GitHub Trending · 2026-10-28

## Was es bringt

- Ermöglicht KI-Werkzeugen die Erstellung kompatibler Landingpages und visueller Systeme von Grund auf
- Fasst Designstandards wie Schriftart, Farbe, Abstand und Animation in einer einzigen Datei zusammen
- Ermöglicht Kodierungsassistenten das Schreiben konsistenterer Benutzeroberflächen mit projektspezifischen Regeln

## Installation

**Zum Claude-Code-Regelordner hinzufügen**

```
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

**Für den KI-Code-Editor Cursor installieren**

```
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte meinem KI-Coding-Tool Designregeln beibringen. Um die notwendige Regeldatei für den Code-Editor Cursor herunterzuladen, führe bitte nacheinander diese Befehle aus: `mkdir -p .cursor/rules` und anschließend `curl -o .cursor/rules/\<skill-name>.md \
https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/\<skill-name>/SKILL.md`. Vergiss nicht, den Platzhalter `\<skill-name>` hierbei durch die Regel zu ersetzen, die wir herunterladen möchten, nämlich `landing-page-design`.

Repository: https://github.com/elayadesign/ai-design-skills. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Markdown](https://trescout.com/de/dictionary/markdown/)
- [Skill](https://trescout.com/de/dictionary/skill/)
- [AI Skills](https://trescout.com/de/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es ist für Produktbesitzer und Entwickler gedacht, die mit KI-gestützten Code-Editoren ästhetische und konsistente Web-Oberflächen entwickeln möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/elayadesign/ai-design-skills)
- [Auf Türkisch lesen →](https://trescout.com/discover/ai-design-skills/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-10-28 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ai-design-skills/
