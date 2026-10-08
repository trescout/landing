# Verstärkende Lernumgebung für Pollen Robotics Microduck

microduck_rl wurde von Pollen Robotics entwickelt und bietet Trainingsumgebungen für verstärktes Lernen und Kontrollrichtlinien auf MuJoCo und mjlab für die Microduck-Roboterplattform.

- ★ 2.281
- Python
- GitHub Trending · 2026-08-31

## Aktualisierungen

- **27. September 2026:** Sterne 1,001 → 2,281.

## Was es bringt

- Realistische MuJoCo-Physiksimulation: Möglichkeit, die Gelenkdrehmomente, Reibung und Schwerkrafteffekte des Roboters bei hoher Geschwindigkeit zu simulieren.
- Vorgefertigte Fortbewegungs- und Gleichgewichtsaufgaben: Vordefinierte Belohnungsfunktionen für Szenarien zum Gehen, Balancieren und Überwinden von Hindernissen.
- Geeignet für die Sim-to-Real-Übertragung: Rauschresistente Steuerungsrichtlinien, die einfach auf physische Microduck-Hardware übertragen werden können.
- Moderne Reinforcement-Learning-Algorithmen: PPO (Proximal Policy Optimization) und SAC unterstützte Trainingsinfrastruktur.
- Visuelle 3D-Auswerteoberfläche: Sofortige Überwachung der Bewegungen des trainierten Roboteragenten im 3D-Simulator auf dem Bildschirm.

## Installation

**Klonen des Repositorys und Einrichten der Simulationsumgebung**

```
git clone https://github.com/pollen-robotics/microduck_rl.git
cd microduck_rl
pip install -e .
```

## Ausführung

**Lauftraining oder Richtlinienbewertung**

```
python -m microduck_rl.train --task walk
# Eğitilen politikayı simülatörde izleme:
python -m microduck_rl.enjoy --checkpoint checkpoint.pt
```

## Technische Architektur und Funktionsweise

- MuJoCo und mjlab Physics Layer: XML/MJCF-Dateien, die die Kinematik, Gelenkgrenzen und Aktormodelle des Roboters definieren.
- Gymnasiumkompatible Beobachtungs- und Aktionsräume: Standardisierung von Motorwinkeln, Geschwindigkeiten, Beschleunigungsmesserdaten (IMU) und Zieldrehmomentvektoren.
- Domänen-Randomisierungsmechanismus: Training realer robuster Modelle durch zufällige Variation von Reibungskoeffizienten, Massenverteilung und Sensorrauschen.

## Richtlinien für physikalische Simulation und Robotiksteuerung

- Verhindern von Hardwareschäden: Beheben Sie die Risiken von Roboterstürzen und Beinbrüchen in einer vollständig virtuellen Umgebung, bevor Sie zum physischen Roboter wechseln.
- Trainieren Sie Millionen von Schritten in beschleunigter Zeit: Absolvieren Sie Trainingstage in Stunden, indem Sie die Physik-Engine 100-mal schneller als in Echtzeit betreiben.
- Benutzerdefinierte Mission und Geländedesign: Testen Sie die Anpassungsfähigkeit des Roboters an verschiedene Gelände, indem Sie Treppen, Gefälle und rutschige Oberflächen hinzufügen.

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mithilfe der microduck_rl-Bibliothek von Pollen Robotics eine Gehrichtlinie für den Microduck-Roboter trainieren. Können Sie die Schritte zum Konfigurieren der MuJoCo-Umgebung, zum Initialisieren des Trainingsbefehls mit dem PPO-Algorithmus und zum Übertragen der resultierenden Steuerungsrichtlinie auf den physischen Roboter erläutern?

## Häufig gestellte Fragen

- Ist ein physischer Microduck-Roboter erforderlich, um microduck_rl auszuführen? Nein. Die Codebasis kann vollständig virtuell auf dem MuJoCo-Simulator ausgeführt werden. Sie können die 3D-Simulation des Roboters auf Ihrem Computer ansehen.
- Ist GPU-Unterstützung erforderlich? MuJoCo läuft auch auf der CPU ziemlich schnell; Beim Training von Reinforcement Learning mit parallelen Umgebungen beschleunigt eine CUDA-unterstützte GPU den Prozess jedoch erheblich.
- Wie wird das trainierte Modell auf den physischen Roboter übertragen? Wenn das Training abgeschlossen ist, wird die generierte ONNX- oder PyTorch-Checkpoint-Datei in den integrierten Steuercomputer von Microduck geladen und direkt mit den Motordrehmomenten verknüpft.
- Unterstützt es verschiedene Robotermodelle? microduck_rl ist hauptsächlich für Microduck optimiert; Dank seines modularen Aufbaus kann es jedoch an ähnliche zweibeinige oder vierbeinige Roboter-MJCF-Modelle angepasst werden.

## Verwandte Begriffe aus dem Glossar

- [Reinforcement Learning](https://trescout.com/de/dictionary/reinforcement-learning/)
- [CPU](https://trescout.com/de/dictionary/cpu/)
- [GPU](https://trescout.com/de/dictionary/gpu/)
- [API](https://trescout.com/de/dictionary/api/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Robotikforscher, Mechatroniker, Experten für Reinforcement Learning und Bastler.
- **Lizenz:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** Python, MuJoCo & mjlab Robotics Framework
- **Plattformen:** Linux, macOS, Windows

## Links

- [GitHub-Repository →](https://github.com/pollen-robotics/microduck_rl)
- [Auf Türkisch lesen →](https://trescout.com/discover/microduck-rl/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-31 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/microduck-rl/
