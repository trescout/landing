# Automatic quadriformization for three-dimensional models

Autoremesher is a tool that automatically converts irregular surface structures in three-dimensional models into quad remeshing. Developed in C++ language, this software is optimized to make complex geometries suitable for animation and modeling processes.

- ★ 3,225
- C++
- GitHub Trending · 2026-07-09

## What you get
- Transforms complex models into clean rectangular meshes
- Provides optimized topology for animation processes
- Offers batch processing support via command line

## Installation
**Compiling on Linux**

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

**Build on macOS**

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


## If you don't write code
I want to convert the 3D model file I have into a rectangular mesh structure. How can I process my input file with specified target number of quadrilaterals, edge scaling and sharp edge settings using the Autoremesher tool? Please create a sample configuration that I can use via the command line.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/autoremesher/
