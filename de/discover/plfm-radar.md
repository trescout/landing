# Quelloffenes Phased-Array-Radarsystem

PLFM RADAR ist ein quelloffenes Phased-Array-Radarsystem, das bei 10,5 GHz (X-Band) arbeitet und über elektronische Strahlschwenkung (electronic beam steering) sowie FPGA-basierte digitale Signalverarbeitung verfügt. Es erfasst und verfolgt Luft- und Bodenziele präzise ohne mechanisch rotierende Bauteile.

- ★ 24.168
- C++
- GitHub Trending · 2026-08-18

## Aktualisierungen
- 18. August 2026: Sterne 24.168, stabile Version v2.0.2-p0-audit (FPGA-Signalfilterung und Reichweitenkalibrierung).

## Was es bringt
- Elektronische Strahlsteuerung: Scannt einen 90-Grad-Sektor innerhalb von Millisekunden über Phasenverschieber ohne mechanischen Verschleiß.
- Zwei Reichweitenmodi: 3 km Taktikmodus für Drohnenerkennung und 20 km Weitbereichsmodus zur Umfeldüberwachung.
- FPGA-Echtzeit-Signalverarbeitung: Hardwarebeschleunigte 2D-FFT und CFAR-Zielerkennung direkt auf dem FPGA-Silizium.
- Erschwingliche Open-Source-Hardware: Senkt die Kosten kommerzieller Militärradare von Hunderttausenden Dollar auf unter eintausend Dollar.
- Python- und SDR-Integration: Verfolgen Sie Zielvektoren in Echtzeit über SDR-Hardware und eine Python-PPI-Radaranzeige.

## Hardwarekomponenten und Radararchitektur

Das PLFM RADAR gliedert sich in HF-Frontend, planares Antennenarray und digitale Signalverarbeitung:
- 10,5 GHz X-Band Mikrostreifen-Patch-Array: Hochfrequenz-Antennenelemente auf verlustarmem Rogers/FR4-Substrat.
- Digital gesteuerte Phasenverschieber: Verzögern die Signalphase jedes Antennenelements in 5,6-Grad-Schritten zur präzisen Strahlausrichtung.
- FMCW-Frequenzsynthesizer: Hochstabiler Lokaloszillator (VCO/PLL) zur Erzeugung frequenzmodulierter Dauerstrichwellen.

## Signalverarbeitung und Steuerungssoftware

Die Radarechos werden auf Hardwareebene gefiltert, um Entfernung, Radialgeschwindigkeit und Azimut zu bestimmen:
- Entfernungs-Doppler 2D-FFT: Zweidimensionale Fourier-Transformation zur gleichzeitigen Auflösung von Abstand und Geschwindigkeit.
- CFAR-Detektor (Konstante Falschalarmrate): Dynamische Schwellenwertanpassung zur Trennung echter Ziele von Bodenclutter und Rauschen.
- Python GUI und PPI-Bildschirm: Visuelle Zielverfolgung auf einer klassischen Rundsicht-Radaranzeige (PPI) mit Kartenüberlagerung.

## Technisches Funktionsprinzip: FMCW und Phased-Array

PLFM RADAR setzt auf Dauerstrich-Frequenzmodulation (FMCW) statt auf herkömmliche Hochleistungsimpulse:
- Abstandsmessung über Schwebungsfrequenz: Das Mischen des Sendesignals mit dem Echo ergibt eine Zwischenfrequenz, die direkt proportional zur Entfernung ist.
- Strahlformung durch konstruktive Interferenz: Gezielte Phasenverschiebungen an den Antennen bündeln die elektromagnetische Welle in die gewünschte Richtung.

## Einsatzszenarien und Praxistests

Die offene Phased-Array-Architektur ermöglicht vielfältige Anwendungen:
- Tiefflug-Drohnenabwehr: Erkennt kleine Drohnen bei Nebel oder Dunkelheit, wenn optische Kameras an ihre Grenzen stoßen.
- Perimeterüberwachung kritischer Infrastruktur: Sichert Flughäfen und Rechenzentren in einem Umkreis von 3 km gegen unbefugte Annäherung.
- Meteorologische Messungen: Analysiert kleinräumige Windbewegungen und Niederschlagsdichten über Mikro-Doppler-Signaturen.

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich möchte die 10,5-GHz-Schaltpläne und die FPGA-Signalverarbeitung des Projekts PLFM RADAR verstehen. Kannst du ein Python-Simulationsskript erstellen, das ein FMCW-Chirpsignal generiert, die 2D-FFT Entfernungs-Doppler-Berechnung durchführt und Abstand und Geschwindigkeit einer simulierten Drohne extrahiert?

- **Für wen:** Radarforscher, Verteidigungsingenieure, Drohnenentwickler und RF/SDR-Enthusiasten.
- **Lizenz:** Open-Source-Hardware- und Software-Lizenz
- **Frequenzband:** 10,5 GHz (X-Band) FMCW
- **Einsatzreichweite:** 3 km (taktische Drohnenerkennung) bis 20 km (Weitbereich)

## Häufig gestellte Fragen
- Kann dieses System selbst gebaut werden? Ja. Alle PCB-Schaltpläne, Gerber-Dateien und FPGA-Verilog-Codes liegen quelloffen auf GitHub bereit und können bei Fertigern in Auftrag gegeben werden.
- Was ist der Vorteil von Phased-Arrays gegenüber rotierenden Antennen? Elektronische Strahlschwenkung erfolgt in Mikrosekunden, erfordert keine mechanischen Verschleißteile und erlaubt das parallele Verfolgen mehrerer Ziele.
- Wird eine Sendegenehmigung benötigt? Das 10,5-GHz-Band ist in vielen Ländern für Amateurfunk oder ISM freigegeben. Laborprüfungen mit geringer Leistung sind meist unbedenklich; Außenabstrahlungen müssen den örtlichen Vorschriften entsprechen.
- Welche FPGA-Entwicklungsboards werden unterstützt? Xilinx Zynq-7000 und AMD UltraScale+ RFSoC Boards werden über FMC-Schnittstellen mit schnellen ADC/DAC-Karten direkt unterstützt.

## Links
- [GitHub →](https://github.com/NawfalMotii79/PLFM_RADAR)

## Verwandte Begriffe aus dem Glossar
Edge Computing Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/de/discover/plfm-radar/
