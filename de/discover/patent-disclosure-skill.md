# Automatisieren Sie die Offenlegung von Patenterfindungen mit KI

Der auf Python basierende Patent Disclosure Skill analysiert technische Erfindungsentwürfe und erstellt technische Beschreibungen, Ansprüche und Vergleiche des Standes der Technik gemäß dem offiziellen Patentformat.

- ★ 10.360
- Python
- GitHub Trending · 2026-08-31

## Was es bringt
- Strukturierte Patenttexterstellung: Erstellung der Abschnitte „Technisches Feld“, „Hintergrund“, „Zusammenfassung“ und „Detaillierte Beschreibung“ der Erfindung gemäß den Standardpatentnormen.
- Unabhängiger und abhängiger Anspruchsbaum: Automatische Erstellung hierarchischer Patentanspruchslisten, die den Umfang des Rechtsschutzes maximieren.
- Analyse der Unterschiede im Stand der Technik: Deutliche Hervorhebung der technischen Unterschiede und des Innovationsstadiums zwischen bestehenden Technologien und der Erfindung.
- Beschleunigte Zusammenarbeit mit Patentanwälten: Kosten- und Zeiteinsparungen durch Umwandlung von Ingenieurentwürfen in optimierte technische Dokumente, die für Patentanwälte bereitstehen.
- Unterstützung mehrsprachiger Patentterminologie: Kompatibilität mit der Terminologie englischer, türkischer und internationaler Patentinstitutionen (WIPO, EPA, USPTO).

## Installation
**Klonen des Repositorys und Installieren von Abhängigkeiten**

```
git clone https://github.com/handsomestWei/patent-disclosure-skill.git
cd patent-disclosure-skill
pip install -r requirements.txt
```


## Ausführung
**Einleitung der Patentanalyse und Offenlegungserstellung**

```
python run_skill.py --input bulus_taslagi.txt --output patent_disclosure.md
```


## Technische Architektur und Funktionsweise
- Technical Discovery Parsing Engine: Erkennt wichtige Eingaben, Ausgaben und Methoden in Software-, Hardware- oder chemischen Prozessbeschreibungen.
- Claim Syntax Verifier: Juristischer Sprachanalysator, der in Ansprüchen nach vagen Ausdrücken und formalen Fehlern sucht.
- Vorlagen- und Markdown-Export: Speichern des Dokuments im standardmäßigen segmentierten Markdown-Format zur Verwendung in formellen Patentanmeldungen.

## Arbeitsabläufe zur Patentanalyse und Anspruchsvorbereitung
- Übersetzen von Softwarealgorithmen in patentierbare Form: Ableiten von für Patentbehörden akzeptablen Methoden- und Systembeschreibungen aus Code- und Architekturdiagrammen.
- Verteidigung gegen Amtsklagen: Erstellung von Antwortentwürfen mit Auflistung der Unterscheidungsmerkmale der Erfindung gegen Einwände von Patentprüfern.
- Prüfung des Portfolios an geistigem Eigentum: Frühzeitige Kartierung patentfähiger Erfindungsschritte unternehmensinterner Technologieprojekte.

## Wenn Sie nicht programmieren
Ich möchte einen formellen Text zur Offenlegung einer Erfindung unter Verwendung der Fähigkeiten zur Patentoffenlegung für einen von mir entwickelten verteilten Datenbank-Caching-Algorithmus vorbereiten. Können Sie den Ablauf des Algorithmus als Eingabe angeben und Schritt für Schritt erklären, wie unabhängige Ansprüche generiert werden, das technische Gebiet der Erfindung und die Unterschiede zum Stand der Technik?

## Häufig gestellte Fragen
- Ersetzt dieses Tool einen formellen Patentanwalt? Nein. Patent Disclosure Skill ist ein Vorbereitungs- und Produktivitätstool, das Ingenieuren hilft, Erfindungsentwürfe zu organisieren und sie für Anwälte vorzubereiten; Rechtsanträge müssen über einen Anwalt gestellt werden.
- Mit welchen LLM-Modellen funktioniert es? Claude 3.5 Sonnet kann für die Arbeit mit GPT-4o oder nativen Open-Heavy-Modellen (Qwen, Llama 3) konfiguriert werden.
- Werden meine vertraulichen technischen Geheimnisse ins Internet gelangen? Bei der Ausführung mit einem lokalen LLM (Ollama oder vLLM) erfolgt die gesamte Patentanalyse vollständig auf Ihrem lokalen Computer, es gehen keine Daten verloren.
- Kann er/sie Patentzeichnungen und Flussdiagramme interpretieren? Wenn multimodale Modelle verbunden werden, können Systemarchitektur- und Blockdiagrammvisualisierungen analysiert und transkribiert werden.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/patent-disclosure-skill/
