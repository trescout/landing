# Ein KI-Tool zum automatischen Verfassen wissenschaftlicher Arbeiten

PaperOrchestra, entwickelt von Google Research, ist ein Multi-Agenten-Framework, das rohe Ideen und Experimentierprotokolle in akademische LaTeX-Entwürfe im Format umwandelt. Die Software unterstützt das Schreiben von Forschungsarbeiten, indem sie Prozesse wie Literaturrecherchen und die Erstellung von Visualisierungen automatisiert.

- ★ 5.197
- Python
- GitHub Trending · 2026-11-17

## Aktualisierungen

- **20. November 2026:** Sterne 4,162 → 5,197.
- **18. November 2026:** Sterne 1,732 → 4,162.

## Was es bringt

- Wandelt rohe Ideen in ein akademisches Format um
- Führt automatische Literaturrecherchen durch
- Erstellt die erforderlichen Abbildungen und Grafiken

## Installation

**Einrichten der erforderlichen Umgebung**

```
conda create -n paper_orchestra python=3.11
    conda activate paper_orchestra
    pip install -r requirements.txt
```

## Ausführung

**Ausführen mit Skript**

```
./paper_writing_cli.sh
```

**Ausführen über die Befehlszeile**

```
python paper_writing_cli.py \
  --raw_materials_dir /path_to_your_raw_materials/ \
  --latex_template_dir /path_to_your_latex_template/ \
  --output_dir /path_to_your_output_folder/ \
  --use_plotting true
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte meine Forschungsideen und Versuchsprotokolle in den Entwurf eines akademischen Artikels umwandeln. Installiere dafür zunächst die erforderlichen Abhängigkeiten, indem du den Befehl conda create -n paper_orchestra python=3.11
conda activate paper_orchestra
pip install -r requirements.txt ausführst. Verwende anschließend den Befehl ./paper_writing_cli.sh, um den Artikel-Schreibprozess zu starten.

Repository: https://github.com/google-research/paper-orchestra. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Multi-Agent Framework](https://trescout.com/de/dictionary/multi-agent-framework/)
- [Multi-agent](https://trescout.com/de/dictionary/multi-agent/)
- [Framework](https://trescout.com/de/dictionary/framework/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es ist für Forscher gedacht, die akademische Entwürfe erstellen möchten, indem sie den Prozess des Schreibens von Forschungsartikeln automatisieren.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/google-research/paper-orchestra)
- [Auf Türkisch lesen →](https://trescout.com/discover/paper-orchestra/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-11-17 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/paper-orchestra/
