# Automatische Quadratur für dreidimensionale Modelle

Autoremesher ist ein Werkzeug, das unregelmäßige Oberflächenstrukturen in dreidimensionalen Modellen automatisch in Quad-Remeshing umwandelt. Diese in der Sprache C++ entwickelte Software ist darauf optimiert, komplexe Geometrien für Animations- und Modellierungsprozesse geeignet zu machen.

- ★ 3.322
- C++
- GitHub Trending · 2026-07-09

## Aktualisierungen

- **24. August 2026:** Sterne 3,225 → 3,322, neueste Version 1.2.0 (23. August 2026).
- **17. August 2026:** Sterne 3,087 → 3,225, neueste Version 1.1.0 (16. August 2026).
- **2. August 2026:** Sterne 2,123 → 3,087, neueste Version 1.0.0 (6. Juli 2026).

## Was es bringt

- Wandelt komplexe Modelle in saubere rechteckige Netze um
- Bietet eine optimierte Topologie für Animationsprozesse
- Bietet Stapelverarbeitungsunterstützung über die Befehlszeile

## Installation

**Kompilieren unter Linux**

```
# Install Qt and build tools
sudo apt install build-essential qt5-qmake qtbase5-dev qttools5-dev-tools libqt5svg5-dev libqt5multimedia5-dev

# Install TBB and OpenGL
sudo apt install libtbb-dev libgl1-mesa-dev

# Clone and build
git clone https://github.com/huxingyi/autoremesher.git
cd autoremesher
qmake
make -j$(nproc)
```

**Bauen Sie auf macOS auf**

```
# Install Xcode Command Line Tools
xcode-select --install

# Install dependencies via Homebrew
brew install qt@5 tbb cmake

# Build
export PATH="/usr/local/opt/qt@5/bin:$PATH"
git clone https://github.com/huxingyi/autoremesher.git
cd autoremesher
qmake CONFIG+=sdk_no_version_check
make -j$(sysctl -n hw.logicalcpu)
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die 3D-Modelldatei, die ich habe, in eine rechteckige Netzstruktur konvertieren. Wie kann ich meine Eingabedatei mit der angegebenen Zielanzahl an Vierecken, Kantenskalierung und scharfen Kanteneinstellungen mit dem Autoremesher-Tool verarbeiten? Bitte erstellen Sie eine Beispielkonfiguration, die ich über die Befehlszeile verwenden kann.

## Verwandte Begriffe aus dem Glossar

- [Quad Remeshing](https://trescout.com/de/dictionary/quad-remeshing/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für Künstler und Entwickler, die Topologiebearbeitung in 3D-Modellierungs- und Animationsprozessen benötigen.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/huxingyi/autoremesher)
- [Auf Türkisch lesen →](https://trescout.com/discover/autoremesher/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-09 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/autoremesher/
