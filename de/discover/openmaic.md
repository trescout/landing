# Interaktive Klassenzimmersimulation mit mehreren KI-Agenten

OpenMAIC, entwickelt von Forschern der Tsinghua-Universität, vereint mehrere Agenten der künstlichen Intelligenz in den Rollen von Lehrern, Schülern und Beobachtern in einer interaktiven Klassenzimmerumgebung.

- ★ 41.041
- TypeScript
- GitHub Trending · 2026-08-31

## Aktualisierungen

- **19. Oktober 2026:** Sterne 40,871 → 41,041, neueste Version v1.2.1 (18. Oktober 2026).
- **16. Oktober 2026:** Sterne 40,363 → 40,871, neueste Version v1.2.0 (16. Oktober 2026).
- **11. Oktober 2026:** Sterne 39,969 → 40,363, neueste Version v1.1.4 (11. Oktober 2026).
- **5. Oktober 2026:** Sterne 39,351 → 39,969, neueste Version v1.1.3 (5. Oktober 2026).

## Was es bringt

- Rollenbasierte Multi-Agenten-Architektur: Dynamische Interaktion von LLM-Agenten in den Rollen Lehrer, Schülerfragesteller, Diskussionsteilnehmer und Zusammenfassender.
- Visuelle und akustische Klassenzimmerschnittstelle: Immersive pädagogische Erfahrung mit virtuellem Whiteboard, sofortigem Q&A-Flow und Sprachsynthese (TTS).
- Anpassbarer Kursplan: Erstellen Sie sofort interaktive Kurse, indem Sie Ihre eigenen PDF-Dokumente oder Textvorlesungsnotizen hochladen.
- Simulationsstart mit einem Klick: Verwalten Sie die komplexe Agenten-Orchestrierung über eine moderne Weboberfläche, ohne technische Programmierkenntnisse zu benötigen.
- Kompatibilität mit offenen gewichteten Modellen: Freiheit, jedes KI-Modell über Ollama-, vLLM- oder Cloud-LLM-Anbieter zu verbinden.

## Installation

**Klonen des Repositorys und Installieren von Abhängigkeiten**

```
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```

## Ausführung

**Starten des Entwicklungsservers**

```
pnpm run dev
# Tarayıcıda http://localhost:3000 adresini açın
```

## Technische Architektur und Funktionsweise

- Conversation Orchestration Engine: Der zentrale Controller, der verwaltet, welcher Agent wann spricht, die Reihenfolge des Sprechens und den Kontext der Diskussion.
- Gedächtnis- und Kontextmanagement: Speichern allgemeiner Tafelinhalte und Schülerfragen, die während der Unterrichtsstunde geteilt werden, im Kurz-/Langzeitgedächtnis.
- Echtzeit-Broadcast über WebSocket: Gesprochene Texte, emotionale Ausdrücke und Animationen ohne Verzögerung an die Frontend-Oberfläche übertragen.

## Dynamik und Rollensimulationen mehrerer Agentenklassen

- Sokratische Diskussionsumgebungen: Agenten mit unterschiedlichen Perspektiven diskutieren ein Thema und regen beim Benutzer kritisches Denken an.
- Personalisierte Tutorunterstützung: Dedizierte KI-Tutoren, die den Schwierigkeitsgrad automatisch an die Verständnisgeschwindigkeit des Benutzers anpassen.
- Studien zur interagenten sozialen Interaktion: Analysieren, wie große Sprachmodelle in Umgebungen großer Gruppen zusammenarbeiten und Informationen austauschen.

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte eine sokratische Diskussionsumgebung simulieren, indem ich meine eigenen Vorlesungsnotizen auf die OpenMAIC-Plattform hochlade. Können Sie Schritt für Schritt erklären, wie die Rollen der Agenten (Lehrer, neugieriger Schüler, kritischer Fragesteller) definiert werden und wie diese Klasse mit einem lokalen Ollama-Modell gefördert wird?

Repository: https://github.com/THU-MAIC/OpenMAIC. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Häufig gestellte Fragen

- Ist für die Verwendung von OpenMAIC eine GPU erforderlich? Wenn Sie Ihr eigenes natives Modell (Ollama/vLLM) ausführen möchten, wird eine GPU empfohlen. kann aber über Cloud-APIs (OpenAI, Gemini, Groq) direkt mit einem Standardcomputer genutzt werden.
- Kann der Benutzer per Stimme an der Simulation teilnehmen? Ja. Dank WebRTC und Spracherkennungsmodul kann der Benutzer an Unterrichtsdiskussionen teilnehmen, indem er mit seinem Mikrofon spricht.
- Wie viele Agenten können gleichzeitig im Klassenzimmer sein? Die Standardkonfiguration bietet eine ideale Interaktion zwischen 3 und 8 Agenten; Überfülltere Klassen können je nach Systemressourcen gestaltet werden.
- In welchen Formaten können Kursinhalte hochgeladen werden? Klartext-, Markdown- und PDF-Dokumente können direkt in die Wissensdatenbank des Systems importiert werden.

## Verwandte Begriffe aus dem Glossar

- [Markdown](https://trescout.com/de/dictionary/markdown/)
- [GPU](https://trescout.com/de/dictionary/gpu/)
- [PDF](https://trescout.com/de/dictionary/pdf/)
- [LLM](https://trescout.com/de/dictionary/llm/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [API](https://trescout.com/de/dictionary/api/)

- **Für wen es gedacht ist:** Pädagogen, KI-Forscher, Edtech-Unternehmer und Studenten.
- **Lizenz:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** TypeScript und Next.js Multi-Agent-Simulator
- **Plattformen:** Webbrowser, Linux, macOS, Windows

## Links

- [GitHub-Repository →](https://github.com/THU-MAIC/OpenMAIC)
- [Auf Türkisch lesen →](https://trescout.com/discover/openmaic/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-31 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openmaic/
