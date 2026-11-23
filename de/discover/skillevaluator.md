# Tool zur Bewertung von KI-Agentenfähigkeiten

SkillEvaluator, entwickelt von NVIDIA, ist ein mehrschichtiges Framework zur Bewertung der Fähigkeiten von KI-Agenten durch Methoden wie Qualitätskontrolle, semantische Konflikterkennung und synthetische Datenerzeugung. Dieses Tool bietet Live-Bewertungsprozesse, um die Auswirkungen auf das Verhalten der Agenten zu messen.

- ★ 4.449
- Python
- GitHub Trending · 2026-11-16

## Aktualisierungen

- **23. November 2026:** Sterne 4,448 → 4,449, neueste Version v1.0.1 (18. November 2026).
- **23. November 2026:** Sterne 3,655 → 4,448, neueste Version v1.1.0 (23. November 2026).
- **18. November 2026:** Sterne 2,913 → 3,655, neueste Version v1.0.1 (18. November 2026).
- **17. November 2026:** Sterne 1,912 → 2,913, neueste Version v0.9.0 (13. November 2026).

## Was es bringt

- Überprüft die Qualität von KI-Agentenfähigkeiten
- Misst die Auswirkung von Agentenfähigkeiten auf Aufgabenergebnisse
- Bietet detaillierte Berichte mit einem geschichteten Framework

## Installation

**Installieren Sie das Paket**

```
pip install skillevaluator
```

## Ausführung

**Qualitätskontrolle durchführen**

```
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-quality
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die Fähigkeiten des KI-Agenten bewerten. Führe zu diesem Zweck die Installation durch, indem du im Terminal den Befehl pip install skillevaluator ausführst, und führe anschließend für einen Muster-Qualitätskontrolltest den Befehl uv run --python 3.13 skillevaluator quality-check \
src/skillevaluator/tier3/reference_skills/text-analyzer \
-r cli -r json -o reports/first-quality aus.

Repository: https://github.com/NVIDIA/SkillEvaluator. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Framework](https://trescout.com/de/dictionary/framework/)
- [Terminal](https://trescout.com/de/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es ist für Entwickler gedacht, die KI-Agenten entwickeln und die Leistungsfähigkeit der Fähigkeiten dieser Agenten testen möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/NVIDIA/SkillEvaluator)
- [Auf Türkisch lesen →](https://trescout.com/discover/skillevaluator/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-11-16 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/skillevaluator/
