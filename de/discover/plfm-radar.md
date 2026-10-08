# Open-Source-Phased-Array-Radar

PLFM RADAR ist ein Open-Source-Phased-Array-Radarsystem, das bei 10,5 GHz (X-Band) mit elektronischer Strahllenkung und FPGA-basierten digitalen Signalverarbeitungsfunktionen arbeitet. Es erkennt und verfolgt Luft- und Bodenziele mit hoher Präzision, ohne mechanisch bewegliche Teile zu verwenden.

- ★ 26.713
- C++
- GitHub Trending · 2026-08-18

## Aktualisierungen

- **6. Oktober 2026:** Sterne 25,440 → 26,713, neueste Version v2.0.2-p0-audit (20. April 2026).
- **27. September 2026:** Sterne 24,168 → 25,440, neueste Version v2.0.2-p0-audit (20. April 2026).
- **18. August 2026:** Sterne 24,163 → 24,168, neueste Version v2.0.2-p0-audit (20. April 2026).

## Was es bringt

- Elektronische Strahllenkung: Scannen eines 90-Grad-Sektors mit Phasenschiebern in Millisekunden, ohne dass ein mechanischer Motor oder eine Drehantenne erforderlich sind.
- Dual-Range-Betriebsmodus: 3 km im Nahbereich (UAV/Drohnenerkennung), 20 km im Fernbereich (Perimeterüberwachung und Flugzeugverfolgung).
- FPGA-basierte Echtzeit-Signalverarbeitung: Hardware-Verarbeitung von Rohradarechos auf FPGA mit Hochgeschwindigkeits-FFT- und CFAR-Algorithmen.
- Kostengünstige, zugängliche Hardware: Senkung der Kosten für kommerzielle und militärische Radare von Hunderttausenden Dollar auf weniger als tausend Dollar mit Open-Source-PCB-Designs.
- Python- und SDR-Integration: Live-Überwachung digitaler Radardaten über Open-Source-SDR-Hardware und Python-Schnittstelle.

## Hardwarekomponenten und Radararchitektur

- 10,5-GHz-X-Band-Mikrostreifenantennenarray: Multi-Patch-Antennenelemente, die auf verlustarmen Rogers/FR4-Schichten entwickelt wurden.
- Numerisch gesteuerte Phasenschieber: HF-ICs, die den Strahl im Raum lenken, indem sie die Signalphase jedes Antennenelements mit einer Präzision von 5,6 Grad verzögern.
- FMCW-Frequenzsynthesizer: Hochstabiler lokaler Oszillator (VCO/PLL), der eine kontinuierliche Welle mit linearer Frequenzmodulation erzeugt.

## Signalverarbeitungs- und Steuerungssoftware

- Entfernungs-Doppler-FFT (2D-FFT): Gleichzeitige Berechnung der Entfernung und der Radialgeschwindigkeit des Ziels, indem zuerst die Entfernung und dann die Doppler-FFT auf das eingehende Signal angewendet werden.
- CFAR-Detektor (Constant False Alarm Rate): Trennung realer beweglicher Ziele von Hintergrundgeräuschen und Bodenechos (Clutter) mit dynamischer Schwellenwertbestimmung.
- Python-GUI und PPI-Bildschirm: Visualisierung von Zielspuren auf einer Live-Karte auf einem herkömmlichen kreisförmigen Radarbildschirm (PPI).

## Technisches Funktionsprinzip: FMCW und Phased Array

- Entfernungsmessung aus Frequenzdifferenz: Die Schwebungsfrequenz wird durch Mischen des gesendeten Chirp-Signals mit dem vom Ziel zurückgegebenen Signal ermittelt. Diese Frequenz ist direkt proportional zur Entfernung.
- Strahlfokussierung mit konstruktiver Interferenz: Indem jedem Antennenelement im Array eine bestimmte Phasenverzögerung zugewiesen wird, wird das Signal in der gewünschten Richtung mit konstruktiver Interferenz und in anderen Richtungen mit destruktiver Interferenz versehen.

## Nutzungsszenarien und Feldtests

- UAV- und Drohnenabwehr in geringer Höhe: Erkennung kleiner unbemannter Luftfahrzeuge bei Nebel oder Nachtbedingungen, bei denen optische Kameras nicht ausreichen.
- Kritische Anlagenperimetersicherheit: Überwachung unbefugter Annäherung von Menschen oder Fahrzeugen in einem Umkreis von 3 km an Flughäfen, Rechenzentren und Industriestandorten.
- Meteorologische und atmosphärische Forschung: Analyse von Wolkenbewegungen und Niederschlagsintensität auf lokaler Ebene mit Mikro-Doppler-Methoden.

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich würde gerne die 10,5-GHz-Phased-Array-Hardwareschaltpläne und FPGA-Signalverarbeitungsblöcke des PLFM RADAR-Projekts überprüfen. Können Sie ein Simulations-Python-Skript erstellen, das die FMCW-Chirp-Signalerzeugung, die Range-Doppler-2D-FFT-Berechnung und die Datenübertragung an die Python-basierte PPI-Radaranzeige beschreibt? Können Sie Schritt für Schritt den Algorithmus zur Entfernungs- und Geschwindigkeitserkennung für ein künstliches Ziel zeigen?

## Häufig gestellte Fragen

- Ist es möglich, das System zu Hause oder im Labor herzustellen? Ja. Alle PCB-Schaltpläne, Gerber-Produktionsdateien und FPGA-Verilog/VHDL-Codes des Projekts sind als Open Source im GitHub-Repository verfügbar. Platinen können bei Standard-Leiterplattenherstellern bestellt und in einer Laborumgebung gelötet werden.
- Was ist der Vorteil der elektronischen Strahlsteuerung gegenüber mechanischen Radargeräten? Während sich mechanische Radare mit 1–2 Umdrehungen pro Sekunde drehen, können Phased-Array-Radare die Richtung des Strahls in Mikrosekunden ändern. Es gibt keine verschleißenden mechanischen Teile und es können mehrere Ziele sofort erfasst werden.
- Ist für den Betrieb eine spezielle Hochfrequenzgenehmigung erforderlich? Das 10,5-GHz-Band unterliegt in vielen Ländern der Amateurfunk- oder Industrie-/Wissenschaftsfrequenzzuteilung (ISM). Obwohl Labortests bei niedrigen Ausgangsleistungen zulässig sind, müssen bei Außenübertragungen über große Entfernungen die örtlichen Vorschriften beachtet werden.
- Mit welchen FPGA-Entwicklungsboards ist es kompatibel? Xilinx Zynq-7000-Serie oder moderne AMD UltraScale+ RFSoC-Karten werden direkt unterstützt; Hochgeschwindigkeits-ADC/DAC-Schnittstellen werden über den FMC-Anschluss angeschlossen.

## Verwandte Begriffe aus dem Glossar

- [Patch](https://trescout.com/de/dictionary/patch/)
- [GUI](https://trescout.com/de/dictionary/gui/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Radarforscher, Ingenieure der Verteidigungsindustrie, Drohnenentwickler und RF/SDR-Enthusiasten.
- **Lizenz:** Açık kaynak donanım ve yazılım lisansı
- **Frequenzband:** 10,5 GHz (X-Band) FMCW
- **Zielbereich:** 3 km (Drohne/taktisch) – 20 km (Großraumüberwachung)

## Links

- [GitHub-Repository →](https://github.com/NawfalMotii79/PLFM_RADAR)
- [Auf Türkisch lesen →](https://trescout.com/discover/plfm-radar/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-18 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/plfm-radar/
