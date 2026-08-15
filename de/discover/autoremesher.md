# Automatische Quadratur für dreidimensionale Modelle

Autoremesher ist ein Werkzeug, das unregelmäßige Oberflächenstrukturen in dreidimensionalen Modellen automatisch in Quad-Remeshing umwandelt. Diese in der Sprache C++ entwickelte Software ist darauf optimiert, komplexe Geometrien für Animations- und Modellierungsprozesse geeignet zu machen.

- ★ 3.087
- C++
- GitHub Trending · 2026-07-09

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
Ich möchte die 3D-Modelldatei, die ich habe, in eine rechteckige Netzstruktur konvertieren. Wie kann ich meine Eingabedatei mit der angegebenen Zielanzahl an Vierecken, Kantenskalierung und scharfen Kanteneinstellungen mit dem Autoremesher-Tool verarbeiten? Bitte erstellen Sie eine Beispielkonfiguration, die ich über die Befehlszeile verwenden kann.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/autoremesher/
