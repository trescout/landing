# Cuadratura automática para modelos tridimensionales.

Autoremesher es una herramienta que convierte automáticamente estructuras de superficies irregulares en modelos tridimensionales en remallado cuádruple. Desarrollado en lenguaje C++, este software está optimizado para hacer que geometrías complejas sean adecuadas para procesos de animación y modelado.

- ★ 3.087
- C++
- GitHub Trending · 2026-07-09

## Actualizar
- 2 de agosto de 2026: Estrella 2123 → 3087, última versión 1.0.0 (6 de julio de 2026).

## Qué aporta
- Transforma modelos complejos en mallas rectangulares limpias
- Proporciona topología optimizada para procesos de animación.
- Ofrece soporte de procesamiento por lotes a través de la línea de comando

## Instalación
**Compilando en Linux**

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

**Construir en macOS**

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


## Si no programa
Quiero convertir el archivo del modelo 3D que tengo en una estructura de malla rectangular. ¿Cómo puedo procesar mi archivo de entrada con un número objetivo específico de cuadriláteros, escalado de bordes y configuraciones de bordes afilados usando la herramienta Autoremesher? Cree una configuración de muestra que pueda usar a través de la línea de comando.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/autoremesher/
