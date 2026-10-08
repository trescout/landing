# Automatic quadriformization for three-dimensional models

Autoremesher is a tool that automatically converts irregular surface structures in three-dimensional models into quad remeshing. Developed in C++ language, this software is optimized to make complex geometries suitable for animation and modeling processes.

- ★ 3,322
- C++
- GitHub Trending · 2026-07-09

## Updates

- **August 24, 2026:** Stars 3,225 → 3,322, latest release 1.2.0 (August 23, 2026).
- **August 17, 2026:** Stars 3,087 → 3,225, latest release 1.1.0 (August 16, 2026).
- **August 2, 2026:** Stars 2,123 → 3,087, latest release 1.0.0 (July 6, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to convert the 3D model file I have into a rectangular mesh structure. How can I process my input file with specified target number of quadrilaterals, edge scaling and sharp edge settings using the Autoremesher tool? Please create a sample configuration that I can use via the command line.

## Related dictionary terms

- [Quad Remeshing](https://trescout.com/en/dictionary/quad-remeshing/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for artists and developers who need to edit topologies in three-dimensional modeling and animation processes.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/huxingyi/autoremesher)
- [Read in Turkish →](https://trescout.com/discover/autoremesher/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-09: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/autoremesher/
