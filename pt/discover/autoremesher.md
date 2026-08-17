# Quadratura automática para modelos tridimensionais

Autoremesher é uma ferramenta que converte automaticamente estruturas de superfície irregulares em modelos tridimensionais em remalhamento quádruplo. Desenvolvido em linguagem C++, este software é otimizado para tornar geometrias complexas adequadas para processos de animação e modelagem.

- ★ 3.225
- C++
- GitHub Trending · 2026-07-09

## O que você ganha
- Transforma modelos complexos em malhas retangulares limpas
- Fornece topologia otimizada para processos de animação
- Oferece suporte para processamento em lote via linha de comando

## Instalação
**Compilando no Linux**

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

**Crie no macOS**

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


## Se você não programa
Quero converter o arquivo do modelo 3D que possuo em uma estrutura de malha retangular. Como posso processar meu arquivo de entrada com um número alvo especificado de quadriláteros, escala de arestas e configurações de arestas vivas usando a ferramenta Autoremesher? Crie um exemplo de configuração que eu possa usar por meio da linha de comando.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/autoremesher/
